---
title: Simulating a Developer Pool
date: 2025-11-19
---

Following [yesterday's post][starting-to-simulate]
about using [SimPy][simpy] for discrete event simulation,
let's have a look at a slightly more interesting scenario:
a pool of developers,
all of whom work at the same speed,
handling tasks of varying duration that arrive at random intervals.

## Overall Structure

The main function of the simulation takes a dictionary of parameter values,
creates a SimPy environment,
does a little bit of magic,
and then simulates the system for a specified length of time:

```python
def main(params):
    """Run simulation."""

    random.seed(params["random_seed"])
    env = simpy.Environment()
    developers = simpy.Resource(env, capacity=params["num_developers"])
    env.process(generate_tasks(params, env, developers))
    env.run(until=params["simulation_duration"])
```

The "magic" referred to earlier has two parts:

1.  Since the developers are all the same (for now),
    we can model them using a SimPy `Resource` with a fixed capacity.
    This basically acts as a pile of things:
    our processes can take a thing if one is available,
    but will be suspended if one is not.
2.  We then call `generate_tasks` to create the generator that adds new tasks to the system
    and give that generator to `env.process` to run.

## Generating Tasks

OK, what does `generate_tasks` do?

```python
def generate_tasks(params, env, developers):
    """Generates tasks at random intervals."""

    while True:
        yield env.timeout(random.expovariate(1.0 / params["task_arrival_rate"]))
	task = TaskUniform(params)
        env.process(simulate_task(env, developers, task))
```

Each time around the loop,
it calls `env.timeout` to create an object representing a delay
and uses `yield` to hand that to SimPy,
which suspends the process until that much simulated time has passed.
When it resumes,
the generator creates a new `TaskUniform` object (we'll look at that in a moment)
and then calls `simulate_task` to create a new process (i.e., a new generator)
to simulate the execution of that task.
(The `while True` in this function is a bit misleading:
this generator hands control back to SimPy each time it encounters the `yield` statement,
and only resumes if SimPy reschedules it,
so it only runs as long as SimPy wants it to.)

> When I first started working with SimPy,
> I found it a bit counter-intuitive to represent tasks as processes
> rather than using processes for the workers.
> It's possible to do the latter,
> but the code turns out to be simpler if we treat developers as a passive resource.
> Read into that what you will…

## What Kind of Randomness?

At this point we need to talk about math,
because `random.expovariate` is anything but intuitive.
Suppose that the probability of a task arriving at any moment is fixed
and completely independent of when the previous task arrived.
This is called a *memoryless* system,
and it turns out that the time between arrivals in such a system has an exponential distribution:
if the average arrival rate is λ events per unit time,
then the time between arrivals is an exponential random variable with mean 1/λ.
Real-world arrival rates are rarely this tidy,
but it's a good starting point.

## Representing Tasks

We now have two bits of code to explore:
the `TaskUniform` class that represents a task
and the `simulate_task` function that models its behavior.
The former just stores a unique ID and a duration,
and knows how to represent itself as a string for printing:

```python
class TaskUniform:
    """Task with uniformly-distributed durations."""

    _id = count()

    def __init__(self, params):
        self._id = next(TaskUniform._id)
        self._duration = random.uniform(1, params["max_task_duration"])

    def __str__(self):
        return f"task-{self._id}/{self._duration:.2f}"
```

Note that we've decided to model task durations as uniformly distributed
between 1.0 and some maximum value.
This might win a prize for "least realistic assumption",
but we'll come back and adjust it later.

## Simulating a Task

Finally,
we get to actually simulating a task.
As before,
the fact that this function uses `yield` means that it creates a generator;
I think that would have been clearer if a keyword like `gen` had been introduced in place of `def`,
but it is what it is:

```python
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
```

Going through this phrase by phrase:

1.  The task starts by reporting how many developers are available.
    (Remember, `developers` is a `Resource` with a fixed capacity;
    its `.count` tells us how much of that resource is currently being used.)
2.  The task then records the time at which it starts running.
    We don't have to do this right at the start of the function
    (before checking the number of available developers)
    because we're not checking the computer's actual clock:
    `env.now` gives us the current simulated time in the SimPy environment,
    and that time only advances when processes tell the framework
    that they want it to.
3.  We then ask for a developer using `developer.request()`.
    This method gives us an object that we store in `req`,
    which we immediately `yield` to tell SimPy what we want.
    If the request can be satisfied right away,
    SimPy immediately reschedules this process;
    if the resource is already at capacity,
    SimPy suspends this process until a developer is available.
4.  …which means that as soon as execution passes the `yield req` line,
    we know that a resource is available.
    We print a message to report how long the task had to wait for a developer…
5.  …and then `yield` the object created by calling `env.timeout` with the task's duration
    to tell SimPy that the task needs that much time to complete.
6.  Finally,
    we print another message to report when the task finished…
7.  …and give the developer back to the developer pool.
    *This isn't visible in the code*:
    it's done automatically when we reach the end of the `with` block,
    in the same way that a file opened in a `with` is automatically closed at the block's end.

## A Sample Run

Let's run the simulation with the following parameters:

```python
PARAMS = {
    "max_task_duration": 10.0,
    "task_arrival_rate": 2.0,
    "num_developers": 2,
    "simulation_duration": 20,
    "random_seed": 12345,
}
```

The output is:

```
1.08: task-0/1.09 arrives, 2 developers available
1.08: task-0/1.09 starts after delay 0.00
2.17: task-0/1.09 finishes
4.57: task-1/3.69 arrives, 2 developers available
4.57: task-1/3.69 starts after delay 0.00
5.49: task-2/2.74 arrives, 1 developers available
5.49: task-2/2.74 starts after delay 0.00
7.15: task-3/2.46 arrives, 0 developers available
7.42: task-4/4.90 arrives, 0 developers available
8.23: task-2/2.74 finishes
8.23: task-3/2.46 starts after delay 1.07
8.25: task-1/3.69 finishes
8.25: task-4/4.90 starts after delay 0.83
9.07: task-5/2.57 arrives, 0 developers available
10.68: task-6/4.19 arrives, 0 developers available
10.68: task-3/2.46 finishes
10.68: task-5/2.57 starts after delay 1.61
13.15: task-4/4.90 finishes
13.15: task-6/4.19 starts after delay 2.47
13.25: task-5/2.57 finishes
17.03: task-7/1.82 arrives, 1 developers available
17.03: task-7/1.82 starts after delay 0.00
17.34: task-6/4.19 finishes
18.85: task-7/1.82 finishes
```

Things are certainly happening:
tasks are arriving and either starting immediately
or waiting until a developer is available.
But is our code correct?
And what does it tell us about how long tasks take to complete
and how busy developers are?
To answer those questions,
we need to collect some data and do a bit of analysis.
Stay tuned…

[starting-to-simulate]: @root/2025/11/18/starting-to-simulate/
[simpy]: https://simpy.readthedocs.io/
