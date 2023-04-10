---
title: "Dressed in Hand-Me-Down Clothes"
date: 2023-04-10
year: 2023
---

I've been updated the Python version of [*Software Design by Example*][sdxjs],
and once again I feel like I'm using the butt end of a screwdriver as a hammer.
Version control systems are designed for developing applications,
but when you're teaching,
you often want to have many versions of the "same" file available at once.
For example,
consider Wasim Lorgat's tutorial on [how to build a text editor in Python][lorgat-editor].
What it *wants* is a horizontal scroll on a single source file
so that readers can move forward and backward in time without losing context
(i.e., while having previous and subsequent versions of the file in view):

<img src="{{'/files/2023/editor-evolution.svg' | relative_url}}" alt="views of Lorgat's evolving editor">

I'd settle for something that would automatically generate an image like the one above—if nothing else,
it would work better in a print edition.
But how do I manage the snapshots of the file's evolution?
Do I create `editor_1.py`, `editor_2.py`, and so on, all in the same directory?
I've been down that road (as I'm sure many other authors have),
and inevitably you wind up creating `editor_1.5.py`
or renaming a dozen files to bump version numbers,
and then realize after the book has shipped that you made a change to eleven of the snapshots but not the twelfth
so now the presentation has continuity glitches.

Version control systems are designed to materialize one copy of each file at any moment.
When you're teaching you often want multiple copies,
each slightly different from the ones before and after in logical order,
but don't want to have to maintain the consistency manually.
In that respect I think teaching and data analysis have more in common with each other
than either does with "normal" software development,
but the first two seem forever having to dress in the latter's hand-me-downs.

[lorgat-editor]: https://wasimlorgat.com/posts/editor.html
[sdxjs]: {{'/sdxjs/' | relative_url}}
