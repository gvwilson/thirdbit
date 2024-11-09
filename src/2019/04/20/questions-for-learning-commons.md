---
date: 2019-04-20
title: "Leading Questions for Creating a Learning Commons"
category: favorite
---

[DataCamp's mishandling of a sexual assault case][computerworld]
has got people thinking about more accountable alternatives.
I don't think we should try to build a new platform:
even a simple one requires a ton of unrewarding work,
and while successful platforms are tremendously influential,
the vast majority fail to achieve critical mass.
A centralized platform is also a single point of failure,
socially as well as technically:
"too big to fail" often means "too big to leave",
and as my brother used to say,
if you can't afford to walk away, you're not negotiating—you're begging.

I therefore believe the best way forward is to foster a commons:
a set of resources accessible to all members of a community which in turn manages those resources.
Rather than centralizing lessons,
we make it easy to create, find, use, and remix them so that
[the people we have can do the things they want to with the time they've actually got](@root/2019/04/14/the-people-you-have/).

If we do this,
though,
we have to keep the Reusability Paradox in mind:
the more reusable a learning object is, the less pedagogically effective it is.
The reason is that a good lesson resembles a novel more than it does a program:
its parts are tightly coupled rather than independent black boxes.
If a community is going to create lessons,
it should plan for them to be remixed rather than used as-is.

We also need to avoid chasing squirrels.
Creating a database is more fun than adding data to it,
and most of us would rather spend a week building a tool to auto-grade learners' code
than a day writing the tests for a particular problem set.
I'm a big believer in building tools,
but my experience tells me that building a community will pay a bigger dividend.

The first step is to ask how lessons should be structured.
I hope the questions in this post are a step toward figuring that out,
and I would be grateful for comments.

## 1. Is your lesson findable?

David Wiley and others [have repeatedly said](@root/2018/12/02/oer-landmines/) that
nobody should ever build another lesson repository ever again
because they don't work.
Instead, people should focus on making lessons findable
by tagging them in ways that search engines will recognize.
Findability was the biggest omission in
"[Ten Simple Rules for Creating an Effective Lesson][ten-lesson]"
and
"[Ten Simple Rules for Collaborative Lesson Development][collab-lesson]",
and [Harper][harper] is my attempt to figure out how we could fix this.
It's almost certainly wrong in every detail,
but it could be up and running quickly.

## 2. Do learners, instructors, and contributors know who your lesson is for?

The most effective way to tell people who a lesson is for is not a list of prerequisites:
it's a set of [learner personas][personas] they can sympathize with.
If a community is going to start building and sharing lessons,
they should write a dozen personas that cover the breadth of their hoped-for audience
and have each lesson point at 1--3 of those.
The Harper proposal doesn't have provisions for a shared set of these,
but they'd be easy to add,
and community discussion about exactly who we're trying to help
would do a lot to ensure that every lesson actually helps someone.

## 3. Does each lesson open with a few motivating questions?

People don't search for learning objectives:
they search for answers to questions.
We can make lessons more findable by clearly explaining *in the learners' terms*
what problems each one will help them solve.

## 4. Do lessons refer to a common glossary?

If I could do [Software Carpentry][swc] over again,
I would create a single glossary that all lessons linked to.
This would give authors and learners a shared vocabulary,
which would also improve findability.
(People could also build tools to semi-automatically propose learning paths
by looking at which lessons define the terms used in other lessons,
but that's another techno-squirrel.)
an earlier version of the Harper proposal required each lesson description file to include a link to the glossary
where its terms are defined;
I think that building such a glossary
(or curating a list of links to Wikipedia articles with novice-accessible definitions)
would help bind the community together.

## 5. Can people share their ideas about a lesson?

Stack Overflow's voting mechanism and comments on GitHub issues
both enable community members to pool their knowledge.
[hypothes.is][hypothesis] could enable this for lessons
without requiring people to master arcane technologies.

## 6. Do lessons explain how to diagnose and fix errors?

Newcomers in any subject spend a lot of time trying to figure out what they're doing wrong and how to fix it.
Most lessons don't devote proportional time to this,
but [they should][diagnose].
Again, if I could do Software Carpentry over again,
I'd devote a lot more time to, "If you see X, then Y has gone wrong, and you can fix it by doing Z."
I think content like this makes a lesson more remixable,
and if the answer to a question about what's gone wrong requires knowledge more advanced than the lesson itself covers,
it's often a sign that the lesson should be reorganized.

## 7. Can learners, instructors, and contributors start a lesson with a single command?

Rule 9 for [helping newcomers become contributors to open projects][newcomers] is "make it easy to get set up".
Two of [Taschuk's Rules][taschuk] make a similar point,
and the same applies to lessons:
can everyone who wants to use it get started with a single command on all major platforms?
"Everyone" means learners who want to go through your lesson,
instructors who want to explore it or remix it,
and potential contributors who want to extend or modify it;
all major platforms means Windows, MacOS, Linux, iOS, Android, and possibly Edge, Safari, Firefox, and Chrome.
Thinking about this inevitably gets us into arguments about Docker, Jupyter Notebooks, and other technical minutiae;
I think it will be more productive to agree on the criteria tools need to meet
before trying to pick them,
and Rule 7 is mine.

## 8. Can authors and other contributors get credit for their lessons?

George Orwell once said that the trick is to do good *and* get paid.
Open access of all kinds relies far too often on altruism, heroism, and stealth;
if we want a learning commons to thrive,
we need to give people credit for their work in ways that actually matter.
[CourseSource][coursesource], [JOSE][jose], and [Engage CS Edu][engage-cs]
all give people publication credit for sharing high-quality lessons,
but this doesn't help practitioners in industry or people in organizations like [Bridge][bridge].
Saying that universities and companies should reward teaching and give people time to do it is meaningless
unless the next few sentences are a plan to achieve that,
and I don't have one.

> Bollier's *[Think Like a Commoner][bollier]* is a good introduction to current thinking about commons.
> Ostrom's *[Governing the Commons][ostrom]* lays out the intellectual and empirical foundations,
> and [this recent article][tragedy] by Mildenberger explains
> the many flaws in "the tragedy of the commons" and why it should be retired.

[bollier]: http://www.thinklikeacommoner.com/
[bridge]: https://bridgeschool.io/
[collab-lesson]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005963
[computerworld]: https://www.computerworld.com/article/3389684/r-community-blasts-datacamp-response-to-execs-inappropriate-behavior.html
[coursesource]: https://www.coursesource.org/
[diagnose]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006915#sec009
[engage-cs]: https://www.engage-csedu.org/
[harper]: @root/ideas/harper/
[hypothesis]: https://web.hypothes.is/
[jose]: https://jose.theoj.org/
[newcomers]: https://github.com/gvwilson/10-newcomers
[ostrom]: https://www.cambridge.org/ca/academic/subjects/politics-international-relations/political-theory/governing-commons-evolution-institutions-collective-action-1
[personas]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006915#sec002
[swc]: http://software-carpentry.org
[taschuk]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005412
[ten-lesson]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006915
[tragedy]: https://blogs.scientificamerican.com/voices/the-tragedy-of-the-tragedy-of-the-commons/
