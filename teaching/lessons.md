---
layout: teaching
permalink: /teaching/lessons.html
title: "How to Teach Programming (and Other Things): Designing Lessons"
---

# Designing Lessons

**Objectives**

* **Learners can describe the steps in reverse instructional design
  and explain why it generally produces better lessons than the
  usual "forward" lesson development process.**
* **Learners can define "teaching to the test" and explain why
  reverse instructional design is *not* the same thing.**
* **Learners can construct and critique five-part learner personas.**
* **Learners can construct good learning objectives and critique
  learning objectives with reference to Bloom's Taxonomy.**

Most people design lessons as follows:

1.  Someone tells you that you have to teach something you haven't
    thought about in ten years.

1.  You start writing slides to explain what you know about the subject.

1.  After two or three weeks, you make up an assignment based more or
    less on what you've taught so far.

1.  You repeat step 3 several times.

1.  You stay awake into the wee hours of the morning to create a final
    exam.

There's a better way, but to explain it, we first need to explain how
_[test-driven development](gloss.html#test-driven-development)_ (TDD)
is used in software development.  Programmers who are using TDD don't
write software and then (possibly) write tests.  Instead, they write
the tests first, then write just enough new software to make those
tests pass, and then clean up a bit.

TDD works because writing tests forces programmers to specify exactly
what they're trying to accomplish and what "done" looks like. It's
easy to be vague when using a human language like English or Korean;
it's much harder to be vague in Python or R.

TDD also reduces the risk of endless polishing, and also the risk of
confirmation bias: someone who hasn't written a program is much more
likely to be objective when testing it than its original author, and
someone who hasn't written a program *yet* is more likely to test
it objectively than someone who has just put in several hours of hard
work and really, really wants to be done.

A similar "backward" method works very well for lesson design.  This
method is something called _[reverse instructional
design](gloss.html#reverse-instructional-design)_ or _[understanding by
design](gloss.html#understanding-by-design)_ after a book by that name
[[Wiggins2005](biblio.html#wiggins-mctighe)]; a similar method is
described in [[Fink2013](biblio.html#fink-significant)] (a summary of
which is freely available online [[Fink2003](biblio.html#fink-short)].)
In brief, lessons should be designed as follows:

1.  Create learner personas (discussed in the next section) to figure
    out who you are trying to teach and what will appeal to them.

1.  Draw concept maps to describe the mental model you want them to
    construct.

1.  Create a summative assessment, such as a final exam or performance,
    that will show you whether learning has actually taken place.

1.  Create formative assessments that will give the learners a chance to
    practice the things they'll be asked to demonstrate in the summative
    assessment, and tell you and them whether they're making progress
    and where they need to focus their work.

1.  Put the formative assessments in order based on their complexity and
    dependencies.

1.  Write just enough to get learners from one formative assessment to
    the next.  An actual classroom lesson will typically then consist of
    three or four such episodes, each building toward a short check that
    learners are keeping up.

This method helps to keep teaching focused on its objectives. It also
ensures that learners don't face anything on the final exam that the
course hasn't prepared them for.

> **Building Lessons by Subtracting Complexity**
>
> One way to build a programming lesson is to write the program you
> want learners to finish with, then remove the most complex part that
> you want them to write and make it the last exercise. You can then
> remove the next most complex part you want them to write and make it
> the penultimate exercise, and so on.  Anything that's left–i.e.,
> anything you don't want them to write as an exercise–becomes the
> starter file(s) that you give them.  This typically includes things
> like importing libraries or helper functions to access data.

<!-- comment needed to separate blockquotes -->

> **How and Why to Fake It**
> 
> One of the most influential papers in the history of software
> engineering was Parnas and Clements' "A Rational Design Process: How
> and Why to Fake It".  In it, the authors pointed out that in real
> life we move back and forth between gathering requirements, interface
> design, programming, and testing, but when we write up our work it's
> important to describe it as if we did these steps one after another so
> that other people can retrace our steps. The same is true of lesson
> design: while we may change our mind about what we want to teach based
> on something that occurs to us while we're writing an MCQ, we want the
> notes we leave behind to present things in the order described above.

<!-- comment needed to separate blockquotes -->

> **Teaching to the Test**
> 
> Reverse instructional design is *not* the same thing as "teaching to
> the test". When using RID, teachers set goals to aid in lesson
> design, and may never actually give the final exam that they
> wrote. In many school systems, on the other hand, an external
> authority defines assessment criteria for all learners, regardless
> of their individual situations, and the outcomes of those summative
> assessments directly affect the teachers' pay and promotion.
> Green's *Building a Better Teacher*
> [[Green2014](biblio.html#green-babt)] argues that this focus on
> measurement is appealing to those with the power to set the tests,
> but is unlikely to improve outcomes unless it is coupled with
> support for teachers to make improvements based on test outcomes.
> This is often missing, because as Scott pointed out in
> [[Scott1999](biblio.html#scott-state)], large organizations usually
> value uniformity over productivity.

## Learner Personas

The first piece of the process above is figuring out who your audience
is.  One way to do this is to write two or three _[learner
personas](gloss.html#learner-persona)_. This technique is borrowed
from user interface design, where short profiles of typical users are
created to help designers think about their audience's needs, and to
give them a shorthand for talking about specific cases.

Learner personas have five parts: the person's general background,
what they already know, what *they* think they want to do, how
the course will help them, and any special needs they might have. A
learner persona for a weekend workshop aimed at new college students
might be:

1.  Jorge has just moved from Costa Rica to Canada to study agricultural
    engineering.  He has joined the college soccer team, and is looking
    forward to learning how to play ice hockey.

1.  Other than using Excel, Word, and the Internet, Jorge's most
    significant previous experience with computers is helping his sister
    build a WordPress site for the family business back home in Costa
    Rica.

1.  Jorge needs to measure properties of soil from nearby farms using a
    handheld device that sends logs in a text format to his computer.
    Right now, Jorge has to open each file in Excel, crop the first and
    last points, and calculate an average.

1.  This workshop will show Jorge how to write a little Python program
    to read the data, select the right values from each file, and
    calculate the required statistics.

1.  Jorge can read English proficiently, but still struggles sometimes
    to keep up with spoken conversation (especially if it involves a lot
    of new jargon).

A single learner persona is sometimes enough, but two or three that
cover the whole range of potential learners is better.  One of the
ways they help is by serving as a shorthand for design issues: when
speaking with each other, lesson authors can say, "Would Jorge
understand why we're doing this?" or, "What installation problems
would Jorge face?"

> **Our Learners Revisited**
>
> The personas of Samira and Moshe in the [introduction](index.html)
> have the five points listed above, rearranged to flow more readably.

## Learning Objectives

Summative and formative assessments help instructors figure out what
they're going to teach, but in order to communicate that to learners
and other instructors, a course description should also have
_[learning objectives](gloss.html#learning-objective)_ (sometimes
also called a *learning goal*). A learning objective is a single
sentence describing what a learner will be able to do once they have
sat through the lesson in order to demonstrate what they have learned.

Learning objectives are meant to ensure that everyone has the same
understanding of what a lesson is supposed to accomplish. For example,
a statement like "understand Git" could mean any of the following,
each of this would be backed by a very different lesson:

*   Learners can describe three scenarios in which version control
    systems like Git are better than file-sharing tools like Dropbox,
    and two in which they are worse.

*   Learners can commit a changed file to a Git repository using a
    desktop GUI tool.

*   Learners can explain what a detached HEAD is and recover from it
    using command-line operations.

> **Objectives vs. Outcomes**
> 
> A learning objective is what a lesson strives to achieve.  A
> _[learning outcome](gloss.html#learning-outcome)_ is what it
> actually achieves, i.e., what learners actually take away.  The role
> of summative assessment is therefore to compare outcomes with
> objectives.

More specifically, a good learning objective has a *measurable or
verifiable verb* that states what the learner will do, and specifies
the *criteria for acceptable performance*.  Writing these kinds of
learning objectives may initially seem restrictive or limiting, but
will make both you, your fellow instructors, and your learners happier
in the long run. You will end up with clear guidelines for both your
teaching and assessment, and your learners will appreciate the clear
expectations.

One tool that can help when writing learning objectives is [Bloom's
taxonomy][wikipedia-bloom], which was first published in 1956.  It
attempts to define levels of understanding in a way that is
hierarchical, measurable, stable, and cross-cultural.  The list below
defines the levels in Bloom's Taxonomy and shows some of the verbs
typically used in learning objectives written for each level.

*   Knowledge: recalling learned information
    (name, define, recall).

*   Comprehension: explaining the meaning of information
    (restate, locate, explain, recognize).

*   Application: applying what one knows to novel, concrete situations
    (apply, demonstrate, use).

*   Analysis: breaking down a whole into its component parts
    and explaining how each part contributes to the whole
    (differentiate, criticize, compare).

*   Synthesis: assembling components to form a new and integrated whole
    (design, construct, organize).

*   Evaluation: using evidence to make judgments about
    the relative merits of ideas and materials (choose, rate, select).

Another way to understand what makes for a good learning objective
is to see how a poor one can be improved:

*   "Learner will be given opportunities to learn good programming practices."
    *Describes the lesson's content, not the attributes of successful
    students.*

*   "Learner will have a better appreciation for good programming practices."
    *Doesn't start with an active verb or define the level of learning,
    and the subject of learning has no context and is not specific.*

*   "Learner will understand how to program in R."
    *Starts with an active verb, but doesn't define the level of
    learning, and the subject of learning is still too vague for
    assessment.*

*   "Learner will write one-page read-filter-summarize-print data
    analysis scripts for tabular data using R and R Studio."
    *Starts with an active verb, defines the level of learning,
    and provides context to ensure that outcomes can be assessed.*

Baume's guide to writing and using good learning outcomes
[[Baume2009](biblio.html#baume-outcomes)] is a good longer discussion of
these issues.

## Challenges

### Learner Personas (30 minutes)

Working in pairs or small groups, create a five-point persona that
describes one of your typical learners.

### Write Learning Objectives (20 minutes)

Write one more learning objectives for something you currently teach
or plan to teach.  Working with a partner, critique and improve the
objectives.

[wikipedia-bloom]: https://en.wikipedia.org/wiki/Bloom's_taxonomy
