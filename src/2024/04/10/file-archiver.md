---
title: "Software Design by Example in Python 10: A File Archiver"
date: 2024-04-10
---

[*Software Design by Example*][sdxpy] began as a response to the shortcomings of [*Beautiful Code*][bc],
but two specific things spurred me to finally write it and [its JavaScript predecessor][sdxjs]:

1.  Mary Rose Cook's [Gitlet][gitlet],
    which is a rational reconstruction of Git's internals in JavaScript	.
    (I'm currently working my way slowly through James Coglan's [*Building Git*][building_git],
    which goes deeper using Ruby.)

2.  The seemingly simple question, "How does a debugger actually work?"

The book addresses the second of these [near its end][sdxpy_debugger],
but once learners understand how mock objects actually work,
they can understand how to build *and test* a little version control system.
The latter is as important as the former:
I was in my forties when I learned that
I could replace the entire filesystem for testing purposes
using something like [pyfakefs][pyfakefs],
and I don't think other people should have to wait that long.

[Chapter 10: A File Archiver][sdxpy_archive] was fun to write;
my only regret is that I dodged the problem of atomic operations on multiple files,
which turned out to be a lot harder than I knew.
Coglan's book tackles it,
though,
so if there's ever a second edition of *SDXPY*,
I hope to include it.

<img class="centered" src="@root/sdxpy/archive/concept_map.svg" alt="Concept map for a file archiver"/>

> Terms defined: atomic operation, base class, compression (of file), Coordinated Universal Time, data migration, file locking, helper function, manifest, race condition, successive refinement, time of check - time of use, timestamp, top-down design, version control system.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[bc]: https://www.oreilly.com/library/view/beautiful-code/9780596510046/
[building_git]: https://shop.jcoglan.com/building-git/
[gitlet]: http://gitlet.maryrosecook.com/
[pyfakefs]: https://pytest-pyfakefs.readthedocs.io/
[sdxjs]: @root/sdxjs/
[sdxpy]: @root/sdxpy/
[sdxpy_archive]: @root/sdxpy/archive/
[sdxpy_debugger]: @root/sdxpy/debugger/
