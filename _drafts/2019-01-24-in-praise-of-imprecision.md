---
layout: post
date: 2019-01-24 03:11
title: "In Praise of Imprecision"
---

> Not everything worth doing is worth doing well.
>
> -- Tom West, quoted in *[The Soul of a New Machine](https://en.wikipedia.org/wiki/The_Soul_of_a_New_Machine)*.

Another day,
another attempt to formalize something whose utility lies in its informality.
Rigor and precision have their place:
years ago,
I dropped off a language development project when someone asked,
"What's the semantics of slicing?"
and the project lead said, "I don't know, look at what the code does."
But UML and the Semantic Web and [Loglan](https://en.wikipedia.org/wiki/Loglan) never caught on for good reasons.
Human beings aren't analytic machines;
we reason by analogy with what we've seen and done before
and only resort to logic when we've painted ourselves into a corner and have no other option.
And even in those cases---circuit diagrams, mathematical proofs, and theology, for example---we
still leap from stone to stone instead of wading through the river
because the experience-based pattern-matching we call "intuition" tells us that it's safe to do so.

This is why I'm skeptical of anything with the word "ontology" in its title.
Yes,
the database needs a schema,
but the more precisely we define a term like "author",
the more inaccessible we make that definition to the people who are using the damn database.
(Go ahead, read [this](https://en.wikipedia.org/wiki/Authorship_and_ownership_in_copyright_law_in_Canada)
and tell me if you feel enlightened.)
And yes,
some systems need a precisely-defined semantics
so that there's at least *some* chance that different implementations will behave the same way,
but its designers' primary goal should be
to make it unnecessary for users to think about the language at that level.

The [Principle of Least Astonishment](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)
