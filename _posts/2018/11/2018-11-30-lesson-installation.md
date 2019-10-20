---
date: 2018-11-30 01:19
title: "Lesson Installation"
---

I [asked this question on Twitter](https://twitter.com/gvwilson/status/1068317515372249088) last night:

> Is there a widely-used packaging format for distributing lesson and exercise files to students?
> Like R packages for R, eggs or wheels for Python, gems for Ruby, etc.?

In more detail, this is the problem I'm trying to solve:

1.  In order to do a programming assignment,
    a learner may want to get several files on her machine,
    including the assignment description, starter code, and some data sets.

2.  In order to get these to her,
    an instructor can create a zip file (or other archive)
    that unpacks to be a directory containing the required files.

3.  Alternatively,
    the instructor can create a version control repository containing the required materials,
    and the student can clone that repository.

4.  But every modern language has a way to create and distribute software and related files,
    such as packages in R, eggs or wheels in Python, or gems in Ruby,
    so a third option is for the instructor to create a package for learners to install.
    (A lesson package would just have a higher documentation-to-code ratio than usual...)

5.  Distributing exercises as packages appeals because it would leverage existing tools
    to handle dependencies.
    Need a particular library to do exercise 3?
    No problem: installing the exercise automatically installs the library.
    The assignment consists of four exercises,
    or several exercises share a large data set:
    Also not a problem:
    installing the assignment triggers installation of the exercises,
    and gives you just one copy of the data set (because that's what package managers are for).

Some technically sophisticated respondents felt that Git is the best way to get files onto learners' machines.
However, "sophisticated" rules out a lot of potential users:
one instructor made it very clear that
if our distribution mechanism requires people to learn Git before they do the first exercise in a stats class,
they'll choose a different distribution mechanism.
(One repository per exercise also seems like the wrong granularity,
but I'm sure we'd get used to it.)

[Another reader pointed out](https://twitter.com/amritavadas/status/1068331539728121856)
that people don't have to be able to use Git in order to get files from GitHub:
they can download the contents of a repository as a zip file.
That solves the multi-file/novice-friendly issues,
but not the dependency/shared file issues.

And these three mechanisms are all ways to get files onto the learner's computer,
but don't specify what those files should contain.
For example,
they don't specify where the local description of the exercise's goals should be
(`README.md`, maybe?)
where pre-submission unit tests should go,
etc.

A few related points:

-   A growing number of learners are going to work in the cloud rather than on their desktop,
    but that just defers the problem:
    someone has to get the lesson into the cloud resource.

-   One reader suggested distributing exercises as Jupyter notebooks,
    but a notebook can't include half a dozen data sets and other files.
    (Well, they *can* if those data sets are embedded as code,
    but 30,000 records don't belong in a notebook.)
    Whatever solution we come up with should allow people to include Jupyter notebooks,
    R Markdown files, and other executable documents,
    but must allow inclusion of other material as well.

-   One reader pointed me at [SCORM](https://scorm.com/scorm-explained/),
    but it specifies how instructors can package things up for inclusion in an LMS,
    rather than for distribution to students' machines.

-   I was surprised to discover that there still isn't a standard machine-readable format for course syllabi:
    the [Open Syllabus Project](http://opensyllabusproject.org/) is collecting syllabi for research purposes,
    but other than a couple of one-off efforts,
    there doesn't yet seem to be a widely-used YAML or Markdown layout for describing courses or exercises.
    (Again, SCORM is LMS-facing, not learner-facing.)

I'm probably over-thinking this---I tend to do that---but `install.packages("stats454-ex3")` really appeals to me:
it uses existing infrastructure to share things,
and it gives learners practice in managing their machine the way we want them to.
And as a growing number of people adopt semi-formal standards for the structure of their GitHub repositories
(general notes in `README.md`, license in `LICENSE.md`, code of conduct in `CONDUCT.md`,
a `CITATION.md` to tell people how to cite the work,
documentation in a `docs` folder, etc.),
it doesn't seem crazy to hope for `INSTRUCTIONS.md` or the like
with a few keywords in a YAML header
to make lessons and exercises easier to find, share, and do.
If this already exists and I'm just looking in the wrong place,
please [let me know](mailto:gvwilson@third-bit.com).

*Note: I apologize for asking for feedback via email,
but I've had to close comments on this blog because of trolls.*
