---
title: "Software Design by Example in Python 9: Functions and Closures"
date: 2024-04-09
year: 2024
---

I didn't initially plan to write this chapter,
but the puzzled looks on my learners' faces the first few times I tried to teach decorators
convinced me it was necessary.
If Python's decorators treated their first argument specially
in the way that methods do,
multi-argument decorators would be simpler to write
and a _lot_ simpler to teach.
Since they don't,
this chapter spends 1800 words on dynamic versus lexical scoping,
eager versus lazy evaluation,
closures,
lambda expressions,
and a handful of other ideas people need
when they're trying to debug Python's more advanced features.

<img class="centered" src="{{'/sdxpy/func/concept_map.svg' | relative_url}}" alt="Concept map for functions and closures"/>

> Terms defined: anonymous function, call stack, closure, dynamic scoping, eager evaluation, extensibility, lambda expression, lazy evaluation, lexical scoping, name collision, stack frame, variable capture.

<img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">

[sdxpy]: {{'/sdxpy/' | relative_url}}
