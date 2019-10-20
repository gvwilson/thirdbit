---
date: 2019-04-24 04:12
title: "Ten Quick Tips for Reviewing Lessons"
---

If you do a degree in English literature,
you spend most of your time reading and critiquing other people's work
rather than writing new material yourself.
I don't know what the balance of reading and doings proofs is in Mathematics---I suspect
it's somewhere near 50/50---but if you do a degree in Computer Science,
you spend far more time writing software than you do reading it critically.

But what of education?
How much time do people spend analyzing great lessons from the past in a B.Ed. or M.Ed.?
Based on what I've read,
I suspect it's more like Computer Science than literature.
And if you're a self-taught, free-range teacher,
you may never have seen or received a detailed critique of any teaching material.

Now that
"[Ten Quick Tips for Creating an Effective Lesson][10-lesson]"
is out,
I'd like to start thinking about how to fill that gap.
As with literature and coding,
I think it can only be done by example:
general principles like character development and modularization only make sense
when you are shown what they are generalizing.
But it's equally important to set out some tentative rules at the start,
because you can't choose examples unless you have some idea what they're examples of.

What follows is my first attempt at defining those rules.
It doesn't cover spelling and grammar or the logical flow of the lesson---I will try
to work up a separate checkable list for that---but I think it's more useful than
[my earlier post]({{site.github.url}}/2019/04/20/questions-for-learning-commons.html).
I hope that people who are sharing lessons freely available online will find it useful,
and I'd be very grateful for feedback.
(I have once again had to disable comments on this blog,
so please [send me ideas by email](mailto:gvwilson@third-bit.com).)

1.  **Is the lesson inclusive?**
    I put this last in [the Quick Tips paper][10-lesson],
    but it should have been front and center.
    Lessons should *be accessible to people with disabilities*
    and *use inclusive language and examples*,
    both because it's the moral thing to do
    and because [kerb cuts help everyone][kerb-cuts].

2.  **Does the lesson's license allow remixing?**
    Most instructors don't use other people's material verbatim in the way that they use a software library.
    Instead, they combine it with other lessons,
    insert or modify a few exercises,
    change one example to tie in with earlier material,
    and so on.
    Authors should *allow* this by using a Creative Commons license
    that *doesn't* include the -NC or -ND clauses.

3.  **Does the lesson's format encourage remixing?**
    "Open" isn't the same as "accessible":
    a pile of PDFs might give instructors ideas,
    but it's effectively impossible to adapt their content to local needs.
    Authors should therefore *support* remixing by making the source of the lesson available in a widely-used, editable form.
    [This doesn't have to be plain text in version control][good-enough],
    but it does have to be something that thousands of people use
    and that allows passers-by to submit suggestions, corrections, and improvements.

4.  **Is the lesson findable?**
    There's no point creating and sharing a lesson if nobody knows it's there.
    Every lesson should therefore *have metadata that search engines can find and index*.
    This emphatically does *not* mean [SCORM][scorm], [Dublin Core][dublin-core],
    or anything else that authors won't create in practice.
    It probably also doesn't mean [Harper][harper],
    but that's my best attempt at finding a balance between the needs of the machine
    and the time and energy authors actually have.

5.  **Are the lesson's learning objectives defined in verifiable ways?**
    "This lesson teaches loops" is not useful:
    it doesn't tell us whether the lesson is an introduction to loops for complete novices
    or a deep dive into loop unrolling for compiler writers.
    More importantly,
    it doesn't explain how the learner and the instructor will tell whether or not the objective was achieved.
    Authors should therefore *write lesson objectives that have one measurable or demonstrable verb*.
    [This section of *Teaching Tech Together*][t3-objectives] has discussion and examples,
    and there are many more detailed guides online.

6.  **Is the lesson's motivation clearly explained in learners' terms?**
    Formal lesson objectives frequently use terms and concepts that learners don't know yet,
    which means they're for other instructors rather than for the lesson's intended audience.
    Each lesson should therefore have *a list of authentic motivating questions*,
    where "authentic" means "things learners would actually type into a web search".

7.  **Are the lesson's requirements clearly spelled out in learners' terms?**
    Prerequisite knowledge is half the story;
    like lesson objectives,
    prerequisites should be described in verifiable ways such as,
    "You can write a `for` loop that concatenates all the strings in a list"
    rather than, "You understand `for` loops."
    Many lessons also have non-functional requirements such as access to broadband and a modern browser
    or to paywalled literature,
    or require learners to install and configure software.
    Lessons should therefore *have a list of prerequisites and requirements*
    and *describe the steps required to meet them*.
    The instructions in Jenny Bryan and Jim Hester's [Happy Git][happy-git] are a good example of content;
    [Harper][harper] has space for package requirements,
    but after some debate,
    we decided not to require step-by-step installation instructions in lesson metadata.

8.  **Does the lesson include a summary of key points and definitions?**
    The complement to verifiable learning objectives is a summary of what the lesson taught
    and the terms it introduced.
    This helps the learner check their understanding,
    and also helps them decide whether they need to go through the lesson at all.
    (If I glance at a cheat sheet and everything on it makes sense,
    I will probably move on to the next lesson.)
    Lessons should therefore *have a summary of key points*
    and *include or refer to a glossary*.

9.  **Does the lesson include timings?**
    "This section typically requires 15 minutes" and "this exercise takes 5-10 minutes"
    is valuable information for both instructors and learners.
    Lessons should therefore *include realistic times for presentations and exercises*.
    "Realistic" is crucial:
    authors should report how long it has actually taken,
    not how long they planned for it to take.
    (Doing this also reassures other instructors and learners that the lesson has actually been delivered at least once.)

10. **Does the lesson include a variety of exercises?**
    Programming isn't the only (or best) way to teach programming.
    and playing basketball isn't the best (or only) way to teach people how to play.
    Every lesson should *include exercises of several different kinds*
    to keep learners engaged and to provide a variety of feedback.
    [This post]({{site.github.url}}/2017/10/16/exercise-types.html) describes some that can be used in programming classes,
    while *[Teaching for Learning][t4l]* and *[The Discussion Book][discussion]* present many others.

[10-lesson]: https://journals.plos.org/ploscompbiol/article/authors?id=10.1371/journal.pcbi.1006915
[discussion]: https://www.wiley.com/en-ad/The+Discussion+Book%3A+50+Great+Ways+to+Get+People+Talking-p-9781119049715
[dublin-core]: http://dublincore.org/
[good-enough]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510#sec014
[happy-git]: https://happygitwithr.com/
[harper]: https://github.com/gvwilson/harper
[kerb-cuts]: https://medium.com/@mosaicofminds/the-curb-cut-effect-how-making-public-spaces-accessible-to-people-with-disabilities-helps-everyone-d69f24c58785
[scorm]: https://scorm.com/
[t3-objectives]: http://teachtogether.tech/en/process/#s:process-objectives
[t4l]: https://www.routledge.com/Teaching-for-Learning-101-Intentionally-Designed-Educational-Activities/Howell-Major-Harris-Zakrajsek/p/book/9780415699365
