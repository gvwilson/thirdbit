import argparse
from collections import defaultdict
import csv
from itertools import count
from prettytable import PrettyTable
import random
import sys
import simpy

PARAMS = {
    "max_dev_time": 10.0,
    "max_test_time": 8.0,
    "num_developers": 2,
    "num_testers": 3,
    "random_seed": 12345,
    "simulation_time": 20,
    "task_arrival_rate": 2.0,
}
PRECISION = 2


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

    def test_time(self):
        return random.uniform(1, self.params["max_test_time"])


class Labeled:
    """Objects with unique IDs."""

    _ids = defaultdict(count)
    _all = defaultdict(list)

    def __init__(self):
        """Construct."""

        name = self.__class__.__name__
        self.id = next(Labeled._ids[name])
        Labeled._all[name].append(self)
        self._times = defaultdict(lambda: None)

    def __getitem__(self, key):
        """Get recorded time."""
        return self._times[key]

    def __setitem__(self, key, value):
        """Record a time."""
        self._times[key] = value


class Task(Labeled):
    """A single (passive) task."""

    @staticmethod
    def generate(sim):
        """Generate tasks and add to the development queue."""

        while True:
            yield sim.timeout(sim.task_arrival())
            task = Task(sim)
            yield sim.dev_queue.put(task)


    def __init__(self, sim):
        """Construct."""

        super().__init__()
        self["arrived"] = sim.now
        self["dev_time"] = sim.dev_time()
        self["test_time"] = sim.test_time()

    def log(self, keys):
        """Convert to loggable entry."""

        return (
            "task",
            self.id,
            *(log_fmt(self[key]) for key in keys)
        )


class Developer(Labeled):
    """A single (active) developer."""

    def __init__(self, sim):
        """Construct."""

        super().__init__()
        self.sim = sim

    def work(self):
        """Simulate work."""

        while True:
            task = yield self.sim.dev_queue.get()
            task["dev_start"] = self.sim.now
            yield self.sim.timeout(task["dev_time"])
            task["dev_end"] = self.sim.now
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
            task = yield self.sim.test_queue.get()
            task["test_start"] = self.sim.now
            yield self.sim.timeout(task["test_time"])
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

def make_log():
    """Save log details as table."""

    time_keys = (
        "arrived",
        "dev_time",
        "dev_start",
        "dev_end",
        "test_time",
        "test_start",
        "test_end"
    )
    log = [("kind", "id", *time_keys)]
    log.extend(task.log(time_keys) for task in Labeled._all["Task"])
    return log


def parse_args():
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--table", action="store_true", help="show results as table")
    parser.add_argument("params", nargs="*", help="parameter overrides")
    return parser.parse_args()


def main(params):
    """Main driver."""

    args = parse_args()
    update_params(params, args.params)
    random.seed(params["random_seed"])

    sim = Simulation(params)
    sim.process(Task.generate(sim))
    for _ in range(params["num_developers"]):
        dev = Developer(sim)
        sim.process(dev.work())
    for _ in range(params["num_testers"]):
        tester = Tester(sim)
        sim.process(tester.work())
    sim.run()

    log = make_log()
    if args.table:
        table = PrettyTable()
        table.align = "r"
        table.field_names = log[0]
        table.add_rows(log[1:])
        print(table)
    else:
        csv.writer(sys.stdout, lineterminator="\n").writerows(log)
    

if __name__ == "__main__":
    main(PARAMS)
