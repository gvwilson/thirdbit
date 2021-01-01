---
title: "Expressing Temporal &quot;Type&quot; Information in Programs"
date: 2006-11-11 15:50:21
year: 2006
---
Several students were in my office this week explaining how their programs work.  In each case, much of the information was temporal: "this happens, then that, then this other thing".  Sequence diagrams and the like were designed to capture this, but I don't know any programming language that allows programmers to specify constraints of this kind on their variables.

Here's an example of what I mean. Jorma Sajaniemi has been doing some interesting work on <a href="http://www.cs.joensuu.fi/~saja/var_roles/">the roles of variables in novices' programs</a> (see in particular his <a href="http://www.cs.joensuu.fi/~saja/var_roles/role_list.html">list of roles</a>).  One such role is a "one-way flag", which, as its name suggests, starts with one value, and is assigned a different one exactly once, after which it can't go back to having the original value.  Another role is a "most-wanted holder", which keeps track of something like the maximum value seen so far.

In both cases, it would be very helpful to be able to specify the intended use of the variable in a machine-checkable way, but I don't know how to do this.  <em>Implementing</em> the behavior is easy: I can write a one-way flag class, or a most-interesting accumulator, in just a few lines of Java or Python.  But how do I tell the compiler and runtime system what the variable "means"?  I can sort of see how to do it in the first case (mumble mumble finite state machines mumble mumble), but in the second, I need to tell the compiler or runtime about some dataflow constraints ("variable X may only be assigned values taken from Y --- other values cannot be assigned to X, even if they are type-compatible").

If anyone knows of languages that allow such constraints to be captured or expressed, I'd welcome pointers.
