---
title: "Software Design by Example in Python 3: Finding Duplicate Files"
date: 2024-04-03
---

The [first chapter][sdxpy_oop] of [*Software Design by Example*][sdxpy] looks inward
at Python itself
to show how objects and classes are really just fancy dictionaries
(for some large value of "just").
[Chapter 3: Finding Duplicate Files][sdxpy_dup] looks outward at the problems Python is used to solve,
and in doing so,
introduces some ideas about hashing,
systems programming,
and the conventions that Unix command-line tools are expected to respect.

The first and third of these ideas are well-defined,
but "systems programming" turned out to be a slippery concept.
For me,
it means "doing things with a program that you'd normally do in the shell",
like making directories and renaming files or changing their permissions,
but I discovered that other people reserve the term for more advanced problems
like authentication and network configuration.
I'm now working sporadically on a [new tutorial][sys_tutorial]
to figure out where I think the topic's boundaries are,
which is proof yet again that every lesson leads to three others.

<img class="centered" src="@root/sdxpy/dup/concept_map.svg" alt="Concept map for finding duplicate files"/>

> Terms defined: big-oh notation, binary mode, bucket, collision (in hashing), cryptographic hash function, hash code, hash function, hexadecimal, SHA-256 (hash function), streaming API, time complexity.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[sdxpy]: @root/sdxpy/
[sdxpy_dup]: @root/sdxpy/dup/
[sdxpy_oop]: @root/sdxpy/oop/
[sys_tutorial]: https://gvwilson.github.io/sys-tutorial/
