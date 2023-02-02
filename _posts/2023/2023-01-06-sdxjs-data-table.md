---
title: "Software Design by Example 6: Data Tables"
date: 2023-01-06
year: 2023
---

[Chapter 6][sdxjs_data_table] of [*Software Design by Example*][sdxjs] was a bit nostalgic for me.
Jon L. Bentley's [*Writing Efficient Programs*][efficient] was the first programming book I ever bought out of personal interest
rather than as a textbook or for a (summer) job.
In less than 200 pages of lucid prose,
Bentley laid out rules for making programs faster or reducing their memory requirements
that I've come back to many times over forty years.

Including a chapter on performance optimization was more than a walk down memory lane, though.
As the introduction to the chapter says:

> …how can we tell which of several designs is going to be the most efficient?
> The best answer is to conduct some experiments.

I've argued for years that we ought to teach software engineering as an experimental discipline—that we should
introduce undergraduates to key findings from the research literature
and teach them enough data science to understand and recapitulate [examples like this][vignette].
There are many reasons to do this;
the most relevant for [*SDXJS*][sdxjs] are that:

1.  performance considerations influence design, but

2.  modern computers are so complex that no-one can predict the performance of even trivial programs.

Since most people use tables for data analysis,
I thought, "Why not compare different implementations of tables?"
It was a bit contrived,
but I think it worked out pretty well,
and it motivated discussion of the difference between interface and implementation rather neatly.

<figure id="data-table-storage-order" align="center">
  <img src="{{'/sdxjs/data-table//storage-order.svg' | relative_url}}" alt="Row-major vs. column-major storage order" class="centered">
  <figcaption>Figure 6.2: Row-major storage vs. column-major storage for data tables.</figcaption>
</figure>

> Terms defined: character encoding, column-major storage, data frame, fixed-width (of strings), fixed-width (of strings), garbage collection, heterogeneous, homogeneous, immutable, index (in a database), JavaScript Object Notation, join, pad (a string), row-major storage, sparse matrix, SQL, tagged data, test harness.

[efficient]: https://www.goodreads.com/book/show/128599.Writing_Efficient_Programs
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxjs_data_table]: {{'/sdxjs/data-table/' | relative_url}}
[vignette]: {{'/2022/08/14/ese-vignette/' | relative_url}}
