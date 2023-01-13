---
title: "Software Design by Example 12: File Interpolator"
date: 2023-01-16
year: 2023
---

Many of the examples in [*Software Design by Example*][sdxjs]
are too long to show comfortably in one block of code on a printed page,
so I needed a way to break them up.
As an experiment,
I wrote a custom module loader
that reads a source file that has specially-formatted comments containing the names of other files,
and then reads and inserts those files before running the code.
Modern programming languages don't work this way,
but it's how C and C++ handle header files
and how static site generators do snippet inclusion.

I decided to use a different approach in the end
because ESLint didn't know what to make of file inclusions.
Despite being a dead end,
I thought the inclusion tool was [worth a chapter][sdxjs_interpolator]
because it shows how programs turn source code into something executable.
I also thought it was important to have a least one example of a working dead end
so that readers would be comfortable when their ideas did what they were supposed to
but still shouldn't be put into production.

<figure id="file-interpolator-conceptual" align="center">
  <img src="{{'/sdxjs/file-interpolator/conceptual.svg' | relative_url}}" alt="Using file inclusions"/>
  <figcaption>Figure 12.1: Including fragments of code to create runnable programs.</figcaption>
</figure>

> Terms defined: header file, literate programming, loader, sandbox, search path, shell variable.

[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxjs_interpolator]: {{'/sdxjs/file-interpolator/' | relative_url}}
