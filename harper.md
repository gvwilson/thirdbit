---
layout: default
permalink: /harper/
title: "Harper: Lesson Discovery and Aggregation"
---

# Harper: Lesson Discovery and Aggregation

-   [Our View of the World](#s:worldview)
-   [Our Proposal](#s:proposal)
-   [Our Community](#s:community)
-   [Usage](#s:usage)
-   [Questions](#s:questions)

Harper's goal is better learning outcomes with less effort.
Its design principles are:

1.  Instead of building another repository or portal,
    we will make it easier for teachers to make their lessons findable,
    then aggregate the information they give us.
2.  We will use tagging, voting, and direct online annotation
    to provide feedback to lesson creators.
3.  We will assume that people are going to adapt and remix material
    instead of using it as-is.
4.  We will not require people to be technically sophisticated
    in order to comment, contribute, and collaborate.

Harper's design is shaped by:

-   The success of RSS for decentralized content syndication.
-   Mike Caulfield's analysis of [Stack Overflow][stack]
    in terms of [choral explanations][choral-explanations].
-   [This list][oer-landmines] of what has been learned from previous open educational resource (OER) projects.
-   [These][twelve-percent] [three][thirteen-percent] [posts][fourteen-percent]
    that included early thoughts on its design.
-   [Lessons learned][lessons-learned] from the [Software Carpentry][swc] project.
-   Discussion with several dozen people over the last ten years.

The project is named after [William Rainey Harper][harper-william],
first president of the University of Chicago,
who encouraged universities to offer distance education courses in the 1890s.
"Harper" also happens to be the name of my youngest niece.

### Acknowledgments {#s:acknowledgments}

I'm grateful to Mike Caulfield,
Alyson Indrunas,
David Wiley,
Bracken Mosbacker,
Mine Çetinkaya-Rundel,
Garrett Grolemund,
Alison Hill,
Jon Udell,
Neal Davis,
and Nick Radcliffe for their comments,
and to Peter Quill for show us that
[you only need twelve percent of a plan][guardians-video] to save the galaxy.
Everything that's still naive, confused, or just plain wrong is my responsibility;
I'd be very grateful for feedback [by email][mailto]
or as comments on this page.

## Our View of the World {#s:worldview}

### Roles

People may be **authors** (who create lessons),
**instructors** (who deliver them),
or **learners** (who use them).
These roles overlap:

1.  Authors are usually also instructors. (At the very least, they're usually the first person to try out new material.)

2.  In practice, instructors are usually also authors, since most people adapt and remix materials rather than using them as-is.

3.  Instructors are often learners: a lot of us are
    [teaching things we don't know well][huston-book].

4.  Instructors may also be absent, i.e., learners may use materials directly without a designated instructor.

5.  Learners are often instructors:
    even where there *is* a designated instructor,
    [people learn as much from peers as from teachers][hidden-lives].

6.  Learners may also be authors: peer contribution of examples and exercises is something we'd strongly like to encourage.

### Use Cases

Most of our use cases are centered around lessons that involve a small amount of programming:

1.  The learner does a programming exercise on her laptop,
    writing code as she would in real life
    and running checks provided by the instructor as she goes along to ensure she's on track,
    then submits the software she has created for grading.
    (By "as she would in real life", we mean "with the same tools she'd use for authentic work".
    Most online environments for teaching programming give learners something akin to Notepad-in-a-browser
    with a bit of syntax highlighting;
    modern IDEs can do a lot more than that,
    and we'd like learners to be able to start using them as soon as possible.)

2.  The learner works through an instructional notebook,
    reading instructions and doing multiple choice questions, short programming challenges, and other kinds of exercises.
    This differs from the previous scenario in that
    (a) the lesson and the exercises are in the same document
    and (b) the learner may not be using the same tools she would use in an authentic situation.

3.  Both of the above, but in the cloud instead of on the learner's laptop.

4.  All of the above, but what is submitted for feedback is prose or a mathematical proof rather than runnable code
    (i.e., is harder to check automatically).

### Distributing Content

The author or instructor might want to distribute the following to learners:

-   Explanations of new ideas.
-   A description of what the learner is supposed to do.
-   A description of what she's supposed to submit (if anything) and how.
-   Practice exercises (i.e., formative assessments), along with automated checks on the user's answers.
-   Glossary definitions, a cheatsheet, a bibliography, and other supporting materials (or links to them).
-   Starter code and data sets in a bewildering variety of formats.
-   Learning objectives.

(Surprisingly there isn't a standard format for these things,
or for other things someone might want to put in a syllabus.)

Our delivery mechanisms for getting lessons to learners are:

1.  Everything on the web:
    instructors don't deliver anything to learners---learners come to a web site and work there.
    Most MOOCs and online coding schools use this model,
    but (a) it begs the question of how instructors get materials into the virtual environments used by the learners
    and (b) it makes authentic work more difficult.
    Solutions such as hosted Jupyter notebooks or [rstudio.cloud][rstudio-cloud] are just one tool;
    in real life,
    people may use many tools in a variety of ways to solve a single problem.
    To emulate that on the web,
    we essentially need to provide a virtual desktop,
    which brings us right back to the question of how we provision it.

2.  Version control:
    the learner clones a repository specified by the instructor
    (which may be the same as the one in which the authors created the lesson or one designed specifically for learners' use).
    Experienced programmers almost always think this is the best solution,
    but "GitHub for teachers" is a dead end because
    [version control is too high a cover charge for most people][oer-landmines]:
    In practice, early adopters will use it because it's cool, everyone else will vote "no" with their feet.

3.  Software packages:
    an R package or Python egg can contain software, data files, and documentation,
    and the infrastructure for finding and installing packages is robust and authentic
    (i.e., is something learners are going to have to master anyway).
    However,
    creating packages requires more time and technical sophistication than many authors have,
    and the required structure of a package may be quite different from the structure we would want for a lesson.
    (For example, the structure of an R package is not the structure of a typical data analysis project.)

4.  Archive files:
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

### Constraints

1.  Most authors and instructors have little or no training in pedagogy,
    so they may not consciously understand the differences between good and mediocre lessons,
    and may not understand the purpose or value of instructional metadata like learning objectives.

2.  Many people believe they need to create their own material in order to understand what they're teaching
    or customize it for their learners.
    This may be related to the previous point,
    i.e.,
    self-taught authors/instructors may find it costlier to re-use other people's work
    in the same way that novice programmers often write their own dot product function rather than using a library.

3.  A corollary to the previous point is that most people won't use others' material directly (without modification),
    so something like a "Lessonopedia" or "Coursepedia" won't work any better than "GitHub for teachers".
    They *will* sample and remix,
    but the [Reusability Paradox][reusability-paradox] states that,
    "The pedagogical effectiveness of a learning object and its potential for reuse are completely at odds with one another".
    The more tightly integrated something is into a larger lesson plan,
    the more effective it is,
    but the harder it is to re-use in other contexts or by other people.

4.  Most people won't use lesson repositories, but *will* use search engines.
    Tagging materials to make them easier to find is therefore more likely to succeed
    than trying to put them all in one place.

5.  Most people will not use technically sophisticated solutions.
    In particular,
    only early adopters will use anything that depends on version control, Docker, or the like.

6.  We don't know what the best granularity for sharing is.
    In software it's the package or library,
    and there's a strong one-to-one relationship between packages and version control repositories.
    In education, people can share at the level of a single exercise, a lecture,
    a module (consisting of several lectures on a particular topic),
    or an entire course (made up of several related modules).
    People seem reluctant to collaborate at the level of entire courses (though there are a few exceptions);
    [Software Carpentry][swc] has had success getting people to collaborate at the level of modules and lessons
    (but again is an exception),
    and there's lots of informal and unacknowledged re-use, but very little collaborative contribution, at the level of exercises.

7.  The discussion earlier focused on how to distribute files.
    It's equally important to think about what ought to be in those files and how to package them.
    Surprisingly, there doesn't seem to be a standard format for this stuff:
    [SCORM][scorm] defines a complex, enterprise-oriented format
    for materials that are to be uploaded to a Learning Management System (LMS) like Moodle or Sakai,
    but assumes that learners will then interact with those materials through the LMS
    rather than (for example) using an IDE on their desktop.

## Our Proposal {#s:proposal}

### Lesson Registration

Authors create one extra text file called `lesson.md` and put it in the lesson's root directory.
(This is inspired by the `feed.xml` and `feed.rss` files used for blogging.)
This file is formatted as Markdown rather than YAML, JSON, or anything else
because Markdown is the simplest set of rules for non-programmers to understand.

`lesson.md` contains the following information, in the specified order.
(We use 'an H2 "XYZ"' to mean 'a level-2 heading with the text "XYZ"'.)

1.  title: short title of lesson (level-1 heading).
1.  abstract: an untitled single-paragraph summary (untitled paragraph immediately below `title`) followed by:
    1.  url: location of lesson.
    1.  author: author's name or comma-separated list of authors' names.
    1.  contact: contact email address.
    1.  date: date of last modification (ISO format please).
    1.  license: name of license.
    1.  copyright: name of copyright holder.
    1.  package: URL of zip file containing starting materials for exercise(s).
    1.  doi: the lesson's DOI (optional).
1.  context: an H2 "Context" with the background or context for the lesson.
1.  requirements: an H2 "Requirements" followed by point-form list of required tools and packages.
    The "requirements" implicitly specify things like "what language does this use?"
    We don't ask for this explicitly because that question may not be relevant
    (e.g., for a question about ethics of data sharing)
    and because a single answer might be wrong
    (e.g., for a lesson that uses the Unix shell, Python, and SQLite).
1.  timeframe: an H2 "Timeframe" followed by a point-form list of
    how long it takes to deliver or do the lesson.
1.  objectives: an H2 "Objectives" followed by point-form list of learning objectives (see below).
1.  glossary: an H2 "Glossary" followed by point-form list of terms and definitions (see below).
1.  keypoints: an H2 "Key Points" followed by point-form list suitable for inclusion in a cheatsheet.

Notes:

-   The original proposal required a URL for the glossary and a point-form list of keys into that glossary
    rather than embedding the glossary directly in `lesson.md`.
    The idea was that this would encourage people to refer to shared glossaries,
    which would in turn encourage them to use a shared vocabulary for lessons.
    Feedback indicated that this was too complicated;
    instead,
    we will look at the glossary entries of registered lessons and try to consolidate them automatically.
-   Materials that learners need to do a lesson are distributed as a zip file
    that unpacks to create a single directory named something like `stat454-exercise03`.
    As noted earlier,
    this isn't as straightforward as many technically sophisticated people believe,
    but it's the simplest thing we can rely on
    that will handle pretty much anything we want to provision.
-   The original proposal required the setup instructions for learners in the lesson description.
    Since learners need these instructions,
    and we can extract them from the zip file,
    that redundancy has been removed.
-   There is no explicit "background knowledge",
    since these are almost always under-estimates of what's actually required.
    Instead,
    we will extract words used in glossary definitions
    (rather than terms defined in the glossary itself)
    and tools mentioned in the learner setup instructions in the zip file
    to compile a list of prerequisite knowledge.
-   The original proposal had a Feedback section
    that authors could use to explain where and how they wanted feedback.
    This proposal assumes [hypothes.is][hypothesis] everywhere.

An example of a `lesson.md` file is shown below;

```
# Tests of Univariate Normality

Describes and compares three ways to test if univariate data is normally distributed.

-   url: http://stats.fringe.tv/stats454/normality.html
-   author: Walter Bishop
-   contact: w.bishop@fringe.tv
-   date: 2018-12-05
-   license: CC-BY-NC-ND
-   copyright: Kelvin Genetics, Inc.
-   package: http://stats.fringe.tv/stats454/normality/stats454-normality.zip

## Context

This material was originally developed as part of a sequence on data integrity
for seniors and graduate students in statistics, then modified for delivery in
conference workshops.  The univariate material feels pretty solid at this point;
the multivariate material has only been used a couple of times, and probably
needs more attention.

## Requirements

-   R (>= 3.5)

## Timeframe

-   Three lectures hours plus three hours of homework.
-   A half-day hands-on workshop doing one exercise per section.

## Objectives

-   Describe the 68-95-99.7 rule and explain why it works and when it fails.
-   Describe and apply the Shapiro-Wilk test for normality of univariate data.
-   Describe and apply the ECF test for normality of multivariate data.

## Glossary

-   68/95/997 Rule: ...definition...
-   Shapiro-Wilk test: ...definition...
-   ECF test: ...definition...

## Keypoints

-   68% of data should lie within one SD of the mean, 95% within two, and 99.7% within three.
-   Use shapiro.test(data) to check normality of univariate data.
-   The StableEstim package implements the ECF test for multivariate data.
```

## Our Community {#s:community}

We support collaboration with a voting mechanism like [Stack Overflow][stack]'s,
but with subject headings drawn from lessons:

1.  An author registers a lesson by providing the URL to its `lesson.md` file,
    just as someone can register a blog by providing a URL to an aggregator.

2.  The site extracts the motivating questions and defined terms from the Markdown
    and displays the lesson under each of those headings (like a possible answer to a question on Stack Overflow).
    Indexing by question helps novices find things;
    indexing by key terms is probably more useful to competent practitioners who already know what they're looking for.

3.  When someone views the page for a question or term,
    they can provide comments on the lessons that appear there and upvote or downvote them.
    This means that a single lesson could appear as the top "answer" to one question and the third "answer" to another.

4.  Each lesson has its own RSS feed,
    so authors and instructors can subscribe to notifications about things they're interested in.
    (We can add this for questions and terms as well, so that if a new lesson appears, interested parties can be notified.)

5.  We will also provide an interactive upload mode:
    after providing a URL for a lesson,
    the author is walked through a very simple online form that asks for the information that goes in the lesson's Markdown file.
    We save that information and give it back to them to download and add to the lesson.
    We still require that the `lesson.md` file be in the lesson's root directory to complete registration
    as a check on authenticity:
    allowing person X to describe a lesson created by person Y opens up too many opportunities for abuse.

5.  When someone registers a new lesson or an update to an existing one,
    the site walks them through a very short workflow to get excerpts from their lessons onto our site.
    We do this for the same reason that blog aggregators display short excerpts from blog posts:
    so that people can tell in advance whether those posts might be worth reading.
    1.  For each of the learning objectives they have listed,
        a pop-up opens that displays their lesson's site.
    2.  The author navigates in this pop-up to the part of their lesson
        that is most closely connected to that learning objective,
        highlights a short excerpt of the lesson,
        and clicks "OK".
    3.  That excerpt is then displayed on our site under their lesson's heading for that objective.

## Usage {#s:usage}

### How does an instructor find a lesson?

1. She does a DuckDuckGo search for the word "lesson" and the keywords or questions she's interested in.
   If we've done our job right,
   the lessons indexed by our site show up near the top of her search,
   just as Stack Overflow answers show up near the top of a search for a technical question.
2. She comes to our site and does a targeted search for her question or keywords.
3. She subscribes to a question or keyword
   and [Feedly][feedly] or some other feed reader
   tells her when something new appears or something relevant is updated.

### How does an author register a lesson?

1. They create a directory on their website with a meaningful name that includes a `lesson.md` file
   and possibly a zip file containing starter materials (if the lesson's exercises need any).
2. They sign into their account on our site and register the URL of the lesson directory.
3. Our site validates their `lesson.md` file.

As noted above,
we *don't* allow people to register lessons that they don't control,
i.e.,
they have to be able to add `lesson.md` to the lesson's website in order for us to accept the registration.

Critically,
our site does some fuzzy matching to suggest rewording of learning objectives or glossary terms
to match ones in lessons that are already registered.
The term "[folksonomy][folksonomy]" seems to have lost its luster,
but encouraging convergence on a shared vocabulary seems crucial to making all of this work.

### How does someone ask for a lesson?

Rather than waiting for people to register their own lessons,
we provide a "please register this" workflow:

1.  Jeanne stumbles across a lesson or exercise she finds interesting.

2.  She clicks the [bookmarklet][bookmarklet]
    in her browser to check if there's a record of it.

3.  If there is, she's given the option of viewing metadata and reviews.

4.  If there isn't, but someone before her has expressed an interest, we add
    one to the "wanna have" count in our database.

5.  If there isn't any record in our database, we scrape the site to get
    contact info for the lesson's author, Vlad.  We then send Vlad a single
    message saying, "Hey, someone's interested in your lesson."

6.  Vlad will probably ignore the message, but if he responds by creating
    a record for his lesson, we stash that so that future inquiries will
    resolve, and notify Jeanne that the record is now available.  This
    workflow serves the triple purpose of attracting more authors, not
    spamming them, and ensuring that the record for a lesson comes from
    someone identified in the lesson's content (i.e., probably not a
    disgruntled former student).

### How does an author update a lesson?

1.  They sign into their account,
    go to "My Lessons",
    and push the "update" button next to the lesson in question.

Note that we archive past `lesson.md` files, but not the actual lesson content.
(We are not a repository, we're an index.)

### How does a learner do a lesson?

1.  The instructor gives him the link to the lesson on our site.
    He clicks the "Download" button on the lesson's page to get a zip file.
2.  Alternatively, the instructor gives him a link directly to the zip file on the author's site.
3.  Finally, the overworked and underpaid graduate student who is TA'ing the course
    could unpack the zip file in a cloud instance
    and send instructions to learners telling them how to get their own copy of that project to run.

## Questions and Comments {#s:questions}

1.  There is nothing in the `lesson.md` file that describes the intended audience for the lesson
    (e.g., how sophisticated they are).
    I'm a big fan of learner personas,
    and I think it's reasonable to ask people to write a couple of paragraphs to explain who the lesson is for,
    but the "Context" section should give us enough to start.
2.  There is nothing in `lesson.md` to connect the lesson to curriculum guidelines.
    While we can debate their relevance,
    linking to them would help instructors find relevant lessons
    and possibly help get buy-in from professional bodies.
3.  Should the license key be a link to a license rather than an acronym?
4.  The "Requirements" field in `lesson.md` is designed to specify packages and tools
    but not things like "access to a yottabyte of temporary storage".
5.  We'll need to provide "export to XYZ" to make incorporation into various LMSes easy.

[bookmarklet]: https://en.wikipedia.org/wiki/Bookmarklet
[choral-explanations]: https://hapgood.us/2016/05/13/choral-explanations/
[feedly]: http://feedly.com
[folksonomy]: https://en.wikipedia.org/wiki/Folksonomy
[fourteen-percent]: {{site.github.url}}/2018/12/19/fourteen-percent.html
[guardians-video]: https://www.youtube.com/watch?v=XC8qrH3Zwog
[harper-william]: https://en.wikipedia.org/wiki/William_Rainey_Harper
[hidden-lives]: https://www.amazon.com/Hidden-Lives-Learners-Graham-Nuthall/dp/1877398241/
[huston-book]: https://www.amazon.com/Teaching-What-You-Dont-Know/dp/0674066170/
[hypothesis]: https://web.hypothes.is/
[lessons-learned]: https://f1000research.com/articles/3-62/v2
[mailto]: mailto:gvwilson@third-bit.com
[oer-landmines]: {{site.github.url}}/2018/12/02/oer-landmines.html
[reusability-paradox]: https://opencontent.org/blog/archives/3854
[rstudio-cloud]: https://rstudio.cloud/
[scorm]: https://scorm.com/
[stack]: http://stackoverflow.com
[student-evals]: https://www.sciencedirect.com/science/article/pii/S0191491X16300323
[swc]: http://software-carpentry.org
[thirteen-percent]: {{site.github.url}}/2018/12/17/thirteen-percent.html
[twelve-percent]: {{site.github.url}}/2018/12/12/twelve-percent.html
