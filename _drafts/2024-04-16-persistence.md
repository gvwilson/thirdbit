---
title: "Software Design by Example in Python 16: Object Persistence"
date: 2024-04-16
year: 2024
---

I don't know how many times I've written code to
[save and load data structures][sdxpy_persist],
but I've done it enough that
writing this chapter felt like visiting an old friend.
Atomic types and a handful of built-in containers like lists and dictionaries are easy;
handling user-defined types is also straightforward
*if* you assume that the code that's loading the data
is using exactly the same classes as the one that created it.
If not—or if you're going across languages and need to figure out
what to do with a Python when you're reading data back in JavaScript—the
problem goes from "done in a coffee break" to "needs the attention of a product manager".

Aliasing falls somewhere in between.
The problem and its solution are well defined,
and writing test cases is easy,
but as [this chapter][sdxpy_persist] shows,
it's easy to implement the loader in ways that are almost-but-not-quite correct.
I hope that showing the "almost" before showing the "correct"
is more enlightening than confusing;
as always
[feedback is welcome](mailto:{{site.author.email}}).

<img class="centered" src="{{'/sdxpy/persist/concept_map.svg' | relative_url}}" alt="Concept map for object persistence"/>

> Terms defined: atomic value, list comprehension, Open-Closed Principle, persistence.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[sdxpy]: {{'/sdxpy/' | relative_url}}
[sdxpy_persist]: {{'/sdxpy/persist/' | relative_url}}
