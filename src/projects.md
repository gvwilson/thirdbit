---
title: "Student Projects"
template: page
---

<div class="row" markdown="1">
  <div class="col col-6" markdown="1">

This map shows the birthplaces of the 146 students I supervised
or co-supervised between 2002 and 2010.  I would welcome a chance to
add a few more points: if you are a student or free-range learner
interested in doing any of the projects described below, or an
instructor whose students need projects, please [get in touch][email].

  </div>
  <div class="col col-6">
    <div class="center">
      <a href="@root/files/2024/csc49x.png">
        <img src="@root/files/2024/csc49x.png" alt="map of student birthplaces" width="100%">
      </a>
    </div>
  </div>
</div>

## In Progress

<div class="row" markdown="1">
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Browsercast

Tools like PowerPoint aren't web-friendly.  When you export a
slideshow to the web, what you get is a bunch of images, while
screencasts are opaque to search engines and disability aids.  In
contrast, [Browsercast][browsercast] plays snippets of audio in the
browser as the viewer moves through the slides, so "View Source",
links, CSS, screen readers, and search work as they should.  The
prototype uses just 5kb of JavaScript; the aim of this project is to
turn it into a functional tool

</div>
</div>
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Marimo and H5P

[Marimo][marimo] is a next-generation computational notebook that
enables data scientists to mix code, discussion, and results in a
reproducible way.  Its plugin system relies on [AnyWidget][anywidget],
which specifies a simple contract between extensions and Marimo's
rendering and execution engine.  The aim of this project is to design,
build, and test a set of Marimo plugins that can be used for classroom
exercises similar to those in the [H5P][h5p] toolkit: multiple choice,
fill in the blanks, and so on.

</div>
</div>
</div>

## Available

<div class="row" markdown="1">
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Narwhals

[Narwhals][narwhals] is a Python package that provides compatibility
between dataframe libraries, allowing applications to use
[Pandas][pandas], [Polars][polars], and other libraries through a
common API. Students working on this project will contribute directly
to Narwhals, and will be responsible for fixing bugs, designing new
features, and shepherding their work through review into production.

</div>
</div>
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Markdown to DOM

[Python-Markdown][py-markdown] converts Markdown to HTML; if an
application needs a DOM tree that it can check or manipulate, it must
then parse the HTML using a library like [BeautifulSoup][bs4], perform
whatever operations it needs to, and then convert the DOM back to
HTML. In this project, students will refactor Python-Markdown so that
it can generate a Beautiful Soup-compatible DOM tree directly.

</div>
</div>
</div>

<div class="row" markdown="1">
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Dragnet

One type of exercise that H5P *doesn't* support is adding labels to
diagrams. [This prototype][dragnet] takes an SVG with some
specially-marked labels, moves those labels to the side, and then lets
the user try to drag them back into the right places.  A deployable
version would need to do a lot more, such as dealing with scaling
transformations; the goal of this project is to turn the demo into
something a classroom teacher could use.

</div>
</div>
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Software Design by Example in Gleam

[Gleam][gleam] is a modern functional language that runs on the
[Erlang/OTP][erlang] platform (and can also be compiled to
JavaScript). The aim of this project is to translate examples from
[*Software Design by Example in Python*][sdxpy] into Gleam to help
people coming from Python and other mainstream languages understand
how to use FP in practice.

</div>
</div>
</div>

<div class="row" markdown="1">
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Parallelizing Marimo Notebooks

[Marimo][marimo] is a next-generation computational notebook that (a)
stores everything as Python source code and (b) analyzes code to
prevent out-of-order execution of cells. [Dagster][dagster] and
[Metaflow][metaflow] are computational workflow tools that allow users
to add decorators to functions and methods to specify computational
chunks. The goal of this project is to see if the two can be married,
i.e., to see if it's possible to add decorators to cell functions in
Marimo to parallelize notebooks directly.

</div>
</div>
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Extending Lox

Lox is a simple interpreted language created by Robert Nystrom for his
(excellent) book [*Crafting Interpreters*][crafting]. Many people have
extended it in various ways; in this project, students would re-create
Lox by working through the second half of Nystrom's book, then add
operator overloading, cooperative concurrency, and a few other features
to bring the language up to par with [Lua][lua].

</div>
</div>
</div>

<div class="row" markdown="1">
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Identification of Variable Roles

Sajaniemi et al's work on [roles of variables][roles] identified and
named ten small patterns in the way variables are used in novice
programs. This project would build static and dynamic analysis tools
to detect those patterns (and possibly others) in programs as an aid
to teaching, debugging, and code review.

</div>
</div>
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### XKCD Charts

[Chart.xkcd][chart-xkcd] is a JavaScript library that displays charts
in the sketchy hand-drawn style of [XKCD][xkcd]. Its creator is no
longer maintaining it; this project will fork the original code, fix
outstanding issues, and add new features such as axis limits and
stable coloring schemes.

</div>
</div>
</div>

<div class="row" markdown="1">
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### The Impact of Calibrated Peer Review

Give a novice programmer a one-page program and have them score it
using a checklist, then grade them on how closely their scoring
matches the instructor’s. (They start with 100%, and lose one mark for
each false positive or false negative.) After doing this a handful of
times, they should learn to see code through the instructor’s
eyes. Does this help them write better code? If so, how quickly and
how well?  This project will attempt to answer these questions.

</div>
</div>
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Analysis of Undergrad Textbooks

Most undergraduate computer science programs have a first- or
second-year course on data structures and algorithms.  What do these
courses actually teach, and how has their content changed since
Wirth's [classic book][wirth] appeared in 1976? To answer these
questions, this project will assemble and apply tools to analyze the
text of several dozen textbooks; along the way, the students doing the
project will have to decide how to identify topics, how to count them,
and how to make their work reproducible.

</div>
</div>
</div>

<div class="row" markdown="1">
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### A Blocks-Based Data Science Tool

[TidyBlocks][tidyblocks] was a prototype of a [Scratch][scratch]-like
tool for teaching introductory data ascience.  It turned out to be an
inappropriate visual paradigm, as there was no natural way to
represent join operations as nested blocks.  The aim of this project
is to explore an alternative using a node-and-connector model like
that of [Node-RED][node-red] or [Yahoo! Pipes][yahoo-pipes].

</div>
</div>
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### A WYSIWYG Computational Notebook

[Jupyter][jupyter] uses JSON as its storage format, while
[Marimo][marimo] and [Quarto][quarto] use Python with embedded strings
and Markdown with embedded code respectively. This project will
explore a third option by building an
[extension][libreoffice-extension] for [LibreOffice][libreoffice]
using the [the Jupyter messaging protocol][jupyter-protocol] so that
people who prefer WYSIWYG editors can embed code and its output
alongside diagrams, tables, and other media.

</div>
</div>
</div>

<div class="row" markdown="1">
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Simulations of Distributed Systems

[*Software Design by Example in Python*][sdxpy] deliberately ignored
concurrency, partial failure, and everything else associated with
modern distributed applications. The aim of this project is to (start
to) fix that by building scale models of distributed protocols and
systems from TCP to BitTorrent and load-balancing tools using either
[Py-DES][pydes] or [SimPy][simpy]. The tutorials will use simulators
so that the accompanying lessons could illustrate edge cases in
reproducible ways.

</div>
</div>
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Software Security by Example

The first lesson in this tutorial will present a simple implementation
of a wiki designed for shared note-taking.  Each of the following
lessons will fix one of its security shortcomings (or one of the
shortcomings introduced by an earlier fix).  Some will be
vulnerabilities such as cross-site scripting or SQL injection; others
will be missing features such as basic authentication or
[OAuth][oauth], role-based access control, the kind of logging that
every sys admin wishes they had, static code analysis, and eventually
the audit and emergency response procedures that such tools are meant
to support.

</div>
</div>
</div>

<div class="row" markdown="1">
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Software Design for Everyone

Each lesson in this tutorial will present a "what if?" scenario and
then explores its implications for software design.  What if you had
crippling arthritis (which you can simulate by taping popsicle sticks
to your fingers): how would you redesign a cell phone app?  What if
you thought your government might take a sharp turn to the right and
retroactively weaponize women's health records: (how) could you
satisfy doctors' need for information with patient safety?  How would
you redesign a Q&A site like Stack Overflow if you thought most people
in the world *didn't* speak English as their first language?  The
practical exercises will assume enough programming skill to build
simple web applications.

</div>
</div>
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Unbreaking Software

Most programmers spend a large part of their time debugging, but most
courses only show working code, and most textbooks don't discuss how
to prevent, diagnose, and fix errors.  This tutorial will fill that
gap by presenting dozens of case studies showing how to find and fix
real-world problems.  Along the way, it will present examples of what
programmers can do to handle errors gracefully, from data structure
repair to automatically restarting servers.

</div>
</div>
</div>

<div class="row" markdown="1">
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Human-Scale Web Programming

[This incomplete tutorial][webonomicon] is an introduction to web
programming aimed at scientists and others will little or no
experience with JavaScript, HTTP requests, and related technologies.
In this project, a student (or team of students) with an interest in
teaching would fill it in and offer it at least once in order to learn
more about how to create and deliver high-quality lessons.

</div>
</div>
<div class="col col-6" markdown="1">
<div class="card" markdown="1">

### Testing Research Software

The [JavaScript][sdxjs] and [Python][sdxpy] versions of *Software
Design by Example* showed readers how to design programs by working
through scaled-down examples. In contrast, this project will develop
scaled-down versions of things like [fluid flow simulators][barba] and
data analysis pipelines, and then shows readers how to test them.
Each lesson will open with a short recap of the science and a
walk-through of the untested code, then explore how that code can be
tested.

</div>
</div>
</div>

[anywidget]: https://anywidget.dev/
[barba]: https://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/
[browsercast]: https://github.com/gvwilson/browsercast
[bs4]: https://beautiful-soup-4.readthedocs.io/
[chart-xkcd]: https://timqian.com/chart.xkcd/
[crafting]: https://craftinginterpreters.com/
[dagster]: https://dagster.io/
[dragnet]: https://iezer.github.io/dragnet/
[email]: mailto:gvwilson@third-bit.com
[erlang]: https://www.erlang.org/
[gleam]: https://gleam.run/
[h5p]: https://h5p.org/content-types-and-applications
[jupyter]: https://jupyter.org/
[jupyter-protocol]: https://jupyter-client.readthedocs.io/en/latest/
[libreoffice]: https://www.libreoffice.org/
[libreoffice-extension]: https://wiki.documentfoundation.org/Documentation/DevGuide/Extensions
[lua]: https://www.lua.org/
[marimo]: https://marimo.io/
[metaflow]: https://metaflow.org/
[narwhals]: https://narwhals-dev.github.io/narwhals/
[node-red]: https://nodered.org/
[oauth]: https://en.wikipedia.org/wiki/OAuth
[pandas]: https://pandas.pydata.org/
[polars]: https://pola.rs/
[pydes]: https://pydes.readthedocs.io/
[py-markdown]: https://python-markdown.github.io/
[quarto]: https://quarto.org/
[roles]: https://www.ppig.org/files/2005-PPIG-17th-sajaniemi.pdf
[scratch]: https://scratch.mit.edu/
[sdxjs]: https://third-bit.com/sdxjs/
[sdxpy]: https://third-bit.com/sdxpy/
[simpy]: https://simpy.readthedocs.io/
[tidyblocks]: https://github.com/tidyblocks/tidyblocks
[webonomicon]: https://lessonomicon.github.io/webonomicon/
[wirth]: https://en.wikipedia.org/wiki/Algorithms_%2B_Data_Structures_%3D_Programs
[xkcd]: https://xkcd.com/
[yahoo-pipes]: https://en.wikipedia.org/wiki/Yahoo!_Pipes
