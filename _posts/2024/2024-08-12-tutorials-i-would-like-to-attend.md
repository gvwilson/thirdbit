---
title: "Tutorials I Would Like to Attend"
date: 2024-08-12
year: 2024
---

I have maintained [a list of unwritten books][nots] for over 25 years
(see [this page][nots-2024] for the latest version).
It has only recently occurred to me that I should put together
a list of tutorials I would like to attend that apparently don't yet exist.
If you are delivering one of these any time soon,
please let me know;
if you're not,
but might be interested in creating one of them,
please [get in touch](mailto:{{site.author.email}}).

1.  *How to Build a Dashboard Engine*
    shows learners how to create tools like [Dash][dash] and [Shiny][shiny]
    that let data scientists build interactive dashboards without writing JavaScript themselves.
    Along the way,
    the tutorial introduces some important ideas about real-world web development:
    for example,
    how to manage long-running server-side processes without the browser freezing up.

1.  *How to Build a Laboratory Information Management System*
    isn't really about building a LIMS—it's about all the design decisions that have to be made along the way,
    from handling authentication and access control
    to representing human workflows in software.

1.  *How to Build an Integrated Development Environment*
    has participants create a tool using [Textualize][textualize]
    that includes an editor, a breakpointing debugger, and a file browser,
    which will help them understand and use their actual IDE more proficiently.

1.  Similarly,
    *A Web Browser in a Day* is a stripped-down version of [this excellent tutorial][browser-tut],
    and helps participants understand how their actual browser works.

1.  *NumPy from the Ground Up*
    builds a (very) simple version of [NumPy][numpy] from scratch
    to give learners a better understanding of how the real thing works.
    Low-level data manipulation could be done in C or Rust,
    or using something like [bitarray][bitarray] or the [array][array] module from Python's standard library
    to be more accessible.

1.  And speaking of Rust,
    *Rust for Python Programmers* is an introduction to a language that might,
    if its community can shed its cryptocurrency baggage,
    be the most important systems programming language of the next twenty years.
    This workshop culminates with participants building a small Python extension in Rust
    and turning it into a shareable package.

1.  *What Every Data Scientist Needs to Know About Deploying an Application*
    addresses the same need as [this unfinished tutorial][sys-tutorial]:
    what do people who *aren't* sys admins need to know in order to put an application into production?

1.  *Product Management for Open Source*
    teaches exactly that.

1.  Finally,
    *Organizational Change for Software Developers* also teaches exactly what the title says.
    As I've said many, many times before,
    open source and open science can't win unless and until we figure out
    how to change the organizations we're in,
    and we don't need to figure that out from scratch.

[array]: https://docs.python.org/3/library/array.html
[bitarray]: https://pypi.org/project/bitarray/
[browser-tut]: https://browser.engineering/
[dash]: https://dash.plotly.com/
[nots]: {{'/not-on-the-shelves/' | relative_url}}
[nots-2024]: {{'/not-on-the-shelves/2024/' | relative_url}}
[numpy]: https://numpy.org/
[shiny]: https://shiny.posit.co/
[sys-tutorial]: https://gvwilson.github.io/sys-tutorial/
[textualize]: https://www.textualize.io/
