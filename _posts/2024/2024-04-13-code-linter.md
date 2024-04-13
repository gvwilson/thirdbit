---
title: "Software Design by Example in Python 13: A Code Linter"
date: 2024-04-13
year: 2024
---

The [HTML validator example][sdxpy_check] in Chapter 11 has two natural follow-ons.
the [template expander][sdxpy_template] of Chapter 12
(discussed [yesterday][template_post])
and [a linter][sdxpy_lint] that checks whether the source of a Python program
obeys a set of rules.
Of these,
I think the second is more important:
the original `lint` utility on Unix helped me learn how to write C properly,
and I now set up [ruff][ruff] before writing the first line of Python in a new project.

One thing that surprised me as I was writing [Chapter 13: A Code Linter][sdxpy_lint]
was how few new ideas it needed to introduce.
By this point in the book,
readers have walked trees using the Visitor pattern
and understand that a program is just a data structure in memory.
Putting those two things together was a lot easier than I feared it would be;
in a way,
the fact that the concept map below is smaller than most of its predecessors
is a sign that I've put topics in the right (or "a" right) order.

*Note: I would be grateful for help getting [the book][sdxpy] to display properly in dark mode.
In particular, if you have a tool that will convert the SVG produced by [draw.io][draw_io] to white-on-black
and some CSS to select them in place of the black-on-white versions,
please [get in touch](mailto:{{site.author.email}}).*

<img class="centered" src="{{'/sdxpy/lint/concept_map.svg' | relative_url}}" alt="Concept map for a code linter"/>

> Terms defined: false negative, linter.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[draw_io]: https://app.diagrams.net/
[ruff]: https://docs.astral.sh/ruff/
[sdxpy]: {{'/sdxpy/' | relative_url}}
[sdxpy_check]: {{'/sdxpy/check/' | relative_url}}
[sdxpy_lint]: {{'/sdxpy/lint/' | relative_url}}
[sdxpy_template]: {{'/sdxpy/template/' | relative_url}}
