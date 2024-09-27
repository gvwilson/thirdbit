---
title: "The Only Features I Need"
date: 2023-03-04
---

> This post is a sequel to earlier ones about [the Lox programming language][change-lox]
> and [empirical design of a language that's no larger than necessary][empirically-minimal].

I've implemented the examples from [*Software Tools in JavaScript*][sdxjs],
and I think that doing them twice has given me a decent perspective
on what features a programming language needs to have
in order to be a sturdy platform for teaching software design:

-   Basic types: Boolean, integer, float, text, null/none/NA, NaN
    -   I've [changed my mind][empirically-minimal]: we *do* need to distinguish integers from floats, even for beginners
    -   But I still think that null/NA can be unified, but are distinct from NaN
    -   And that true/false are different from 1/0
-   Collections: list, set, key-value map (i.e., dicts), multi-dimensional array, dataframe
    -   I think that dicts and sets should both be ordered or unordered (dicts are ordered in current versions of Python but sets aren't)
    -   I know you can implement dataframes and N-dimensional arrays using other structures,
        but many things are simpler if they're basic types
-   Control flow: iterators for `for` loops, `while` loops, `if`/`else`, functions
    -   I think pattern-matching with capture in conditional branches is really handy
    -   I use exceptions all the time because that's what my languages provide,
        but I still hope there's something better out there.
        (Succes/failure return types that have to be checked immediately are *not* better for high-level programming.)
    -   In contrast,
        I use syntactic support for resources allocation (i.e., Python's `with`) all the time,
        and have started using `finally` blocks wherever they're allowed as well
-   Higher-order programming: first-class functions, closures, run-time introspection, walking parse trees, and very occasionally `eval`
    -   I use decorators for the same reason I use exceptions—they're what the language provides—but
        I still believe Python's implementation could have been better.
        Just as methods are declared `m(self, a1, a2)` and then called `obj(p1, p2)`,
        we should declare decorators `d(func, a1, a2)` and use them as `@d(a1, a2)`.
        Yes, we can achieve the same effect by adding an extra layer inside the decorator,
        but it would be a _lot_ simpler to teach people how to use them if that wasn't necessary.
-   Concurrency: I've avoided it in most of the books' examples,
    and I don't think I should make any claims about ease of learning/ease of use
    until I've implemented the books' examples with them.
    -   CSP-style channels quickly become unmanageable.
        (Back in my [occam][occam] days we used to joke that they were the revenge of the `goto`,
        since you quickly found yourself wondering,
        "If I put a message in this channel, where will it go to?")
    -   Generators are hard for even intermediate programmers to understand and work with,
        but they're a lot better than the mess of callbacks, promises, and async/await that modern JavaScript provides.
    -   I've always preferred futures and tuple spaces,
        and I'd like to try fiber-style coroutines as found in languages like [Wren][wren],
        but see the caveat in the main bullet point.
-   Programming at scale: classes with single inheritance, modules, and a decent bloody package and environment manager

This list is obviously incomplete:
for example,
I haven't specified what operations I want for lists and dicts,
whether it should be possible to define default values for functions' arguments,
what kinds of classes I want,
and so on.
But here's the thing:
I think we can answer these questions empirically.
As I [said last year][empirically-minimal],
I think we could go through a dozen books on software design
(or some data structures & algorithms textbooks),
tally up what's used,
and then design a language that includes only the top N features.
It would result in a very conservative language,
but I think that's what we want for teaching:
something that introduces people to the things they're most likely to encounter
no matter what language they use next.
If you have a student looking for a project,
please [give me a shout](mailto:gvwilson@third-bit.com).

[change-lox]: @root/2022/02/01/what-i-would-change-in-lox/
[empirically-minimal]: @root/2022/10/02/empirically-minimal/
[occam]: https://en.wikipedia.org/wiki/Occam_(programming_language)
[sdxjs]: @root/sdxjs/
[wren]: https://wren.io/
