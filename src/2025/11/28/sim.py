import argparse
from collections import defaultdict
from itertools import count
import json
import random
import sys
import simpy

PARAMS = {
    "max_dev_time": 10.0,
    "num_developers": 2,
    "num_testers": 2,
    "prob_rework": 0.5,
    "random_seed": 12345,
    "simulation_time": 10,
    "task_arrival_rate": 2,
    "test_fraction": [0.5, 1.5],
}
PRECISION = 2


class Simulation:
    """Store simulation artifacts."""

    def __init__(self, params):
        self.params = params
        self.env = simpy.Environment()
        self.dev_queue = simpy.Store(self.env)
        self.test_queue = simpy.Store(self.env)

    def process(self, proc):
        self.env.process(proc)

    def run(self):
        self.env.run(until=self.params["simulation_time"])

    def timeout(self, time):
        return self.env.timeout(time)

    @property
    def now(self):
        return self.env.now

    def task_arrival(self):
        return random.expovariate(1.0 / self.params["task_arrival_rate"])

    def task_rework(self):
        return random.uniform(0, 1) < self.params["prob_rework"]

    def dev_time(self):
        return random.uniform(1, self.params["max_dev_time"])

    def test_time(self, task):
        return task["dev_time"] * random.uniform(*self.params["test_fraction"])


class Labeled:
    """Objects with unique IDs."""

    _ids = defaultdict(count)
    _all = defaultdict(list)

    @staticmethod
    def _next_id(obj):
        """Generate next ID for an object."""

        name = obj.__class__.__name__
        result = next(Labeled._ids[name])
        Labeled._all[name].append(obj)
        return result

    def __init__(self, sim):
        """Construct."""

        self.sim = sim
        self.id = Labeled._next_id(self)
        self._vals = defaultdict(float)

    def __getitem__(self, key):
        """Get recorded time."""
        return self._vals[key]

    def __setitem__(self, key, value):
        """Record a time."""
        self._vals[key] = value

    def __str__(self):
        """Printable representation."""
        name = self.__class__.__name__.lower()
        return f"{name}-{self.id}"


class Task(Labeled):
    """A single task."""

    @staticmethod
    def generate(sim):
        """Generate tasks and add to the development queue."""

        while True:
            yield sim.timeout(sim.task_arrival())
            task = Task(sim)
            print(f"creating {task} at {sim.now:.2f}")
            yield sim.dev_queue.put(task)

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)
        self["dev_time"] = sim.dev_time()


class Developer(Labeled):
    """A single developer."""

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)

    def work(self):
        """Simulate work."""

        while True:
            task = yield self.sim.dev_queue.get()
            print(f"{self} starts {task} at {self.sim.now:.2f}")
            yield self.sim.timeout(task["dev_time"])
            print(f"{self} completes {task} at {self.sim.now:.2f}")
            yield self.sim.test_queue.put(task)


class Tester(Labeled):
    """A single tester."""

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)

    def work(self):
        """Simulate work."""

        while True:
            task = yield self.sim.test_queue.get()
            print(f"{self} starts {task} at {self.sim.now:.2f}")
            yield self.sim.timeout(task["test_time"])
            print(f"{self} completes {task} at {self.sim.now:.2f}")
            if self.sim.task_rework():
                print(f"...{self} asks for rework on {task}")
                self.sim.dev_queue.put(task)


def update_params(params, args):
    """Adjust parameters based on command line arguments."""

    for arg in args:
        fields = arg.split("=")
        assert len(fields) == 2 and all(len(f) > 0 for f in fields)
        key, value = fields[0], fields[1]
        assert key in params
        if isinstance(params[key], int):
            params[key] = int(value)
        else:
            params[key] = float(value)


def parse_args():
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument("params", nargs="*", help="parameter overrides")
    return parser.parse_args()


def main(params):
    """Main driver."""

    # Handle command-line arguments and parameters.
    args = parse_args()
    update_params(params, args.params)
    random.seed(params["random_seed"])

    # Create and run the simulation.
    sim = Simulation(params)
    sim.process(Task.generate(sim))
    for _ in range(params["num_developers"]):
        sim.process(Developer(sim).work())
    for _ in range(params["num_testers"]):
        sim.process(Tester(sim).work())
    sim.run()


if __name__ == "__main__":
    main(PARAMS)
