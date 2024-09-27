---
title: "Software Design by Example in Python 6: Running Tests"
date: 2024-04-06
---

Having written a bunch of tests while building [the parser][sdxpy_parse] and [pattern matcher][sdxpy_glob]
in the previous chapters,
it was long past time to show learners how to build a testing framework like [pytest][pytest].
In particular,
[Chapter 6: Running Tests][sdxpy_test] was another opportunity to show that
a program is just another kind of data,
and that introspection can make a lot of things easier to build but harder to understand.
Finding functions dynamically ensures that we don't ever write tests but forget to run them;
however,
it means that the program's text doesn't contain an explicit list of tests that are going to be run.
This tradeoff is intrinsic and unavoidable:
higher-level abstractions put more power into experienced programmers' hands
but make their code more difficult for novices to understand.
Helping novices become comfortable with those abstractions
was the main goal of this book and [its predecessor][sdxjs].

<img class="centered" src="@root/sdxpy/test/concept_map.svg" alt="Concept map for running tests"/>

> Terms defined: actual result (of test), assertion, dynamic typing, error (result of test), exception, expected result (of test), failure (result of test), fixture, global, local, pass (result of test), pretty print, raise (an exception), register (in code), scope, unit test.

And now a request:
if you have experience implementing support for dark mode in browsers
and can submit a PR to change the CSS for [this project][repo],
I'd be very grateful for your help.
I believe the solution is going to involve a media query,
redefining some colors,
and using the CSS `invert` function to make the SVG diagrams white-on-black,
but I've never done this and need to focus on other work right now.
If you can spare the time,
thank you in advance.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[pytest]: https://docs.pytest.org/
[repo]: https://github.com/gvwilson/sdxpy/
[sdxjs]: @root/sdxjs/
[sdxpy]: @root/sdxpy/
[sdxpy_glob]: @root/sdxpy/glob/
[sdxpy_parse]: @root/sdxpy/parse/
[sdxpy_test]: @root/sdxpy/test/
