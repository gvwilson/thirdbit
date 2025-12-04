"""Active task simulation."""

import argparse
from collections import defaultdict
from enum import Enum
from itertools import count
import json
import random
import simpy
import sys


# Simulation parameters.
PARAMS = {
    "nolog": 0,
    "n_dev": 3,
    "n_tester": 3,
    "p_rework_chosen": 0.5,
    "p_rework_needed": 0.5,
    "rng_seed": 12345,
    "t_arrival": 4.0,
    "t_dev": 5.0,
    "t_log": 5,
    "t_sim": 20,
    "t_test": 4.0,
}

# Floating-point rounding precision.
PREC = 2

# Summary values to save.
TASK_KEYS = ("t_create", "n_dev", "t_dev", "n_test", "t_test")
WORKER_KEYS = ("busy", "n_task", "n_both", "n_dev", "n_rework")


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

        self.developers = [Developer(self) for _ in range(params["n_dev"])]
        self.dev_queue = simpy.Store(self.env)

        self.testers = [Tester(self) for _ in range(params["n_tester"])]
        self.test_queue = simpy.Store(self.env)

        self.logger = Log(self)

    @property
    def now(self):
        """Shortcut for current time."""
        return self.env.now

    def process(self, proc):
        """Shortcut for running a process."""
        self.env.process(proc)

    def timeout(self, time):
        """Shortcut for delaying a fixed time."""
        return self.env.timeout(time)

    def generate(self):
        """Generate tasks at random intervals starting at t=0."""

        yield self.dev_queue.put(Task(self))
        while True:
            yield self.timeout(self.t_arrival())
            yield self.dev_queue.put(Task(self))

    def run(self):
        """Run the whole simulation."""

        if not self.params["nolog"]:
            self.process(self.logger.work())
        self.process(self.generate())
        for workers in (self.developers, self.testers):
            for w in workers:
                self.process(w.work())
        self.env.run(until=self.params["t_sim"])

    def t_dev(self):
        """Development time."""
        return random.lognormvariate(0, 1) * self.params["t_dev"]

    def t_arrival(self):
        """Task arrival time."""
        return random.expovariate(1.0 / self.params["t_arrival"])

    def t_test(self):
        """Testing time."""
        return random.lognormvariate(0, 1) * self.params["t_test"]

    def p_rework_chosen(self):
        """Will the developer choose rework over new development?"""
        return random.uniform(0, 1) < self.params["p_rework_chosen"]

    def p_rework_needed(self):
        """Does this task need to be reworked?"""
        return random.uniform(0, 1) < self.params["p_rework_needed"]


class Log:
    """Keep a log of interesting things."""

    def __init__(self, sim):
        """Construct."""

        self.sim = sim
        self.snapshot = {
            "tasks": [],
            "queues": [],
            "workers": [],
        }

    def get_log(self):
        """Get entire log."""

        # Summarize tasks.
        tasks = [
            {
                "id": obj.id,
                "state": str(obj.state),
                **{key: round(obj[key], PREC) for key in TASK_KEYS},
            }
            for obj in Labeled._all[Task]
        ]

        # Summarize developrs and testers.
        workers = []
        for kind, cls in (("dev", Developer), ("test", Tester)):
            for w in Labeled._all[cls]:
                workers.append(
                    {
                        "id": w.id,
                        "kind": kind,
                        **{key: round(w[key], PREC) for key in WORKER_KEYS},
                    }
                )

        # Entire log.
        return {
            "params": self.sim.params,
            "snapshot": self.snapshot,
            "summary": {
                "tasks": tasks,
                "workers": workers,
            },
        }

    def work(self):
        """Create log entries every fixed time interval."""

        while True:
            self._record()
            yield self.sim.timeout(self.sim.params["t_log"])

    def _record(self):
        """Record a log entry at a particular moment."""

        now = self.sim.now
        for t in Labeled._all[Task]:
            self.snapshot["tasks"].append(
                {"time": now, "id": t.id, "state": str(t.state)}
            )
        for name, queue in (("dev", self.sim.dev_queue), ("test", self.sim.test_queue)):
            self.snapshot["queues"].append(
                {"time": now, "name": name, "length": len(queue.items)}
            )
        for kind, cls in (("dev", Developer), ("test", Tester)):
            for w in Labeled._all[cls]:
                self.snapshot["workers"].append(
                    {"time": now, "kind": kind, "id": w.id, "state": str(w.state)}
                )


class WorkLog:
    """Context manager to keep track of elapsed time."""

    def __init__(self, worker, task, task_states, key_num, key_time):
        """Construct."""

        self.worker = worker
        self.task = task
        self.task_states = task_states
        self.key_num = key_num
        self.key_time = key_time
        self.start = None

    def __enter__(self):
        """Start the clock."""
        self.start = self.worker.sim.now
        self.worker.state = Worker.State.BUSY
        self.task.state = self.task_states[0]

    def __exit__(self, exc_type, exc_value, traceback):
        """Stop the clock."""

        elapsed = self.worker.sim.now - self.start

        self.worker.state = Worker.State.IDLE
        self.worker["busy"] += elapsed
        self.worker["n_task"] += 1

        if self.task_states[1] is not None:
            self.task.state = self.task_states[1]
        self.task[self.key_num] += 1
        self.task[self.key_time] += elapsed

        return False


class DeveloperLog(WorkLog):
    """Log a developer's work."""

    def __init__(self, developer, task):
        super().__init__(
            developer,
            task,
            (Task.State.DEV, Task.State.WAIT_TEST),
            "n_dev",
            "t_dev",
        )


class TesterLog(WorkLog):
    """Log a tester's work."""

    def __init__(self, tester, task):
        super().__init__(
            tester,
            task,
            (Task.State.TEST, None),
            "n_test",
            "t_test",
        )


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

    # Task priorities.
    PRI_HIGH = 0
    PRI_LOW = 1

    class State(ValueEnum):
        """Task states."""

        WAIT_DEV = "wait_dev"
        DEV = "dev"
        WAIT_TEST = "wait_test"
        TEST = "test"
        COMPLETE = "complete"

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)
        self.state = Task.State.WAIT_DEV
        self.priority = Task.PRI_LOW
        self.required_dev = self.sim.t_dev()
        self.required_test = self.sim.t_test()
        self["t_create"] = self.sim.now
        self.developer = None

    def __lt__(self, other):
        return self.priority < other.priority


class Worker(Labeled):
    """A generic worker."""

    class State(ValueEnum):
        """Task states."""

        IDLE = "idle"
        BUSY = "busy"

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)
        self.state = Worker.State.IDLE


class Developer(Worker):
    """A developer."""

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)
        self.rework_queue = simpy.Store(self.sim.env)

    def work(self):
        """Simulate."""

        while True:
            req_dev = self.sim.dev_queue.get()
            req_rework = self.rework_queue.get()
            result = yield (req_dev | req_rework)
            task = self.choose(result, req_dev, req_rework)

            with DeveloperLog(self, task):
                yield self.sim.timeout(task.required_dev)

            task.developer = self
            yield self.sim.test_queue.put(task)

    def choose(self, result, req_dev, req_rework):
        """Choose a task and cancel other request."""
        if len(result.events) == 2:
            choice = "rework" if self.sim.p_rework_chosen() else "dev"
            self["n_both"] += 1
        elif req_dev in result:
            choice = "dev"
            self["n_dev"] += 1
        elif req_rework in result:
            choice = "rework"
            self["n_rework"] += 1
        else:
            assert False, "how did we get here?"

        if choice == "dev":
            task = result[req_dev]
            req_rework.cancel()
        elif choice == "rework":
            task = result[req_rework]
            req_dev.cancel()
        else:
            assert False, "how did we get here?"

        return task


class Tester(Worker):
    """A tester."""

    def work(self):
        """Simulate."""

        while True:
            task = yield self.sim.test_queue.get()

            with TesterLog(self, task):
                yield self.sim.timeout(task.required_test)

            if self.sim.p_rework_needed():
                assert task.developer is not None
                task.priority = Task.PRI_HIGH
                task.state = Task.State.WAIT_DEV
                yield task.developer.rework_queue.put(task)
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
