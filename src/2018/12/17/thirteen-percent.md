---
date: 2018-12-17
title: "Thirteen Percent and Counting"
---

Last week, I posted a description of a half-baked plan for
[lesson aggregation](@root/2018/12/12/twelve-percent/).
I've had some useful discussions since then; what follows is hopefully
the first in a series of summaries.

**First,** after further conversation with David Wiley, publishing educational
resources in a single place with consistent formatting, giving them a sensible
organizational structure, and making reasonable SEO efforts are all great ideas.
However, creating a lot of standards-based metadata and providing your own
sophisticated local search interfaces and services on top of that usually fails.

You're going to publish content either way, but repository projects inevitably
end up including metadata and local search because they are what differentiate a
repository from a website.  Experience tells us that almost no one is going to
use your local search engine or leverage your metadata: people are going to use
Google for search and deep link into your site from there. Do you really want to
spend your project's limited time and effort competing with Google on search or
creating 30 or more fields worth of IMS/SCORM/IEEE/Dublin Core/Schema.org
conformant metadata?

**Second,** after conversation with Niall Beard, I've realized that while
[TESS](https://tess.elixir-europe.org/) focuses on helping *learners* find and
use lessons, [my proposal](@root/2018/12/12/twelve-percent/)
focuses more on helping *other instructors* find and *remix* lessons.  I still
believe that YAML-in-GitHub is too high a barrier to entry for most people, but
I think that we can (and should) generate XML or JSON-LD descriptions for
interoperability with existing aggregators.  I'm also now even more interested
in using [hypothes.is](https://web.hypothes.is/) to support aggregation:

1.  Rather than writing a Markdown file and putting it in a lesson's root
    directory, can someone provide the same information by annotating the course
    with hypothes.is?  (The answer is "yes", so I guess the question should be,
    will they?)

2.  Can we provide multiple levels of aggregation?  A course consists of
    lectures, which in turn consist of topics and exercises; rather than
    allowing only one record for aggregation purposes that spans the entire
    thing, can we allow multiple record per site to identify smaller units of
    remixing?  (Again, the answer is "yes", so the question is really, "If we do
    this, will people use it?")

3.  Rather than creating an explicit course-module-lesson-topic hierarchy, can
    we allow authors to put time estimates on the things they provide for
    aggregation, and/or allow re-users to tell us how long it actually took?  We
    asked for the latter information with [Carpentry](http://carpentries.org)
    lessons, but very few people provided it; would hypothes.is annotation on
    the resource itself get more response?

4.  Rather than waiting for people to register their own lessons, we could
    easily provide a "please register this" workflow:

    1.  Jeanne stumbles across a lesson or exercise she finds interesting.

    2.  She clicks the [bookmarklet](https://en.wikipedia.org/wiki/Bookmarklet)
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

**Third,** I had a good conversation with Carl Boettiger, who has [written a
`lesson.md` file](https://github.com/espm-157/climate-template/blob/master/lesson.md)
for one of the modules in his "Data Science and Global Change Ecology" course at
Berkeley.  (Thanks, Carl.)  Here are the key changes he made:

-   Introduced a level-2 heading "Overview" for the front matter.
-   Added a "Context" section that explains why the module was developed
    and how it is usually delivered.
-   Added a "Timeframe" section that describes how long the module takes to deliver.
-   Added a "Background Reading" section with links to related material.

He also asked, "Why are 'glossary' and 'terms' defined separately?"
The idea is that "glossary" is just a link to a site full of definitions,
like [this one](https://developers.google.com/machine-learning/glossary/),
while "terms" are keys into that glossary, like `AB_testing`.
The idea was to (strongly) encourage people to take all their definitions
from one glossary, but this is probably overly clever, so I'll change it.

Similarly, Jeff Oliver suggested that there should be a "DOI" field, which is
eminently sensible and I'm embarrassed for not having thought of it myself.

The revised spec and an example are below.  The words in `fixed font` are
section headings or list keys, depending on indentation; terms in *italics* are
names for content that aren't explicitly keyed (e.g., the abstract is just "the
paragraph immediately below the H1-level title").  As Carl said, parsing this
will be more complicated than parsing YAML, but on the other hand, I think
people might actually write this.

> Another late-breaking change is the introduction of a `sources` field,
> which lists the lesson or lessons that this lesson is (partially) derived from.
> These entries are supposed to be links to those other lessons' `lesson.md` files;
> if the source lesson doesn't have one, it should go under `reading` instead.

Note that this still doesn't describe pre-requisite knowledge: in my experience,
authors' lists are always incomplete, and I believe it will be more accurate to
scrape the content for use of terms defined in selected glossaries (and in other
registered lessons).  And yes, it's still too long: what can we cut?
[Feedback](mailto:gvwilson@third-bit.com) is always appreciated.

1.  `title`: short title of lesson [text].
    1.  *abstract*: a single-paragraph summary [long text].
1.  `overview`: just a heading
    1.  *context*: a single paragraph of background information [long text].
    1.  `author`: author's name or list of authors' names [text or list of text].
    1.  `contact`: contact email address [text].
    1.  `url`: definitive URL for the directory containing the lesson as a whole (not this file) [text].
    1.  `date`: date of last modification [datetime as text].
    1.  `license`: name of license [text].
    1.  `copyright`: name of copyright holder [text].
    1.	`doi`: DOI (if published)
    1.  `package`: URL of zip file containing starting materials for exercise(s) [text].
1.  `timeframe`: how long it takes to do or deliver the module [list of text]
1.  `feedback`: where and how to give feedback [list of text in order of preference].
1.  `questions`: learner questions that this lesson addresses [list of text].
1.  `objectives`: learning objectives [list of text].
1.  `keypoints`: take-aways suitable for inclusion in a cheatsheet [list of text].
1.  `glossary`: list of defined terms (preferably linking to external definitions rather than defining here) [list of text].
1.  `requirements`: list of tools/packages required [text].
1.  `instructions`: point-form list of instructions for learners [list of text].
1.  `sources`: other lessons that this lesson draws on [list of links to other `lesson.md` files].
1.  `reading`: other things to read [list of text].

```
# Tests of Univariate and Multivariate Normality

Describes and compares three ways to test if univariate data is normally distributed.

## Overview

Originally developed as part of a sequence on data integrity for seniors and
graduate students in statistics, then modified for delivery in conference
workshops.  The univariate material feels pretty solid at this point; the
multivariate material has only been used a couple of times, and probably needs
more attention.

- author: "Walter Bishop"
- contact: "w.bishop@fringe.tv"
- url: "http://stats.fringe.tv/stats454/normality/"
- date: "2018-12-05"
- license: "CC-BY-NC-ND"
- copyright: "Kelvin Genetics, Inc."
- doi: "1234-56-789"
- package: "http://stats.fringe.tv/stats454/normality/stats454-normality.zip"

## Timeframe

- Two lecture hours with seniors and graduate students (code-along in class).
- One hour in conference workshops (straight presentation with very little code-along).

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

## Glossary

- [68_95_997_rule](http://all-the-words.org/#68-95-997-rule)
- [shapiro_wilk_test](http://all-the-words.org/#shapiro-wilk-test)
- [ecf_test](http://all-the-words.org/#empirical-characteristic-function)

## Requirements

- "R (>= 3.5)"

## Instructions

- "Download and unzip lesson."
- "install.packages('frequentist_heresy')"
- "Open exercise.Rmd."
```

## Sources

- http://euphoric.edu/katherines-awesome-stats-lesson/lesson.md

## Reading

- [Normality tests](https://en.wikipedia.org/wiki/Normality_test): Wikipedia article
```
