---
title: "Software Design by Example 14: Style Checker"
date: 2023-01-18
year: 2023
---

Programmers argue endlessly about the best way to format their programs,
but (almost) everyone agrees that the most important thing is to be consistent.
Since checking rules by hand is tedious,
most programmers use linting tools to make sure their code meets a set of rules
and to reformat it if it doesn't.
[Chapter 14][sdxjs_checker] of [*Software Design by Example*][sdxjs]
builds a simple linter inspired by ESLint,
which I used to check all the code samples in the book.
This tool parses source code to create a data structure,
then goes through that data structure and applies rules.

As with many previous chapters,
it emphasizes the idea that a program is just another kind of data.
It also re-introduces the Visitor design pattern
that carries an action to each element of a data structure.
If I'd had time and energy,
I would have also implemented this tool using the Iterator pattern
that brings each element to the action
so that I could compare and contrast the two approaches.
If anyone feels motivated to give this a try,
please [give me a shout][email].

<figure id="style-checker-walk-tree" class="figure-here" class="center">
  <img src="{{'/sdxjs/style-checker/walk-tree.svg' | relative_url}}" alt="Walking a tree" class="centered">
  <figcaption>Figure 14.2: Walking a tree to perform an operation at each node.</figcaption>
</figure>

> Terms defined: abstract syntax tree, Adapter pattern, column-major storage, dynamic lookup, generator function, intrinsic complexity, Iterator pattern, linter, Markdown, row-major storage, walk (a tree).

This chapter got me thinking about why Lisp-like languages such as Scheme have remained a niche interest
despite computer scientists using them in introductory courses for several decades.
These languages' distinguishing features are (a) their preference for recursion instead of iteration
and (b) the fact that programs are explicitly represented as data structures (in this case, nested lists),
which makes the kind of introspection and manipulation described in this chapter much easier.
I firmly believe that recursion is harder for most people to wrap their heads around than loops,
though I accept that true believers won't ever agree with me.
What took me longer to realize,
though,
is that Lisp's homoiconic representation of programs as lists is irrelevant to most novices
because *it solves a problem they aren't ready to worry about yet*.
Looking over [*Software Design by Example*][sdxjs] now,
I'm not sure it introduces challenges in the order that readers will be ready for;
I'm going to have to think hard about this for the Python edition.

[email]: mailto:{{site.author.email}}
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxjs_checker]: {{'/sdxjs/style-checker/' | relative_url}}
