---
title: "Software Design by Example in Python 16: Object Persistence"
date: 2024-04-16
---

I don't know how many times I've written code to save and load data structures,
but I've done it enough that
[Chapter 16: Object Persistence][sdxpy_persist] felt like visiting an old friend.
Atomic types and built-in containers like lists and dictionaries are easy;
handling user-defined types is also straightforward
*if* you assume that the code that's loading the data
is using exactly the same classes as the one that created it.
If not,
or if you're going across languages and need to figure out
what to do with a Python when you're reading data back in JavaScript,
the problem goes from "done in a coffee break"
to "needs the attention of a product manager".

Aliasing falls somewhere in between.
The problem and its solution are well defined,
and writing test cases is easy,
but as [this chapter][sdxpy_persist] shows,
it's easy to implement the loader in ways that are almost-but-not-quite correct.
I hope that showing the "almost" before showing the "correct"
is more enlightening than confusing;
as always [feedback is welcome](mailto:gvwilson@third-bit.com).

<img class="centered" src="@root/sdxpy/persist/concept_map.svg" alt="Concept map for object persistence"/>

> Terms defined: atomic value, list comprehension, Open-Closed Principle, persistence.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[sdxpy]: @root/sdxpy/
[sdxpy_persist]: @root/sdxpy/persist/
