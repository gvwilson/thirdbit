---
layout: post
date: 2019-06-06 16:27
title: "What I Would Build (If I Still Wrote Software)"
favorite: true
---

My previous two posts described
[things I would do (if I still did research)]({{site.github.url}}/2019/06/05/things-i-would-do.html)
and [what I would write (if I was smarter than I am)]({{site.github.url}}/2019/06/06/what-i-would-write.html).
I also have a list of things I would build if I still wrote software:

A computational notebook for blocks-based programming.
:   R Markdown, Stencila, and the Jupyter notebook are great ways to tell dynamic stories with and about code.
    I'd really like a notebook whose code sections were built with blocks rather than text.

A computational notebook that includes a drawing tool.
:   And while we're at it, the workflow for putting hand-drawn (vector) diagrams into notebooks is pretty clumsy.
    Open drawing tool, save file, add reference to notebook, render, curse, re-draw, re-render...
    I'd like to be able to click on a diagram in a notebook and edit it in place
    just like I can in Word or Google Doc.
    There are several good open source JavaScript vector drawing tools out there,
    and the SVG could either be embedded in the notebook document or stored in a side file.

[Browsercast]({{site.github.url}}/browsercast/).
:   It's been almost ten years since I first wanted to be able to add a voiceover to an HTML slideshow.
    I still want it,
    but these days I'd like to be able to replay a computational notebook with commentary as well.
    We came close a couple of times, but never quite got there;
    playback is straightforward,
    but tools to edit and sync the audio require more thought.

A lightweight lesson aggregation tool.
:   Instead of building yet another repository for lessons or trying to get people to use a single template,
    it would probably be more useful to
    [aggregate metadata about the lessons they already have](https://github.com/gvwilson/harper).

Tutorial implementations of common software tools.
:   *[Software Tools](http://www.amazon.com/Software-Tools-Brian-W-Kernighan/dp/020103669X/)*
    and *[its sequel](http://www.amazon.com/Software-Tools-Pascal-Brian-Kernighan/dp/0201103427/)*
    taught my generation how to design software
    by showing us how to create small versions of the very tools we were using.
    I'd like to do the same exercise using JavaScript, JSON, and HTTP
    instead of C, ASCII strings, and standard I/O.
    Mary Rose Cook's [Gitlet](http://gitlet.maryrosecook.com/) is a beautiful example of what this might look like;
    I want to do the same thing for eslint, NPM, and the like
    and then use them to teach software architecture.

A single-pass LaTeX compiler.
:   Because we can fit an entire encyclopedia into memory these days
    and I am *so* done with writing Makefiles to run LaTeX two or three times
    to update numbered cross-references.
