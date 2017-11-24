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
  learning objectives with reference to Bloom's Taxonomy and/or
  Fink's Taxonomy.**

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
design](gloss.html#reverse-instructional-design)_ and was developed
independent in [[Wiggins2005](biblio.html#wiggins-mctighe)],
[[Biggs2011](biblio.html#biggs-tang-quality)],
and [[Fink2013](biblio.html#fink-significant)] (a summary of
which is freely available online [[Fink2003](biblio.html#fink-short)].)
In brief, lessons should be designed as follows:

1.  Brainstorm to get a rough idea of what you want to cover, how
    you're going to do it, what problems or misconceptions you expect
    to encounter, what's *not* going to be included, and so on.

2.  Create or recycle learner personas (discussed in the next section)
    to figure out who you are trying to teach and what will appeal to
    them.

3.  Draw concept maps to describe the mental model you want learners
    to construct.

4.  Create assessments that will give the learners a chance to
    practice the things they're trying to learn and tell you and them
    whether they're making progress and where they need to focus their
    work.

5.  Put the assessments in order based on their complexity and
    dependencies to construct a course outline.

6.  Write just enough to get learners from one formative assessment to
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

One way to understand what makes for a good learning objective is to
see how a poor one can be improved:

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

[Bloom's taxonomy](gloss.html#blooms-taxonomy) can be used to organize
learning objectives.  First published in 1956, it attempts to define
levels of understanding in a way that is hierarchical, measurable,
stable, and cross-cultural.  The list below defines its levels and
shows some of the verbs typically used in learning objectives written
for each level.

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

FIXME: Anderson and Krathwohl update.

Another way to think about learning objectives comes from
[[Fink2013](biblio.html#fink-significant)], which defines learning in
terms of the change it is intended to produce in the learner.
[Fink's Taxonomy](gloss.html#finks-taxonomy) has six categories:

*   Foundational Knowledge: understanding and remembering information
    and ideas.
*   Application: skills, critical thinking, managing projects.
*   Integration: connecting ideas, learning experiences, and real life.
*   Human Dimension: learning about oneself and others.
*   Caring: developing new feelings, interests, and values.
*   Learning How to Learn: becoming a better student.

A set of learning objectives based on this taxonomy for an
introductory course on HTML and CSS might be:

> By the end of this course, students will:
>
> * Understand the difference between markup and presentation,
>   the nested nature of HTML,
>   what CSS properties are,
>   and how CSS selectors work.
>
> * Know how to write and style a web page using common tags
>   and CSS properties.
>
> * Be able to compare and contrast authoring with HTML and CSS
>   to authoring with desktop publishing tools.
>
> * Understand how the visually impaired interact
>   and people in low-bandwidth environments interact with web pages
>   and take their needs into account when designing new pages.
>
> * Understand the role that JavaScript plays in styling web pages
>   and want to learn more about how to use it.
>
> * Be familiar with [W3Schools][w3schools] and other free tutorials
>   for HTML and CSS, and know what search terms to use to find answers
>   on [Stack Overflow][stack-overflow].

## Maintainability

Good courses take a lot of effort to build, but building them is only
the first challenge.  Once they have been written, someone needs to
maintain them, and doing that is a lot easier if the lessons have been
built in a maintainable way.

But what exactly does "maintainable" mean?  The short answer is that a
course is maintainable if it's cheaper to update it than to replace
it. This equation depends on many factors, only some of which are
under our control:

1. *How well documented the course's design is.* If the person doing
   maintenance doesn't know (or doesn't remember) what the course is
   supposed to accomplish or why topics are introduced in a particular
   order, it will take her more time to update it.  One of the reasons
   to use the template described earlier is to capture decisions about
   why each course is the way it is.

2. *How the course's content is structured.* Version control is the
   secret sauce that allows software development to scale, but today's
   version control systems (still) can't handle widely-used file
   formats like Word and PowerPoint.  Lessons should therefore either
   be written in plain-text formats like HTML, Markdown, or LaTeX, or
   stored online in systems like Google Docs that allow many people to
   edit the same files.  (The next section discusses this in more
   detail.)

3. *How people are using the course.* FIXME: feedback from instructors
   and students alike.

4. *How much the subject matter has changed.* FIXME

5. *How much we know about how to teach.* People have been teaching as
   long as there have been people, but new discoveries and new
   technologies constantly change what's possible.  Each time
   instructors deliver a course, we learn more about how the next
   course should be created. FIXME

## How to Share

FIXME: rewrite in terms of lessons.

Keeping track of what you and your collaborators have done is a
critical part of any data analysis project. Being able to go back to a
specific version of your software or data helps people review your
work, helps you respond to their comments, and reassures readers that
your results are trustworthy.

The most powerful tools for tracking changes are the version control
systems used in software development, such as Git, Mercurial, and
Subversion. They record what was changed in a file, when, and by whom,
and synchronize changes between computers so that multiple
contributors can safely manage the same set of files.

While version control tools make tracking changes easier, they can
have a steep learning curve. For novices, and for smaller proejcts, a
systematic manual approach is sometimes good enough.  Whichever
approach you pick, a handful of best practices will make your life
easier:

1. **Back up (almost) everything created by a human being as soon as
   it is created.** This includes scripts and programs of all kinds,
   software packages that your project depends on, and
   documentation. A few exceptions to this rule are discussed below.

2. **Keep changes small.** For example, a single change that changes
   several hundred lines in an analysis script is probably too large
   to test or review, as it will not allow changes to different
   components of the analysis to be understood separately. As a rule
   of thumb, a good size for a single change is a group of edits that
   you could imagine wanting to undo in one step at some point in the
   future.

3. **Share changes frequently.** Everyone working on the project
   should share and incorporate changes from others on a regular
   basis. Do not allow individual investigator's versions of the
   project repository to drift apart, as the effort required to merge
   differences goes up faster than the size of the difference. This is
   particularly important for the manual versioning procedure describe
   below, which does not provide any assistance for merging
   simultaneous, possibly conflicting, changes.

4. **Create, maintain, and use a checklist for saving and sharing
   changes to the project.** The list should include writing log
   messages that clearly explain any changes, style guidelines for
   code, updating to-do lists, and bans on committing half-done work
   or broken code.

5. **Store each project in a folder that is mirrored off anyone's
   personal machine** using one of the tools discussed below, and
   **synchronize that folder at least daily**. It may take a few
   minutes, but that time is repaid the moment a laptop is stolen or
   its hard drive fails.

You really should use a version control system, but if you choose to
manage your files manually, you should still follow three simple
rules.  First, make sure that your files are *not* stored on a single
computer (which can be stolen, lost, or accidentally wiped). Instead,
use a cloud-based service such as Dropbox so that changes are recorded
somewhere less vulnerable.

Second, add a file called `CHANGELOG.txt` to the project, and keep
dated notes about changes in this file in reverse chronological order
(that is, most recent first). This file is the equivalent of a lab
notebook, and should contain entries like these:

```
## 2016-04-08

* Switched to cubic interpolation as default.
* Moved question about family's TB history to end of questionnaire.

## 2016-04-06

* Added option for cubic interpolation.
* Removed question about staph exposure (can be inferred from blood test results).
```

Third, copy the entire project whenever a significant change has been
made (that is, one that materially affects the results), and store
that copy in a sub-folder whose name is the date it was created. This
approach results in projects being organized as shown below:

```
.
|-- project_name
|   -- current
|       -- ...project content as described earlier...
|   -- 2016-03-01
|       -- ...content of 'current' on Mar 1, 2016
|   -- 2016-02-19
|       -- ...content of 'current' on Feb 19, 2016
```

Here, the `project_name` folder is mapped to external storage (e.g.,
Dropbox), `current` is where new work is being done, and other folders
within `project_name` are old versions.

Data scientists often say that "data is cheap, but time is expensive".
Copying everything like the above approach suggests may seem wasteful,
since many files won't have changed, but consider: a terabyte hard
drive costs about $50, which means that 50 GByte costs less than
$5. Provided very large data files are kept out of the backed-up area,
this approach costs less than the time it would take to select files
by hand for copying.

This manual procedure is good enough for small projects with a small
number of collaborators. If many people are working on the same
project, though, or as the project grows larger, colleagues will need
to coordinate so that only a single person is working on specific
files at any time. In particular, they may wish to create one
changelog file per contributor, and to merge those files whenever a
backup copy is made.

The version control tools that underpin our second approach don't just
accelerate the manual process described above: they automate some
steps while enforcing others, and thereby require less self-discipline
for more reliable results.

It's hard to know what version control tool is most widely used in
research today, but the one that's most talked about is undoubtedly
Git. This is largely because of GitHub, a popular hosting site that
combines the technical infrastructure for collaboration via Git with a
modern web interface. GitHub is free for public and open source
projects and for users in academia and nonprofits.  GitLab is a
well-regarded alternative that many people now prefer because the
platform itself is free and open source. Bitbucket provides free
hosting for both Git and Mercurial repositories, but does not have
nearly as many scientific users.

The core of any version control workflow is an update-work-commit
cycle:

-   **Update** your working copy to bring in changes other people have
    made.
-   Do whatever **work** you were planning to.
-   **Commit** your work to the shared repository, merging any conflicts
    between what you've done and what others have done.

Modern version control systems like Git and Mercurial encourage people
to make each change in a **branch**, which is a temporary parallel
copy of the entire project.  Using branches allows people to work on
several things at once without tripping over themselves, which in turn
makes it easier to explore new ideas without risk.

The benefits of version control systems don't apply equally to all
file types.  First, file comparison in version control systems is
optimized for plain text files, such as source code. The ability to
see so-called "diffs" is one of the great joys of version
control. Unfortunately, while Microsoft Office files (like the `.docx`
files used by Word) or other formats like PDF can be stored in version
control, it is not possible to pinpoint specific changes from one
version to the next.  Tabular data, such as CSV files, can be put in
version control as well, but changing the order of the rows or columns
will create a big change for the version control system, even if the
data itself has not changed.

Second, raw data should not change, and therefore should not require
version tracking.  Keeping intermediate data files and other results
under version control is also not necessary if you can regenerate them
from raw data and software. However, if data and results are small,
it's recommended to version them for ease of access.

Third, today's version control systems were not designed to handle
very large files, so large data or results files should not be
included.  (As a benchmark for "large", the limit for an individual
file on GitHub is 100MB.)  Some emerging hybrid systems such as Git
LFS put textual notes under version control, while storing the large
data itself in a remote server, but these are not yet mature enough
for us to recommend.

Regardless of what system you use, it's important to be wary of
inadvertent sharing.  Researchers dealing with data subject to legal
restrictions that prohibit sharing (such as medical data) should be
careful not to put data into cloud storage or public version control
systems. Some institutions may provide access to private version
control systems, so it is worth checking with your IT department.
Additionally, be sure not to unintentionally place security
credentials, such as passwords and private keys, in a version control
system where it may be accessed by others.

## Challenges

### Learner Personas (30 minutes)

Working in pairs or small groups, create a five-point persona that
describes one of your typical learners.

### Write Learning Objectives (20 minutes)

Write one more learning objectives for something you currently teach
or plan to teach using Bloom's Taxonomy.  Working with a partner,
critique and improve the objectives.

### Write More Learning Objectives (20 minutes)

Write one more learning objectives for something you currently teach
or plan to teach using Fink's Taxonomy.  Working with a partner,
critique and improve the objectives.

[stack-overflow]: https://stackoverflow.com/
[w3schools]: https://www.w3schools.com/
