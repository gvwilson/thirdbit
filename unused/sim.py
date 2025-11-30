"""Active task simulation."""

import argparse
from collections import defaultdict
from enum import Enum
from itertools import count
import json
import random
import simpy
import sys


PARAMS = {
    "log_interval": 1,
    "num_dev": 3,
    "num_tester": 3,
    "median_dev_time": 5.0,
    "median_test_time": 4.0,
    "prob_rework": 0.5,
    "rng_seed": 12345,
    "sim_time": 10,
    "task_arrival": 4.0,
}
PREC = 2
PRI_HIGH = 0
PRI_LOW = 1
TASK_KEYS = ("t_create", "n_dev", "t_dev", "n_test", "t_test")
WORKER_KEYS = ("busy", "n_task")


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

    def rework(self, task):
        """Does this task need to be reworked?"""
        return random.uniform(0, 1) < self.params["prob_rework"]

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
                {
                    "id": obj.id,
                    "state": str(obj.state),
                    **{key: round(obj[key], PREC) for key in TASK_KEYS},
                }
                for obj in Labeled._all[Task]
            ],
            "developers": [
                {"id": obj.id, **{key: round(obj[key], PREC) for key in WORKER_KEYS}}
                for obj in Labeled._all[Developer]
            ],
            "testers": [
                {"id": obj.id, **{key: round(obj[key], PREC) for key in WORKER_KEYS}}
                for obj in Labeled._all[Tester]
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


class WorkLog:
    """Context manager to keep track of elapsed time."""

    def __init__(self, worker, task, key_n, key_t):
        """Construct."""

        self.worker = worker
        self.task = task
        self.key_n = key_n
        self.key_t = key_t
        self.start = None

    def __enter__(self):
        """Start the clock."""
        self.start = self.worker.sim.now

    def __exit__(self, exc_type, exc_value, traceback):
        """Stop the clock."""

        elapsed = self.worker.sim.now - self.start
        self.worker["busy"] += elapsed
        self.worker["n_task"] += 1
        self.task[self.key_n] += 1
        self.task[self.key_t] += elapsed
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
        self.priority = PRI_LOW
        self.required_dev = self.sim.dev_time()
        self.required_test = self.sim.test_time()
        self["t_create"] = self.sim.now

    def __lt__(self, other):
        return self.priority < other.priority


class Developer(Labeled):
    """A developer."""

    def work(self):
        """Simulate."""

        while True:
            task = yield self.sim.dev_queue.get()
            task.state = Task.State.DEV
            with WorkLog(self, task, "n_dev", "t_dev"):
                yield self.sim.timeout(task.required_dev)
            task.state = Task.State.WAIT_TEST
            yield self.sim.test_queue.put(task)


class Tester(Labeled):
    """A tester."""

    def work(self):
        """Simulate."""

        while True:
            task = yield self.sim.test_queue.get()
            task.state = Task.State.TEST
            with WorkLog(self, task, "n_test", "t_test"):
                yield self.sim.timeout(task.required_test)
            if self.sim.rework(task):
                task.priority = PRI_HIGH
                task.state = Task.State.WAIT_DEV
                self.sim.dev_queue.put(task)
            else:
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
    json.dump(sim.logger.get_log(), sys.stdout)


if __name__ == "__main__":
    main(PARAMS)
