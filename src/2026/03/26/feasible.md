---
title: "Feasible"
date: 2026-03-26
---

A couple of years ago I wrote a list of student projects I'd like to (co-)supervise.
Some are now done and some others are under way,
but my experiments with LLMs in the last couple of months
have convinced me that I just might be able to do some of the others on my own.
If I don't find a full-time job,
I will think very seriously about tackling one or more of the projects below.

## Unbreaking Software

Most programmers spend a large part of their time debugging, but
most courses only show working code, and most textbooks don't
discuss how to prevent, diagnose, and fix errors.  This tutorial
will fill that gap by presenting dozens of case studies showing how
to find and fix real-world problems.  Along the way, it will present
examples of what programmers can do to handle errors gracefully,
from data structure repair to automatically restarting servers.

## Markdown to DOM

<a href="https://python-markdown.github.io/">Python-Markdown</a>
converts Markdown to HTML; if an application needs a DOM tree that
it can check or manipulate, it must then parse the HTML using a
library like <a href="https://beautiful-soup-4.readthedocs.io/">BeautifulSoup</a>,
perform whatever operations it needs to, and then convert the DOM
back to HTML. In this project, students will refactor
Python-Markdown so that it can generate a Beautiful Soup-compatible
DOM tree directly.

## Identification of Variable Roles

Sajaniemi et al's work on
<a href="https://www.ppig.org/files/2005-PPIG-17th-sajaniemi.pdf">roles of variables</a>
identified and named ten small patterns in the way variables are used
in novice programs. This project would build static and dynamic
analysis tools to detect those patterns (and possibly others) in
programs as an aid to teaching, debugging, and code review.

## A Tower Support Game

A <a href="https://en.wikipedia.org/wiki/Tower_defense">tower defense game</a>
is one in which the player builds fixed defenses against incoming waves of
attackers. (<a href="https://en.wikipedia.org/wiki/Kingdom_Rush">Kingdom Rush</a>
is a personal favorite.) The objective of this game is to prototype a simple
tower <em>support</em> game, in which the player builds bridges, first aid
stations, and so on to help travelers reach their destination.

## A WYSIWYG Computational Notebook

<a href="https://jupyter.org/">Jupyter</a> uses JSON as its storage format, while
<a href="https://marimo.io/">Marimo</a>
and <a href="https://quarto.org/">Quarto</a> use Python with
embedded strings and Markdown with embedded code respectively. This
project will explore a third option by building an
<a href="https://wiki.documentfoundation.org/Documentation/DevGuide/Extensions">extension</a>
for <a href="https://www.libreoffice.org/">LibreOffice</a> using
the <a href="https://jupyter-client.readthedocs.io/en/latest/">the
Jupyter messaging protocol</a> so that people who prefer WYSIWYG
editors can embed code and its output alongside diagrams, tables,
and other media.

## A Little WYSIWYG Editor

Panchekha and Harrelson's
<a href="https://browser.engineering/"><em>Web Browser Engineering</em></a>
builds a small but fully-functional web browser step by step to show
students how real ones work. The aim of this project is to build an
equally simple desktop WYSIWYG editor in Python that supports both
styled text and embedded sketching.
