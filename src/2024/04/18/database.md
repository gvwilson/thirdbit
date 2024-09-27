---
title: "Software Design by Example in Python 18: A Database"
date: 2024-04-18
---

<blockquote>
  The book is an excellent guide for anyone going from "just programming" to building larger projects.
  It's like a choose-your-own adventure,
  but the adventure is learning to build very complex software as a composition of much simpler patterns.
  <br>
  - <a href="https://jenniferplusplus.com/">Jennifer Moore</a>
</blockquote>

One of the joys of writing is learning new things yourself in order to explain them to others.
By that standard [Chapter 18: A Database][sdxpy_db] was more joyful than most,
though it didn't feel that way at the time.
I knew at the outset that a relational database using B-trees wouldn't fit in my one-hour limit,
so I started reading about log-structured databases.
Once my head stopped swimming I tried to build one,
and quickly realized that if I wanted it to be manageable
I would have to ignore the same issues around atomic multi-file operations
that I ignored in the chapter on [a file archiver][sdxpy_archive].
I thought I would come back to them,
but time, interest, and space all ran out;
if there's ever a sequel to [this book][sdxpy],
I hope that will be its first chapter.

<img class="centered" src="@root/sdxpy/db/concept_map.svg" alt="Concept map for a database"/>

> Terms defined: block (of memory), compact (data or files), garbage collection, key-value store, log-structured database, null byte, page.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[sdxpy]: @root/sdxpy/
[sdxpy_archive]: @root/sdxpy/archive/
[sdxpy_db]: @root/sdxpy/db/
