---
title: "How to Write a Memo"
date: 2021-01-18
---

One of the most popular talks I give is on [how to run a meeting](https://www.youtube.com/watch?v=5f3-q9SzkeE).
In it and in my description of [Martha's Rules](@root/2019/06/13/marthas-rules/)
I talk about writing short memos to summarize proposals so that people know what they're being asked to support
(or equivalently what they're actually opposing),
but I don't show any examples.
Writing these makes meetings fairer:
if all discussion is off the cuff
then the deck is stacked again people who aren't extroverts,
quick thinkers,
on the end of a reliable low-latency connection,
*and* fluent in the language being used in the meeting.

This memo is an edited version of what I would write for something simple;
[this proposal](@root/ideas/#what-i-would-organize-if-i-still-organized-things)
shows the level of detail I would include if money was needed.
Remember,
the memo's point is not to persuade but to summarize,
and to make it clear to everyone what they're actually agreeing to.

----

**Summary:** Use verification of Zipf's Law as a running example through the entire book.

**Background**

*Research Software Engineering with Python* is going to introduce readers to a lot of new tools and terminology.
Using different problems for the major examples in each chapter will be an extra burden for readers,
who will have to learn about seismology, baseball, and whatever else we choose
as well as Git, Make, and Python packaging.
Using different problems will also be a burden on us,
as we will have to write and maintain several different (small) projects or packages.

**Proposal**

Use verification of [Zipf's Law](https://en.wikipedia.org/wiki/Zipf%27s_law) as the running example throughout all chapters.

1.  Lots of raw data available (novels from the Gutenberg Project, Wikipedia pages, etc.).

2.  Raw data is messy and cleanup has multiple stages so we can show workflows.

3.  Problem is very easy to describe and only requires a bit of math.

4.  Data is all open license so we can build/share a package without any worries.

**Budget and Staffing**

-   No budget required.
-   Approx. 2 hours for one person to get and package raw data.

**Alternatives**

1.  Different chapters use different examples.
    -   Pro: less coupling between chapters (can change one without ripple effects on later chapters).
    -   Pro: variety is the spice of life (multiple examples might be more compelling).
    -   Con: cognitive load (learners have to get up to speed with multiple examples).
    -   Con: the more domains our examples come from, the more likely it is that a learner will hit one that's unfamiliar.

**History**

-   2019-06-06/all: adopted.
-   2019-05-12/GVW: incorporate revisions from RJ.
-   2019-05-03/GVW: first draft.
