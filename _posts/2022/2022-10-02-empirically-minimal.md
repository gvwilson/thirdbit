---
title: "Empirically Minimal"
date: 2022-10-02
year: 2022
---

I'm wrapping up the JavaScript version of [*Software Design by Example*]({{'/sdxjs/' | relative_url}})
and hope to finish the Python version early next year.
Writing these has convinced me that it's harder to teach with languages like Python or JavaScript
than it used to be.
These languages have features and libraries that make industrial-strength coding more productive,
but that richness is bewildering for newcomers:
every online search for "how do I XYZ?" throws them into a sea of concepts, terms, and APIs
that they haven't yet met.

I'm therefore spending a lot of time thinking about minimal languages that are novice-friendly.
[Hedy](https://www.hedycode.com/) is explicitly layered;
[Quorum](https://quorumlanguage.com/)'s insistence on testing new features' usability keeps it small;
[Lua](https://www.lua.org/)'s focus on embeddability has the same effect,
and materialized thought experiments like [Wren](https://wren.io/)
are even closer to what I want.

But what exactly *do* I want?
Looking at [*SDXJS*]({{'/sdxjs/' | relative_url}}) and its Python sibling,
and at my programming lessons for scientists,
I rely on the following:

-   Atomic types: Boolean, number, text, null
    -   JavaScript has convinced me that we don't need to distinguish integers from reals for novices
    -   I think null and NA are interchangeable for this audience as well
    -   But I *do* distinguish Boolean from 1/0 even though the latter is perfectly serviceable
-   Collections: list, set, key-value map, multi-dimensional array, dataframe
    -   I prefer sets to maps-without-values for the same reason that I prefer Booleans to 1's and 0's
    -   Yes, you can implement dataframes and multi-dim arrays using lists and maps,
        but so many examples are so much easier if they're first-class citizens
    -   Weirdly, I don't feel the same way about graphs even though I use them pretty frequently
-   Control flow: while loop, iterators, if/else-if/else, with, try-catch
    -   By "iterators" I mean "a 'for' loop that gives you each value in a collection in order".
        This implies some way to extend the set of collections in the language (see below).
    -   Syntactic support for resource management (e.g., Python's `with` statement)
        has had a surprisingly big impact on my lessons.
        Again, it's most useful if it's extensible.
    -   try-catch has always felt like a clumsy case of "what else are we going to do?"
        but, well, what else are we going to do?
        (Please don't say "multiple return values, one of which is conventionally an error code".)
-   Extensibility: function, module, class
    -   This is where it's hardest for me to know where to stop.
        User-definable functions are a no-brainer;
        I don't need default parameter values or variable-length argument lists,
        but if I have to choose I'll take the former over the latter
        (because people can always pass "extra" arguments in lists or maps).
    -   Modules that are namespaces are similarly a no-brainer.
    -   But classes: once you open that up, where do you stop?
        You need some way for people to create records with named parts,
        extend the set of things they can iterate over,
        and so on,
        but if there's a core set of features in my writing and teaching,
        I can't see it.
-   The weird stuff: coroutines, introspection
    -   It may seem weird to put coroutines in a list of "basic" features,
        but concurrency is too important to be left out of lessons on software design,
        and coroutines are the easiest way to introduce it.
    -   (The easiest-easiest way is actually [tuple spaces](https://en.wikipedia.org/wiki/Tuple_space),
        but I put them in the same bucket as Lisp-like syntax:
        if they were going to catch on, they'd have caught on by now.)
    -   Introspection might also seem out of place in this list,
        but so many software design techniques rely on being able to treat code as data
        that I'd struggle to teach without it.

But here's the thing:
this list is based on nothing more substantial than an hour-long cruise
through lessons I've developed.
What I *really* want is for some enterprising graduate student
to spend a couple of months going through lessons and textbooks
and counting how often various language constructs are used
(cf. #10 and #48 in [this list](https://neverworkintheory.org/2022/08/30/software-engineering-research-questions.html)).
I think it would be analogous to the way that chip designers work:
look at what operations programs execute most often
in order to figure out what to optimize.
If you're interested,
please [give me a shout](mailto:gvwilson@third-bit.com):
this is something I'd be happy to make time for.
