---
title: No More Encyclopedias
date: 2025-04-14
---

There were three encyclopedias in our house when I was growing up:
one full of bright photographs and illustrations for children,
one with dense, dark text for grownups
(and teenagers who had outgrown the first one and would never admit they missed it),
and a third one in a box in the basement
that I discovered after [my dad died][dad].
There isn't one in this house,
though,
because we have the internet at our fingertips.
[Wikipedia][wikipedia] gives us short summaries when we need them,
and we can turn to various search engines and Q&A sites when we need to go further.

What brought this to mind was reading Janssens and Nieuwdorp's
[*Python Polars: The Definitive Guide*][book] over the weekend.
It's well written,
but I don't think I will ever look at it again.
Tables with one-line summaries of operators and aggregation functions
feel redundant when the documentation they're taken from is a click away.
More importantly,
five-line examples showing how to use them are now also redundant thanks to AI tools.
"How do I find the three largest annual drops in overdose fatalities in this dataset?"
is now a question my computer can answer *and explain*.
I never copied code directly from [Claude][claude] while rewriting [snailz][snailz],
but over and over I found myself asking a question,
looking at its answer,
nodding my way through its explanation,
and then modifying what it offered to solve my problem.

Since technical books can't address the specific in-the-moment need of the reader,
what role do they have (if any)?
I think the answer is now,
"To give readers the mental model they need to write a good prompt and then recognize and adapt a useful[^1] answer."
If you don't know what a cache is,
how hashing works,
or that HTML and source code are both represented in memory as trees,
you won't be able to go as far as an LLM might take you.

I didn't have this in mind when I wrote [*Software Design by Example*][sdxpy],
but in retrospect I think (or hope) that it meets this need.
Unfortunately,
I also think that LLMs (and [Stack Overflow][so] before it, and search before that)
are making people less patient with long-form technical prose.
I now struggle to read more than a few pages at a time,
even when the subject matter is as engrossing as [this][browser].
If I ever complete either of [these][rsdx] [projects][webonomicon],
it will be because I think I have an answer to this riddle that's worth trying out.
If you have one,
I'd [like to hear it][email].

[^1]: The word "useful" is important: it sometimes took several tries to get [Claude][claude] to solve the problem I actually had, and occasionally it simply couldn't.

[book]: https://www.oreilly.com/library/view/python-polars-the/9781098156077/
[browser]: https://browser.engineering/
[claude]: https://claude.ai/
[dad]: @root/2015/09/22/dad/
[email]: mailto:gvwilson@third-bit.com
[rsdx]: https://gvwilson.github.io/rsdx/
[sdxpy]: @root/sdxpy/
[snailz]: https://gvwilson.github.io/snailz/
[so]: https://stackoverflow.com/
[webonomicon]: https://gvwilson.github.io/webonomicon/
[wikipedia]: https://www.wikipedia.org/