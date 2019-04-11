---
layout: post
date: 2019-04-10 06:13
title: "What Docs and When"
---

[This blog post from Divio](https://www.divio.com/blog/documentation/)
divides documentation into tutorials, how-to guides, explanations, and reference works.
After discussing it with some of my colleagues,
we'd like to put forward an alternative.
Its starting point is a four-stage model of cognitive development:

-   *Unconscious incompetence*: the person doesn't know what they don't know.

-   *Conscious incompetence*: the person realizes that they don't know something.

-   *Conscious competence*: the person has learned how to do something,
    but can only do it while concentrating and may need to break things down into steps.

-   *Unconscious competence*: the skill has become second nature
    and the person can do it reflexively.

Here's a map showing which kinds of documentation help people get from stage to stage
and which other kinds are useful across multiple stages:

<img src="{{site.github.url}}/files/2019/04/materials.svg" width="80%" alt="Documentation model" />

1.  An *introduction* is a general overview that makes people aware something exists.
    We'd like to find a better term for this,
    but introductions are often delivered as webinars,
    as the first lecture of a larger workshop or course,
    or as elevator pitches and other marketing material.

2.  A *tutorial* is a planned lesson that helps people build a mental model of a domain
    and acquire a few basic skills so that they can start to tackle problems of interest.

3.  Practice with feedback is dashed because it isn't a category of documentation---it's
    what people need to become experts
    (i.e., to get from conscious competence to unconscious competence).
    This is where instructors stop teaching fixed rules to be applied in predictable situations
    and start saying,
    "It depends..." and where individualized critique of students' work takes over from grading against a rubric.
    A lot of material at this level takes the form of introspective *essays*,
    like King's *[On Writing](https://www.amazon.com/Writing-Memoir-Craft-Stephen-King/dp/1439193630/)*
    or Kael's *[The Age of Movies](https://www.amazon.com/Age-Movies-Selected-Writings-Publication/dp/1598535080/)*,
    in which the author implicitly says,
    "Any rules I write down will be banal, so here's how the world looks through my eyes,"
    and relies on the learner to generalize.
    <br/>
    We don't have nearly enough examples of this in computing,
    though Stroustrup's *[Design and Evolution of C++](https://www.amazon.com/Design-Evolution-C-Bjarne-Stroustrup/dp/0201543303/)*,
    Johnson's *[GUI Bloopers](https://www.amazon.com/GUI-Bloopers-2-0-Interactive-Technologies/dp/0123706432/)*,
    and most of Kernighan's books come to mind.
    *Case studies* and *critiques* often go here:
    in retrospect,
    that's the gap *[Beautiful Code](https://www.amazon.com/Beautiful-Code-Leading-Programmers-Practice/dp/0596510047/)*
    and *[The Architecture of Open Source Applications](http://aosabook.org)* were trying to fill.

4.  *Reference* material only starts being useful once you have a mental model of some kind,
    but keeps being useful [no matter how far you progress](https://xkcd.com/1168/).

5.  *Cookbooks* are helpful even before you know what you're trying to do,
    but stop being needed as you move from conscious competence to expertise:
    by that stage,
    you will have internalized the procedures and most of the steps,
    and only occasionally need to check the order.
    *Checklists*, on the other hand,
    continue to be [useful even for experts](https://www.newyorker.com/magazine/2007/12/10/the-checklist).

6.  As [Peggy Storey](http://margaretstorey.com/) and others have pointed out,
    *Q&A* sites like [Stack Overflow](https://stackoverflow.com/) are the biggest advance in how we program in the last 20 years.
    A lot of companies and projects run their own discussion forums (like [RStudio Community](https://community.rstudio.com/))
    and a lot of people learn from them,
    but only once they know enough to ask a meaningful question and recognize a useful answer.

7.  Finally, a *report* is something that presents and justifies a specific conclusion,
    such as, "Teenage vaping is up 22% which is going to impact healthcare costs starting in 2025,"
    or, "Project Spartnubble is going to deliver three months late because reasons."
    A report is a kind of lesson,
    since it explains what and why,
    but most people don't think of reports that way.

This list doesn't encompass everything,
but I think most of what's not here can fit into it or be explained in terms of it:

-   A *workshop* is a way to deliver a tutorial;
    a *book* is another,
    and a *discussion* is a third.
-   A *cheatsheet* is a one-page reference guide that opens with an introduction and includes a bit of cookbook material as well.
-   *Worked examples* are tutorials or case studies,
    depending on the level of detail and analysis.
-   An *explanation* can be either a tutorial that isn't accompanied by any exercises
    ("here's how callbacks work in JavaScript")
    or an introspective essay ("here's the thought process that led me to decide to use callbacks for this part of the program").
-   Similarly, a *knuth*
    (more often called a "computational notebook" or "literate program",
    but "knuth" is pithier and gives credit where credit is due)
    can be a tutorial or a report,
    again depending on whether its primary purpose is to convey general content or a specific conclusion.

This model makes more sense to us than others we have seen;
we'd be grateful for your feedback on whether it makes sense to you,
and on what we've missed or misunderstood.

*Note:
we pulled a bit of a fast one in point #3 above when we equated unconscious competence with expertise.
It's possible to have the former without having the latter:
for example,
if you've driven a particular route every day for years,
you can be capable of doing it without consciously thinking about when to turn where,
but still not be an expert driver in general.
However,
you can't achieve expertise without unconscious competence in component skills:
if you have to think about each step consciously,
you don't have any processing power left over to also think about higher-level solution strategies, edge cases, and the like.*
