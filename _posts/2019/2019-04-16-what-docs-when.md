---
date: 2019-04-16 03:13
year: 2019
title: "What Docs When"
---

**Note: this post updates [an earlier one]({{'/2019/04/10/what-docs-and-when.html' | relative_url}})
based on feedback from several people.
Please keep the comments coming.**

[This blog post from Divio](https://www.divio.com/blog/documentation/)
divides documentation into tutorials, how-to guides, explanations, and reference works.
After discussion, we'd like to put forward an alternative.
Its starting point is a three-stage model of cognitive development:

-   A *novice* doesn't yet have a mental model of the domain.
    They don't know what they don't know,
    don't speak the jargon,
    and do things by analogy or by rote.
-   A *competent practitioner* has a usable mental model of the domain.
    They can do routine tasks and solve routine problems,
    know where to look to find more information,
    and can recognize solutions to their problems when they find them.
-   An *expert* has a large, densely-connected model of the domain.
    They can solve common problems at a glance and figure out the one-in-a-thousand cases.

The diagram below shows how different kinds of material help different people.
The X axis is the user's general knowledge of R, RStudio, the tidyverse, and data science.
The Y axis is how well they understand the particular problem they're trying to solve.
The difference is illustrated by these two cases:

-   Someone can have expert knowledge of R in general,
    but be a novice when it comes to the features of the latest release of the IDE.
    (The jargon term for such a person is *false beginner*:
    they look like a novice if you test their knowledge,
    but move much faster than someone without their background knowledge.)
-   Less commonly,
    someone can be competent in one specific area
    but know little or nothing about the larger domain.
    Someone who has learned how to install and configure RStudio Connect but has never used it may fall into this category.
    We sometimes say that their understanding is *brittle*:
    even small changes can shatter their ability to accomplish tasks because they don't have enough of a mental model to generalize or adapt.

<img src="{{'/files/2019/04/doctypes.svg' | relative_url}}" width="100%" alt="Documentation Types" />

This diagram refers to the following kinds of material:

1.  A **how-to** is a step-by-step recipe for solving a particular problem.
    Novices can use it without understanding the "why" behind each step.
2.  An **overview** is a high-level introduction that makes people aware something exists.
    Overviews are often delivered as webinars,
    as the first lecture of a larger workshop or course,
    or as elevator pitches and other marketing material;
    concept maps and other visual aids are particularly useful.
3.  A **tutorial** is a planned lesson that helps people build a mental model of a domain
    and acquire a few basic skills so that they can start to tackle problems of interest.
    We have shown tutorials as moving people from novice to competent;
    tutorials to advance their competence are also common,
    but would clutter this diagram.
4.  A **translation** shows a reader who knows how to do something with tool X how to do it with tool Y;
    it leverages understanding of one topic to increase understanding of another.
5.  **Release notes** and similar "updaters" are for false beginners:
    they assume general understanding, and fill in pre-identified gaps in knowledge.
6.  **References** assume you know what you're looking for but have forgotten or never knew the details.
    They keep being useful no matter how far you progress,
    so the arrow should extend into expertise,
    but that would clutter the diagram.
7.  A **cookbook** full of worked examples is like a how-to
    but assumes the user knows enough to generalize from a specific series of steps to solve a particular problem.
    Cookbooks become less necessary as the user moves from competence to expertise:
    by the latter stage,
    they will have internalized the procedures and most of the steps
    and only occasionally need to check the order.
    (**Checklists**, on the other hand, continue to be useful even for experts.)
8.  **Q&A** sites are included with cookbooks because they fill a similar need,
    but are constructed in a different way:
    Q&A sites are driven by users asking specific questions and the community (or experts) filling in the answers.
    Sites like Stack Overflow are the biggest advance in how we program in the last 20 years.
    A lot of companies and projects run their own discussion forums (like RStudio Community)
    and a lot of people learn from them,
    but only once they know enough to ask a meaningful question and recognize a useful answer.
9.  The transition from competent to expert is where instructors stop teaching fixed rules to be applied in predictable situations
    and start saying, "It depends..."
    A lot of material at this level takes the form of introspective essays,
    like King's *On Writing* or Kael's *The Age of Movies*,
    in which the author implicitly says,
    "Here's how the world looks through my eyes."
    This is also where people use case studies; where an essay is primarily about viewpoint with cases as support,
    a case study is mostly about the particular instance with the author's viewpoint as the added value.
    We don't have nearly enough examples of this in computing,
    though Stroustrup's *Design and Evolution of C++*, Johnson's *GUI Bloopers*, and most of Kernighan's books come to mind.

This list doesn't encompass everything,
but I think most of what's not here can fit into it or be explained in terms of it.
The key is to distinguish content from presentation,
i.e., what's being delivered from how it's being delivered:

-   A **workshop** is usually a way to deliver a tutorial.
-   A **book** often includes tutorials, reference material, worked examples, and case studies in one place.
-   A **vignette** can be an overview or a worked example.
-   A **cheatsheet** is a one-page reference guide that opens with an overview
    and includes a bit of cookbook material as well;
    it's mostly a reminder of things the reader has probably already seen with a few other useful bits thrown in.
-   An **explanation** can be either a tutorial that isn't accompanied by any exercises ("here's how callbacks work in JavaScript")
    or an introspective essay ("here's what led me to decide to use callbacks for this part of the program").
    Explanations are often presented as blog posts or conference talks.
-   Similarly, a **knuth**
    (more often called a "computational notebook" or "literate program", but "knuth" is pithier and gives credit where credit is due)
    can be a tutorial,
    a case study,
    a reference manual,
    or many other things depending on its primary purpose.

This model makes more sense to us than others we have seen;
we'd be grateful for your feedback on whether it makes sense to you
and on what we've missed or misunderstood.
