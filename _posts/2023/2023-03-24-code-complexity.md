---
title: "Code Complexity"
date: 2023-03-24
year: 2023
---

I wrote a small program this afternoon to parse a set of Python files
using the [`ast`](https://docs.python.org/3/library/ast.html) module
and then count the number of distinct language features used in each file.
I then divided the results into three groups:

1.  `lib`: extensions I've written for [Ivy](https://www.dmulholl.com/docs/ivy/dev/)
    (my favorite static site generator)
    that create a glossary,
    cross-reference figures,
    and so on.

2.  `bin`: tools I've written to convert a set of HTML files to LaTeX,
    check the structure of book projects,
    and so on.

3.  `src`: examples used in the *Software Design by Example* book
    I'm currently writing.

The examples use fewer of Python's features than my tools do.
I'm rather pleased by this:
my goal is to teach general principles of software design rather than advanced Python,
and I think that the more of Python's features I use,
the less transferable the concepts will be.

<div align="center">
<img src="{{'/files/2023/code-complexity.png' | relative_url}}" alt="Histogram of language feature usage"/>
</div>

> Follow-up: I didn't mean to suggest that using fewer language features means the code is simpler.
> Language features are a compression mechanism:
> if you don't use them,
> you often have to implement the same functionality in libraries,
> which increases the volume of code the next person has to read and understand.
> (OK, not "has to", but if we're comparing apples to apples…)
> You can move complexity and learning burden around but not eliminate it.
