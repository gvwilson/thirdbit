---
title: "Software Design by Example 17: Module Bundler"
date: 2023-01-23
year: 2023
---

JavaScript was designed in a hurry to make web pages interactive.
Nobody expected it would become so popular,
so it didn't include things like
a standard, reliable way to turn a set of source files into a single "executable" for browsers to load.

[This chapter][sdxjs_bundler] of [*Software Design by Example*][sdxjs]
builds a simple module bundler
that finds all the files that an application depends on
and combines them into one.
A bundler has to do two things:

1.  Find the root file's dependencies—which is impossible in theory because of dynamic loading,
    but which is mostly solvable in practice.

2.  Combine all those files into one without breaking namespacing.

Why is the problem of finding dependencies unsolvable in theory?
Suppose creates an alias for `require` and uses that to load other files:

```js
const req = require
const weWillMissThis = req('./other-file')
```

We could try to trace variable assignments to catch cases like these,
but someone could still fool us by writing this:

```js
const clever = eval(`require`)
const weWillMissThisToo = clever('./other-file')
```

If you still don't believe me, consider this:

```js
const module_id = Math.floor(Math.random() * NUM_EXTENSIONS)
const module_name = `./extension-${module_id}.js`
const extension = req(module_name)
```

That's right:
the code loads a randomly-selected module.
In the program where I first encountered this,
the extensions controlled the behavior and appearance of characters in a game.
Hundreds were available,
so the game's author had (quite reasonably) decided to load only the ones needed in a particular session.

Once again,
*there is no general solution to this problem*
other than running the code to see what it does.
If you would like to understand why not,
and learn about a pivotal moment in the history of computing,
I highly recommend [*The Annotated Turing*][annotated_turing].
You might also enjoy [*Linkers and Loaders*][linkers_loaders],
which taught me more about how system-level software actually works
than a full course on operating systems.
*Linkers and Loaders* was also one of the inspirations for *SDXJS*:
it convinced me that a challenge-and-response analysis of solutions to a problem
could be readable as well as informative.

<figure id="module-bundler-bundling" align="center">
  <img src="{{'/sdxjs/module-bundler/bundling.svg' | relative_url}}" alt="Bundling modules"/>
  <figcaption>Figure 17.1: Combining multiple modules into one.</figcaption>
</figure>

> Terms defined: entry point, module bundler, transitive closure.

[annotated_turing]: http://www.theannotatedturing.com/
[linkers_loaders]: https://www.elsevier.com/books/linkers-and-loaders/levine/978-0-08-051031-6
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxjs_bundler]: {{'/sdxjs/module-bundler/' | relative_url}}
