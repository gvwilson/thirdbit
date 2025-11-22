from collections import defaultdict
import csv
from itertools import count
import random
import sys
import simpy

PARAMS = {
    "max_task_duration": 10.0,
    "num_developers": 2,
    "random_seed": 12345,
    "simulation_duration": 10,
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
        self.queue = simpy.Store(self.env)

    def process(self, proc):
        self.env.process(proc)

    def run(self):
        self.env.run(until=self.params["simulation_duration"])

    def timeout(self, duration):
        return self.env.timeout(duration)

    @property
    def now(self):
        return self.env.now

    def task_arrival(self):
        return random.expovariate(1.0 / self.params["task_arrival_rate"])

    def task_duration(self):
        return random.uniform(1, self.params["max_task_duration"])


class Labeled:
    """Objects with unique IDs."""

    _ids = defaultdict(count)
    _all = defaultdict(list)

    def __init__(self):
        """Construct."""

        name = self.__class__.__name__
        self.id = next(Labeled._ids[name])
        Labeled._all[name].append(self)


class Task(Labeled):
    """A single (passive) task."""

    @staticmethod
    def generate(sim):
        """Generate tasks and add to the queue."""

        while True:
            yield sim.timeout(sim.task_arrival())
            task = Task(sim)
            yield sim.queue.put(task)


    def __init__(self, sim):
        """Construct."""

        super().__init__()
        self.arrived = sim.now
        self.duration = sim.task_duration()
        self.started = None
        self.completed = None

    def log(self):
        """Convert to loggable entry."""

        return (
            "task",
            self.id,
            log_fmt(self.duration),
            log_fmt(self.arrived),
            log_fmt(self.started),
            log_fmt(self.completed)
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
            task = yield self.sim.queue.get()
            task.started = self.sim.now
            yield self.sim.timeout(task.duration)
            task.completed = self.sim.now


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

def write_log(stream):
    """Write task details as CSV."""

    log = [("kind", "id", "duration", "arrived", "started", "completed")]
    log.extend(task.log() for task in Labeled._all["Task"])
    csv.writer(stream, lineterminator="\n").writerows(log)


def main(params):
    """Main driver."""

    update_params(params, sys.argv[1:])
    random.seed(params["random_seed"])

    sim = Simulation(params)
    sim.process(Task.generate(sim))
    for _ in range(params["num_developers"]):
        dev = Developer(sim)
        sim.process(dev.work())
    sim.run()

    write_log(sys.stdout)
    

if __name__ == "__main__":
    main(PARAMS)
