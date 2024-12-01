---
title: "More Student Project Proposals"
date: 2024-12-01
---

Six weeks ago I posted some [undergraduate software projects][first-post]
that I would be excited about supervising.  Two of those—Browsercast
and the Marimo plugins—have been picked up by students at the
University of Toronto.  The other three are still available, and I've
added a couple of others (see below). If you're a senior looking for
a capstone project or a professor looking for projects with a
supervisor, please [get in touch][email].

## Dragnet

One type of exercise that H5P *doesn't* support is adding labels to
diagrams. [This prototype][dragnet] takes an SVG with some
specially-marked labels, moves those labels to the side, and then lets
the user try to drag them back into the right places.  A deployable
version would need to do a lot more, such as dealing with scaling
transformations; the goal of this project is to turn the demo into
something a classroom teacher could use.

## Tutorial Simulations of Distributed Systems

[*Software Design by Example in Python*][sdxpy] deliberately ignored
concurrency, partial failure, and everything else associated with
modern distributed applications. The aim of this project is to (start
to) fix that by building scale models of distributed protocols and
systems from TCP to BitTorrent and load-balancing tools using either
[Py-DES][pydes] or [SimPy][simpy]. The tutorials will use simulators
so that the accompanying lessons could illustrate edge cases in
reproducible ways.

## Software Design by Example in Gleam

[Gleam][gleam] is a modern functional language that runs on the
[Erlang/OTP][erlang] platform (and can also be compiled to
JavaScript). The aim of this project is to translate examples from
[*Software Design by Example in Python*][sdxpy] into Gleam to help
people coming from Python and other mainstream languages understand
how to use FP in practice.

## Parallelizing Marimo Notebooks

[Marimo][marimo] is a next-generation computational notebook that (a)
stores everything as Python source code and (b) analyzes code to
prevent out-of-order execution of cells. [Dagster][dagster] and
[Metaflow][metaflow] are computational workflow tools that allow users
to add decorators to functions and methods to specify computational
chunks. The goal of this project is to see if the two can be married,
i.e., to see if it's possible to add decorators to cell functions in
Marimo to parallelize notebooks directly.

## Extending Lox

Lox is a simple interpreted language created by Robert Nystrom for his
(excellent) book [*Crafting Interpreters*][crafting]. Many people have
extended it in various ways; in this project, students would re-create
Lox by working through the second half of Nystrom's book, then add
operator overloading, cooperative concurrency, and a few other features
to bring the language up to par with [Lua][lua].

## Automatic Identification of Variable Roles

Sajaniemi et al's work on [roles of variables][roles] identified and
named ten small patterns in the way variables are used in novice
programs. This project would build static and dynamic analysis tools
to detect those patterns (and possibly others) in programs as an aid
to teaching, debugging, and code review.

## Entity-Relationship Diagrams for Dataframes

Entity-relation (ER) diagrams are one of the few graphical notations
that programmers actually use voluntarily.  This project would use
static and dynamic analysis to extract ER diagrams from programs that
use dataframe libraries like [Pandas][pandas] and [Polars][polars] to
show how dataframes are being combined, e.g., to infer foreign key
relationships.

## The Impact of Calibrated Peer Review

Give a novice programmer a one-page program and have them score it
using a checklist, then grade them on how closely their scoring
matches the instructor’s. (They start with 100%, and lose one mark for
each false positive or false negative.) After doing this a handful of
times, they should learn to see code through the instructor’s
eyes. Does this help them write better code? If so, how quickly and
how well?

[crafting]: https://craftinginterpreters.com/
[dagster]: https://dagster.io/
[dragnet]: https://iezer.github.io/dragnet/
[email]: mailto:gvwilson@third-bit.com
[erlang]: https://www.erlang.org/
[first-post]: @root/2024/10/18/student-project-proposals/
[gleam]: https://gleam.run/
[lua]: https://www.lua.org/
[marimo]: https://marimo.io/
[metaflow]: https://metaflow.org/
[pandas]: https://pandas.pydata.org/
[polars]: https://pola.rs/
[pydes]: https://pydes.readthedocs.io/
[roles]: https://www.ppig.org/files/2005-PPIG-17th-sajaniemi.pdf
[sdxpy]: https://third-bit.com/sdxpy/
[simpy]: https://simpy.readthedocs.io/
