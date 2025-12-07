---
title: Handling Interruptions
date: 2025-12-07
---

The [previous post in this series][rework] looked at the effects of re-work on throughput.
Its version of the simulation assumed that
a task that needed to be re-done was given back to the developer who had originally worked on it,
and that she would tackle that task once she finished whatever she was doing at the time.
In reality,
though,
developers (and testers) often interrupt what they're doing,
switch to another task,
and then switch back.
This post looks at how to simulate that in [SimPy][simpy].

## A Simpler Model

To start with,
let's go back to a simpler model in which one process adds new tasks to a queue at random intervals,
while developers take tasks,
work on them,
and then mark them as done.
While we're building it,
we'll use these parameters:

```python
PARAMS = {
    "n_dev": 1,          # number of developers
    "rng_seed": 12345,   # random number generation seed
    "t_arrival": 8.0,    # mean task arrival time
    "t_dev": 5.0,        # median development time
    "t_interrupt": 3.0,  # time between interrupts
    "t_sim": 20,         # length of simulation
}
```

As before,
we define a `Simulation` class to hold all our bits and pieces.
Its constructor caches the parameters,
then creates the SimPy `Environment`,
the development queue,
and the developers.
It also creates a simple list called `.log` to store log messages:

```python
class Simulation:
    """Overall simulation."""

    def __init__(self, params):
        """Construct."""

        self.params = params
        self.env = simpy.Environment()
        self.dev_queue = simpy.Store(self.env)
        self.developers = [Developer(self) for _ in range(params["n_dev"])]
        self.log = []
```

For lack of anywhere better to put it,
we define the task generator as a method of `Simulation`.
The order of statements in the `while` loop ensures that
the first task is generated at t=0:

```python
class Simulation:
    …previous code…

    def generate(self):
        """Generate tasks at random intervals starting at t=0."""

        while True:
            yield self.dev_queue.put(Task(self))
            yield self.timeout(self.t_arrival())

    def process(self, proc):
        """Shortcut for running a process."""
        return self.env.process(proc)
```

As before,
we also give `Simulation` some convenience methods like `.process`
so that we can type `sim.process(…)` rather than `sim.env.process(…)`.

## Creating Interrupts

What's new in this simulation is another process
whose only purpose is to interrupt developers.
It does this by choosing a random developer `dev` every few clock ticks
and then calling `dev.proc.interrupt()`:

```python
class Simulation:
    …previous code…

    def annoy(self):
        """Generate annoying interruptions."""

        while True:
            yield self.timeout(self.params["t_interrupt"])
            dev = random.choice(self.developers)
            dev.proc.interrupt()
```

`dev.proc.interrupt()` only makes sense once we have looked at
the constructor for the `Developer` class:

```python
class Developer:
    """A generic worker."""

    def __init__(self, sim):
        """Construct."""

        self.sim = sim
        self.proc = self.sim.process(self.work())

    def work(self):
        …the generator simulating a developer's behavior…
```

Here's what's going on:

1.  `Developer.work` is (going to be) a generator that simulates
    an individual developer's behavior.

1.  Calling it as `self.work()` in `Developer.__init__` *doesn't* start a process.
    Instead, that call creates a generator object.

1.  We pass that generator object to `self.sim.process()`,
    which gives it to the SimPy `Environment` to run.
    Doing this means that developers start running as soon as they are created.

1.  Finally,
    `self.sim.process(…)` returns the generator object that was passed into it.
    We save this in the `Developer` object as `self.proc`
    so that we can access it later.
    (This step was the one that initially confused me.
    `Developer` isn't a SimPy process:
    the generator object created by calling `Developer.work` is the process.
    If we want to interrupt the process,
    we need to get at the generator object,
    and the logical place to store a reference to it is
    in the object that defines its behavior.)

So let's jump back to `Simulation.annoy`. It contains the lines:

```python
    dev = random.choice(self.developers)
    dev.proc.interrupt()
```

which mean:

1.  Choose a developer at random.

1.  Get a reference to that developer's generator object `dev.proc`.

1.  Call the object's `.interrupt` method.

The last of those steps injects a `simpy.Interrupt` exception into the process,
so let's take a look at how we handle that.

## Handling Interrupts

Here's a simple version of a developer that can handle interrupts:

```python
class Developer(Labeled):
    …constructor…

    def work(self):
        while True:
            req = None
            try:
                req = self.sim.dev_queue.get()
                task = yield req
                yield self.sim.timeout(task.dev_required)
            except simpy.Interrupt as exc:
                if req is not None:
                    req.cancel()
```

This developer does the following each time it goes around the `while` loop:

1.  Create a request to get a task from the development queue.

1.  `yield` that request,
    which hands the request to the SimPy `Environment`
    and suspends this process until the request can be satisfied.

1.  The result of yielding the request is a task from the development queue,
    so wait a while to simulate working on that task.

1.  *Unless* a `simpy.Interrupt` exception occurs,
    in which case the developer cancels the request for a task
    and goes around the loop again.

We have run into [the need to cancel][cancel] before.
In the first version of this code,
I assumed that interrupts would only occur while a developer was working on a task,
so the body of the `except` block was just `pass`:

```python
    # This version is wrong!
    def work(self):
        while True:
            req = None
            try:
                req = self.sim.dev_queue.get()
                task = yield req
                yield self.sim.timeout(task.dev_required)
            except simpy.Interrupt as exc:
                pass
```

What I found was that if the interrupt occurred while the developer was waiting on the queue,
and I *didn't* cancel the request,
subsequent requests were never satisfied.
In other words,
once a developer had been interrupted,
she would never get any more work.

## How It Behaves

I won't bother to show the code that adds log messages to `Simulation.log`
or collects the states of all the tasks when the simulation is done,
but here's the JSON output from a typical short run:

```
{
  "params": {
    …as shown earlier…
  },
  "messages": [
    "developer-0 0.00 start task-0",
    "developer-0 3.00 interrupted in task-0",
    "developer-0 6.00 interrupted in None",
    "developer-0 9.00 interrupted in None",
    "developer-0 12.00 interrupted in None",
    "developer-0 13.95 start task-1",
    "developer-0 15.00 interrupted in task-1",
    "developer-0 15.01 start task-2",
    "developer-0 16.68 complete task-2",
    "developer-0 18.00 interrupted in None"
  ],
  "tasks": [
    {
      "id": 0,
      "created": 0,
      "dev_required": 4.33,
      "state": ["dev_queue", "dev", "interrupted"]
    },
    {
      "id": 1,
      "created": 13.95,
      "dev_required": 5.72,
      "state": ["dev_queue", "dev", "interrupted"]
    },
    {
      "id": 2,
      "created": 15.01,
      "dev_required": 1.67,
      "state": ["dev_queue", "dev", "complete"]
    }
  ]
}
```

As you can see,
the first two tasks are interrupted and discarded while they're being worked on,
while the developer manages to finish the third task before she's interrupted.
The next step will be to resume tasks rather than just throwing them away.

[cancel]: @root/2025/12/03/you-have-to-cancel/
[rework]: @root/2025/12/04/the-effects-of-rework/
[simpy]: https://simpy.readthedocs.io/
