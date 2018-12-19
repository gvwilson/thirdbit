---
layout: post
date: 2018-12-12 02:00
title: "Twelve Percent of a Plan"
---

I've spent much of the last eight years teaching people
[how to develop lessons collaboratively](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005963)
and [wondering why they don't do it more often]({{site.github.url}}/2016/04/29/why-teachers-dont-collaborate.html).
As part of my job at [RStudio](http://rstudio.com),
I wanted to turn what I think I know into a tool like R's [usethis](https://usethis.r-lib.org/)
to automate common tasks in lesson setup
and help ensure that lessons are structured in a uniform way to make sharing easier.
After some discussions with experts on Open Educational Resources (OER)
about [what hasn't worked in the past]({{site.github.url}}/2018/12/02/oer-landmines.html),
though,
I realized that my original plan was wrong-headed.
It assumed far more technical knowledge than most instructors have;
more importantly,
it assumed that people would re-use lessons with little or no modification,
the way they re-use software libraries,
when in practice it seems that most instructors want to sample and remix.

I've therefore been working on a plan that tries to do less,
but which I hope will thereby accomplish more.
This is still very much a work in progress---I'd be very grateful for feedback,
which you can [send by email](mailto:gvwilson@third-bit.com).

## Goals

Our primary goal is better learning outcomes with less effort on the part of
authors (who create lessons),
instructors (who deliver them),
and learners (who use them).
These roles overlap:

1. Authors are usually also instructors. (At the very least, they're usually the first person to try out new material.)

2. In practice, instructors are usually also authors, since most people adapt and remix materials rather than using them as-is.

3. Instructors are often learners: a lot of us are
   [teaching things we don't know well](https://www.amazon.com/Teaching-What-You-Dont-Know/dp/0674066170/).

4. Instructors may also be absent, i.e., learners may use materials directly without a designated instructor.

5. Learners are often instructors:
   even where there *is* a designated instructor,
   [people learn as much from peers as from teachers](https://www.amazon.com/Hidden-Lives-Learners-Graham-Nuthall/dp/1877398241/).

6. Learners may also be authors: peer contribution of examples and exercises is something we'd strongly like to encourage.

We believe that building lessons collaboratively and re-using lesson materials
(which aren't necessarily the same thing)
will improve learning outcomes and reduce the load on authors and instructors:

1. Collaborative construction will produce better lessons because authors will hybridize their best ideas.

2. Sharing will reduce effort because instructors won't have to create all their own materials from scratch.
   (However, this depends on the time required to master and adapt materials
   being less than the time required to develop new materials.)

3. Sharing might also produce better lessons because material will be tested in the classroom more frequently.
   (However, this depends on instructors giving feedback on materials they use.)

## Models and Inspirations

1. Direct inheritance:
   author/instructor X develops materials and uses them,
   then instructor Y inherits those materials and continues to evolve them in parallel with X's continued changes,
   but with no systematic sharing of changes.

2. Scavenging:
   an instructor scours the web to find and assemble material.
   This is a one-sided, hybridizing version of direct inheritance
   (i.e., the various X's may not know that Y is using their material),
   but again, there is no systematic sharing of changes.

3. Open source software construction on GitHub and other software forges:
   work is done independently, but is usually then merged with a master copy after review.
   Differing goals or incompatible personalities occasionally lead to work being forked,
   but there are still only a handful of alternatives
   (i.e., the number of active projects may be greater than 1, but is much less than the number of users).
   There are also multiple levels of involvement:
   one or a few maintainers,
   a slightly larger circle of contributors,
   an even larger pool of active observers who file bug reports and make feature requests,
   and a much larger group of [dark matter users](https://www.hanselman.com/blog/DarkMatterDevelopersTheUnseen99.aspx).

4. Article revision on Wikipedia:
   this is also open and collaborative,
   but requires much less technical sophistication
   (editing a wiki is much easier than using Git).
   More importantly, everyone is always working with a single authoritative master copy.

5. Q&A sites like [Stack Overflow](https://stackoverflow.com/) and [Quora](https://www.quora.com/):
   these allow multiple texts rather than a single authoritative text,
   and rely on feedback from users to refine alternatives and make them more or less prominent.
   Caulfield has dubbed the result [a chorus of explanations](https://hapgood.us/2016/05/13/choral-explanations/)
   because this model allows explanations for readers at different levels and with different interests to coexist.

6. Annotation services like [hypothes.is](https://web.hypothes.is/):
   these allow people to create and share annotations on specific parts of arbitrary web pages
   without needing explicit support from the hosts of those pages.

## Use Cases

Since we're primarily teaching data science, most of our use cases are centered around programming:

1. The learner does a programming exercise on her laptop,
   writing code as she would in real life
   and running checks provided by the instructor as she goes along to ensure she's on track,
   then submits the software she has created for grading.
   (By "as she would in real life", we mean "with the same tools she'd use for authentic work".
   Most online environments for teaching programming give learners something akin to Notepad-in-a-browser
   with a bit of syntax highlighting;
   modern IDEs can do a lot more than that,
   and we'd like learners to be able to start using them as soon as possible.)

2. The learner works through an instructional notebook,
   reading instructions and doing multiple choice questions, short programming challenges, and other kinds of exercises.
   This differs from the previous scenario in that
   (a) the lesson and the exercises are in the same document
   and (b) the learner may not be using the same tools she would use in an authentic situation.

3. Both of the above, but in the cloud instead of on the learner's laptop.

4. All of the above, but what is submitted for feedback is prose or a mathematical proof rather than runnable code
   (i.e., is harder to check automatically).

> All of the above assume that the learner's deliverable is a noun rather than a verb,
> i.e., that what's assessed is the code or prose the learner creates rather than how they created it.
> Many disciplines have lab exams or performance exams;
> it would be nice if our solution for lesson sharing allowed for this,
> but that's out of scope for this proposal.

## Content for Learners

A lesson might contain anything; what might we want to distribute to learners?

- Explanations of new ideas.
- A description of what the learner is supposed to do.
- A description of what she's supposed to submit (if anything) and how.
- Practice exercises (i.e., formative assessments), along with automated checks on the user's answers.
- Glossary definitions, a cheatsheet, a bibliography, and other supporting materials (or links to them).
- Starter code and data sets in a bewildering variety of formats.
- Learning objectives.

Surprisingly there isn't a standard format for these things,
or for other things someone might want to put in a syllabus:
the Open Syllabus Project is collecting material,
but other than a few one-off efforts,
nobody seems to have defined a lightweight format for course descriptions.

## Delivery

Our delivery mechanisms for getting lessons to learners are:

1. Everything on the web:
   instructors don't deliver anything to learners---learners come to a web site and work there.
   Most MOOCs and online coding schools use this model,
   but (a) it begs the question of how instructors get materials into the virtual environments used by the learners
   and (b) it makes authentic work more difficult.
   Solutions such as hosted Jupyter notebooks or [rstudio.cloud](https://rstudio.cloud/) are just one tool;
   in real life,
   people may use many tools in a variety of ways to solve a single problem.
   To emulate that on the web,
   we essentially need to provide a virtual desktop,
   which brings us right back to the question of how we provision it.

2. Version control:
   the learner clones a repository specified by the instructor
   (which may be the same as the one in which the authors created the lesson or one designed specifically for learners' use).
   Experienced programmers almost always think this is the best solution,
   but "GitHub for teachers" is a dead end because
   [version control is too high a cover charge for most people]({{site.github.url}}/2018/12/02/oer-landmines.html):
   In practice, early adopters will use it because it's cool, everyone else will vote "no" with their feet.

3. Software packages:
   an R package or Python egg can contain software, data files, and documentation,
   and the infrastructure for finding and installing packages is robust and authentic
   (i.e., is something learners are going to have to master anyway).
   However,
   creating packages requires more time and technical sophistication than many authors have,
   and the required structure of a package may be quite different from the structure we would want for a lesson.
   (For example, the structure of an R package is not the structure of a typical data analysis project.)

4. Archive files:
   we assume that learners can download and unpack a zip file or similar archive,
   but this does nothing to help ensure that the right versions of the right software are installed,
   doesn't provide a way for learners to submit their work (which committing to a repository does),
   and the assumption itself may be wrong.
   A common pattern is that a zip file contains a whole project with multiple required files.
   Users click into the zip (which their desktop GUI helpfully makes look like a normal folder)
   and double-click the one file they need,
   which the OS puts in a temporary directory.
   hat file then cannot find its sibling files,
   and the user is baffled because nothing seems to work.

## Cautionary Tales

1. Most authors and instructors have little or no training in pedagogy,
   so they may not consciously understand the differences between good and mediocre lessons,
   and may not understand the purpose or value of instructional metadata like learning objectives.

2. Many people believe they need to create their own material in order to understand what they're teaching
   or customize it for their learners.
   This may be related to the previous point,
   i.e.,
   self-taught authors/instructors may find it costlier to re-use other people's work
   in the same way that novice programmers often write their own dot product function rather than using a library.

3. A corollary to the previous point is that most people won't use others' material directly (without modification),
   so something like a "Lessonopedia" or "Coursepedia" won't work any better than "GitHub for teachers".
   They *will* sample and remix,
   but the [Reusability Paradox](https://opencontent.org/blog/archives/3854) states that,
   "The pedagogical effectiveness of a learning object and its potential for reuse are completely at odds with one another".
   The more tightly integrated something is into a larger lesson plan,
   the more effective it is,
   but the harder it is to re-use in other contexts or by other people.

4. Most people won't use lesson repositories, but *will* use search engines.
   Tagging materials to make them easier to find is therefore more likely to succeed
   than trying to put them all in one place.

5. Most people will not use technically sophisticated solutions.
   In particular,
   only early adopters will use anything that depends on version control, Docker, or the like.

6. We don't know what the best granularity for sharing is.
   In software it's the package or library,
   and there's a strong one-to-one relationship between packages and version control repositories.
   In education, people can share at the level of a single exercise, a lecture,
   a module (consisting of several lectures on a particular topic),
   or an entire course (made up of several related modules).
   People seem reluctant to collaborate at the level of entire courses (though there are a few exceptions);
   [Software Carpentry](http://carpentries.org) has had success getting people to collaborate at the level of modules and lessons
   (but again is an exception),
   and there's lots of informal and unacknowledged re-use, but very little collaborative contribution, at the level of exercises.

7. The discussion earlier focused on how to distribute files.
   It's equally important to think about what ought to be in those files and how to package them.
   Surprisingly, there doesn't seem to be a standard format for this stuff:
   SCORM defines a (complex, enterprise-oriented) format
   for materials that are to be uploaded to a Learning Management System (LMS) like Moodle or Sakai,
   but assumes that learners will then interact with those materials through the LMS
   rather than (for example) using an IDE on their desktop.

## Proposal

Our proposed solution requires authors to create one extra text file.
Just as every RSS feed has a metadata file called `feed.xml` (or `feed.rss`, or `atom.xml`---ah, standards...),
every lesson must have a Markdown file called `lesson.md` in its root directory.

> Why Markdown rather than YAML?
> For the same reason that we're not going to require Git as a backing store or Jekyll/Hugo/whatever as a formatter:
> we're already asking authors and instructors to learn a bunch of new things,
> some of them quite large,
> and the simple Markdown we're asking for is more accessible than the indented key-value lists of YAML.

We support collaboration with a voting mechanism like Stack Overflow's,
but with subject headings drawn from lessons:

1. An author registers a lesson by providing the URL to its `lesson.md` file,
   just as someone can register a blog by providing a URL to an aggregator.

2. The site extracts the motivating questions and defined terms from the Markdown
   and displays the lesson under each of those headings (like a possible answer to a question on Stack Overflow).
   Indexing by question helps novices find things;
   indexing by key terms is probably more useful to competent practitioners who already know what they're looking for.

3. When someone views the page for a question or term,
   they can provide comments on the lessons that appear there and upvote or downvote them.
   This means that a single lesson could appear as the top "answer" to one question and the third "answer" to another.

4. Each lesson has its own RSS feed,
   so authors and instructors can subscribe to notifications about things they're interested in.
   (We can add this for questions and terms as well, so that if a new lesson appears, interested parties can be notified.)

5. We will also provide an interactive upload mode:
   after providing a URL for a lesson,
   the author is walked through a very simple online form that asks for the information that goes in the lesson's Markdown file.
   We save that information and give it back to them to download and add to the lesson.
   We still require that the `lesson.md` file be in the lesson's root directory to complete registration
   as a check on authenticity:
   allowing person X to describe a lesson created by person Y opens up too many opportunities for abuse.

5. When someone registers a new lesson or an update to an existing one,
   the site walks them through a very short workflow to get excerpts from their lessons onto our site.
   We do this for the same reason that blog aggregators display short excerpts from blog posts:
   so that people can tell in advance whether those posts might be worth reading.
   1. For each of the motivating questions or learning objectives they have listed,
      a pop-up opens that displays their lesson's site.
   2. The author navigates in this pop-up to the part of their lesson that is most closely connected to that learning objective,
      highlights a short excerpt of the lesson,
      and clicks "OK".
   3. That excerpt is then displayed on our site under their lesson's heading for that question or objective.

The fields in `lesson.md` are:

1. title: short title of lesson [text].
1. abstract: brief summary [long text].
1. author: author's name or list of authors' names [text or list of text].
1. contact: contact email address [text].
1. url: definitive URL for the directory containing the lesson as a whole (not this file) [text].
1. date: date of last modification [datetime as text].
1. license: name of license [text].
1. copyright: name of copyright holder [text].
1. glossary: URL of glossary in which terms are defined [text].
1. package: URL of zip file containing starting materials for exercise(s) [text].
1. feedback: where and how to give feedback [list of text in order of preference].
1. questions: learner questions that this lesson addresses [list of text].
1. objectives: learning objectives [list of text].
1. keypoints: suitable for inclusion in a cheatsheet [list of text].
1. terms: keys into that glossary [text].
1. requirements: list of tools/packages required [text].
1. instructions: point-form list of instructions for learners [list of text].

Notes:

- Yes, this is a lot of fields, and yes, we should try to shorten the list.
- The "requirements" implicitly specify things like "what language does this use?"
  We don't ask for this explicitly because that question may not be relevant
  (e.g., for a question about ethics of data sharing)
  and because a single answer might be wrong
  (e.g., for a lesson that uses the Unix shell, Python, and SQLite).
- The "instructions" are how to get started, not how to submit,
  since that will vary widely from institution to institution.
- We do not ask for the instructions in machine-executable form
  because we don't want people to copy and paste them into a shell prompt
  because hello, security holes.
- Materials that learners need to do a lesson are distributed as a zip file
  that unpacks to create a single directory named something like `stat454-exercise03`.
  As noted earlier,
  this isn't as straightforward as many technically sophisticated people believe,
  but it's the simplest thing we can rely on
  that will handle pretty much anything we want to provision.

An example of a `lesson.md` file is shown below.

```
# Tests of Univariate Normality

## Overview

Describes and compares three ways to test if univariate data is normally distributed.

- author: "Walter Bishop"
- contact: "w.bishop@fringe.tv"
- url: "http://stats.fringe.tv/stats454/normality/"
- date: "2018-12-05"
- license: "CC-BY-NC-ND"
- copyright: "Kelvin Genetics, Inc."
- glossary: "http://education.rstudio.com/glossary/"
- package: "http://stats.fringe.tv/stats454/normality/stats454-normality.zip"

## Feedback

- "Issues or pull requests in http://github.com/fringebishop/stats454/"
- "Comments on http://stats.fringe.tv/stats454/"

## Questions

- "What is a quick back-of-the-envelope way to test normality?"
- "How should I test whether my data is normally distributed?"

## Objectives

- "Describe the 68-95-99.7 rule and explain why it works and when it fails."
- "Describe and apply the Shapiro-Wilk test for normality of univariate data."
- "Describe and apply the ECF test for normality of multivariate data."

## Keypoints

- "68% of data should lie within one SD of the mean, 95% within two, and 99.7% within three."
- "Use shapiro.test(data) to check normality of univariate data."
- "The StableEstim package implements the ECF test for multivariate data."

## Terms

- "68_95_997_rule"
- "shapiro_wilk_test"
- "ecf_test"

## Requirements

- "R (>= 3.5)"

## Instructions

- "Download and unzip lesson."
- "install.packages('frequentist_heresy')"
- "Open exercise.Rmd."
```

This `lesson.md` file implies that `http://education.rstudio.com/glossary/#ecf_test` and similar glossary URLs will resolve.
After registration,
this lesson will show up under two question headings and three glossary definition headings.

## Usage

### How does an instructor find a lesson?

1. She does a DuckDuckGo search for the word "lesson" and the keywords or questions she's interested in.
   If we've done our job right,
   the lessons indexed by our site show up near the top of her search,
   just as Stack Overflow answers show up near the top of a search for a technical question.
2. She comes to our site and does a targeted search for her question or keywords.
3. She subscribes to a question or keyword and Feedly tells her when something new appears or something relevant is updated.

### How does an author register a lesson?

1. They create a directory on their website with a meaningful name that includes a `lesson.md` file
   and possibly a zip file containing starter materials (if the lesson's exercises need any).
2. They sign into their account on our site and register the URL of the lesson directory.
3. Our site validates their lesson and does some fuzzy matching to suggest rewording of questions or keywords
   to match questions already registered.

As noted above,
we *don't* allow people to register lessons that they don't control,
i.e.,
they have to be able to add `lesson.md` to the lesson's website in order for us to accept the registration.

### How does an author update a lesson?

1. They sign into their account, go to "My Lessons", and push the "update" button next to the lesson in question.

Note that we archive past `lesson.md` files, but not the actual lesson content.
(We are not a repository, we're an index.)

### How does a learner do a lesson?

1. The instructor gives him the link to the lesson on our site.
   He clicks the "Download" button on the lesson's page to get a zip file.
2. Alternatively, the instructor gives him a link directly to the zip file on the author's site.
3. Finally, the overworked and underpaid graduate student who is TA'ing the course
   could unpack the zip file in a cloud instance
   and send instructions to learners telling them how to get their own copy of that project to run.

## Questions

1. Will enough authors be willing to write description files?
1. Will enough of them be willing to comment/vote on registered lessons? Will authors incorporate that feedback?
1. What criteria will users use to vote on lessons?
   Votes are unlikely to capture how well the lesson worked in the classroom
   because instructors are only likely to teach one lesson (and hence have little basis for comparison),
   and intuitive comparisons are likely to be hindered by most authors' and instructors' lack of training in pedagogy.
   We could therefore wind up making the same mistake as
   [relying on student evaluations of courses](https://www.sciencedirect.com/science/article/pii/S0191491X16300323).
1. There is nothing in the `lesson.md` file that describes the intended audience for the lesson
   (e.g., how sophisticated they are).
   I'm a big fan of learner personas,
   and I think it's reasonable to ask people to write a couple of paragraphs to explain who the lesson is for.
   If so, these personas should be shared in the same way as glossary definitions.
1. Similarly, nothing in `lesson.md` specifies prerequisites.
   This is implied at a high level by learner personas,
   but (a) we haven't agreed to those yet,
   and (b) that's too high a level.
   We could search lesson content for uses of terms that are in the same glossary as the lesson's definitions
   and construct a list of dependencies automatically.
1. There is nothing in `lesson.md` to connect the lesson to curriculum guidelines.
   While we can debate their relevance,
   linking to them would help instructors find relevant lessons
   and possibly help get buy-in from professional bodies.
1. Should the license key be a link to a license rather than an acronym?
1. The "Requirements" field in `lesson.md` is designed to specify packages and tools
   but not things like "access to a yottabyte of temporary storage".
1. Is it too geeky to suggest adding a `<link type="application/lesson+yaml".../>` header to lessons' home pages?
   Yes?
   OK.

## Next Steps

I'm grateful to Mike Caulfield, Alyson Indrunas, David Wiley Udell, Bracken Mosbacker,
Mine Çetinkaya-Rundel, Garrett Grolemund, Alison Hill, and Jon Udell for their comments,
and to Peter Quill for show us all that
[you only need twelve percent of a plan](https://www.youtube.com/watch?v=XC8qrH3Zwog)
to save the world.
Everything that's still naive, confused, or just plain wrong is my responsibility;
as noted at the start,
I'd be very grateful for feedback,
which you can [send by email](mailto:gvwilson@third-bit.com).
(I apologize for not allowing discussion here:
following my criticism of Shopify's continued support for white nationalist sites,
it seemed best to disable comments on this blog until the trolls turned their attention elsewhere.)
