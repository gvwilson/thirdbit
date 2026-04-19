---
title: "asimpy Improvements"
date: 2026-04-19
---

Following up on [yesterday's post about benchmarking][benchmark],
Claude and I have made some improvements to [asimpy][asimpy].

## 1. Eliminate `functools.partial` in `resume()`

Before, every time an event fired and needed to reschedule a waiting process, `resume()` did this:

```python
from functools import partial

def resume(self, value=None):
    if not self._done:
        self._env.immediate(partial(self._loop, value))
```

`partial` is a C-level callable, so it is fast,
but it still allocates a new object on every event completion.
The fix stores the value directly on the process and schedules `_loop` without wrapping it:

```python
def resume(self, value=None):
    if not self._done:
        self._resume_value = value
        self._env.immediate(self._loop)

def _loop(self):
    value = self._resume_value
    self._resume_value = None
    ...
```

## 2. Inline `_add_waiter` in `_loop`

When a process parks on a pending event, the original code called through a method:

```python
yielded._add_waiter(self.resume)
```

The inlined version writes directly to the event's waiter slot:

```python
if v is _PENDING:
    w = yielded._waiter
    if w is None:
        yielded._waiter = self.resume
    elif isinstance(w, list):
        w.append(self.resume)
    else:
        yielded._waiter = [w, self.resume]
```

This saves one Python function-call dispatch per `await` on a pending event.

## 3. Move the Exception Check from `Event.__await__` to `Process._loop`

The original `__await__` checked whether the received value was an exception on every resume,
even when the event succeeded normally:

```python
def __await__(self):
    value = yield self
    if isinstance(value, BaseException):
        raise value
    return value
```

Moving the check to `_loop` lets `__await__` become a single expression with no branch:

```python
def __await__(self):
    return (yield self)
```

In `_loop`, the value from a failed event causes `coro.throw()` instead of `coro.send()`:

```python
if isinstance(value, BaseException):
    yielded = self._coro.throw(value)
else:
    yielded = self._coro.send(value)
```

Every normal (non-failing) `await` now avoids the `isinstance` check entirely.

## 4. Lazy Waiter Slot

Every `Event.__init__` previously allocated an empty list for `_waiters`,
which is wasted work in the common case where at most one process ever waits on a given event.
The fix replaces the list with a single `_waiter` slot that upgrades lazily:

- `None`: no waiter yet (initial state, no allocation)
- `callable`: exactly one waiter (the common case)
- `list`: two or more waiters (`AllOf` and `FirstOf`)

```python
__slots__ = ("_env", "_value", "_waiter", "_on_cancel")

def __init__(self, env):
    ...
    self._waiter = None  # None | callable | list[callable]
```

`succeed()` dispatches on the same three cases and avoids iterating an empty list
for the typical single-waiter event.

## Benchmark Results

Benchmarks were run with `sys.monitoring` (Python bytecode instruction counts)
and `time.perf_counter()` (wall-clock time),
each over 1000 executions of the feature under test.
The comparison is against SimPy 5, which uses generator-based scheduling.

| Feature | Before (µs) | After (µs) | Wall-clock Δ | Instr Δ |
|:---|---:|---:|---:|---:|
| Event | 0.522 | 0.446 | -14.6% | -1 |
| Event (fail) | 0.967 | 0.770 | -20.4% | -2 |
| Timeout | 0.686 | 0.623 | -9.2% | -1 |
| Environment.run(until=) | 0.749 | 0.638 | -14.8% | -1 |
| Container | 0.694 | 0.647 | -6.8% | -4 |
| Container (float amounts) | 0.745 | 0.640 | -14.1% | -4 |
| Queue | 0.729 | 0.657 | -9.9% | -4 |
| Queue (blocking get) | 1.733 | 1.605 | -7.4% | -4 |
| Queue (blocking put) | 1.870 | 1.723 | -7.9% | -4 |
| Store | 0.706 | 0.692 | -2.0% | -4 |
| Store (filtered get) | 0.721 | 0.695 | -3.6% | -4 |
| PriorityQueue | 0.710 | 0.673 | -5.2% | -4 |
| Resource (uncontended) | 0.364 | 0.339 | -6.9% | -2 |
| Resource (context manager) | 0.493 | 0.481 | -2.4% | -2 |
| Resource (contention) | 1.825 | 1.676 | -8.2% | +13 |
| Resource (multi-capacity) | 1.843 | 1.738 | -5.7% | +13 |
| AllOf | 1.059 | 1.022 | -3.5% | -4 |
| AllOf (blocking) | 2.243 | 2.054 | -8.4% | +4 |
| FirstOf | 1.067 | 1.009 | -5.4% | -3 |
| FirstOf (blocking) | 2.240 | 2.189 | -2.3% | +2 |
| Interrupt | 1.866 | 1.763 | -5.5% | -1 |
| Interrupt (with cause) | 1.918 | 1.770 | -7.7% | -1 |
| Barrier | 1.381 | 1.280 | -7.3% | -2 |
| PreemptiveResource | 3.196 | 3.179 | -0.5% | -5 |
| PreemptiveResource (no-preempt) | 2.558 | 2.422 | -5.3% | -3 |
| Process | 1.431 | 1.994 | +39.3% | +14 |

## What the Numbers Show

Wall-clock time improved by 2-20% for every benchmark except `Process`.
The largest gains appeared where events are created and triggered frequently:
failing events (-20%),
basic `Event` and `Timeout` (-15%),
and `Environment.run(until=)` (-15%).
The savings come primarily from eliminating one C-level allocation per event completion
(the `partial` object in change 1)
and one per event creation (the empty list in change 4).
Neither of these shows up as fewer Python bytecodes
because `sys.monitoring` counts only Python-level instructions, not C heap allocations.
This is is why instruction counts changed by only 1-5 for most benchmarks
even when wall-clock time fell.

The instruction increases on `Resource (contention/multi-capacity)` (+13) and `Process` (+14)
come from the three new bytecodes per `_loop` entry introduced by change 1
(read `_resume_value`, clear it to `None`)
and the `isinstance` branch introduced by change 3.
For resource contention,
where multiple processes queue for the same resource,
these extra instructions are more than offset by the C-level savings:
wall-clock still fell 6-8%.

The `Process` microbenchmark is the one genuine regression (+39% wall-clock, +14 instructions).
It measures the cost of creating and running a single minimal process to completion.
At that scale the fixed per-`_loop` overhead from changes 1 and 3 has nothing to amortise against.
In any simulation where a process awaits more than one event during its lifetime,
which is the overwhelmingly common case,
those costs are shared across many events and the net result is a speedup.

## What I Can't Benchmark

These changes definitely make asimpy harder to understand:
for example,
inlining `_add_waiter` moves an action from what feels like its natural home
to an entirely different part of the library.
I wouldn't have thought of doing this on my own,
and while I understand what Claude suggested in retrospect,
I don't know how long it would take to wrap my head around it
if I was reading the code for the first time.
People are using phrases like "cognitive debt" and "comprehension debt" to describe this phenomenon;
my only consolation is that software systems have *always* struggled with this.

[asimpy]: https://asimpy.readthedocs.io/
[benchmark]: @root/2026/04/18/asimpy-performance-benchmarking/
