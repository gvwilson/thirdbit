---
title: "Software Design by Example 4: Unit Testing"
date: 2023-01-04
year: 2023
---

The first draft of [*Software Design by Example*][sdxjs] didn't have either
[the warmup chapter on systems programming][sdxjs_systems_programming]
or [this chapter on building a unit testing framework][sdxjs_unit_test].
Instead,
it opened with a tiny version control system
inspired by [Mary Rose Cook's][cook_mary_rose] excellent [Gitlet][gitlet] project.

But no book outline ever survives contact with reality.
I made so many mistakes while writing the chapter on version control
that I realized I'd have to show readers
how to test something that interacted with the file system.
I could have used Mocha without explanation,
but showing how xUnit testing frameworks find files containing tests
and run tests from those files
turned out to be a great way to introduce some ideas
that I needed later.

Backfilling like this is a normal part of [writing a technical book][11_techbook].
You start by drawing a [concept map][concept_map] like this:

<div align="center">
  <img src="{{'/files/2023/backup_concept_map.svg' | relative_url}}" alt="File backup concept map" width="80%" />
</div>

but it is necessarily just a small subgraph of a much larger set of ideas and relationships.
The box in the upper left labelled `unique name`
and the arc labelled `uniquely identifies` can both be implemented incorrectly
in several different ways,
so you find yourself turning "uniqueness" into a concept of its own
and elaborating on it to show how to tell that something really is unique,
and then realize that your lesson needs to undergo mitosis
because your callout box on testing is now several pages long.

Automatic numbering of cross-references quickly becomes an author's best friend,
but every time a chapter fissions
you have to proof-read both parts and everything that depends on them
to make sure that (for example) terms are still defined where they are first used.
I spend a lot more time on manual checking when I'm writing lessons than when I'm writing reference material,
but that's because a good lesson tells a story with a narrative arc.
It all leaves me wondering how the hell people write movies like [*Memento*][memento] or [*Knives Out*][knives_out]
without going mad…

> Terms defined: absolute error, actual result (of test), assertion, caching, defensive programming, design pattern, dynamic loading, error (in a test), exception handler, expected result (of test), exploratory programming, fail (a test), fixture, global variable, introspection, lifecycle, pass (a test), relative error, side effect, Singleton pattern, test runner, test subject, throw (exception), unit test.

<figure id="unit-test-lifecycle">
  <img src="{{'/sdxjs/unit-test/lifecycle.svg' | relative_url}}" alt="Unit testing lifecycle"/>
  <figcaption markdown="1">Figure 4.3: Lifecycle of dynamically-discovered unit tests.</figcaption>
</figure>

[11_techbook]: https://github.com/gvwilson/11-techbook
[concept_map]: https://teachtogether.tech/en/index.html#s:memory-concept-maps
[cook_mary_rose]: https://maryrosecook.com/
[gitlet]: http://gitlet.maryrosecook.com/
[knives_out]: https://www.imdb.com/title/tt8946378/
[memento]: https://www.imdb.com/title/tt0209144/
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxjs_systems_programming]: {{'/sdxjs/systems-programming/' | relative_url}}
[sdxjs_unit_test]: {{'/sdxjs/unit-test/' | relative_url}}
