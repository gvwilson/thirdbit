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
    """Create log."""

    def __init__(self, sim):
        """Construct."""

        self.sim = sim

    def get_log(self):
        """Get entire log."""

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
            "workers": workers,
        }


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

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)
        self.dev_required = self.sim.t_dev()
        self.dev_done = 0.0
        self.test_required = self.sim.t_test()
        self["t_create"] = self.sim.now
        self.developer = None


class Developer(Labeled):
    """A developer."""

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)
        self.pending = []

    def work(self):
        """Simulate."""

        while True:
            if len(self.pending) > 0:
                task = self.pending.pop(0)
            else:
                task = yield self.sim.dev_queue.get()
                task.developer = self
            t_start = self.sim.now
            try:
                yield self.sim.timeout(task.dev_required - task.dev_done)
            except simpy.Interrupt as exc:
                pass # FIXME

            yield self.sim.test_queue.put(task)


class Tester(Labeled):
    """A tester."""

    def work(self):
        """Simulate."""

        while True:
            task = yield self.sim.test_queue.get()
            yield self.sim.timeout(task.test_required)
            if self.sim.p_rework_needed():
                assert task.developer is not None
                task.developer.pending.append(task)
                # FIXME: interrupt developer


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
    json.dump(Log(sim).get_log(), sys.stdout)


if __name__ == "__main__":
    main(PARAMS)
