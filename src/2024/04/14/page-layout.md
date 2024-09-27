---
title: "Software Design by Example in Python 14: Page Layout"
date: 2024-04-14
---

As I said [a week ago][post_interp],
some people think you don't really understand how computers work
unless you've written a compiler.
My rejoinder these days is that
writing a web browser will teach you a lot more about modern computer systems.
Panchekha and Harrelson's [*Web Browser Engineering*][browser]
covers everything from downloading HTML and constructing a DOM tree
to keeping data private,
scheduling tasks,
caching,
and accessibility.
I couldn't possibly cover all of that,
so [Chapter 14: Page Layout][sdxpy_layout] focused on one small problem:
how to decide what is displayed where on a page.

That question led to the most intensely algorithmic chapter of the book,
as row-and-column layout with elastic constraints
requires a bit of tricksy recursion.
The chapter doesn't get very far,
but I hope that by the end readers will understand
that the problem is much harder than it first appears
and that CSS is every bit as much a programming language as Lisp or C++.

<img class="centered" src="@root/sdxpy/layout/concept_map.svg" alt="Concept map for page layout"/>

> Terms defined: accidental complexity, block (on page), confirmation bias, easy mode, intrinsic complexity, layout engine, Liskov Substitution Principle, mixin class, z-buffering.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[browser]: http://browser.engineering/
[post_interp]: @root/2024/04/07/an-interpreter/
[sdxpy_layout]: @root/sdxpy/layout/
