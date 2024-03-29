---
title: "Software Design by Example in Python 6: Running Tests"
date: 2024-04-06
year: 2024
---

Having written a bunch of tests while building [the parser][sdxpy_parse] and [pattern matcher][sdxpy_glob]
in the previous chapters,
it was long past time to show learners how to build a testing framework like [pytest][pytest].
In particular,
this chapter was another opportunity to show that a program is just another kind of data,
and that introspection can make a lot of things easier to build but harder to understand.
Finding functions dynamically ensures that we don't ever write tests but forget to run them;
however,
it means that the program's text doesn't contain an explicit list of tests that are going to be run.
This tradeoff is intrinsic and unavoidable:
higher-level abstractions put more power into experienced programmers' hands
but make their code more difficult for novices to understand.
Helping novices become comfortable with those abstractions
was the main goal of this book and [its predecessor][sdxjs].

<img class="centered" src="{{'/sdxpy/test/concept_map.svg' | relative_url}}" alt="Concept map for running tests"/>

> Terms defined: actual result (of test), assertion, dynamic typing, error (result of test), exception, expected result (of test), failure (result of test), fixture, global, local, pass (result of test), pretty print, raise (an exception), register (in code), scope, unit test.

<img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">

[pytest]: https://docs.pytest.org/
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxpy]: {{'/sdxpy/' | relative_url}}
[sdxpy_glob]: {{'/sdxpy/glob/' | relative_url}}
[sdxpy_parse]: {{'/sdxpy/parse/' | relative_url}}
[sdxpy_test]: {{'/sdxpy/test/' | relative_url}}
