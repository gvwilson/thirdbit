---
title: "Four Traditions Revisited"
date: 2026-01-28
category: favorite
---

Tedre and Sutinen's paper "[Three Traditions of Computing: What Educators Should Know][doi]"
has shaped my thinking ever since I first read it.
And this table (reproduced from the paper) summarizes their analysis:

<table class="centered">
<tr>
  <th valign="top"></th>
  <th valign="top">Mathematical tradition</th>
  <th valign="top">Engineering tradition</th>
  <th valign="top">Scientific tradition</th>
</tr>
<tr>
  <th valign="top">Assumptions</th>
  <td valign="top">Programs (algorithms) are abstract objects, they are correct or incorrect, as well as more or less efficient – knowledge is a priori</td>
  <td valign="top">Programs (processes) affect the world, they are more or less effective and reliable – knowledge is a posteriori</td>
  <td valign="top">Programs can model information processes, models are more or less accurate – knowledge is a posteriori</td>
</tr>
<tr>
  <th valign="top">Aims</th>
  <td valign="top">Coherent theoretical structures and systems</td>
  <td valign="top">Investigating and explaining phenomena, solving problems</td>
  <td valign="top">Constructing useful, efficient, and reliable systems; solving problems</td>
</tr>
<tr>
  <th valign="top">Strengths</th>
  <td valign="top">Rigorous, results are certain, utilized in other traditions</td>
  <td valign="top">Combines deduction and induction, cumulative</td>
  <td valign="top">Able to work under great uncertainty, flexible, progress is tangible</td>
</tr>
<tr>
  <th valign="top">Weaknesses</th>
  <td valign="top">Incommensurability of results, uncertainty about what counts as proper science</td>
  <td valign="top">Limited to axiomatic systems</td>
  <td valign="top">Rarely follows rigid, preordained procedures; poor generalizability</td>
</tr>
<tr>
  <th valign="top">Methods</th>
  <td valign="top">Empirical, inductive, and deductive</td>
  <td valign="top">Analytic, deductive (and inductive)</td>
  <td valign="top">Empirical, constructive</td>
</tr>
</table>

As [I wrote three years ago][previous],
I'm struck now by what's *not* there.
I think there should be a fourth column titled "Humanist tradition"
that focuses on values,
on how computing is used,
and on how cognitive and social psychology support, shape, and limit
what we can build and how we build it.

I also now think that their distinction between the engineering and scientific traditions
isn't particularly useful.
In practice,
they are nearly-identical attempts to turn software development into
an engineering discipline on par with chemical or electrical engineering.
UML,
requirements engineering,
the use of statistical models to predict bug rates:
all are signs of "engineering envy",
and by and large,
practitioners have voted with their feet and *not* adopted them.

Instead,
the overwhelming majority of the programmers I've worked with
fall into what I used to call a "craft" tradition,
but which I now think has a lot more in common with
[industrial design][bicycle].
Using Tedre and Sutinen's categories:

-   **Assumptions**: Programs are built by people who learn design and construction from examples.

-   **Aims**: Answer the questions, "Does it do what it's supposed to?" and "Does its design facilitate its construction and maintenance?"

-   **Strengths**: Matches most practitioners' mental model of their work.

-   **Weaknesses**: Lacks a rigorous foundation. (Discussions of software design are intellectually shallow compared to discussions of the design of bicycles and teapots.)

-   **Methods**: Mentoring.

I think this analysis explains
why practitioners and software engineering researchers mostly talk past one another.
Most researchers subscribe to what Scott's book *[Seeing Like a State][seeing]*
labelled "high modernism":
they believe comprehensibility and control will come from uniformity and formalism.
Practitioners,
on the other hand,
are defending the local traditions in which they are personally invested.
In my idle moments,
I wonder where we'd be if [that long-ago NATO conference][nato]
had adopted industrial design as a metaphor instead of engineering.

[doi]: https://doi.org/10.1080/08993400802332332
[bicycle]: @root/2017/12/17/consider-the-bicycle/
[nato]: https://en.wikipedia.org/wiki/NATO_Software_Engineering_Conferences
[previous]: @root/2022/12/29/the-fourth-tradition/
[seeing]: https://isbnsearch.org/isbn/9780300078152
