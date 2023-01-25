---
title: "Software Design by Example 2: Systems Programming"
date: 2023-01-02
year: 2023
---

The biggest difference between JavaScript and most other programming languages
is how many operations in JavaScript are asynchronous.
Its designers didn't want browsers to freeze while waiting for data to arrive or for users to click on things,
so operations that might be slow are implemented by describing now what to do later.
And since anything that touches the hard drive is slow from a processor's point of view,
Node implements filesystem operations the same way.

…which makes the language a bit of a mess from a teaching point of view.
Early JavaScript programs used callback functions for async operations,
but they're hard to understand even in small programs,
so successive versions of the language wrapped them in promises
and then tried to hide the whole mess behind the `async`/`await` keywords.
[Chapter 2: Systems Programming][sdxjs_systems_programming]
therefore has three goals:

1.  introduce the Node libraries the book uses for file I/O,
    creates and read directories,
    and so on;

2.  show readers how callback-based programming works
    and why they don't want to use it;
    and

3.  introduce what turned out to be the most important idea in the whole book,
    which is that *programs are just another kind of data*.

I knew that last point was going to be a big one,
but it turned out to be the heart of most designs.
From passing functions as parameters
to introspection of live programs
and walking abstract syntax trees,
this theme is going to come up in program after program.

> Terms defined: anonymous function, asynchronous, Boolean, callback function, cognitive load, command-line argument, console, current working directory, destructuring assignment, edge case, filename extension, filesystem, filter, globbing, idiomatic, log message, path (in filesystem), protocol, scope, single-threaded, string interpolation.

<figure id="systems-programming-callbacks" align="center">
  <img src="{{'/sdxjs/systems-programming/callbacks.svg' | relative_url}}" alt="Running callbacks"/>
  <figcaption>Figure 2.2: How JavaScript runs callback functions.</figcaption>
</figure>

[sdxjs_systems_programming]: {{'/sdxjs/systems-programming/' | relative_url}}
