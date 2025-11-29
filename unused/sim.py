"""Active task simulation."""

import argparse
from collections import defaultdict
from enum import Enum
from itertools import count
import random
import simpy


PARAMS = {
    "log_interval": 1,
    "num_dev": 1,
    "num_tester": 1,
    "median_dev_time": 5.0,
    "median_test_time": 4.0,
    "rng_seed": 12345,
    "sim_time": 10,
    "task_arrival": 3,
}
PREC = 2


class ValueEnum(Enum):
    """Enum that shows values instead of class.values."""

    def __str__(self):
        """Create string representation."""
        return self.value


class Simulation:
    """Overall simulation."""

    def __init__(self, params):
        """Construct."""

        self.params = params
        self.env = simpy.Environment()

        self.developers = [Developer(self) for _ in range(params["num_dev"])]
        self.dev_queue = simpy.PriorityStore(self.env)

        self.testers = [Tester(self) for _ in range(params["num_tester"])]
        self.test_queue = simpy.PriorityStore(self.env)

        self.logger = Log(self)

    @property
    def now(self):
        """Shortcut for current time."""
        return self.env.now

    def generate(self):
        """Generate tasks at random intervals."""

        while True:
            yield self.timeout(self.task_arrival())
            yield self.dev_queue.put(Task(self))

    def process(self, proc):
        """Shortcut for running a process."""
        self.env.process(proc)

    def run(self):
        """Run the whole simulation."""

        self.process(self.generate())
        self.process(self.logger.work())
        for workers in (self.developers, self.testers):
            for w in workers:
                self.process(w.work())
        self.env.run(until=self.params["sim_time"])

    def dev_time(self):
        """Development time."""
        return random.lognormvariate(0, 1) * self.params["median_dev_time"]

    def task_arrival(self):
        """Task arrival time."""
        return random.expovariate(1.0 / self.params["task_arrival"])

    def test_time(self):
        """Testing time."""
        return random.lognormvariate(0, 1) * self.params["median_test_time"]

    def timeout(self, time):
        """Shortcut for delaying a fixed time."""
        return self.env.timeout(time)


class Log:
    """Keep a log of interesting things."""

    def __init__(self, sim):
        """Construct."""

        self.sim = sim
        self.log = []

    def get_log(self):
        """Make a log entry."""

        return {
            "params": self.sim.params,
            "log": self.log,
            "tasks": [
                {"id": obj.id, "dev": obj["dev_time"], "test": obj["test_time"], "state": str(obj.state)}
                for obj in Labeled._all[Task]
            ],
            "developers": [
                {"id": obj.id, "busy": round(obj["busy"], PREC)} for obj in Labeled._all[Developer]
            ],
            "testers": [
                {"id": obj.id, "busy": round(obj["busy"], PREC)} for obj in Labeled._all[Tester]
            ],
        }

    def work(self):
        """Create log entries every fixed time interval."""

        while True:
            self._record()
            yield self.sim.timeout(self.sim.params["log_interval"])

    def _record(self):
        """Record a log entry at a particular moment."""

        # States of all tasks.
        task_states = {state: 0 for state in Task.State}
        for t in Labeled._all[Task]:
            task_states[t.state] += 1
        task_states = {str(key): value for key, value in task_states.items()}

        # Add log entry.
        self.log.append(
            {
                "time": round(self.sim.now, PREC),
                "dev_queue": len(self.sim.dev_queue.items),
                "test_queue": len(self.sim.test_queue.items),
                **task_states,
            }
        )


class Elapsed:
    """Context manager to keep track of elapsed time."""

    def __init__(self, obj, key):
        """Construct."""

        self.obj = obj
        self.key = key
        self.start = None

    def __enter__(self):
        """Start the clock."""
        self.start = self.obj.sim.now

    def __exit__(self, exc_type, exc_value, traceback):
        """Stop the clock."""

        self.obj[self.key] += self.obj.sim.now - self.start
        return False


class Labeled:
    """Parent class for objects that have unique IDs and are tracked."""

    _id = defaultdict(count)  # Next ID by class
    _all = defaultdict(list)  # All instances of class

    def __init__(self, sim):
        """Construct."""

        self.sim = sim
        cls = self.__class__
        Labeled._all[cls].append(self)
        self.id = next(Labeled._id[cls])
        self._vals = defaultdict(float)

    def __str__(self):
        """String representation."""

        name = self.__class__.__name__.lower()
        return f"{name}-{self.id}"

    def __getitem__(self, key):
        """Get value associated with key (for logging)."""
        return self._vals[key]

    def __setitem__(self, key, value):
        """Set value associated with key (for logging)."""
        self._vals[key] = value


class Task(Labeled):
    """A task."""

    class State(ValueEnum):
        """Task states."""

        WAIT_DEV = "task_wait_dev"
        DEV = "task_dev"
        WAIT_TEST = "task_wait_test"
        TEST = "task_test"
        COMPLETE = "task_complete"

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)
        self.state = Task.State.WAIT_DEV
        self.priority = 0
        self["t_dev"] = self.sim.dev_time()
        self["t_test"] = self.sim.test_time()

    def __lt__(self, other):
        return self.priority < other.priority


class Developer(Labeled):
    """A developer."""

    def work(self):
        """Simulate."""

        while True:
            task = yield self.sim.dev_queue.get()
            task.state = Task.State.DEV
            with Elapsed(self, "busy"):
                yield self.sim.timeout(task["t_dev"])
            task.state = Task.State.WAIT_TEST
            yield self.sim.test_queue.put(task)


class Tester(Labeled):
    """A tester."""

    def work(self):
        """Simulate."""

        while True:
            task = yield self.sim.test_queue.get()
            task.state = Task.State.TEST
            with Elapsed(self, "busy"):
                yield self.sim.timeout(task["t_test"])
            task.state = Task.State.COMPLETE


def parse_args():
    """Parse command-line arguments (used to modify parameters)."""

    parser = argparse.ArgumentParser()
    parser.add_argument("params", nargs="*", help="parameter overrides")
    return parser.parse_args()


def update_params(params, args):
    """Update parameters from command-line arguments."""

    for arg in args:
        fields = arg.split("=")
        assert len(fields) == 2 and all(len(f) > 0 for f in fields)
        key, value = fields[0], fields[1]
        assert key in params
        if isinstance(params[key], int):
            params[key] = int(value)
        else:
            params[key] = float(value)


def main(params):
    """Main driver."""

    # Handle command-line arguments and parameters.
    args = parse_args()
    update_params(params, args.params)
    random.seed(params["rng_seed"])

    # Run simulation.
    sim = Simulation(params)
    sim.run()

    # Report.
    print(sim.logger.get_log())


if __name__ == "__main__":
    main(PARAMS)
