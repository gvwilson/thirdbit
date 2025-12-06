"""Active task simulation."""

import argparse
from collections import defaultdict
from itertools import count
import json
import random
import simpy
import sys


# Simulation parameters.
PARAMS = {
    "n_dev": 1,
    "n_tester": 1,
    "rng_seed": 12345,
    "t_arrival": 8.0,
    "t_dev": 5.0,
    "t_sim": 20,
    "t_test": 4.0,
}

# What to save for tasks.
TASK_KEYS = ("id", "created", "state", "dev_required", "test_required")

# What to save for workers.
WORKER_KEYS = ("id", "kind")

# Round or leave alone.
def r(val):
    if isinstance(val, float):
        return round(val, 2)
    return val

class Simulation:
    """Overall simulation."""

    def __init__(self, params):
        """Construct."""

        self.params = params
        self.env = simpy.Environment()

        self.dev_queue = simpy.Store(self.env)
        self.test_queue = simpy.Store(self.env)

        self.developers = [Developer(self) for _ in range(params["n_dev"])]
        self.testers = [Tester(self) for _ in range(params["n_tester"])]
        self.workers = self.developers + self.testers

    @property
    def now(self):
        """Shortcut for current time."""
        return self.env.now

    def process(self, proc):
        """Shortcut for running a process."""
        return self.env.process(proc)

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

        self.process(self.generate())
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

    def __str__(self):
        """String representation."""

        name = self.__class__.__name__.lower()
        return f"{name}-{self.id}"


class Task(Labeled):
    """A task."""

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)
        self.created = self.sim.now
        self.dev_required = self.sim.t_dev()
        self.test_required = self.sim.t_test()
        self.state = ["dev_queue"]


class Worker(Labeled):
    """A generic worker."""

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)
        self.kind = self.__class__.__name__.lower()
        self.proc = self.sim.process(self.work())


class Developer(Worker):
    """A developer."""

    def work(self):
        """Simulate."""

        while True:
            task = yield self.sim.dev_queue.get()
            task.state.append("dev")
            yield self.sim.timeout(task.dev_required)
            task.state.append("test_queue")
            yield self.sim.test_queue.put(task)


class Tester(Worker):
    """A tester."""

    def work(self):
        """Simulate."""

        while True:
            task = yield self.sim.test_queue.get()
            task.state.append("test")
            yield self.sim.timeout(task.test_required)
            task.state.append("complete")


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


def get_log(sim):
    """Get log."""

    tasks = [{k: r(getattr(t, k)) for k in TASK_KEYS} for t in Labeled._all[Task]]
    workers = [{k: r(getattr(w, k)) for k in WORKER_KEYS} for w in sim.workers]
    return {
        "params": sim.params,
        "tasks": tasks,
        "workers": workers,
    }


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
    json.dump(get_log(sim), sys.stdout)


if __name__ == "__main__":
    main(PARAMS)
