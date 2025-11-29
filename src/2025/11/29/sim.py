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
    "simulation_time": 10000,
    "task_arrival_rate": 3,
    "test_fraction": [0.5, 1.5],
}
PRECISION = 2

PRI_REWORK = 0
PRI_NEW = 1
PROB_REWORK = [0.0, 0.1, 0.3, 0.5]

class Simulation:
    """Store simulation artifacts."""

    def __init__(self, params):
        self.params = params
        self.env = simpy.Environment()
        self.dev_queue = simpy.PriorityStore(self.env)
        self.test_queue = simpy.PriorityStore(self.env)

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
        median = (1 + self.params["max_dev_time"]) / 2.0
        return random.lognormvariate(0, 1) * median

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

    @staticmethod
    def reset():
        Labeled._ids = defaultdict(count)
        Labeled._all = defaultdict(list)

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
            yield sim.dev_queue.put(simpy.PriorityItem(PRI_NEW, task))

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)
        self["dev_time"] = sim.dev_time()
        self["test_time"] = sim.test_time(self)
        self["time_dev"] = 0
        self["count_dev"] = 0 
        self["time_test"] = 0
        self["count_test"] = 0
        self["done"] = False


class Developer(Labeled):
    """A single developer."""

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)

    def work(self):
        """Simulate work."""

        while True:
            item = yield self.sim.dev_queue.get()
            priority, task = item
            start = self.sim.now
            yield self.sim.timeout(task["dev_time"])
            task["time_dev"] += (self.sim.now - start)
            task["count_dev"] += 1
            yield self.sim.test_queue.put(item)


class Tester(Labeled):
    """A single tester."""

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)

    def work(self):
        """Simulate work."""

        while True:
            item = yield self.sim.test_queue.get()
            priority, task = item
            start = self.sim.now
            yield self.sim.timeout(task["test_time"])
            task["time_test"] += (self.sim.now - start)
            task["count_test"] += 1
            if self.sim.task_rework():
                self.sim.dev_queue.put(simpy.PriorityItem(PRI_REWORK, task))
            else:
                task["done"] = True


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


def log_fmt(val):
    """Format floating point values for log."""

    return None if val is None else round(val, PRECISION)


def make_log(quarter):
    """Create report of results."""
    return [
        {
            "quarter": quarter,
            "id": t.id,
            "time_dev": log_fmt(t["time_dev"]),
            "count_dev": log_fmt(t["count_dev"]),
            "time_test": log_fmt(t["time_test"]),
            "count_test": log_fmt(t["count_test"]),
        }
        for t in Labeled._all["Task"]
    ]


def main(params):
    """Main driver."""

    # Handle command-line arguments and parameters.
    args = parse_args()
    update_params(params, args.params)
    random.seed(params["random_seed"])

    # Run simulations.
    log = []
    for quarter, prob in enumerate(PROB_REWORK):
        Labeled.reset()
        sim = Simulation({**params, "prob_rework": prob})
        sim.process(Task.generate(sim))
        for _ in range(params["num_developers"]):
            sim.process(Developer(sim).work())
        for _ in range(params["num_testers"]):
            sim.process(Tester(sim).work())
        sim.run()
        print(quarter, sum(t["done"] for t in Labeled._all["Task"]), file=sys.stderr)
        log.extend(make_log(quarter + 1))

    # Report results.
    json.dump(log, sys.stdout)


if __name__ == "__main__":
    main(PARAMS)
