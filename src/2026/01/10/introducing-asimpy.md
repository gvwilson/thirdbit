---
title: Introducing asimpy
date: 2026-01-10
---

I put [the tutorial on discrete event simulation][sim] on hold a couple of days ago
and spent a few hours building
[a small discrete event simulation framework of my own][asimpy]
using `async`/`await` instead of `yield`.
As I hoped,
I learned a few things along the way.

First,
Python's `await` is just a layer on top of its iterator machinery
(for an admittedly large value of "just").
When Python encounters `await obj` it does something like this:

```python
iterator = obj.__await__()  # get an iterator
try:
    value = next(iterator)  # run to the first yield
except StopIteration as e:
    value = e.value         # get the result
```

Breaking this down:

1.  Call the object's `__await__()` method to get an iterator.
2.  It then advances that iterator to its first `yield` to get a value.
3.  If the iterator doesn't `yield`, the result is whatever the iterator returns.
    (That value arrives as the `.value` field of the `StopIteration` exception.)

We can simulate these steps as follows:

```python
# Define a class whose instances can be awaited.
class Thing:
    def __await__(self):
        print("before yield")
        yield "pause"
        print("after yield")
        return "result"

# Get the __await__ iterator directly
awaitable = Thing()
iter = awaitable.__await__()  # this is an iterator

# run to first yield
value = next(iter)
print("iterator yielded:", value)

# Step 2: resume until completion
try:
    next(iter)
except StopIteration as e:
    value = e.value
    print("final result:", value)
```
```text
before yield
iterator yielded: pause
after yield
final result: result
```

`asimpy` builds on this by requiring processes to be derived from a `Process` class
and to have an `async` method called `run`:

```python
class Process:
    def __init__(self, env):
        self.env = env

    @abstractmethod
    async def run(self):
        pass


class Sleeper(Process):
    async def run(self):
        for _ in range(3):
            await self.env.sleep(2)
```

We can then create an instance of `Sleeper` and pass it to the environment,
which calls its `run()` method to get a coroutine
and schedules that coroutine for execution:

```python
env = Environment()
s = Sleeper(env)
env.immediate(s)
env.run()
```

`Environment.run` then pulls processes from its run queue until it hits a time limit
or runs out of things to execute:

```python
class Environment:
    def run(self, until=None):
        while self._queue:
            pending = heapq.heappop(self._queue)
            if until is not None and pending.time > until:
                break

            self.now = pending.time
            proc = pending.proc

            try:
                awaited = proc._coro.send(None)
                awaited.act(proc)

            except StopIteration:
                continue
```

The two key lines are in the `try` block:

1.  Send `None` to the process's coroutine to resume its execution.
2.  Get something back the next time it calls `await`.
3.  Run that something's `act()` method.

For example,
here's how `sleep` works:

```python
class Environment:
    # …as above…
    def sleep(self, delay):
        return _Sleep(self, delay)

class _Sleep:
    def __init__(self, env, delay):
        self._env = env
        self._delay = delay

    def act(self, proc):
        self._env.schedule(self._env.now + self._delay, proc)

    def __await__(self):
        yield self
        return None
```

1.  `Environment.sleep()` returns an instance of `_Sleep`,
    so `await self.env.sleep(t)` inside a process
    gives the environment an object that says, "Wait for *t* ticks."
2.  When the environment calls that object's `act()` method,
    it reschedules the process that created the `_Sleep` object
    to run again in *t* ticks.

It is a bit convoluted—the environment asks the process for an object
that in turn manipulates the environment—but so far
it seems to be able to handle shared resources, job queues, and gates.
Interrupts were harder to implement ([interrupts are always hard][interrupts]),
but [they are in the code as well][asimpy-repo].

Was this worth building?
It only has a fraction of [SimPy][simpy]'s features,
and while I haven't benchmarked it yet,
I'm certain that `asimpy` is much slower.
On the other hand,
I learned a few things along the way,
and it gave me an excuse to try out [ty][ty] and [taskipy][taskipy] for the first time.
It was also a chance to practice using an LLM as a coding assistant:
I wouldn't call what I did "vibe coding",
but ChatGPT's explanation of how `async`/`await` works was helpful,
as was its diagnosis of a couple of bugs.
I've [published `asimpy` on PyPI][asimpy-pypi],
and if a full-time job doesn't materialize some time soon,
I might come back and polish it a bit more.

> What I cannot create, I do not understand.
>
> — Richard Feynman

[asimpy]: https://gvwilson.github.io/asimpy/
[asimpy-pypi]: https://pypi.org/project/asimpy/
[asimpy-repo]: https://github.com/gvwilson/asimpy/
[interrupts]: @root/2025/12/08/the-real-hardest-problem/
[sim]: https://gvwilson.github.io/sim/
[simpy]: https://simpy.readthedocs.io/
[taskipy]: https://github.com/taskipy/taskipy
[ty]: https://docs.astral.sh/ty/
