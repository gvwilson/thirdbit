---
date: 2024-02-03
year: 2024
title: "First Draft of SQL Tutorial"
---

I still need to draw half a dozen diagrams,
and it would be nice to have a few more examples for the appendix
on PostgreSQL permissions,
geospatial operations,
and the like,
but [this SQL tutorial][sql-tutorial] is now in a teachable state.
I hope to deliver it for the first time later this month;
comments, corrections, and additions are always welcome.

Meanwhile,
here are some early morning thoughts on lesson design and implementation.
I just converted a hand-drawn (i.e., illegible to anyone but me) concept map
into something readable and [posted it in the tutorial][concept-map].
The problem is,
the lesson as implemented doesn't line up with the design:
blobs and some of the row constraints mentioned in the diagram haven't been introduced at this point.

In particular, "primary key" fit more naturally into the material on joins,
but it's a data definition constraint.
So what do I do?

1.  Throw them in at this point and promise they'll be useful later?
    Nope: every time an instructor makes a forward reference, they lose a few learners.

2.  Repeat this concept map later with a few additions?
    I've tried that in the past,
    but even if the new concepts are highlighted the duplication is confusing.
    It's also hard to maintain:
    ideally,
    I'd be able to label the elements of the diagram as visible or not visible
    based on some flag given in the HTML when the diagram is included (think about incremental reveal in slides),
    but that doesn't appear to be a thing.

3.  Find a way to introduce notions here,
    i.e., introduce primary key as a way to safely delete or update exactly the records you want?
    I fiddled with that,
    but so far I haven't come up with anything that doesn't feel clumsy.
    That could just be me, though:
    I hope that someone out there will find a way to do this
    and will send me a pull request that makes it work. 

Things like this are part of why we don't have open lessons with thousands of contributors.
If I refactor code,
I can run the test suite to make sure I haven't broken things.
I don't have equivalent guardrails when I refactor a lesson:
I don't have a way to check automatically and repeatably
that moving topic X earlier or later hasn't introduced a forward reference or some other potential source of confusion.
(I also can't auto-check diagrams against prose, but ignore that for now.)

This, I think, is one of the reasons I focus on day-long tutorials rather than months-long courses:
it's feasible to track the dependencies of something the size of this SQL tutorial manually,
which means it's possible to collaborate without breaking things at every turn.
It may also be part of why Wikipedia and [AOSA][aosa] work:
in the absence of a cognitive regression test suite,
we *have* to create independent brain-sized chunks of learning if we want lots of contributors.

All of which brings me to a question:
can LLMs help?
Not for writing lessons,
but for checking for breakage as changes are made.
I don't expect or require it to be perfect:
the test suite for the last big software project I worked on
didn't catch all of the regressions we introduced in a large refactoring,
but it was still very useful
and we wouldn't have dared tackle the work without that safety net.
Can something like LLMs be given the existing lesson and a PR and say,
"Uh, wait a sec…"?

*See also "[OER Landmines][oer-landmines]" from 2018.*

[aosa]: https://aosabook.org/
[concept-map]: https://gvwilson.github.io/sql-tutorial/img/concept_map_datamod.svg
[oer-landmines]: {{'/2018/12/02/oer-landmines/' | relative_url}}
[sql-tutorial]: https://gvwilson.github.io/sql-tutorial/
