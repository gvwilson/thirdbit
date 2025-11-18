---
title: Starting to Simulate
date: 2025-11-18
---

Inspired in part by [the software development simulator][hendrickson-sim]
that Elisabeth Hendrickson and friends built,
I've been toying with the idea of using [SimPy][simpy] to create something
that could be used in a half-day workshop to
(a) show people how powerful discrete event simulation can be, and
(b) demonstrate why simple measurements of developers' work are almost always misleading.
It's been thirty-five years since I did this kind of simulation,
SimPy uses some features of Python that I haven't kept up with,
and I've never taught this topic before,
so I'm planning to do a few blog posts about how it works and what I'm learning.

## Generators

A *generator* is a Python function that creates an object
which uses its stack to maintain persistent state.
That probably doesn't make any sense unless you already understand it,
so here's an example:

```python
def gen_char_from_string(text):
    i = 0
    while i < len(text):
        yield text[i]
        i += 1
```

The magic is the keyword `yield`,
which tells Python that this function creates a generator.
(I think the code would be easier to understand
if a keyword like `gen` had to be used instead of `def`,
but that ship sailed a long time ago.)
We can use our generator like this:

```python
gen = gen_char_from_string("one")
try:
    i = 0
    while True:
        ch = next(gen)
        print(f"{i}: {ch}")
        i += 1
except StopIteration:
    print("ended by exception")
```

As this code shows,
calling `gen_char_from_string` creates an object rather than immediately returning a value.
Each time we call `next` on that object,
it advances to the next `yield`.
The generator object preserves its stack,
so the local variables `text` and `i` persist from one invocation to the next.
When execution reaches the end of the generator,
Python thows a `StopIteration` exception to tell us it's done.

Why go to all this trouble?
First,
`for` loops understand how to interact with generators,
so we can rewrite the snippets above as:

```python
def gen_char_from_string(text):
    for ch in text:
        yield ch

characters = [ch for ch in gen_char_from_string("two")]
print(f"result as list: {characters}")
```

Second,
we can do things like create "infinite" generators:

```python
def gen_infinite(text):
    pos = 0
    while True:
        yield text[pos]
        pos = (pos + 1) % len(text)


for (i, ch) in enumerate(gen_infinite("three")):
    if i > 9:
        break
    print(i, ch)
```
```
0 t
1 h
2 r
3 e
4 e
5 t
6 h
7 r
8 e
9 e
```

or generate the cross-product of two arbitrary collections:

```python
def gen_combinations(left, right):
    for left_item in left:
        for right_item in right:
            yield (left_item, right_item)


for pair in gen_combinations("abc", [1, 2, 3]):
    print(pair)
```
```
('a', 1)
('a', 2)
('a', 3)
('b', 1)
('b', 2)
('b', 3)
('c', 1)
('c', 2)
('c', 3)
```

We can even store our generators in a list (after all, they're just objects)
and then use them however we want:

```python
def alternate(processes):
    while True:
        try:
            for proc in processes:
                yield next(proc)
        except StopIteration:
            break

def seq(values):
    for v in values:
        yield v

sequences = [seq("ab"), seq("123")]
for thing in alternate(sequences):
    print(thing)
```
```
a
1
b
2
```

## Discrete Event Simulation

*Discrete event simulation* models a system as a series of events,
each of which occurs at a particular instant in time.
We can simulate such a system by advancing the clock one tick at a time,
but it's more efficient to have each *process* tell us when it's next going to do something
and then jump ahead to the least of those times.

> Note: we're using the word "process" to mean "something active"
> rather than "an operating system process".
> I prefer the word "actor",
> but "process" is pretty deeply embedded in discrete event simulation terminology.

SimPy handles all these details for us.
All we have to do is:

1.  Create an *environment* that stores all the SimPy-ish stuff
    like the list of running processes.
2.  Give it some processes to run.
3.  Tell it to run the simulation until all the processes are done.

```python
import sys
import simpy

def main():
    env = simpy.Environment()
    env.process(random_worker(env, worker_id=1, num_jobs=3, job_time=2))
    env.process(random_worker(env, worker_id=2, num_jobs=3, job_time=3))
    env.run()
    print(f"\nSimulation completed at T={env.now}")
```

The key thing here is that `random_worker` *isn't* a normal function call.
Instead of handing a value to `env.process`,
it creates a generator for the environment to run.
That generator yields `env.timeout(delay)` to tell SimPy
that it wants to wait for a certain length of time,
e.g.,
to simulate being busy.
(Processes can yield other things as well—we'll see some in future posts.)

```python
def random_worker(env, worker_id, num_jobs, job_time):
    """Actor with random-time jobs."""
    print(f"T={env.now} worker {worker_id} starts")

    for job_num in range(num_jobs):
        print(f"T={env.now} worker {worker_id} starts job {job_num} duration {job_time}")
        yield env.timeout(job_time)
        print(f"T={env.now} worker {worker_id} finishes job {job_num}")

    print(f"T={env.now} worker {worker_id} finishes")
```

Here's the output:

```
T=0 worker 1 starts
T=0 worker 1 starts job 0 duration 2
T=0 worker 2 starts
T=0 worker 2 starts job 0 duration 3
T=2 worker 1 finishes job 0
T=2 worker 1 starts job 1 duration 2
T=3 worker 2 finishes job 0
T=3 worker 2 starts job 1 duration 3
T=4 worker 1 finishes job 1
T=4 worker 1 starts job 2 duration 2
T=6 worker 2 finishes job 1
T=6 worker 2 starts job 2 duration 3
T=6 worker 1 finishes job 2
T=6 worker 1 finishes
T=9 worker 2 finishes job 2
T=9 worker 2 finishes
Simulation completed at T=9
```

## Next Steps

A couple of workers doing fixed-size jobs, completely independently,
isn't a particularly interesting scenario.
The next post in this series will look at two things:

1.  How do we make a more realistic simulation?
2.  How do we create more comprehensible output?

These questions are equally important because
there's no point building something whose results we can't understand (and check).
Stay tuned…

[hendrickson-sim]: https://sim.curiousduck.io/
[simpy]: https://simpy.readthedocs.io/
