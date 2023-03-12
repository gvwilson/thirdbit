---
title: "Rethinking Design Examples"
date: 2023-03-12
year: 2023
---

We're five weeks into the class I'm running on
the Python version of [*Software Design by Example*][sdxjs],
and it's already clear that I'm going to have to reorganize and rewrite almost everything:

1.  The backgrounds and needs of my [three personas][personas] are too broad.
    I now believe I should focus on Aïsha:
    a data scientist who wants to fill in gaps in her foundational understanding of programming.

2.  Many of the chapters move too quickly.
    I could split them and enlarge the pieces,
    but that would result in a 600-page tome.
    Instead,
    I need to cut some examples entirely and simplify others.

The figure below is my first draft of a new outline.
The circles mark entry points,
the arrows show dependencies,
and the whole thing builds toward a static site generator
for reporting and tracking data analysis results.
Figuring two weeks of real time per chapter to revise and polish,
it will take me about 35 weeks.
I won't be able to start until I'm finished this class in seven weeks,
so the earliest I can expect to have the next version is the end of 2023.
That's disappointing—it means the book won't be in print until the second half of 2024—but
as my brother used to say,
when you're planning a project,
"optimistic" is just another word for "doomed".

<div class="center">
  <img
  src="{{'/files/2023/design-examples.svg' | relative_url}}"
  alt="Pedagogical dependencies for 'Software Design by Example in Python'">
</div>

The biggest obstacle to completing this book, though,
is that I no longer believe it will make a difference.
I've been working with biologists for seventeen months,
and as far as I can tell,
most of them don't know any more about programming than they did [in 1996][ieee-what].
A class on hashing, introspection, and asynchronous I/O isn't going to change that;
we need an overhaul of the undergraduate curriculum,
changes to how faculty are evaluated and compensated,
and an end to today's exploitive research publishing system.

We won't get any of that without teaching people about institutional change
and helping them organize to apply what they've learned,
but existing open science groups get very uncomfortable when I suggest that
being nice never fixed anything that actually matters.
I don't have enough energy (or knowledge) to try to build another organization from scratch,
so for now I'll draw diagrams,
simplify my code,
and dream of a better, braver world.

[ieee-what]: https://doi.org/10.1109/99.503313
[personas]: {{'/2023/01/29/would-you-take-this-class/' | relative_url}}
[sdxjs]: {{'/sdxjs/' | relative_url}}
