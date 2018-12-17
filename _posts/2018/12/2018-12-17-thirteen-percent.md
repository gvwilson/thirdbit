---
layout: post
date: 2018-12-17 02:00
title: "Thirteen Percent and Counting"
---

Last week, I posted a description of a half-baked plan for [lesson
aggregation]({{site.github.url}}/2018/12/12/twelve-percent.html).  I've had some
useful discussions since then; what follows is hopefully the first in a series
of summaries.

First, after further conversation with David Wiley, publishing educational
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

Second, after conversation with Niall Beard, I've realized that while
[TESS](https://tess.elixir-europe.org/) focuses on helping *learners* find and
use lessons, [my proposal]({{site.github.url}}/2018/12/12/twelve-percent.html)
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
