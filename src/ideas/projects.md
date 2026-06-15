---
title: "Potential Student Projects"
template: page
---

Supervising graduate and undergraduate projects at the University of Toronto was
one of the most rewarding and satisfying things I ever did. If you're a student
or a faculty member in need of a one- or two-semester project, and any of the
ones listed below seem interesting, please reach out.

## In Progress

### Analysis of Undergrad Textbooks (research)

Most undergraduate computer science programs have a first- or second-year course
on data structures and algorithms.  What do these courses actually teach, and
which of these algorithms and data structures are used in upper-year courses? To
answer these questions, this project will assemble and apply tools to analyze
the text of several dozen textbooks; along the way, the students doing the
project will have to decide how to identify topics, how to count them, and how
to make their work reproducible.

### Project Closure (research)

There are hundred of books in print about how to start a business. Only a
handful discuss how to pass one on, and even talk about how to wind one down.
This project will study when, why, and how software projects are wound down,
either deliberately or on short notice.

### Validity of Software Engineering Claims (research)

Are some programmers really ten times more productive than others?  Does
test-driven development actually make programmers more productive?  And do
people actually believe these claims?  This project will conduct a quantitative
survey of best-selling books on software developmnt to measure how many of their
claims are backed by citations, and of those, how many are considered valid,
then survey programmers to see which (if any) they believe.

## Some Work Done But Not Active

### Blocks-Based Data Science (development)

[TidyBlocks](https://github.com/tidyblocks/tidyblocks) was a prototype of a
[Scratch](https://scratch.mit.edu/)-like tool for teaching introductory data
ascience.  It turned out to be an inappropriate visual paradigm, as there was no
natural way to represent join operations as nested blocks.  The aim of this
project is to explore an alternative using a node-and-connector model like that
of [Node-RED](https://nodered.org/) or [Yahoo! Pipes][pipes].

### Browsercast (development)

Tools like PowerPoint aren't web-friendly.  When you export a slideshow to the
web, what you get is a bunch of images, while screencasts are opaque to search
engines and disability aids.  In contrast, [Browsercast](@root/browsercast/)</a>
plays snippets of audio in the browser as the viewer moves through the slides,
so "View Source", links, CSS, screen readers, and search work as they should.
The [prototype](https://github.com/gvwilson/browsercast) uses just 5kb of
JavaScript; the aim of this project is to turn it into a functional tool.

### Identification of Variable Roles (research)

Sajaniemi's work on [roles of variables][variable-roles] identified and named
ten small patterns in the way variables are used in novice programs. This
project would build static and dynamic analysis tools to detect those patterns
(and possibly others) in programs as an aid to teaching, debugging, and code
review.

### Simulations of Distributed Systems (development)

[*Software Design by Example in Python*](@root/sdxpy/) deliberately ignored
concurrency, partial failure, and everything else associated with modern
distributed applications. [This project](@root/dsdx/) is fixing that by building
scale models of distributed protocols and systems from TCP to BitTorrent and
load-balancing tools using [asimpy](https://asimpy.readthedocs.io/). The
tutorials will use simulators so that the accompanying lessons could illustrate
edge cases in reproducible ways.

### Software Design by Example in Gleam (tutorial)

[Gleam](https://gleam.run/) is a modern functional language that runs on the
[Erlang/OTP](https://www.erlang.org/) platform and can also be compiled to
JavaScript. [This project](@root/gl4py/) will translate examples from [*Software
Design by Example in Python*](@root/sdxpy/) into Gleam to help people coming
from Python and other mainstream languages understand how to use FP in practice.

### Software Design by Example in Lean (tutorial)

[Lean](https://lean-lang.org/) is a modern functional language used primarily
for theorem proving. [This project](@root/l4py/) will translate examples from
[*Software Design by Example in Python*](@root/sdxpy/) into Lean to help people
coming from Python and other mainstream languages understand how to use FP in
practice.

### Unbreaking Software (tutorial)

Most programmers spend a large part of their time debugging, but most courses
only show working code, and most textbooks don't discuss how to prevent,
diagnose, and fix errors.  This tutorial fills that gap by presenting dozens of
case studies showing how to find and fix real-world problems.  Along the way, it
will present examples of what programmers can do to handle errors gracefully,
from data structure repair to automatically restarting servers.

### XKCD Charts (development)

[Chart.xkcd](https://timqian.com/chart.xkcd/) is a JavaScript library that
displays charts in the hand-drawn style of [XKCD](https://xkcd.com/). Its
creator is no longer maintaining it; this project will fork the original code,
fix outstanding issues, and add new features such as axis limits and stable
coloring schemes.

## Nothing Done Yet

### Bubbles! (game)

The aim of the game is to get your bug from one end of the map to the other by
riding on the surface of bubbles, which drift in the current.  Bubbles bounce
off each other, and off obstacles, deforming as they do so.  Your bug can only
move from one bubble to another during collision; to do so, it simply crawls
along the surface. But you have to be careful: if your bug is caught between two
bubbles, or between a bubble and an obstacle, it's crushed. Extensions include:

-   Your bug can kick its wee feet to push the bubble it's currently riding on
    in a particular direction. It won't have much effect (it's just a wee bug,
    after all), but it's enough to change the angle of attack for collisions.
-   There are Other Things crawling around on the bubbles as well that will eat
    your bug if they can catch it.
-   You have two bugs, each controlled by a different hand. I think this makes
    the game several times more difficult and interesting.

### Calibrated Code Review (research)

Give a novice programmer a one-page program and have them score it using a
checklist, then grade them on how closely their scoring matches the
instructor's. (They start with 100%, and lose one mark for each false positive
or false negative.) After doing this a handful of times, they should learn to
see code through the instructor's eyes. Does this help them write better code?
If so, how quickly and how well?  This project will attempt to answer these
questions.

### Developer Discussion Tools (development)

Most of the techniques catalogued in [*The Discussion Book*][discussion-book]
are not supported by the communication and coordination tools that programmers
routinely use. The aim of this project is to implement the most promising and
study how useful they are.

### A Little WYSIWYG Editor (development)

[*Web Browser Engineering*](https://browser.engineering/) builds a small but
fully-functional web browser step by step to show students how real ones
work. The aim of this project is to build an equally simple desktop WYSIWYG
editor in Python that supports both styled text and embedded sketching.

### Markdown to DOM (development)

[Python-Markdown](https://python-markdown.github.io/) converts Markdown to HTML;
if an program needs to check or manipulate a DOM tree, it must parse the HTML
using a library like [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/),
perform whatever operations it needs to, and then convert the DOM back to
HTML. In this project, students will refactor Python-Markdown so that it can
generate a Beautiful Soup-compatible DOM tree directly.

### Save the Humans! (game)

The zombies have attacked.  The people at the zoo have panicked, and it's up to
the animals to save them in this tongue-in-cheek game. The tiger can chase
people away from danger, but they might run straight into the arms of the
ravenous horde. The bunny is so cute that people will chase *it*, but if they
catch it they'll just stand there petting it until they're eaten, and so on.

### Software Performance by Example (tutorial)

Each lesson in this tutorial will take a simple application, analyze its
performance, and then make it faster. Along the way, the lessons will present
general tips for improving performance similar to those in Jon Bentley's classic
book *Writing Efficient Programs*, update them, and show how to apply them in
practice.

### Software Security by Example (tutorial)

The first lesson in this tutorial will present a simple implementation of a wiki
designed for shared note-taking.  Each of the following lessons will fix one of
its security shortcomings (or one of the shortcomings introduced by an earlier
fix).  Some will be vulnerabilities such as cross-site scripting or SQL
injection; others will be missing features such as basic authentication or
OAuth, role-based access control, the kind of logging that every sys admin
wishes they had, static code analysis, and eventually the audit and emergency
response procedures that such tools are meant to support.

### Tower Support Game (game)

A [tower defense game](https://en.wikipedia.org/wiki/Tower_defense) is one in
which the player builds fixed defenses against incoming waves of attackers. The
objective of this game is to prototype a simple tower *support* game, in which
the player builds bridges, first aid stations, and so on to help travelers reach
their destination.

### Understanding Ethics (research)

This project will start by creating a set of scenarios in which a programmer
needs to make an ethical decision, each with multiple-choice options.  An expert
will determine the best answer for each; students and professionals will then be
asked to answer the same questions, and the results will be analyzed to see how
well each group matches the experts' opinions and whether practitioners'
opinions are any better than those of students.

### A WYSIWYG Computational Notebook (development)

[Jupyter](https://jupyter.org/) uses JSON as its storage format, while
[Marimo](https://marimo.io/) and [Quarto](https://quarto.org/) use Python with
embedded strings and Markdown with embedded code respectively. This project will
explore a third option by building an [extension][lo-extension] for
[LibreOffice](https://www.libreoffice.org/) using the the Jupyter messaging
[protocol](https://jupyter-client.readthedocs.io/en/latest/) so that people who
prefer WYSIWYG editors can embed code and its output alongside diagrams, tables,
and other media.

[discussion-book]: https://www.wiley.com/en-us/The+Discussion+Book%3A+50+Great+Ways+to+Get+People+Talking-p-9781119049715
[lo-extension]: https://wiki.documentfoundation.org/Documentation/DevGuide/Extensions
[pipes]: https://en.wikipedia.org/wiki/Yahoo!_Pipes
[variable-roles]: https://www.ppig.org/files/2005-PPIG-17th-sajaniemi.pdf
