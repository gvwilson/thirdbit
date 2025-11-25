import argparse
from collections import defaultdict
from itertools import count
import json
import random
import sys
import simpy

PARAMS = {
    "max_dev_time": 10.0,
    "min_test_fraction": 0.5,
    "max_test_fraction": 1.5,
    "num_developers": 2,
    "num_testers": 2,
    "random_seed": 12345,
    "simulation_time": 1000,
    "task_arrival_rate": 2.0,
}
PRECISION = 2

TASK_KEYS = (
    "arrived",
    "dev_queue_length",
    "dev_time",
    "dev_start",
    "dev_end",
    "test_queue_length",
    "test_time",
    "test_start",
    "test_end",
)
DEVELOPER_KEYS = (
    "working",
    "waiting",
)
TESTER_KEYS = (
    "working",
    "waiting",
)


def log_fmt(val):
    """Format floating point values for log."""

    return None if val is None else round(val, PRECISION)


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

    def dev_time(self):
        return random.uniform(1, self.params["max_dev_time"])

    def test_time(self, task):
        return task["dev_time"] * random.uniform(
            self.params["min_test_fraction"], self.params["max_test_fraction"]
        )


class Labeled:
    """Objects with unique IDs."""

    _ids = defaultdict(count)
    _all = defaultdict(list)

    def __init__(self):
        """Construct."""

        name = self.__class__.__name__
        self.id = next(Labeled._ids[name])
        Labeled._all[name].append(self)
        self._times = defaultdict(float)

    def __getitem__(self, key):
        """Get recorded time."""
        return self._times[key]

    def __setitem__(self, key, value):
        """Record a time."""
        self._times[key] = value


class Task(Labeled):
    """A single (passive) task."""

    _dev_queue = []
    _test_queue = []

    @staticmethod
    def generate(sim):
        """Generate tasks and add to the development queue."""

        while True:
            yield sim.timeout(sim.task_arrival())
            task = Task(sim)
            Task._dev_queue.append((sim.now, len(sim.dev_queue.items)))
            yield sim.dev_queue.put(task)

    def __init__(self, sim):
        """Construct."""

        super().__init__()
        self["arrived"] = sim.now
        self["dev_time"] = sim.dev_time()
        self["test_time"] = sim.test_time(self)


class Developer(Labeled):
    """A single (active) developer."""

    def __init__(self, sim):
        """Construct."""

        super().__init__()
        self.sim = sim

    def work(self):
        """Simulate work."""

        while True:
            now = self.sim.now
            task = yield self.sim.dev_queue.get()
            self["waiting"] += self.sim.now - now

            now = task["dev_start"] = self.sim.now
            yield self.sim.timeout(task["dev_time"])
            task["dev_end"] = self.sim.now
            self["working"] += self.sim.now - now

            Task._test_queue.append((self.sim.now, len(self.sim.test_queue.items)))
            yield self.sim.test_queue.put(task)


class Tester(Labeled):
    """A single (active) tester."""

    def __init__(self, sim):
        """Construct."""

        super().__init__()
        self.sim = sim

    def work(self):
        """Simulate work."""

        while True:
            now = self.sim.now
            task = yield self.sim.test_queue.get()
            self["waiting"] += self.sim.now - now

            now = task["test_start"] = self.sim.now
            yield self.sim.timeout(task["test_time"])
            self["working"] += self.sim.now - now
            task["test_end"] = self.sim.now


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


def make_log(sim):
    """Save log as JSON."""

    log = {}

    for name, entries in (
        ("dev_queue", Task._dev_queue),
        ("test_queue", Task._test_queue),
    ):
        log[name] = [
            {"time": log_fmt(time), "count": length} for (time, length) in entries
        ]

    time_log = [("kind", "id", "key", "value")]
    for class_name, keys in (
        ("Task", TASK_KEYS),
        ("Developer", DEVELOPER_KEYS),
        ("Tester", TESTER_KEYS),
    ):
        name = class_name.lower()
        log[name] = [
            {"name": name, "id": obj.id, **{k: log_fmt(obj[k]) for k in keys}}
            for obj in Labeled._all[class_name]
        ]

    return log


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

    # Report results.
    log = make_log(sim)
    json.dump(log, sys.stdout)


if __name__ == "__main__":
    main(PARAMS)
