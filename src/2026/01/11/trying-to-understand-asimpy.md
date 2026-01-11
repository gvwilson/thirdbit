---
title: Trying to Understand asimpy
date: 2026-01-11
---

As a follow-on to [yesterday's post][introducing-asimpy],
I'm trying to figure out why the code in the `tracing-sleeper` branch of <https://github.com/gvwilson/asimpy>
actually works.
The files that actually matter for the moment are:

-   `src/asimpy/environment.py`:
    the simulation environment with the main event loop and the `_Sleep` action (described below).
-   `src/asimpy/actions.py`:
    the base class for actions (described below).
-   `src/asimpy/process.py`:
    the base class for active processes.
-   `examples/sleep.py`:
    an example of a process sleeping.

I've added lots of print statements to `sleep.py` and the three files in the package that it relies on.
To run the code:

```shell
$ git clone git@github.com:gvwilson/asimpy
$ cd asimpy
$ uv venv
$ source .venv/bin/activate
$ uv sync
$ python examples/sleep.py
```

Inside `src/asimpy/actions.py` there's a class called `BaseAction`
that the framework uses as the base of all awaitable objects.
When a process does something like sleep,
or try to get something from a queue,
or anything else that requires synchronization,
it creates an instance of a class derived from `BaseAction`
(such as the `_Sleep` class defined in `src/asimpy/environment.py`).

Now,
if I understand the protocol correctly,
when Python encounters 'await obj', it does the equivalent of:

```python
iter = obj.__await__()  # get an iterator
try:
    value = next(iter)  # run to the first yield
except StopIteration as e:
    value = e.value     # get the result 
```

After stripping out docs, typing, and print statements,
`BaseAction`'s implementation of `__await__()` is just:

```python
def __await__(self):
    yield self
    return None
```

Looking at the printed output,
both lines are _always_ executed, and I don't understand why.
Inside `Environment.run()`, the awaitable is advanced by calling:

```python
awaited = proc._coro.send(None)
```

(where `proc` is the object derived from `Process`
and `proc._coro` is the iterator created by invoking the process's `async` `run()` method).
My mental model is that `value` should be set to `self`
because that's what the first line of `__await__()` yields;
I don't understand why execution ever proceeds after that,
but my print statements show that it does.

And I know execution _must_ proceed because (for example)
`BaseQueue.get()` in `src/asimpy/queue.py` successfully returns an object from the queue.
This happens in the second line of that file's `_Get.__await__()`,
and the more I think about this the more confused I get.

I created this code by imitating what's in [SimPy][simpy],
reasoning through what I could,
and asking ChatGPT how to fix a couple of errors late at night.
It did all make sense at one point,
but as I try to write the tutorial to explain it to others,
I realize I'm on shaky ground.
ChatGPT's explanations aren't helping;
if I find something or someone that does,
I'll update this blog post.

[introducing-asimpy]: @root/2026/01/10/introducing-asimpy/
[simpy]: https://simpy.readthedocs.io/
