---
title: "Software Design by Example in Python 19: A Build Manager"
date: 2024-04-19
---

Having had to learn almost everything that went into [the previous chapter][sdxpy_db] from scratch,
it was a relief to explain some code that I got right (almost) the first time.
I've been using Make for forty years,
and have implemented graph-based dependency managers at least twice
when off-the-shelf tools wouldn't do what I needed.
Representing dependencies,
checking for circularity,
sorting topologically,
providing a way to write generic rules:
it felt a lot like humming along to an old, familiar song.

However,
[Chapter 19: A Build Manager][sdxpy_build] fell flat when I taught it last year.
Looking back,
I think the problem was that
most of my learners didn't have a need for such a tool.
One or two of them had used compiled languages,
and a couple of others had encountered problems big enough to need workflow engines,
but the rest were data scientists doing laptop-scale analyses.
If they had seen [marimo][marimo]
(a Python notebook that tracks inter-cell dependencies)
they might have been more enthusiastic;
instead,
this was one of the few times when I needed to tell them that the problem was real.

<img class="centered" src="@root/sdxpy/build/concept_map.svg" alt="Concept map for a build manager"/>

> Terms defined: affordance, build manager, build recipe, build rule, circular dependency, compiled language, cycle, dependency (in build), directed acyclic graph, dry run, link (a program), phony target, stable sort, stale (in build), target (in build), Template Method pattern, topological order.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[marimo]: https://marimo.io/
[sdxpy_build]: @root/sdxpy/build/
[sdxpy_db]: @root/sdxpy/db/
