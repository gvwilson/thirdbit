---
title: Observability
date: 2025-11-30
---

So far we've been collecting whatever data we want
whenever something significant happens in the simulation,
but we can't do that in the real world.
Since we need to tidy up the simulation a bit,
let's  data collection a little more realistic as well.

## The Overall Simulation

As before,
we're going to store the major pieces of the simulation in a `Simulation` object
so that we don't have to pass lots of bits and pieces to every function and method.
This class holds:

-   the simulation parameters;
-   the [SimPy][simpy] `Environment`;
-   the developers (represented as `Developer` objects);
-   the queue of tasks waiting for a developer;
-   the testers (represeented as `Tester` objects) and the queue of tasks waiting for them;
    and
-   an instance of a new `Log` class that will collect data about the state of the simulation.

```python
class Simulation:
    """Overall simulation."""

    def __init__(self, params):
        """Construct."""

        self.params = params
        self.env = simpy.Environment()

        self.developers = [Developer(self) for _ in range(params["num_dev"])]
        self.dev_queue = simpy.PriorityStore(self.env)

        self.testers = [Tester(self) for _ in range(params["num_tester"])]
        self.test_queue = simpy.PriorityStore(self.env)

        self.logger = Log(self)
```

As before,
we provide some convenience methods to get at useful properties
of the underlying `Environment`:

```python
class Simulation:
    …previous code…

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
```

and put all the randomization here as well:

```python
class Simulation:
    …previous code…

    def rand_task_arrival(self):
        """Task arrival time."""
        return random.expovariate(1.0 / self.params["task_arrival"])

    def rand_test_time(self):
        """Testing time."""
        return random.lognormvariate(0, 1) * self.params["median_test_time"]

    def rand_rework(self):
        """Does this task need to be reworked?"""
        return random.uniform(0, 1) < self.params["prob_rework"]

    def rand_dev_time(self):
        """Development time."""
        return random.lognormvariate(0, 1) * self.params["median_dev_time"]
```

Finally,
we provide one method to generate new tasks
and one to launch all the active processes in the simulation:

```python
class Simulation:
    …previous code…

    def generate(self):
        """Generate tasks at random intervals starting at t=0."""

        yield self.dev_queue.put(Task(self))
        while True:
            yield self.timeout(self.rand_task_arrival())
            yield self.dev_queue.put(Task(self))

    def run(self):
        """Run the whole simulation."""

        self.process(self.generate())
        self.process(self.logger.work())
        for workers in (self.developers, self.testers):
            for w in workers:
                self.process(w.work())
        self.env.run(until=self.params["sim_time"])
```

Two things to note in the code above:

1.  We always generate the first task at time 0.
    We don't have to do this,
    but it always felt weird looking at the statistics
    to have a small delay at the start before anything happened.

2.  The logger is an active process,
    just like the developers, testers, and task generator.
    We'll look at it in more detail in a bit.

## Developers

Earlier posts in this series showed
how we give each developer (and tester) a unique ID
and how we automatically create lists of them.
We won't repeat that code here,
since the most interesting thing about a developer is the work she does:

```python
class Developer(Worker):

    def work(self):
        while True:
            task = yield self.sim.dev_queue.get()

            with WorkLog(
                self,
                (Worker.State.BUSY, Worker.State.IDLE),
                task,
                (Task.State.DEV, Task.State.WAIT_TEST),
                "n_dev",
                "t_dev",
            ):
                yield self.sim.timeout(task.required_dev)

            yield self.sim.test_queue.put(task)
```

If we ignore `WorkLog` for a moment,
we can see that `Developer.work` is:

```python
    def work(self):
        while True:
            task = yield self.sim.dev_queue.get()
            yield self.sim.timeout(task.required_dev)
            yield self.sim.test_queue.put(task)
```

i.e.,
wait to a get a take from the development queue,
pause for a while to do the work,
and then put the task in the testing queue.

## Recording Work

So what is `WorkLog`?
It's a *context manager*,
i.e.,
a class that does something at the start of a block
and then automatically does some cleanup at the end of the block.
In our case,
what it does at the start is record the start time of the work
and change the state flags of the worker and task:

```python
class WorkLog:
    """Context manager to keep track of elapsed time."""

    def __init__(self, worker, worker_states, task, task_states, key_num, key_time):
        """Construct."""

        self.worker = worker
        self.worker_states = worker_states
        self.task = task
        self.task_states = task_states
        self.key_num = key_num
        self.key_time = key_time
        self.start = None

    def __enter__(self):
        """Start the clock."""
        self.start = self.worker.sim.now
        self.worker.state = self.worker_states[0]
        self.task.state = self.task_states[0]
```

At the end of the block—i.e.,
after the simulated work is done—the context manager
records how long the worker spent and how many tasks it has processed,
then changes the states of the task and worker again:

```python
class WorkLog:
    …previous code…

    def __exit__(self, exc_type, exc_value, traceback):
        """Stop the clock."""

        elapsed = self.worker.sim.now - self.start

        self.worker.state = self.worker_states[1]
        self.worker["busy"] += elapsed
        self.worker["n_task"] += 1

        if self.task_states[1] is not None:
            self.task.state = self.task_states[1]
        self.task[self.key_num] += 1
        self.task[self.key_time] += elapsed

        return False
```

Using `WorkLog` adds eight lines to what was a three-line simulation loop,
but we've learned the hard way as this code evolves
that keeping the record keeping for developers and testers in sync is error-prone.
Putting that code in a class,
and ensuring that the end-of-work record keeping is always done,
speeds up development.

## Testers

The `Tester` class is similar to the `Developer` class:

```python
class Tester(Worker):

    def work(self):
        while True:
            task = yield self.sim.test_queue.get()

            with WorkLog(
                self,
                (Worker.State.BUSY, Worker.State.IDLE),
                task,
                (Task.State.TEST, None),
                "n_test",
                "t_test",
            ):
                yield self.sim.timeout(task.required_test)

            if self.sim.rand_rework():
                task.priority = Task.PRI_HIGH
                task.state = Task.State.WAIT_DEV
                self.sim.dev_queue.put(task)
            else:
                task.state = Task.State.COMPLETE
```

This class gets work from the ready-to-test queue,
and then decides once the work is done
whether the task needs to be re-developed or not.
If it does,
it goes back into the ready-to-develop queue with high priority
to ensure that tasks needing rework are done before tasks that haven't been touched yet.
Without this rule,
far fewer tasks are completed,
and far more tasks are half-done at the simulation's end.

## Logging

It's finally time to look at the `Log` class that records data.
Its constructor makes space to record snapshots of
the states of all the tasks in the system,
the lengths of all the queues,
and what the developers and testers are doing:

```python
class Log:
    """Keep a log of interesting things."""

    def __init__(self, sim):
        """Construct."""

        self.sim = sim
        self.snapshot = {
            "tasks": [],
            "queues": [],
            "workers": [],
        }
```

The generator that does the active work is simplicity itself:
record the state of the simulation,
then wait a fixed interval
(which we will initially set to one clock tick):

```python
    def work(self):
        while True:
            self._record()
            yield self.sim.timeout(self.sim.params["log_interval"])
```

The code to record the simulation state is a bit messy,
because it depends on the implementations of various classes,
but in brief it creates records for:

1.  the state of every task in the system;

2.  the lengths of the two queues; and

3.  the state of each developer and tester.

```python
    def _record(self):
        """Record a log entry at a particular moment."""

        now = self.sim.now
        for t in Labeled._all[Task]:
            self.snapshot["tasks"].append(
                {"time": now, "id": t.id, "state": str(t.state)}
            )
        for name, queue in (("dev", self.sim.dev_queue), ("test", self.sim.test_queue)):
            self.snapshot["queues"].append(
                {"time": now, "name": name, "length": len(queue.items)}
            )
        for kind, cls in (("dev", Developer), ("test", Tester)):
            for w in Labeled._all[cls]:
                self.snapshot["workers"].append(
                    {"time": now, "kind": kind, "id": w.id, "state": str(w.state)}
                )
```

## What Have We Learned?

The first thing we learned from this refactoring is that
roughly half the code is devoted to collecting data.
This won't come as a surprise to anyone who has ever built a monitoring tool:
figuring out what's going on is often as hard as making things happen,
and sometimes harder.

The second thing we've learned is that our simulation can still surprise us.
The graph on the left shows the lengths of the develpment and testing queues over time,
while the one on the right shows how many tasks are in each of the possible states:

<div class="row">
  <div class="col-6 center">
    <img src="@root/files/2025/11/30/sample_queues.svg" alt="queue lengths" width="90%">
    <br>
    Queue Lengths
  </div>
  <div class="col-6 center">
    <img src="@root/files/2025/11/30/sample_tasks.svg" alt="task states" width="90%">
    <br>
    Task States
  </div>
</div>

The steady growth in the number of tasks waiting for a developer makes sense:
we're generating new ones faster than they can be completed.
But why does the length of the testing queue rise and then fall?
Is it just random variation?
Or is it revealing some unexpected property of our development process?
That question will have to wait for tomorrow.

[simpy]: https://simpy.readthedocs.io/
