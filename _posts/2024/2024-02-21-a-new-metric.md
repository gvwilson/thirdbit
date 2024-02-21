---
title: "A New Metric"
date: 2024-02-21
year: 2024
---
Back in the 1980s,
Roger Hockney invented two measures for computer performance.
The first,
*r<sub>∞</sub>*,
is the maximum possible performance when given infinite data
(i.e., when startup overheads are ignored).
The second,
*n<sub>½</sub>*,
is how big the problem has to be for the machine to achieve half of its peak performance.
Hockney observed that *n<sub>½</sub>* is effectively infinity in many cases,
since no machine ever delivers more than 10-20% of the performance
is manufacturer claims it will.

In the mid-90s,
I suggested that another interesting metric would be
how long it takes a programmer to learn how to write code
that achieves half a machine's rated performance.
I called it *p<sub>½</sub>*,
and later revised its definition to be,
"How long does it take a newcomer to learn enough about X
to solve half of the problems *they* will ever use X to solve?"
It turned out to be a poor metric,
but not for the reason I originally thought.
"Different people have different needs" wasn't the problem:
different people have different heights and blood pressures too,
but that doesn't stop us talking about means and distributions.
The real problem is that the metric is unstable:
the more people learn about a tool,
the more problems they can solve with it,
so the horizon recedes as they approach it.

So here's my latest attempt:

> *w<sub>½</sub>* is the time required for half of learners to believe
> that something was actually worth learning.

Based on purely personal experience teaching graduate students with no formal computer science background
who want to do some data science:

| Topic | *w<sub>½</sub>* | Note |
| ----- | --------------- | ---- |
| plotting with the tidyverse | 10 minutes |
| regular expressions | 30 minutes | assuming they already program |
| the Unix command line | 2 hours | |
| object-oriented programming | 2 days | |
| version control with Git | 1 week | and only if they're in a group project |
| unit testing | ∞ | most data scientists don't ever become believers |

I am currently trying to figure out what the likely *w<sub>½</sub>* values are
for [SQL][sql-tutorial], [security][safety-tutorial], and ethics.
If you have thoughts on these topics or others,
[please drop me a line](mailto:{{site.author.email}}).

[safety-tutorial]: https://gvwilson.github.io/safety-tutorial/
[sql-tutorial]: https://gvwilson.github.io/sql-tutorial/
