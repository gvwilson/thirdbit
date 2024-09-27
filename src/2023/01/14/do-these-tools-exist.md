---
title: "Do These Tools Exist?"
date: 2023-01-14
---

I wrote several posts last year about why teaching or learning programming
is much harder than actually programming ([[1][third-dimension]], [[2][debuggable-explanations]])
and about the tools I wish we had to make this easier
([[3][code-in-textbooks]], [[4][memory-diagram]], [[5][explain-code]]).
Looking at what's supposed to be the final draft of the Python version of [*Software Design by Example*][sdxjs],
I don't think I'm going to be happy shipping it
until I can incorporate at least one new explanatory technology.
Before I start building anything,
I'd like to know if there's already a tool
(preferably written in Python or JavaScript)
that will take two text files as input
and produce the sort of side-by-side diff that many version control GUIs display:

<img src="@root/files/2023/diff-lineup.svg" alt="side-by-side diff of text files" class="centered">

The catch is that the result must still be text that can be copied and pasted
(and that can be accessed by screen readers and other accessibility aids),
not an image or an SVG with characters placed one by one.
The connecting lines can be drawn using SVG, though,
or with a `canvas` element or whatever else clever kids are using these days.
And yes,
this only solves half the problem—I'll need to figure out
some way to produce LaTeX in order to create the PDF my publisher needs—and yes,
I'll need to embed this in a pipeline that selects small portions from larger before-and-after files
so that I can show the differences between selected sections
rather than the differences between entire files,
but I know how to figure out all that stuff.

Similarly,
along with [memory diagram snapshots][memory-diagram],
I'd like a tool that illustrates the execution order of a small snippet of code:

<img src="@root/files/2023/sequence-of-steps.svg" alt="sequence of steps in code execution" class="centered">

I can create all these diagrams by hand,
but (a) it takes a lot of time
and (b) maintenance is a killer:
if I make even a small change in an example I have to check and re-do all the diagrams,
and if I decide to change fonts or line styles I have to re-do *all* of them.
If you have solutions,
I'd be grateful if you would [reach out][email].

[debuggable-explanations]: @root/2022/11/18/debuggable-explanations/
[code-in-textbooks]: @root/2022/11/30/what-i-want-for-code-in-textbooks/
[memory-diagram]: @root/2022/12/04/i-want-a-memory-diagram-generator/
[third-dimension]: @root/2022/12/14/teaching-in-the-third-dimension/
[explain-code]: @root/2022/12/28/ways-to-explain-code/
[sdxjs]: @root/sdxjs/
[email]: mailto:gvwilson@third-bit.com
