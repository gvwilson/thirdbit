---
title: Refactoring the Simulation
date: 2025-11-22
---

After [yesterday's experiments with rework][rework]
I was going to spend a post or two building some charts,
but apparently people find a task-centric simulation less natural than a worker-centric one,
so instead I'm going to do some rearchitecting.

## Parameters

Let's start by going back to a pool of developers doing tasks one at a time without rework.
As before,
we'll define some default parameters,
including a random number seed to ensure reproducibility:

```python
PARAMS = {
    "max_task_duration": 10.0,
    "num_developers": 2,
    "random_seed": 12345,
    "simulation_duration": 10,
    "task_arrival_rate": 2.0,
}
```

To allow ad hoc experiments,
we can add a helper function `update_params` to parse a command line like:

```shell
python sim.py simulation_duration=50 random_seed=67890
```

and override the default parameters.
(You can see the function in [the source code][sim-source].)

## Bundling Simulation Elements

As our simulation becomes more complex,
we're going to have more assets to manage:
pools of developers,
a work queue,
and eventually some testers and maybe even a manager or two.
Rather than passing a dozen objects around,
let's define a `Simulation` class to store them all:

```python
class Simulation:
    """Store simulation artifacts."""

    def __init__(self, params):
        self.params = params
        self.env = simpy.Environment()
        …more stuff will go here…

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
```

To save ourselves from repeatedly needing to type `sim.env`,
this class provides pass-through methods for the simulation environment's key methods and properties.
And since it is storing the simulation parameters,
it seems like the logical place to put the code
that uses those parameters to generate task arrival times and durations.

## Tasks

This version of the simulator has active workers and passive tasks,
i.e.,
the workers are going to be processes that act on tasks.
A task is therefore just a sack full of properties like
when it arrived,
how long it takes to complete,
when work on it started,
and when work was completed:

```python
class Task(Labeled):
    """A single (passive) task."""

    …more stuff will go here…

    def __init__(self, sim):
        """Construct."""

        super().__init__()
        self.arrived = sim.now
        self.duration = sim.task_duration()
        self.started = None
        self.completed = None

        …more stuff will go here…
```

Note that `Task` is derived from a generic class called `Labeled`.
This class automatically gives each instance of `Task` a unique integer ID
and keeps a list of all the tasks created so far;
if you're interested,
you can see the magic in [the source code][sim-source].

## Where Do Tasks Go?

Before we move on to modeling developers,
let's define a generator to create new tasks
and give the simulation a place to store them.
For the latter,
we will use a SimPy `Store`,
which provides a queue with `put` and `get` methods:

```python
class Simulation:

    def __init__(self, params):
        …previous code…
        self.queue = simpy.Store(self.env)
```

We then define a generator to add new tasks to this queue at random intervals.
This generator could be a free-standing function,
but we're likely to want to add other generators to the simulation in the future,
so let's make it a static method of the `Task` class instead:

```python
class Task(Labeled):

    @staticmethod
    def generate(sim):
        while True:
            yield sim.timeout(sim.task_arrival())
            task = Task(sim)
            yield sim.queue.put(task)
```

As we explained in [the first post in this series][starting],
`generate`'s use of `yield` means that it isn't a regular function.
Instead,
it creates a generator that SimPy can suspend and restart as often as it wants.
Each time around the `while` loop,
`generate` calls `sim.task_arrival()` to generate a random delay,
then calls `sim.timeout()` to create an object that means,
"Please suspend this generator for this length of time."
The first `yield` inside the loop passes that object to SimPy,
which parks the generator until that much simulated time has passed.
When the generator resumes,
it creates a new task object and adds it to the queue of pending work.

> My first implementation of this function had a bug:
> it called `sim.queue.put(task)` but didn't `yield` the result.
> It took me a couple of minutes to remember that
> a SimPy `Store` can have a limited capacity,
> and that an attempt to add a new item to a `Store` will block
> until there's room for it.
> `sim.queue.put(task)` therefore doesn't actually add the object to the store;
> instead,
> it creates a temporary object that means,
> "Please add this to the store when there's space."
> The generator has to give that temporary object to SimPy with `yield`
> so that the framework can suspend the generator if necessary.
> Our work queue has infinite capacity,
> so the generator will never block waiting for space,
> but we still need to use `yield`.

## Modeling Developers

With all that in place,
modeling each developer as an active process is fairly straightforward:

```python
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
```

As with `Task`,
we derive `Developer` from `Labeled` so that
each developer will automatically have a unique integer ID.
`Developer.work` repeatedly gets a task from the work queue
(blocking if necessary until one is available),
records the task's start time,
suspends itself for some simulated length of time,
and then records the task's completion time.

## Logging

Once the simulation is done,
we're going to want to look at how many tasks were completed
and how long tasks spent waiting for a developer:

```python
def write_log(stream):
    """Write task details as CSV."""

    log = [("kind", "id", "duration", "arrived", "started", "completed")]
    log.extend(task.log() for task in Labeled._all["Task"])
    csv.writer(stream, lineterminator="\n").writerows(log)
```

`Labeled._all["Task"]` is a list of all the task objects created so far
(again, see [the source code][sim-source] if you want details),
while `task.log()` is just:

```python
class Task(Labeled):

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
```

with a bit of helper code:

```python
PRECISION = 2

def log_fmt(val):
    return None if val is None else round(val, PRECISION)
```

## The Output

If we run the simulation with the default parameter values,
we get this output:

```
kind,id,duration,arrived,started,completed
task,0,1.09,1.08,1.08,2.17
task,1,3.69,4.57,4.57,8.25
task,2,2.74,5.49,5.49,8.23
task,3,2.46,7.15,8.23,
task,4,4.9,7.42,8.25,
task,5,2.57,9.07,,
```

If we reformat this as a table:

| kind | id | duration | arrived | started | completed |
| ---- | -: | -------: | ------: | ------: | --------: |
| task |  0 |     1.09 |    1.08 |    1.08 |      2.17 |
| task |  1 |     3.69 |    4.57 |    4.57 |      8.25 |
| task |  2 |     2.74 |    5.49 |    5.49 |      8.23 |
| task |  3 |     2.46 |    7.15 |    8.23 |           |
| task |  4 |     4.9  |    7.42 |    8.25 |           |
| task |  5 |     2.57 |    9.07 |         |           |

we can see that work started on the first three tasks as soon as they arrived,
that work started on the next two after a delay but didn't finish by the time the simulation ended,
and that the last task wasn't even started.

## Some Introspection

Is this worker-centric design better that the previous task-centric design?
It was certainly easier to write,
but that's probably because I learned more about SimPy
and thought through design questions
while working on the earlier versions.
The real test is whether *you*, the reader, find it easier or harder to follow.
If you have an opinion,
please [reach out](mailto:gvwilson@third-bit.com).

[rework]: @root/2025/11/21/simulating-rework/
[sim-source]: https://github.com/gvwilson/thirdbit/blob/main/src/2025/11/22/sim.py
[starting]: @root/2025/11/18/starting-to-simulate/
