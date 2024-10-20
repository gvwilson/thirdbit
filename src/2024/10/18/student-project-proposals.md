---
title: "Student Project Proposals"
date: 2024-10-18
---

My laptop screensaver says "no new projects" but I'd make an exception
to supervise a team of 2-4 undergraduates who wanted to tackle one of
the challenges described below. If you are teaching an undergraduate
capstone course and might be interested, please reach out.

## Browsercast

Tools like PowerPoint aren't web-friendly.  When you export a
slideshow to present on the web, what you actually get is a bunch of
images.  There's no text, just pixels arranged in the shapes of
letters; no hyperlinks; and nothing search engines or disability aids
can read.  What's worse, if you want something people can replay, you
have to make a screencast, which are just as opaque to search engines
and disability aids and probably several times larger than the
original slides.

Browsercast is our solution to this problem.  It plays snippets of
audio in your browser as you move through your slides.  "View Source",
links, CSS, screen readers, and search work as they should because
it's all still web-native HTML.  And since it's just text and audio,
it's a fraction of the size of a video, which makes it ideal for
mobile devices.

Our prototype uses just 5kb of JavaScript and is available under the
MIT License. There are many open questions; we are looking for a team
of 2-4 students with strong JavaScript skills and an interest in user
experience design to explore ways we can make it better.

- [Browsercast][browsercast]

## Marimo and H5P

Marimo is a next-generation computational notebook that enables data
scientists to mix code, discussion, and results in a reproducible way.
Its plugin system relies on AnyWidget, which specifies a simple
contract between extensions and Marimo's rendering and execution
engine.

The aim of this project is to design, build, and test a set of Marimo
plugins that can be used for classroom exercises similar to those in
the H5P toolkit: multiple choice, fill in the blanks, and so on. We
are looking for a team of 2-4 students with both JavaScript and Python
skills who have an interest in both user experience design and
teaching.

- [Marimo Notebook][marimo]
- [AnyWidget][anywidget]
- [H5P Content Types][h5]

## Dragnet

One type of exercise that H5P *doesn't* support is adding labels to
diagrams. [This prototype][dragnet] takes an SVG with some
specially-marked labels, moves those labels to the side, and then lets
the user try to drag them back into the right places.  A deployable
version would need to do a lot more, such as dealing with scaling
transformations; the goal of this project is to turn the demo into
something a classroom teacher could use.

- [Dragnet][dragnet]

## A Tutorial Simulation of Network Protocols

[*Software Design by Example in Python*][sdxpy] deliberately ignored
concurrency, partial failure, and everything else associated with
modern distributed applications. The aim of this project is to (start
to) fix that by building scale models of real network protocols such
as TCP and the BitTorrent protocol using either [Py-DES][pydes] or
[SimPy][simpy]. The tutorials will use simulators so that the
accompanying lessons could illustrate edge cases in reproducible ways;
making the implementations work on a real network as well will be a
good stretch goal.

## Software Design by Example in Gleam

For decades, functional programming (FP) has offered an alternative to
the imperative, procedural model used by most languages. As highly
concurrent systems have become the norm, FP's promise of preventing
entire classes of bugs by avoiding mutable state has led a growing
number of programmers to re-examine it, but there is still often a
gulf between the kinds of examples language designers find
interesting and the kinds of things most working programmers build.

[Gleam][gleam] is a modern functional language that runs on the
[Erlang/OTP][erlang] platform (and can also be compiled to
JavaScript). The aim of this project is to translate examples from
[*Software Design by Example in Python*][sdxpy] into Gleam to help
people coming from Python and other mainstream languages understand
how to use FP in practice.

[anywidget]: https://anywidget.dev/
[browsercast]: https://github.com/gvwilson/browsercast
[dragnet]: https://iezer.github.io/dragnet/
[erlang]: https://www.erlang.org/
[gleam]: https://gleam.run/
[h5p]: https://h5p.org/content-types-and-applications
[marimo]: https://marimo.io/
[pydes]: https://pydes.readthedocs.io/
[sdxpy]: https://third-bit.com/sdxpy/
[simpy]: https://simpy.readthedocs.io/
