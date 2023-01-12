---
title: "Software Design by Example 10: Build Manager"
date: 2023-01-12
year: 2023
---

Make was the first programming support tool I ever learned how to use,
and forty-one years later,
I still reach for it whenever I need to automate a workflow.
I know there are dozens of others,
many of which are objectively better in various ways,
but I suppose you never forget your first love.

But that's not why [*Software Design by Example*][sdxjs] includes
[this chapter on how build managers work][sdxjs_build]—at least,
it's not the main reason.
A build manager's primary responsibility is to manage a directed (hopefully acyclic) graph,
so showing people how to implement one is a natural way to introduce fundamental graph algorithms
like cycle detection and topological sorting.

As I was revising the book I realized that
I should have implemented a second build manager
that used observer/observable rather than explicitly constructing and traversing a graph.
Comparing the central control of the graph-based implementation
with the decentralized execution of the one I didn't build
would have been even more interesting than the discussion of either option,
but by the time that was clear I had run out of steam.
It's on the list for the Python version;
I'll let you know in a few months whether my energy levels picked up or not.

<figure id="build-manager-template-method" align="center">
  <img src="{{'/sdxjs/build-manager/template-method.svg' | relative_url}}" alt="Template Method pattern"/>
  <figcaption>Figure 10.3: The Template Method pattern in action.</figcaption>
</figure>

> Terms defined: automatic variable, build manager, build recipe, build rule, build target, compiled language, cycle (in a graph), dependency, directed acyclic graph, driver, interpreted language, link (a program), pattern rule, runnable documentation, stale (in build), Template Method pattern, topological order.

[sdxjs]: {{'/sdxjs/build-manager/' | relative_url}}
[sdxjs_build]: {{'/sdxjs/build-manager/' | relative_url}}
