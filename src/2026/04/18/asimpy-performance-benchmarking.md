---
title: "asimpy Performance Benchmarking"
date: 2026-04-18
---

[asimpy][asimpy] is a discrete event simulation framework written in Python.
Unlike [SimPy][simpy], it uses `async`/`await` rather than `yield`,
which is more in keeping with modern Python idioms
and makes it easier to (for example) write simulation-based mocks of modern `async` libraries
to use in testing and teaching.
The latest version on [PyPI][asimpy-pypi] includes some benchmarking scripts
that compare the performance of the two libraries.

The results below show that asimpy is faster for some things but slower for others.
SimPy is faster for basic scheduling primitives:
Timeout, Event, Interrupt, and Process creation all need roughly half as many instructions
because Python's `yield` carries lower per-resumption overhead than `async`/`await`.
(A generator frame advance is a single C-level operation,
but an `async` coroutine suspension goes through the __await__ protocol
and a coroutine wrapper before reaching the same point.)

asimpy is faster for resource, container, and store operations
because SimPy models every such interaction as a pair of distinct event objects
(`Request`/`Release`, `ContainerPut`/`ContainerGet`, and `StorePut`/`StoreGet`)
that must be allocated, appended to a queue, scheduled on the heap, popped,
and then trigger a separate chain of callbacks.
All together,
these operations require roughly three times as many instructions asimpy's equivalent
for an uncontended resource acquire and release.
In short,
asimpy pays more than SimPy per scheduler tick but less per resource operation,
so which library is faster for a given simulation
depends on how many processes spend their time waiting on timeouts and events
versus competing for shared resources.

I'd like to find a way to reduce asimpy's instruction count for simple operations.
If you'd like to have a look and offer suggestions (or pull requests),
they would be very welcome.

> Note: most of the tests for asimpy were generated using Claude,
> as were the benchmark programs,
> and I asked its advice several times
> while trying to make asimpy's implementation more uniform
> and while trying to debug `FirstOf`.

| Feature                           | asimpy |  simpy | asimpy/simpy |
| :---------------------------------|------: |------: |------------: |
| AllOf                             |  338.2 |  569.6 |        0.594 |
| AllOf (blocking)                  |  674.4 |  703.8 |        0.958 |
| Barrier / Barrier (via Event)     |  440.4 |  258.8 |        1.702 |
| Container                         |  273.2 |  520.8 |        0.525 |
| Container (float amounts)         |  273.2 |  520.8 |        0.525 |
| Container (non-blocking)          |   53.2 |    N/A |          N/A |
| Environment.get_log               |   11.2 |    N/A |          N/A |
| Environment.log                   |   20.2 |    N/A |          N/A |
| Environment.run(until=)           |  253.3 |  121.5 |        2.084 |
| Event                             |  181.2 |  129.6 |        1.399 |
| Event (cancel)                    |   42.2 |    N/A |          N/A |
| Event (fail)                      |  210.2 |  166.6 |        1.262 |
| FirstOf / AnyOf                   |  326.2 |  469.6 |        0.695 |
| FirstOf / AnyOf (blocking)        |  659.4 |  603.8 |        1.092 |
| Interrupt                         |  532.4 |  427.8 |        1.244 |
| Interrupt (with cause)            |  540.4 |  440.8 |        1.226 |
| PreemptiveResource                |  922.4 | 1423.8 |        0.648 |
| PreemptiveResource (cause fields) |  933.4 | 1444.8 |        0.646 |
| PreemptiveResource (no-preempt)   |  829.3 | 1283.0 |        0.646 |
| PriorityQueue / PriorityStore     |  271.2 |  494.7 |        0.548 |
| Process                           |  349.1 |  323.4 |        1.080 |
| Queue                             |  268.2 |    N/A |          N/A |
| Queue (blocking get)              |  553.4 |    N/A |          N/A |
| Queue (blocking put)              |  606.3 |    N/A |          N/A |
| Queue (non-blocking)              |   53.2 |    N/A |          N/A |
| Resource (contention)             |  565.0 |  804.5 |        0.702 |
| Resource (context manager)        |  160.2 |  482.8 |        0.332 |
| Resource (multi-capacity)         |  563.3 |  804.4 |        0.700 |
| Resource (try_acquire)            |   39.2 |    N/A |          N/A |
| Resource (uncontended)            |  138.2 |  445.8 |        0.310 |
| Store                             |  264.2 |  479.8 |        0.551 |
| Store (FIFO queue)                |    N/A |  479.8 |          N/A |
| Store (blocking get)              |    N/A |  635.0 |          N/A |
| Store (blocking put)              |    N/A |  638.9 |          N/A |
| Store (filtered get)              |  273.2 |  517.7 |        0.528 |
| Store (non-blocking)              |   47.2 |    N/A |          N/A |
| Timeout                           |  252.2 |  123.6 |        2.041 |

[asimpy]: https://asimpy.readthedocs.io/
[asimpy-pypi]: https://pypi.org/project/asimpy/
[simpy]: https://simpy.readthedocs.io/
