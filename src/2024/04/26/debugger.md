---
title: "Software Design by Example in Python 26: A Debugger"
date: 2024-04-26
---

As [I wrote two weeks ago][file_archiver],
two things led me to write the [JavaScript][sdxjs] and [Python][sdxpy] versions of
*Software Design by Example*:
Mary Rose Cook's [Gitlet][gitlet]
and the question, "How does a debugger work?"
Earlier chapters addressed the first,
and [Chapter 26: A Debugger][sdxpy_dbg] addresses the second.

I've complained many times over more than two decades about the fact that
universities don't teach debugging as a first-class skill,
and that while there are hundreds of books on how to write compilers,
I've only ever found three that explained how to write a debugger
(none of which were particularly good).
Showing people how to create and manage breakpoints isn't going to fix that,
but I'm glad I had a chance to do what I could.

*My thanks to <a href="https://jenniferplusplus.com/">Jennifer Moore</a>,
<a href="https://naomiceder.tech/">Naomi Ceder</a>,
and <a href="https://www.benormal.info/">Sue Smith</a>
for the reviews now posted on this site's [home page](@root/):
I'm glad they enjoyed the book.*

<img class="centered" src="@root/sdxpy/debugger/concept_map.svg" alt="Concept map for a debugger"/>

> Terms defined: breakpoint, clear (a breakpoint), conditional breakpoint, debugger, disassemble, reverse lookup, watchpoint.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[file_archiver]: @root/2024/04/10/file-archiver/
[gitlet]: http://gitlet.maryrosecook.com/
[sdxjs]: @root/sdxjs/
[sdxpy]: @root/sdxpy/
[sdxpy_dbg]: @root/sdxpy/debugger/
