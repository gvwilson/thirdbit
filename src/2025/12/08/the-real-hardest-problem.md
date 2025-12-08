---
title: The Real Hardest Problem
date: 2025-12-08
---

> There are only two hard things in computer science:
> cache invalidation and naming things.
>
> — Phil Karlton

With respect,
I think that handling interrupts is harder than either of these.
[Yesterday's post][handling] explained how [SimPy][simpy] does this.
Today,
after several near misses,
we'll look at how to add it to our simulation.

## A Quick Recap

Our `Simulation` class now includes a process
that waits a random interval,
chooses a random developer,
and interrupts her by calling `.interrupt`:

```python
class Simulation:

    def annoy(self):
        while True:
            yield self.timeout(self.t_interrupt_arrival())
            dev = random.choice(self.developers)
            dev.proc.interrupt(self.t_interrupt_duration())
```

When `.interrupt` is called,
SimPy injects a `simpy.Interrupt` exception into the target process;
the argument to `.interrupt` is attached to that exception object.
If we're comfortable throwing away the task we're currently working on,
the `Developer` process can catch the exception like this:

```python
class Developer(Labeled):
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

The trickiest part of this is canceling the outstanding request
to get something from the development queue.
As we discovered yesterday,
if we *don't* do this,
the developer won't ever get anything else from the queue.

## Nearly Right

What if we *don't* want to throw away our current task when we're interrupted?
What if instead we want to handle the interruption and then resume that task?
Here's an implementation that's almost right:

```python
    # This code is wrong.
    def work(self):
        task = None
        while True:
            req = None
            try:
                if task is None:
                    req = self.sim.dev_queue.get()
                    task = yield req
                t_start = self.sim.now
                yield self.sim.timeout(task.dev_required - task.dev_done)
                task.dev_done += self.sim.now - t_start
                if task.is_done():
                    task = None
            except simpy.Interrupt as exc:
                if req is not None:
                    req.cancel()
                yield self.sim.timeout(exc.cause)
```

Inside the `try` block we get a task if we don't already have one,
then try to wait for as much time as the task still requires.
When we're done we add some time to the task and check if it's now complete.
If we're interrupted,
we cancel any outstanding request for a new task
and then wait for as long as the interrupt tells us to.

There are (at least) two things wrong with this code.
The first and less important is that when we're interrupted,
we throw away any work we've done on the task during this iteration of the loop.
That's relatively easy to fix:
we just add some code to the `except` block to increment the `.dev_done` time in the task.

The bigger problem,
though,
is that sooner or later this code fails because of an uncaught `Interrupt` exception.
The problem is that we can be interrupted
*inside our interrupt handler*.
It isn't likely,
which means it doesn't happen very often,
but if we run the simulation often enough with different random seeds,
it eventually falls over.

## A Corrected Version

The "fix" (I'll explain the scare quotes around that word in a moment)
is to move interrupt handling into the `try` block.
To do that,
we have to add another state variable `interrupt_delay`
that tells the process if it's currently supposed to be handling an interruption delay:

```python
    def work(self):
        task = None
        interrupt_delay = None
        while True:
            req = None
            try:
                if interrupt_delay is not None:
                    yield self.sim.timeout(interrupt_delay)
                    interrupt_delay = None
                else:
                    if task is None:
                        req = self.sim.dev_queue.get()
                        task = yield req
                    yield self.sim.timeout(task.dev_required - task.dev_done)
                    if task.is_done():
                        task = None
            except simpy.Interrupt as exc:
                if req is not None:
                    req.cancel()
                interrupt_delay = exc.cause
```

So why did I put scare quotes around the word "fix"?
Because I'm still not 100% sure this works.
It hasn't failed yet,
despite multiple runs with different seeds and parameters,
but this code is now complex enough that I could well believe it contains
a one-in-a-million edge case.
I *think* the `except` block is now a critical region,
i.e.,
that no interrupts can occur within it
because none of those three lines hands control back to SimPy,
but I'm not completely sure.

And yes,
this code still throws away any work the developer has done on a task
during a particular loop iteration
if an interrupt occurs;
the interrupt handler should increment `task.dev_done`.
And yes,
it's possible for an interrupt to be interrupted:
a more realistic implementation would stack interrupt delays,
but honestly,
if my boss interrupts me while I'm being interrupted,
I don't have any qualms about discarding the first interruption.

## Yaks and More Yaks

My goal with this series of blog posts was
to simulate the development process of a small software team.
I've spent most of the last week learning more about [SimPy][simpy];
it feels like [yak shaving][yak],
but without it,
I don't think I'd have confidence in the code shown above
(or be able to review its AI-generated equivalent).

[handling]: @root/2025/12/07/handling-interruptions/
[simpy]: https://simpy.readthedocs.io/
[yak]: https://en.wiktionary.org/wiki/yak_shaving
