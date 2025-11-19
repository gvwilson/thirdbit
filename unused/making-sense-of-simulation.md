---
title: Making Sense of Simulation
date: 2025-11-20
---

I ended [yesterday's post][developer-pool] by saying that
we need to collect some data and do a bit of analysis.
[SimPy][simpy] [doesn't do monitoring][simpy-monitoring] out of the box,
so we have to roll our own.

## Tracking Time in Tasks

The first step is to update the class that represents a task
so that it can keep track of how much time it takes.
To do this,
we add two fields called `._current` (the most recent start-of-work time)
and `._elapsed` (the total time so far).
We then add three methods:
`.start` to signal the start of work,
`.end` to signal the end of work,
and `.is_complete` so that we can ask if the task has been completed:

```python
class TaskRecorder:
    """Task with uniformly-distributed durations that records activity."""

    _id = count()

    def __init__(self, params):
        self._id = next(TaskRecorder._id)
        self._duration = TaskRecorder.duration(params)
        self._elapsed = 0.0
        self._current = None

    def start(self, env):
        assert self._current is None
        self._current = env.now

    def end(self, env):
        assert self._current is not None
        self._elapsed += env.now - self._current
        self._current = None

    def is_complete(self):
        return (self._current is None) and (self._elapsed > 0.0)
```

The logic of `.is_complete` needs a bit of explanation.
When the task is initially created,
its current start time is `None`.
When it is being executed,
`._current` records the (simulated) time at which work started,
and when it's done,
we re-set `._current` to `None` and record the elapsed time in `._elapsed`.
The task is therefore complete if `._current` is `None`
*and* some elapsed time has been set.

With this in place,
we can modify the generator that simulates task execution
to signal the start and stop of work:

```python
def simulate_task(env, developers, task):
    """Simulate a task flowing through the system."""

    task.start(env)
    with developers.request() as req:
        yield req
        yield env.timeout(task._duration)
        task.end(env)
```

(We pass the simulation environment `env` to `task.start` and `task.end`
so that the task can check the current simulated time with `sim.now`.)

## Gathering Statistics

Now that each task is recording its elapsed time,
we need to gather statistics for all of them.
Let's go back to the `TaskRecord` class
and have each new task add itself to a list owned by the class:

```python
class TaskRecorder:
    """Task with uniformly-distributed durations that records activity."""

    …previous code…
    _all = []

    def __init__(self, params):
        …previous code…
        TaskRecorder._all.append(self)
```

When the simulation is finished,
we can walk through this list to find out
how much time was spent on each task
and whether that task was completed or not:

```python
PRECISION = 2


def write_log(params, stream):
    """Create and write entire log."""

    log = [("kind", "id", "elapsed", "completed")]
    log.extend([
        ("task", x._id, round(x._elapsed, PRECISION), x.is_complete())
        for x in TaskRecorder._all
    ])
    total = sum(x._elapsed for x in TaskRecorder._all)
    log.append(("total", "task", round(total, PRECISION), None))
    csv.writer(stream, lineterminator="\n").writerows(log)


def main(params):
    …previous code…
    write_log(params, sys.stdout)
```

Let's run it for 100 simulated timesteps
with two developers:

```
kind,id,elapsed,completed
task,0,1.09,True
task,1,3.69,True
task,2,2.74,True
…,…,…,…
task,39,0.0,False
task,40,0.0,False
task,41,0.0,False
total,task,378.68,
```

Cool!
Our simulation is working—except it isn't.

## Don't Trust, Just Verify

Take a look at the last line of the output shown above.
It's telling us that our workers did a total of 378.68 timesteps of work during this simulation,
but that's impossible:
we have two developers and the simulation ran for 100 timesteps,
so even if both developers were busy 100% of the time,
they couldn't have done more than 200 timesteps of work.
What's gone wrong?

The answer lies in `simulate_task`,
which we reproduce here from above:

```python
def simulate_task(env, developers, task):
    task.start(env)
    with developers.request() as req:
        yield req
        yield env.timeout(task._duration)
        task.end(env)
```

The problem is that we're including the time the task spends waiting for a developer
in our measure of how long the task was worked on.
The fix is to move `task.start` *after* `yield req`,
so that we start the task's clock when we start work on it:

```python
def simulate_task(env, developers, task):
    with developers.request() as req:
        yield req
        task.start(env)
        yield env.timeout(task._duration)
        task.end(env)
```

When we re-run the simulation with the same parameters,
we get:

```
kind,id,elapsed,completed
task,0,1.09,True
task,1,3.69,True
task,2,2.74,True
…,…,…,…
task,39,0.0,False
task,40,0.0,False
task,41,0.0,False
total,task,149.41,
```

This result is physically plausible but still puzzling:
why are the developers only busy 75% of the time?
Let's try running the simulation for 100,000 timesteps instead:

```
…,…,…,…
total,task,199961.93,
```

That works out to 99.98% utilization,
so the earlier figure of 75% seems to be due to warmup effects.

## What We've Learned

What I learned from this bug is that
badly-designed measurements can produce numbers that are wrong
without being obviously wrong.
I didn't immediately notice that worker utilization in the buggy simulation was impossible;
I don't believe I would have noticed at all if the measure or the simulation
were more complicated.
As I build more realistic simulations,
I'm going to add checks on the results
based on the properties of the model
(e.g., "we can't have done more work than is physically possible").
Similarly,
when we start to monitor real developers,
I'm going to think very carefully about whether
what I'm measuring is measuring what I want to.

[developer-pool]: @root/2025/11/19/simulating-a-developer-pool/
[simpy]: https://simpy.readthedocs.io/
[simpy-monitoring]: https://simpy.readthedocs.io/en/latest/topical_guides/monitoring.html
