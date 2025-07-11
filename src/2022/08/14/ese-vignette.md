---
title: "Empirical Software Engineering Vignettes"
date: 2022-08-14
---

I have been [arguing for years][essay]
that we should replace the standard undergraduate course on software engineering
with one that:

1.  shows students how to gather and analyze data about programs, programmers, and programming,
    and then

2.  has them recapitulate key findings from empirical software engineering research.

The vignette below is an example of what I mean.
It introduces several important ideas
and would naturally lead into in-class analysis of
how quickly the students themselves could complete some small tasks,
how big and how correct their solutions were,
and so on.
A re-analysis of [Fucci et al's data on test-driven development][fucci_tdd]
or a repeat of [Ragkhitwetsagul et al's study of toxic code snippets on Stack Overflow][so_code]
would be just as much fun,
and would helps students learn about code analysis tools and practical data science
as well as teaching them what we actually know about software engineering
and why we believe it's true.

I think it would take one year to build this course,
test it in the classroom,
and get it into production.
I'm pessimistic about update—my current job has reminded me
just how slowly academia curricula change—but as my spouse keeps reminding me,
you miss 100% of the shots you don't take.
If you know someone who would back this project,
I'd be grateful for an introduction.

<hr/>

Are some programmers really ten times more productive than average?
To find out,
[Prechelt2000](#Prechelt2000)
had a set of programmers solve the same problem in the language of their choice,
then looked at how long it took them,
how good their solutions were,
and how fast those solutions ran.
The data,
which is [available online][prechelt_data],
looks like this:

```
person,lang,z1000t,z0t,z1000mem,stmtL,z1000rel,m1000rel,whours,caps
s015,C++,0.050,0.050,24616,374,99.24,100.0,11.20,??
s017,Java,0.633,0.433,41952,509,100.00,10.2,48.90,??
s018,C,0.017,0.017,22432,380,98.10,96.8,16.10,??
s020,C++,1.983,0.550,6384,166,98.48,98.4,3.00,??
s021,C++,4.867,0.017,5312,298,100.00,98.4,19.10,??
s023,Java,2.633,0.650,89664,384,7.60,98.4,7.10,??
s025,C++,0.083,0.083,28568,150,99.24,98.4,3.50,??
…
```

The columns hold the following information:

| Column | Meaning |
| ------ | ------- |
| person | subject identifier |
| lang | programming language used |
| z1000t | running time for z1000 input file |
| z0t | running time for z0 input file |
| z1000mem | memory consumption at end of z1000 run |
| stmtL | program length in statement lines of code |
| z1000rel | output reliability for z1000 input file |
| m1000rel | output reliability for m1000 input file |
| whours | total subject work time |
| caps | subject self-evaluation |

The `z1000rel` and `m1000rel` columns tell us that
all of these implementations are correct 98% of the time or better,
which is considered acceptable.
The rest of the data is much easier to understand as a box-and-whisker plot
of the working time in hours (the `whours` column from the table).
Each dot is a single data point
jittered up or down a bit to be easier to see).
The left and right boundaries of the box show the 25th and 75th percentiles respectively,
i.e., 25% of the points lie below the box and 25% lie above it,
and the mark in the middle shows the median:

<div align="center">
<figure>
<img src="@root/files/talks/productivity.svg" alt="Box-and-whisker plot show that most developers spent between zero and 20 hours but a few took as long as 63 hours.">
<figcaption><strong>Development Time</strong></figcaption>
</figure>
</div>

So what does this data tell us about productivity?
As [Prechelt2019](#Prechelt2019) explains,
that depends on exactly what we mean.
The shortest and longest development times were 0.6 and 63 hours respectively,
giving a ratio of 105X.
However,
the subjects used seven different languages;
if we only look at those who used Java (about 30% of the whole)
the shortest and longest times are 3.8 and 63 hours,
giving a ratio of "only" 17X.

But comparing the best and the worst of anything is guaranteed to give us
an exaggerated impression of the difference.
If we compare the 75th percentile (which is the middle of the top half of the data)
to the 25th percentile (which is the middle of the bottom half)
we get a ratio of 18.5/7.25 or 2.55;
if we compare the 90th percentile to the 50th we get 3.7,
and other comparisons give us other values.
The answers to our original question are therefore:

1.  It depends what you mean.

2.  No, good programmers aren't 10 times more productive than average.

3.  But yes, it's reasonable to say that they are about four times more productive.

<dl>
<dt id="Prechelt2000">Prechelt2000</dt>
<dd>
Lutz Prechelt:
"An empirical comparison of seven programming languages".
<em>IEEE Computer</em>,
2000,
<a href="https://doi.org/10.1109/2.876288">doi:10.1109/2.876288</a>.
</dd>

<dt id="Prechelt2019">Prechelt2019</dt>
<dd>
Lutz Prechelt:
"The mythical 10x programmer".
In Sadowski and Zimmermann (eds.)
<a href="https://link.springer.com/book/10.1007/978-1-4842-4221-6"><em>Rethinking Productivity in Software Engineering</em></a>,
2019.
</dd>

</dl>

[essay]: @root/2020/07/09/acm-sigsoft-award/
[fucci_tdd]: https://neverworkintheory.org/2016/10/05/test-driven-development.html
[prechelt_data]: http://page.mi.fu-berlin.de/prechelt/packages/jccpprtTR.csv
[so_code]: https://neverworkintheory.org/2021/08/19/toxic-code-snippets-on-stack-overflow.html
