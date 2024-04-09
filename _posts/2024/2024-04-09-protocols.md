---
title: "Software Design by Example in Python 9: Protocols"
date: 2024-04-09
year: 2024
---

As I wrote [yesterday][func_post]
I didn't want to spend an entire chapter of [*Software Design by Example*][sdxpy] on closures,
but I needed to be sure learners understood them
before presenting mock objects, `with` statements, and how `for` loops use iterators.
What I try to show in [Chapter 9: Protocols][sdxpy_protocols]
is that these are all examples of a *protocol*:
if a program has feature X,
then language feature Y will make use of it.

I'm a little embarrassed to admit how long it took me to realize that
protocols like this are everywhere in modern languages.
Constructors?
That's a protocol.
Operator overloading?
That's another,
but in my mind they were both things in their own right,
not instances of a larger concept.
I don't think we need to go all the way to [metaobject protocols][mop] when teaching this
(at least, not to this audience);
if you have thoughts on whether this approach works,
I'd [welcome feedback](mailto:{{site.author.email}}).

<img class="centered" src="{{'/sdxpy/protocols/concept_map.svg' | relative_url}}" alt="Concept map for protocols"/>

> Terms defined: append mode, context manager, decorator, infinite recursion, iterator, Iterator pattern, mock object, protocol.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[func_post]: {{'/2024/04/08/functions-closures/' | relative_url}}
[mop]: https://en.wikipedia.org/wiki/Metaobject
[sdxpy]: {{'/sdxpy/' | relative_url}}
[sdxpy_protocols]: {{'/sdxpy/protocols/' | relative_url}}
