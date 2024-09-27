---
title: "Software Design by Example in Python 24: Undo and Redo"
date: 2024-04-24
---

[Chapter 24: Undo and Redo][sdxpy_undo]
is a direct continuation of [Chapter 23][sdxpy_viewer],
which felt a bit like cheating on my "one hour per topic" rule
but was unavoidable.
Having created a curses-based file viewer,
the obvious next steps are to allow users to insert and delete characters
and then to undo and redo operations.
Both turn out to have awkward edge cases,
and I'm still not sure this chapter does an adequate job of explaining them all.

On a personal note,
one thing I wrote, re-wrote, and finally decided to leave out was
the sense of wonder I felt when I first encountered "undo" in the summer of 1981.
I was working in a government office in a small town in British Columbia
that had just taken delivery of its first word processor
(yes, a dedicated machine, not a PC with a word processing application).
Being able to fix what was on the screen before printing it
was quite amazing to people who had been using typewriters for years (in my case)
or decades (in the case of my older colleagues).
The fact that *the computer remembered what you'd done*
and could make the changes for you
seemed like sorcery.

I know that most of the people reading this page have grown up taking that ability for granted,
but wanting to know how it worked was,
quite seriously,
one of the things that made me become a programmer.
Forty-three years later,
I hope I've managed to pass on how magical it once felt.

<img class="centered" src="@root/sdxpy/undo/concept_map.svg" alt="Concept map for undo and redo"/>

> Terms defined: buffer (of text), delayed construction, enumeration, factory method, log file, synthetic data, viewport.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[sdxpy_undo]: @root/sdxpy/undo/
[sdxpy_viewer]: @root/sdxpy/viewer/
