"""Pool of developers with tasks as processes."""

from itertools import count
import random
import simpy

PARAMS = {
    "max_task_duration": 10.0,
    "task_arrival_rate": 2.0,
    "num_developers": 2,
    "simulation_duration": 20,
    "random_seed": 12345,
}


class TaskUniform:
    """Task with uniformly-distributed durations."""

    _id = count()

    def __init__(self, params):
        self._id = next(TaskUniform._id)
        self._duration = random.uniform(1, params["max_task_duration"])

    def __str__(self):
        return f"task-{self._id}/{self._duration:.2f}"


def simulate_task(env, developers, task):
    """Simulate a task flowing through the system."""

    available = developers.capacity - developers.count
    print(f"{env.now:.2f}: {task} arrives, {available} available")
    request_start = env.now
    with developers.request() as req:
        yield req
        delay = env.now - request_start
        print(f"{env.now:.2f}: {task} starts after delay {delay:.2f}")
        yield env.timeout(task._duration)
        print(f"{env.now:.2f}: {task} finishes")


def generate_tasks(params, env, developers):
    """Generates tasks at random intervals."""

    while True:
        yield env.timeout(random.expovariate(1.0 / params["task_arrival_rate"]))
        task = TaskUniform(params)
        env.process(simulate_task(env, developers, task))


def main(params):
    """Run simulation."""

    random.seed(params["random_seed"])
    env = simpy.Environment()
    developers = simpy.Resource(env, capacity=params["num_developers"])
    env.process(generate_tasks(params, env, developers))
    env.run(until=params["simulation_duration"])


if __name__ == "__main__":
    main(PARAMS)
