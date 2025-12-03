---
title: In Search of Sturdiness
date: 2025-12-03
---

I took a break from this series of posts for a couple of days
to focus on [looking for a new role][looking-for-work]
and because I've hit a bit of a roadblock.
In the most recent version of the simulation,
testers can bounce work back to the development queue if they find bugs:

```
+----------------+    +-----------+    +------------+    +------------+    +---------+
| task generator | -> | dev queue | -> | developers | -> | test queue | -> | testers |
+----------------+    +-----------+    +------------+    +------------+    +---------+
                            ^                                                   |
                            |                                                   |
                            +---------------------------------------------------+
```

Tasks that have been sent back for more work always have higher priority than new tasks,
but that's not realistic.
What I'd like to model is a system in which re-work is done by
the same developer who did the initial work.
I can do this by creating a re-work queue for each developer,
and use [SimPy][simpy]'s `AnyOf` operator to select from either queue:

```python
class Developer(Worker):

    def work(self):
        while True:
            rework_get = self.rework_queue.get()
            new_get = self.sim.dev_queue.get()
            result = yield(simpy.AnyOf(rework_get, new_get))

            if rework_get in result.events:
                task = result[rework_get]
                new_get.cancel()
            else:
                task = result[new_get]
```

Notice that the "get" request for the new-work queue is canceled
when there's re-work to be done.
Doing this takes care of the case in which items were available in *both* queues
(which turns out to be very common);
I found by trial and error that canceling a "get" request has no effect
if the request is still pending,
which simplifies the logic a little bit.

So here's my problem:
when there is re-work to be done *and* the developer is working on a new task,
I'd like to interrupt the developer and have them do re-work,
then resume their previous task;
in other words,
I'd like re-work to take *immediate* precedence over new work.
However,
if the developer is already doing re-work,
I don't want to interrupt them.

SimPy supports interrupts:
if you have a process `p`, you can call `p.interrupt()` to throw an exception into it.
The process can catch this and do whatever it wants:

```python
def p():
    while True:
        try:
            …normal operation…
        except simpy.Interrupt:
            …interrupt handler…
```

So now what?
As near as I can figure,
when a developer is interrupted,
it checks to see whether it's already doing re-work or not.
If it is,
it puts the task associated with the re-work interrupt in its re-work queue.
If not,
it puts the (new) task it's working on in the re-work queue
and switches tasks.
Hm,
that means the developer's queue has to be a priority queue
so that re-work takes precedence over new work.
And we need to keep track of time spent so far on each task.
And there's probably at least one corner case I haven't thought of yet,
because this is a concurrent system with interrupts
and there are *always* corner cases.

A few final thoughts:

1.  The title of this post is "In Search of Sturdiness"
    because I think that word best sums up what I'm looking for.
    I don't care all that much if a solution is elegant or graceful or clever;
    I want something sturdy because I want to make more changes to the simulation
    and I don't want to have to come back and re-design this part.

1.  AI tools aren't much help here,
    at least not the ones I've tried.
    They're good at generating plausible answers,
    but this situation needs one that's right as well.

1.  This is where I'd like to make use of a tool like [Alloy][alloy] or [TLA+][tla],
    but they aren't already part of my repertoire,
    and I don't have time for a three-month side quest to master one of them.

1.  I've tried to find an experienced SimPy user, without luck.
    If you are one,
    and are willing to offer some design advice,
    I'd be very grateful if you would [reach out](mailto:gvwilson@third-bit.com).

[alloy]: https://alloytools.org/
[looking-for-work]: @root/2025/11/21/looking-for-work/
[observability]: @root/2025/11/30/observability/
[simpy]: https://simpy.readthedocs.io/
[tla]: https://en.wikipedia.org/wiki/TLA%2B
