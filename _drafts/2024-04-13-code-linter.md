---
title: "Software Design by Example in Python 13: A Code Linter"
date: 2024-04-13
year: 2024
---

As I wrote [yesterday][template_post],
the [HTML validator example][sdxpy_check] has two natural follow-ons:
a [template expander][sdxpy_template]
and a [linter][sdxpy_lint] that checks whether the source of a Python program
obeys a set of rules.
Of these,
I think the second is more important:
the original `lint` utility on Unix helped me learn how to write C properly,
and I now set up [ruff][ruff] before writing the first line of Python in a new project.

One thing that surprised me as I was writing this chapter
was how few new ideas it needed to introduce.
By this point in the book,
readers understand that a program is just a data structure in memory
and have walked trees using the Visitor pattern;
putting those two things together was a lot easier than I feared it would be.
In a way,
the fact that the concept map below is smaller than most of its predecessors
is a sign that I've put topics in the right (or "a" right) order.

<img class="centered" src="{{'/sdxpy/lint/concept_map.svg' | relative_url}}" alt="Concept map for a code linter"/>

> Terms defined: false negative, linter.

<img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">

[ruff]: https://docs.astral.sh/ruff/
[sdxpy]: {{'/sdxpy/' | relative_url}}
[sdxpy_check]: {{'/sdxpy/check/' | relative_url}}
[sdxpy_lint]: {{'/sdxpy/lint/' | relative_url}}
[sdxpy_template]: {{'/sdxpy/template/' | relative_url}}
