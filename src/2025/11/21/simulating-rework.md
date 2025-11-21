---
title: Simulating Rework
date: 2025-11-21
---

In [yesterday's post][making-sense] we started collecting data from our simulation,
and discovered that our metrics will always give us numbers,
but those numbers might be garbage if we're measuring the wrong things or the wrong way.
In this post we'll make the simulation more realistic
by taking into account the fact that most first attempts to fix a bug
either don't fix it or introduce new bugs.

## Rework

Let's introduce a new parameter to specify
the probability that a task needs to be re-done.
For the moment,
we'll assume this probability doesn't depend on
how many attempts have been made to finish the task so far.
While we're at it,
we'll introduce another parameter to specify
how many times we want to run the simulation:

```python
PARAMS = {
    …previous parameters…
    "rework_probability": 0.6,
    "num_simulations": 1,
}
```

Next, we introduce a loop in `simulate_task`.
Each time around the loop,
we get a developer,
spend some time on the task,
and then check if we're done.
If we are,
we mark the task as completed and break out of the loop;
if not,
we go around the loop again.

```python
def simulate_task(params, env, developers, task):
    """Simulate a task flowing through the system."""

    while True:
        with developers.request() as req:
            yield req
            task.start(env)
            yield env.timeout(task._duration)
            task.end(env)
            if random.uniform(0, 1) >= params["rework_probability"]:
                task.completed()
                break
```

If we run our simulation a few times for 100,000 timesteps with two developers,
we complete an average of 14,550 tasks,
which works out to about 13.7 timesteps per task.
That's about 40% of the 36,000 tasks we complete in the same time without rework,
and gives us a baseline against which to compare
a more interesting variation on this model.

## Keeping the Same Developer

When a task needs to be redone,
the code shown above always grabs the next available developer.
In most development teams,
though,
the same developer would keep working on the task.

We need to make two changes to the simulation to capture this.
First,
we create a `FilterStore` instead of a `Resource` to represent
our pool of developers:

```python
    developers = simpy.FilterStore(env, capacity=params["num_developers"])
```

The difference between the two is that `FilterStore` allows us to specify
a test or check that a resource has to satisfy when we claim it.
Here's the modified `simulate_task` that makes use of that:

```python
def simulate_task(params, env, developers, task):
    """Simulate a task being re-worked by the same developer."""

    dev = None
    while True:
        if dev is None:
            dev = yield developers.get()
        else:
            dev = yield developers.get(lambda item: item._id == dev._id)
        task.start(env)
        yield env.timeout(task._duration)
        developers.put(dev)
        task.end(env)
        if random.uniform(0, 1) >= params["rework_probability"]:
            task.completed()
            break
```

Initially,
the task isn't associated with a developer
so `dev` is set to `None`.
The first time around the loop,
we use `developers.get()` without a test to claim a developer.
After that,
we always re-claim the same developer
by passing a function to `developers.get()` that says,
"The only developer we want is the one with the same ID."
We then do some work,
put the developer back in the pool,
and check to see if we're done with this task or not.

## Does It Make a Difference?

So here's our question:
does this policy change the total number of tasks completed or not?
On the one hand we could argue that it would
because we wouldn't be taking full advantage of idle developers.
On the other hand,
our developers are currently working almost 100% of the time,
so there aren't actually idle cycles going to waste.

The answer is that *under the assumptions baked into our simulation*
this change in policy doesn't have an impact on the total number of tasks that are completed.
If we increase the number of developers
and lower the rate at which new tasks arrive,
though,
that answer changes:
if developers *do* have idle cycles,
having developers "own" tasks is less efficient
than allowing whoever's free to work on whatever needs done.

Of course,
that model doesn't take into account the ramp-up time
that real developers need to familiarize themselves with new problems.
(Putting it another way,
it doesn't account for the time saved by having someone who understands the problem
go back to it.)
We could add another parameter to our model and another few lines of code to capture this,
but before we do that,
we need to put some better analysis machinery in place.

[making-sense]: @root/2025/11/20/making-sense-of-simulation/
