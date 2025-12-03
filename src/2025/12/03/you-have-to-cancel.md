---
title: You Have to Cancel
date: 2025-12-03
---

It has taken me almost three hours to answer [my earlier question][sturdiness] about [SimPy][simpy],
and once I recover,
I'm going to submit a couple of PRs for their documentation.
To recap,
the most recent version of the simulation
all testers to bounce work back to the development queue if they find bugs:

```
+----------------+    +-----------+    +------------+    +------------+    +---------+
| task generator | -> | dev queue | -> | developers | -> | test queue | -> | testers |
+----------------+    +-----------+    +------------+    +------------+    +---------+
                            ^                                                   |
                            |                                                   |
                            +---------------------------------------------------+
```

I'm going to walk through the code I wrote,
the problem I had,
and the solution I (think I've) found step by step.
If there's a simpler way,
or if this *is* documentation clearly somewhere,
please [let me know](mailto:gvwilson@third-bit.com).

## Tasks

A `Task` has a unique ID and keeps track of how many times it has been worked on:

```python
class Task:
    def __init__(self, ident):
        self.ident = ident
        self.count = 0

    def __str__(self):
        return f"task-{self.ident}/{self.count}"
```

## The Overall Simulation

Since I don't want to have to pass a whole bunch of parameters around,
`Simulation` stores the SimPy `Environment`,
our single developer,
our single tester,
and the three queues:
one for new tasks,
one for tasks that need to be reworked,
and one for tasks that are ready for testing:

```python
class Simulation:
    def __init__(self):
        # Environment.
        self.env = simpy.Environment()

        # One developer and one tester.
        self.developer = Developer(self)
        self.tester = Tester(self)

        # Queues for new development work, rework, and testing.
        self.q_dev = simpy.Store(self.env)
        self.q_rework = simpy.Store(self.env)
        self.q_test = simpy.Store(self.env)
```

`Simulation` also defines the generator that creates new tasks
and puts them in the ready-to-develop queue:

```python
class Simulation:
    …previous code…
    def generate(self):
        i = 0
        while True:
            task = Task(i)
            i += 1
            print(f"{self.env.now:.2f} create {task}")
            yield self.q_dev.put(task)
            yield self.env.timeout(T_GEN)
```

Finally,
`Simulation` defines a convenience method that runs everything:

```python
    def run(self):
        self.env.process(self.generate())
        self.env.process(self.developer.work())
        self.env.process(self.tester.work())
        self.env.run(until=T_SIM)
```

For testing,
the parameters are:

```python
N_TASK = 2  # number of tasks to create
T_GEN = 1   # time between tasks
T_DEV = 1   # time to do development
T_TEST = 1  # time to do testing
T_SIM = 4   # how long to run the whole simulation
```

## Workers

A generic `Worker` (either a developer or a tester)
caches the object that holds the overall simulation
and provides a couple of convenience methods for getting the current time
and for printing itself:

```python
class Worker:
    def __init__(self, sim):
        self.sim = sim

    @property
    def now(self):
        return self.sim.env.now

    def __str__(self):
        return f"{self.__class__.__name__}/{self.now:.2f}"
```

## Testers

The tester gets a task from the testing queue,
waits a tick to simulate work,
increments the task's internal count of how many times it has gone around the loop,
and then puts it in the rework queue:

```python
class Tester(Worker):
    def work(self):
        while True:
            # Get a task from the testing queue.
            print(f"{self}: wait for task(s)")
            task = yield self.sim.q_test.get()
            print(f"{self}: got {task}")

            # Do testing.
            yield self.sim.env.timeout(T_TEST)
            task.count += 1

            # Always put the task in the rework queue.
            yield self.sim.q_rework.put(task)
            print(f"{self}: put {task} in rework queue")
```

## Developers (the wrong version)

**This code is wrong, but will be fixed below.**

My original `Developer` waited until a task was available in *either*
the development queue or the rework queue,
then selected one of those tasks (giving priority to rework),
waited a tick to simulate work,
and put the task in the testing queue:

```python
class DeveloperWrong(Worker):
    def work(self):
        while True:
            # Get either a task for development or a task for rework.
            req_dev = self.sim.q_dev.get()
            req_rework = self.sim.q_rework.get()
            print(f"{self}: wait for task(s)")
            result = yield simpy.AnyOf(self.sim.env, [req_dev, req_rework])

            # Give priority to rework.
            if req_rework in result:
                task = result[req_rework]
                print(f"{self} got {task} from rework with {len(result.events)} events")
            elif req_dev in result:
                task = result[req_dev]
                print(f"{self} got {task} from dev with {len(result.events)} events")
            else:
                assert False, "how did we get here?"

            # Do development.
            yield self.sim.env.timeout(T_DEV)

            # Put the task in the testing queue.
            yield self.sim.q_test.put(task)
            print(f"{self}: put {task} in testing queue")
```

According to the documentation,
`simpy.AnyOf` creates an object that means "give me any of the following".
Its result is a dictionary-like object
whose keys are the requests
and whose values are items from one or more of the queues being waited on:
"or more" because it's possible for items to be available in multiple queues simultaneously.

## Output from the Buggy Version

Here's the output using the `DeveloperWrong` class shown above:

```
0.00 create task-0/0
DeveloperWrong/0.00: wait for task(s)
Tester/0.00: wait for task(s)
DeveloperWrong/0.00 got task-0/0 from dev with 1 events
1.00 create task-1/0
DeveloperWrong/1.00: put task-0/0 in testing queue
DeveloperWrong/1.00: wait for task(s)
Tester/1.00: got task-0/0
DeveloperWrong/1.00 got task-1/0 from dev with 1 events
2.00 create task-2/0
Tester/2.00: put task-0/1 in rework queue
Tester/2.00: wait for task(s)
DeveloperWrong/2.00: put task-1/0 in testing queue
DeveloperWrong/2.00: wait for task(s)
Tester/2.00: got task-1/0
DeveloperWrong/2.00 got task-2/0 from dev with 1 events
3.00 create task-3/0
Tester/3.00: put task-1/1 in rework queue
Tester/3.00: wait for task(s)
DeveloperWrong/3.00: put task-2/0 in testing queue
DeveloperWrong/3.00: wait for task(s)
Tester/3.00: got task-2/0
DeveloperWrong/3.00 got task-3/0 from dev with 1 events
```

A lot is going on in those 23 lines,
so let's look at what the developer got from where:

```
DeveloperWrong/0.00 got task-0/0 from dev with 1 events
DeveloperWrong/1.00 got task-1/0 from dev with 1 events
DeveloperWrong/2.00 got task-2/0 from dev with 1 events
DeveloperWrong/3.00 got task-3/0 from dev with 1 events
```

Hm:
the developer is never taking tasks from the rework queue.
Is the tester putting them in?

```
Tester/0.00: wait for task(s)
Tester/1.00: got task-0/0
Tester/2.00: put task-0/1 in rework queue
Tester/2.00: wait for task(s)
Tester/2.00: got task-1/0
Tester/3.00: put task-1/1 in rework queue
Tester/3.00: wait for task(s)
Tester/3.00: got task-2/0
```

So what's going on?

## A Corrected Developer

Here's the skeleton of the corrected developer's `work` method:

```python
class DeveloperRight(Worker):
    def work(self):
        which = "dev"
        take = None
        while True:
            # Get either a task for development or a task for rework.
            req_dev = self.sim.q_dev.get()
            req_rework = self.sim.q_rework.get()
            print(f"{self}: wait for task(s)")
            result = yield simpy.AnyOf(self.sim.env, [req_dev, req_rework])

            …magic happens here…

            # Do development.
            yield self.sim.env.timeout(T_DEV)

            # Put the task in the testing queue.
            yield self.sim.q_test.put(task)
            print(f"{self}: put {task} in testing queue")
```

The bit of magic in the middle is that as far as I can tell,
all of the requests that *weren't* selected have to be canceled,
even if there wasn't something in the queue at the time for the developer to take.
For example,
the first time the developer gets a task from the development queue,
the rework queue is guaranteed to be empty,
but we still have to cancel the request for something from it.

In order to demonstrate this,
I've filled in the magic portion of `work` with code that alternates between
taking work from the development queue (if available)
and taking work from the rework queue (ditto).
Of course,
if there is only one event in the result from `AnyOf`,
the code uses that,
but *still cancels the other request*:

```python
    def work(self):
        which = "dev"
        take = None
        while True:
            …get either a task for development or a task for rework…

            # Pick one.
            if len(result.events) == 2:
                print(f"{self}: ...got two events")
                if which == "dev":
                    take = "dev"
                    which = "rework"
                else:
                    take = "rework"
                    which = "dev"
            elif req_dev in result.events:
                print(f"{self}: ...got dev")
                take = "dev"
            elif req_rework in result.events:
                print(f"{self}: ...got rework")
                take = "rework"
            else:
                assert False, "how did we get here?"

            # Now take it.
            if take == "dev":
                print(f"{self}: ...taking dev")
                task = result[req_dev]
                req_rework.cancel()
            elif take == "rework":
                print(f"{self}: ...taking rework")
                task = result[req_rework]
                req_dev.cancel()
            else:
                assert False, "how did we get here?"
            print(f"{self} got {task}")

            …do development and put the task in the testing queue…
```

Here are the relevant bits of output when the simulation is run for 10 ticks instead of just 4:

```
DeveloperRight/0.00: ...taking dev
DeveloperRight/1.00: ...taking dev
DeveloperRight/2.00: ...taking dev
DeveloperRight/3.00: ...taking rework
DeveloperRight/4.00: ...taking dev
DeveloperRight/5.00: ...taking rework
DeveloperRight/6.00: ...taking dev
DeveloperRight/7.00: ...taking rework
DeveloperRight/8.00: ...taking dev
DeveloperRight/9.00: ...taking rework
```

As I said at the outset,
I'm going to submit some PRs for SimPy's documentation
to shout loudly and clearly that outstanding requests need to be canceled
(or possibly recycled: I haven't tried that yet).
Meanwhile,
I can now get back to playing with the impact of rework fractions on throughput.

[simpy]: https://simpy.readthedocs.io/
[sturdiness]: @root/2025/12/03/in-search-of-sturdiness/
