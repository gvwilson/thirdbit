"""Pool of developers with tasks as processes and the possibility of rework."""

import csv
from itertools import count
import random
import sys
import simpy

PARAMS = {
    "num_simulations": 1,
    "max_task_duration": 10.0,
    "rework_probability": 0.6,
    "task_arrival_rate": 2.0,
    "num_developers": 2,
    "simulation_duration": 20,
    "random_seed": 12345,
}
PRECISION = 2


class Task:
    """Tasks."""

    _id = count()
    _all = []

    @staticmethod
    def arrival(params):
        return random.expovariate(1.0 / params["task_arrival_rate"])

    @staticmethod
    def duration(params):
        return random.uniform(1, params["max_task_duration"])

    @staticmethod
    def reset():
        Task._all = []

    def __init__(self, params):
        self._id = next(Task._id)
        self._duration = Task.duration(params)
        self._elapsed = 0.0
        self._current = None
        self._complete = False
        Task._all.append(self)

    def start(self, env):
        assert self._current is None
        self._current = env.now

    def end(self, env):
        assert self._current is not None
        self._elapsed += env.now - self._current
        self._current = None

    def completed(self):
        assert not self._complete
        self._complete = True

    def is_complete(self):
        return self._complete


def simulate_task(params, env, developers, task):
    """Simulate a task flowing through the system."""

    while True:
        with developers.request() as req:
            yield req
            task.start(env)
            yield env.timeout(task._duration)
            task.end(env)
            if random.uniform(0, 1) >= params["rework_probability"]:
                task.completed()
                break


def generate_tasks(params, env, developers):
    """Generates tasks at random intervals."""

    while True:
        yield env.timeout(Task.arrival(params))
        task = Task(params)
        env.process(simulate_task(params, env, developers, task))


def get_log(kind, cls):
    """Build one set of log entries."""

    records = [
        (kind, x._id, round(x._elapsed, PRECISION), x._complete) for x in cls._all
    ]
    total = sum(x._elapsed for x in cls._all)
    completed = sum(x._complete for x in cls._all)
    return records, round(total, PRECISION), completed


def get_params(params):
    """Convert parameters to log entries."""

    return [
        ("parameter", name, value, None)
        for name, value in sorted(params.items())
    ]


def write_log(params, stream, *args):
    """Create and write entire log."""

    log = [("kind", "id", "elapsed", "completed")]
    log.extend(get_params(params))
    for name, data in args:
        records, total, completed = get_log(name, data)
        log.extend(records)
        log.append(("total", name, total, None))
        log.append(("completed", name, completed, None))
    csv.writer(stream, lineterminator="\n").writerows(log)


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


def main(params):
    """Run simulation."""

    update_params(params, sys.argv[1:])
    random.seed(params["random_seed"])
    for _ in range(params["num_simulations"]):
        Task.reset()
        env = simpy.Environment()
        developers = simpy.Resource(env, capacity=params["num_developers"])
        env.process(generate_tasks(params, env, developers))
        env.run(until=params["simulation_duration"])
        write_log(params, sys.stdout, ("task", Task))


if __name__ == "__main__":
    main(PARAMS)
