---
title: "Software Design by Example in Python 7: An Interpreter"
date: 2024-04-08
year: 2024
---

A lot of people who have done computer science degrees believe that
if you've never written a compiler or an interpeter,
you don't really understand how computers work.
The fact that many people who haven't routinely create great software
doesn't seem to shake their belief,
but I decided to include a simple tree-walking interpreter to show (once again)
that programs are just data
and so that learners understand how things like operator overloading work.
In my experience,
telling people that "'+' is just a function"
doesn't work as well as showing people that operations are just functions in a lookup table
and we can look up something else if we want to.

<img class="centered" src="{{'/sdxpy/interp/concept_map.svg' | relative_url}}" alt="Concept map for an interpreter"/>

> Terms defined: compiler, control flow, defensive programming, dictionary comprehension, dynamic dispatch, environment, expression, infix notation, interpreter, introspection, prefix notation, runtime, statement, type hint.

<img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">

[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxpy]: {{'/sdxpy/' | relative_url}}
