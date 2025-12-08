"""Active task simulation."""

import argparse
from collections import defaultdict
from itertools import count
import json
import random
import simpy
import sys


MIN_FLOAT_DIFF = 1.0e-6
PREC = 2

# Simulation parameters.
PARAMS = {
    "n_dev": 1,
    "rng_seed": 12345,
    "t_task_arrival": 8.0,
    "t_dev": 5.0,
    "t_interrupt_arrival": 3.0,
    "t_interrupt_duration": 1.0,
    "t_sim": 20,
}


class Simulation:
    """Overall simulation."""

    def __init__(self, params):
        """Construct."""

        self.params = params
        self.env = simpy.Environment()
        self.dev_queue = simpy.Store(self.env)
        self.developers = [Developer(self) for _ in range(params["n_dev"])]
        self._log = []

    def log(self, author, msg):
        self._log.append(f"{self.now:.2f} {author}: {msg}")

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
            task = Task(self)
            task.state.append("dev_queue")
            yield self.dev_queue.put(task)
            yield self.timeout(self.t_task_arrival())

    def annoy(self):
        """Generate annoying interruptions."""

        while True:
            yield self.timeout(self.t_interrupt_arrival())
            dev = random.choice(self.developers)
            dev.proc.interrupt(self.t_interrupt_duration())

    def run(self):
        """Run the whole simulation."""

        self.process(self.generate())
        self.process(self.annoy())
        self.env.run(until=self.params["t_sim"])

    def t_task_arrival(self):
        """Task arrival time."""
        return random.expovariate(1.0 / self.params["t_task_arrival"])

    def t_interrupt_arrival(self):
        """Interrupt arrival time."""
        return random.expovariate(1.0 / self.params["t_interrupt_arrival"])

    def t_interrupt_duration(self):
        """Interrupt duration."""
        return random.lognormvariate(0, 1) * self.params["t_interrupt_duration"]

    def t_dev(self):
        """Development time."""
        return random.lognormvariate(0, 1) * self.params["t_dev"]


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

    # What to save for tasks.
    LOG_KEYS = ("id", "created", "started", "completed", "developer_id", "state", "dev_required", "dev_done")

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)
        self.created = self.sim.now
        self.started = None
        self.completed = None
        self.dev_required = self.sim.t_dev()
        self.dev_done = 0.0
        self.state = []
        self.developer_id = None

    def is_done(self):
        """Is this task complete?"""
        return abs(self.dev_required - self.dev_done) < MIN_FLOAT_DIFF


class Developer(Labeled):
    """A generic worker."""

    # What to save for developers.
    LOG_KEYS = ("id", "n_start", "n_interrupt", "n_complete")

    def __init__(self, sim):
        """Construct."""

        super().__init__(sim)
        self.proc = self.sim.process(self.work())
        self.n_start = 0
        self.n_complete = 0
        self.n_interrupt = 0

    def work(self):
        """Simulate."""

        task = None
        interrupt_delay = None
        while True:
            self.sim.log(self, "top of loop")
            req = None
            try:
                if interrupt_delay is not None:
                    self.sim.log(self, f"start interrupt {round(interrupt_delay, PREC)}")
                    yield self.sim.timeout(interrupt_delay)
                    self.sim.log(self, f"…end interrupt {round(interrupt_delay, PREC)}")
                    interrupt_delay = None
                else:
                    if task is None:
                        self.sim.log(self, "start wait for new task")
                        req = self.sim.dev_queue.get()
                        task = yield req
                        task.developer_id = self.id
                        task.started = self.sim.now
                        self.n_start += 1
                        self.sim.log(self, f"…end wait for new task {task}")
                    self.sim.log(self, f"start work {task} ({task.dev_done:.2f} / {task.dev_required:.2f})")
                    t_start = self.sim.now
                    yield self.sim.timeout(task.dev_required - task.dev_done)
                    task.dev_done += self.sim.now - t_start
                    self.sim.log(self, f"…end work {task} ({task.dev_done:.2f} / {task.dev_required:.2f})")
                    if task.is_done():
                        self.sim.log(self, f"complete {task} ({task.dev_done:.2f} / {task.dev_required:.2f})")
                        self.n_complete += 1
                        task.completed = self.sim.now
                        task.state.append("complete")
                        task = None
            except simpy.Interrupt as exc:
                self.n_interrupt += 1
                self.sim.log(self, f"interrupt with {task} for {exc.cause:.2f}")
                if req is not None:
                    req.cancel()
                if task is not None:
                    task.state.append("interrupt")
                interrupt_delay = exc.cause


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

    tasks = [{k: r(getattr(t, k)) for k in Task.LOG_KEYS} for t in Labeled._all[Task]]
    devs = [{k: r(getattr(w, k)) for k in Developer.LOG_KEYS} for w in Labeled._all[Developer]]
    return {
        "params": sim.params,
        "messages": sim._log,
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
