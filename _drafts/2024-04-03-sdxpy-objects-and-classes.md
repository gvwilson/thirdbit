---
title: "Software Design by Example in Python 2: Objects and Classes"
date: 2024-04-03
year: 2024
---

Python is an object-oriented language,
but many of its more advanced features rely on its support for *introspection*,
i.e.,
on the ability of running programs to ask,
"What do I contain?"
In order to show newcomers how this works,
[Chapter 1: Objects and Classes][sdxpy_obj_class]
shows learners that objects and classes are "just" dictionaries.
In particular,
it demonstrates that:

1.  Objects and classes can be thought of as dictionaries with stereotyped behavior.

2.  Objects can exist without classes, but classes make them easier to understand.

3.  Objects that satisfy the same contract are polymorphic,
    i.e.,
    they can be used interchangeably even if they do different specific things.

4.  Inheritance can be implemented in several ways
    that differ in the order in which objects and classes are searched for methods.

By its end,
this chapter has introduced the most important idea in the whole book,
which is that *programs are just another kind of data*.
Understanding this turns out to be key to many designs:
from passing functions as parameters
to loading modules dynamically or walking abstract syntax trees,
it comes up in program after program.

<img class="centered" src="{{'/sdxpy/oop/concept_map.svg' | relative_url}}" alt="Concept map for objects and classes"/>

> Terms defined: alias, argument, cache, class method, constructor, derived class, design by contract, monkey patching, multiple inheritance, object-oriented programming, parameter, polymorphism, recursion, spread, static method, upcall, varargs.

<img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">

[sdxpy_obj_class]: {{'/sdxpy/oop/' | relative_url}}
