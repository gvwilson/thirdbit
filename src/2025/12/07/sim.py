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
    "rng_seed": 12345,
    "t_arrival": 8.0,
    "t_dev": 5.0,
    "t_interrupt": 3.0,
    "t_sim": 20,
}

# What to save for tasks.
TASK_KEYS = ("id", "created", "state", "dev_required")

# What to save for workers.
WORKER_KEYS = ("id",)


class Simulation:
    """Overall simulation."""

    def __init__(self, params):
        """Construct."""

        self.params = params
        self.env = simpy.Environment()
        self.dev_queue = simpy.Store(self.env)
        self.developers = [Developer(self) for _ in range(params["n_dev"])]
        self.log = []

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

        while True:
            yield self.dev_queue.put(Task(self))
            yield self.timeout(self.t_arrival())

    def annoy(self):
        """Generate annoying interruptions."""

        while True:
            yield self.timeout(self.params["t_interrupt"])
            dev = random.choice(self.developers)
            dev.proc.interrupt()

    def run(self):
        """Run the whole simulation."""

        self.process(self.generate())
        self.process(self.annoy())
        self.env.run(until=self.params["t_sim"])

    def t_dev(self):
        """Development time."""
        return random.lognormvariate(0, 1) * self.params["t_dev"]

    def t_arrival(self):
        """Task arrival time."""
        return random.expovariate(1.0 / self.params["t_arrival"])


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
        self.state = ["dev_queue"]


class Developer(Labeled):
    """A generic worker."""

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)
        self.proc = self.sim.process(self.work())

    def work(self):
        """Simulate."""

        while True:
            task = None
            req = None
            try:
                req = self.sim.dev_queue.get()
                task = yield req
                self.sim.log.append(f"{self} {self.sim.now:.2f} start {task}")
                task.state.append("dev")
                yield self.sim.timeout(task.dev_required)
                self.sim.log.append(f"{self} {self.sim.now:.2f} complete {task}")
                task.state.append("complete")
            except simpy.Interrupt as exc:
                self.sim.log.append(f"{self} {self.sim.now:.2f} interrupted in {task}")
                if req is not None:
                    req.cancel()
                if task is not None:
                    task.state.append("interrupted")


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

    def r(val):
        return round(val, 2) if isinstance(val, float) else val

    tasks = [{k: r(getattr(t, k)) for k in TASK_KEYS} for t in Labeled._all[Task]]
    devs = [{k: r(getattr(w, k)) for k in WORKER_KEYS} for w in Labeled._all[Developer]]
    return {
        "params": sim.params,
        "messages": sim.log,
        "tasks": tasks,
        "devs": devs,
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
