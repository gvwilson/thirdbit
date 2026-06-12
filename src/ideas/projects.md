---
title: "Projects"
template: page
---

## Altruism in Software Teams

Is it possible to detect altruism in software teams (i.e., to measure how much
time developer A spends helping developer B even though B's problem isn't part
of A's job)? If so, this project will try to determine if there is any
correlation between altruism and (for example) staff turnover or the long-term
maintainability of the code base.
<br>
*Unstarted.*

## Analysis of Undergrad Textbooks

Most undergraduate computer science programs have a first- or second-year course
on data structures and algorithms.  What do these courses actually teach, and
which of these algorithms and data structures are used in upper-year courses? To
answer these questions, this project will assemble and apply tools to analyze
the text of several dozen textbooks; along the way, the students doing the
project will have to decide how to identify topics, how to count them, and how
to make their work reproducible.
<br>
*In progress.*

## Blocks-Based Data Science

[TidyBlocks](https://github.com/tidyblocks/tidyblocks) was a prototype of a
[Scratch](https://scratch.mit.edu/)-like tool for teaching introductory data
ascience.  It turned out to be an inappropriate visual paradigm, as there was no
natural way to represent join operations as nested blocks.  The aim of this
project is to explore an alternative using a node-and-connector model like that
of [Node-RED](https://nodered.org/) or
[Yahoo! Pipes](https://en.wikipedia.org/wiki/Yahoo!_Pipes).
<br>
*Dormant.*

## Browsercast

Tools like PowerPoint aren't web-friendly.  When you export a slideshow to the
web, what you get is a bunch of images, while screencasts are opaque to search
engines and disability aids.  In contrast, [Browsercast](@root/browsercast/)</a>
plays snippets of audio in the browser as the viewer moves through the slides,
so "View Source", links, CSS, screen readers, and search work as they should.
The [prototype](https://github.com/gvwilson/browsercast) uses just 5kb of
JavaScript; the aim of this project is to turn it into a functional tool.
<br>
*Dormant.*

## Calibrated Code Review

Give a novice programmer a one-page program and have them score it using a
checklist, then grade them on how closely their scoring matches the
instructor’s. (They start with 100%, and lose one mark for each false positive
or false negative.) After doing this a handful of times, they should learn to
see code through the instructor’s eyes. Does this help them write better code?
If so, how quickly and how well?  This project will attempt to answer these
questions.
<br>
*Unstarted.*

## Developer Discussion Tools

Most of the techniques catalogued in [*The Discussion Book*][discussion-book]
are not supported by the communication and coordination tools that programmers
routinely use. The aim of this project is to implement the most promising and
study how useful they are.
<br>
*Unstarted.*

## Identification of Variable Roles

Sajaniemi's work on [roles of variables][variable-roles] identified and named
ten small patterns in the way variables are used in novice programs. This
project would build static and dynamic analysis tools to detect those patterns
(and possibly others) in programs as an aid to teaching, debugging, and code
review.
<br>
*Dormant.*

## A Little WYSIWYG Editor

[*Web Browser Engineering*](https://browser.engineering/) builds a small but
fully-functional web browser step by step to show students how real ones
work. The aim of this project is to build an equally simple desktop WYSIWYG
editor in Python that supports both styled text and embedded sketching.
<br>
*Unstarted.*

## Markdown to DOM

[Python-Markdown](https://python-markdown.github.io/) converts Markdown to HTML;
if an program needs to check or manipulate a DOM tree, it must parse the HTML
using a library like [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/),
perform whatever operations it needs to, and then convert the DOM back to
HTML. In this project, students will refactor Python-Markdown so that it can
generate a Beautiful Soup-compatible DOM tree directly.
<br>
*Unstarted.*

## Project Closure

There are hundred of books in print about how to start a business. Only a
handful discuss how to pass one on, and even talk about how to wind one down.
This project will study when, why, and how software projects are wound down,
either deliberately or on short notice.
<br>
*In progress.*

## Simulations of Distributed Systems

[*Software Design by Example in Python*](@root/sdxpy/) deliberately ignored
concurrency, partial failure, and everything else associated with modern
distributed applications. [This project](@root/dsdx/) is fixing that by building
scale models of distributed protocols and systems from TCP to BitTorrent and
load-balancing tools using [asimpy](https://asimpy.readthedocs.io/). The
tutorials will use simulators so that the accompanying lessons could illustrate
edge cases in reproducible ways.
<br>
*Dormant.*

## Software Design by Example in Gleam

[Gleam](https://gleam.run/) is a modern functional language that runs on the
[Erlang/OTP](https://www.erlang.org/) platform and can also be compiled to
JavaScript. [This project](@root/gl4py/) will translate examples from [*Software
Design by Example in Python*](@root/sdxpy/) into Gleam to help people coming
from Python and other mainstream languages understand how to use FP in practice.
<br>
*Dormant.*

## Software Design by Example in Lean

[Lean](https://lean-lang.org/) is a modern functional language used primarily
for theorem proving. [This project](@root/l4py/) will translate examples from
[*Software Design by Example in Python*](@root/sdxpy/) into Lean to help people
coming from Python and other mainstream languages understand how to use FP in
practice.
<br>
*Dormant.*

## Software Performance by Example

Each lesson in this tutorial will take a simple application, analyze its
performance, and then make it faster. Along the way, the lessons will present
general tips for improving performance similar to those in Jon Bentley's classic
book *Writing Efficient Programs*, update them, and show how to apply them in
practice.
<br>
*Unstarted.*

## Software Security by Example

The first lesson in this tutorial will present a simple implementation of a wiki
designed for shared note-taking.  Each of the following lessons will fix one of
its security shortcomings (or one of the shortcomings introduced by an earlier
fix).  Some will be vulnerabilities such as cross-site scripting or SQL
injection; others will be missing features such as basic authentication or
OAuth, role-based access control, the kind of logging that every sys admin
wishes they had, static code analysis, and eventually the audit and emergency
response procedures that such tools are meant to support.
<br>
*Unstarted.*

## Tower Support Game

A [tower defense game](https://en.wikipedia.org/wiki/Tower_defense) is one in
which the player builds fixed defenses against incoming waves of attackers. The
objective of this game is to prototype a simple tower *support* game, in which
the player builds bridges, first aid stations, and so on to help travelers reach
their destination.
<br>
*Unstarted.*

## Unbreaking Software

Most programmers spend a large part of their time debugging, but most courses
only show working code, and most textbooks don't discuss how to prevent,
diagnose, and fix errors.  This tutorial fills that gap by presenting dozens of
case studies showing how to find and fix real-world problems.  Along the way, it
will present examples of what programmers can do to handle errors gracefully,
from data structure repair to automatically restarting servers.
<br>
*Dormant.*

## Understanding Ethics

This project will start by creating a set of scenarios in which a programmer
needs to make an ethical decision, each with multiple-choice options.  An expert
will determine the best answer for each; students and professionals will then be
asked to answer the same questions, and the results will be analyzed to see how
well each group matches the experts' opinions and whether practitioners'
opinions are any better than those of students.
<br>
*Unstarted.*

## Validity of Software Engineering Claims

Are some programmers really ten times more productive than others?  Does
test-driven development actually make programmers more productive?  And do
people actually believe these claims?  This project will conduct a quantitative
survey of best-selling books on software developmnt to measure how many of their
claims are backed by citations, and of those, how many are considered valid,
then survey programmers to see which (if any) they believe.
<br>
*In progress.*

## XKCD Charts

[Chart.xkcd](https://timqian.com/chart.xkcd/) is a JavaScript library that
displays charts in the hand-drawn style of [XKCD](https://xkcd.com/). Its
creator is no longer maintaining it; this project will fork the original code,
fix outstanding issues, and add new features such as axis limits and stable
coloring schemes.
<br>
*Dormant.*

## A WYSIWYG Computational Notebook

[Jupyter](https://jupyter.org/) uses JSON as its storage format, while
[Marimo](https://marimo.io/) and [Quarto](https://quarto.org/) use Python with
embedded strings and Markdown with embedded code respectively. This project will
explore a third option by building an
[extension](https://wiki.documentfoundation.org/Documentation/DevGuide/Extensions)
for [LibreOffice](https://www.libreoffice.org/) using the the Jupyter messaging
[protocol](https://jupyter-client.readthedocs.io/en/latest/) so that people who
prefer WYSIWYG editors can embed code and its output alongside diagrams, tables,
and other media.
<br>
*Unstarted.*

[discussion-book]: https://www.wiley.com/en-us/The+Discussion+Book%3A+50+Great+Ways+to+Get+People+Talking-p-9781119049715
[variable-roles]: https://www.ppig.org/files/2005-PPIG-17th-sajaniemi.pdf
