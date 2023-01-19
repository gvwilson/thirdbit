---
title: "Software Design by Example 15: Code Generator"
date: 2023-01-19
year: 2023
---

[Chapter 14][sdxjs_checker] turned source code into a data structure
in order to check that the code obeyed style rules.
[This chapter][sdxjs_generator] reverses the process
by turning the data structure that represents source code back into text.
This may seem like a pointless exercise,
but in between the parsing and the unparsing
we can modify the data structure
in order to produce a program that's slightly different from the one we started with.
If we do this carefully,
we can insert extra statements to check which functions are called when the program runs
or to record how long their execution takes.
Once more,
treating programs as data allows us to do some pretty powerful things.

Tools like this are hard to build for languages like JavaScript
because the source code as written is very different from
the data structure that represents it in memory.
The greatest strength of languages like [Scheme][scheme] is that
these two representations are much more closely aligned,
which makes this kind of metaprogramming much easier---once you get over the hurdle
of typing in parse trees.
As [noted yesterday][sdxjs_checker],
the overwhelming majority of programmers still prefer not to do this
sixty years after Lisp syntax was invented and despite decades of use in education.
I [used to believe][extensible] that programmers would one day switch from
punchcard-compatible programming tools to ones that separated models from views,
but I no longer expect to see that in my lifetime.
It's a shame---experiments like [the Glamorous Toolkit][glamorous]
make programming with lines of text look as antiquated as chiseling hieroglyphics onto stone tablets---but
even with this self-imposed clumsiness,
I still believe that [beautiful is possible][bicycle].

> Terms defined: byte code, code coverage (in testing), compiler, Decorator pattern, macro, nested function, two hard problems in computer science.

[bicycle]: {{'/2017/12/17/consider-the-bicycle/' | relative_url}}
[extensible]: https://queue.acm.org/detail.cfm?id=1039534
[glamorous]: https://gtoolkit.com/
[scheme]: https://en.wikipedia.org/wiki/Scheme_(programming_language)
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxjs_checker]: {{'/sdxjs/style-checker/' | relative_url}}
[sdxjs_generator]: {{'/sdxjs/code-generator/' | relative_url}}
