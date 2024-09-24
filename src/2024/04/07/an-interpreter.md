---
title: "Software Design by Example in Python 7: An Interpreter"
date: 2024-04-07
---

A lot of people who have done computer science degrees believe that
if you have never written a compiler or an interpeter,
you don't really understand how computers work.
The fact that many people who haven't done this routinely create great software
doesn't seem to shake their belief,
but I decided to include a simple tree-walking interpreter
in [Chapter 7: An Interpreter][sdxpy_interp] so that
the next time someone is the target of this kind of gatekeeping
they can say, "Sure, I've done that,"
and move the conversation back to more useful topics.

As a bonus,
this chapter also shows how things like operator overloading work.
In my experience,
telling people that "'+' is just a function"
doesn't work as well as showing people that those things we have special notation for
are looked up in tables like other operations
and that we can look up something else if we want to.

<img class="centered" src="@root/sdxpy/interp/concept_map.svg" alt="Concept map for an interpreter"/>

> Terms defined: compiler, control flow, defensive programming, dictionary comprehension, dynamic dispatch, environment, expression, infix notation, interpreter, introspection, prefix notation, runtime, statement, type hint.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[sdxpy_interp]: @root/sdxpy/interp/
