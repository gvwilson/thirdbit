---
title: "Making Maintainable Lessons"
date: 2017-10-21 11:00:00
year: 2017
---

Good courses take a lot of effort to build, but building them is only half the
battle. If you have a hundred courses, you have more than a hundred combinations
of data, code, and explanation to maintain.  To manage all of this, we can
borrow ideas from open source software development, article curation on
Wikipedia, [Software Carpentry][swc], and other sources.

But what exactly does "maintainable" mean?  The short answer is that a
course is maintainable if it's cheaper to update it than to replace
it. This equation depends on many factors, only some of which are
under our control:

1. *How well documented the course's design is.* If the person doing maintenance
   doesn't know (or doesn't remember) what the course is supposed to accomplish
   or why topics are introduced in a particular order, it will take her more
   time to update it.  I have therefore started experimenting with a lightweight
   template to capture decisions about why each course is the way it is.

2. *How the course's content is structured.* Version control is the
   secret sauce that allows software development to scale, but today's
   version control systems (still) can't handle widely-used file
   formats like Word and PowerPoint.  We therefore use text formats
   like Markdown, and are working on support for widely-used tools
   like the [Jupyter Notebook][jupyter].

3. *Who the audience actually is.* Up-to-date information on the demographics of
   current students helps instructors focus on making the changes that will
   matter, and skip over ones that won't. Going forward, it will be just as
   important to provide data on the audience we *want* to have, their needs, and
   their constraints.

4. *How the audience is using the course.* Online teaching makes it easy to tell
   which exercises learners get wrong most often, but knowing that doesn't tell
   us why, or what changes would make a particular explanation more
   effective. Most platforms have had a "send feedback" button since day one;
   the next step is to involve learners more directly in the course improvement
   process.

5. *How much our platform has changed.* We are constantly improving
   our platform to provide the best learning experience possible, but
   each improvement introduces the risk that old courses will either
   need to be updated to continue running, or *should* be updated
   because it's now possible to deliver their content in better
   ways. Here, we can reduce maintenance costs by re-testing courses
   automatically to detect breakages, and keep our platform
   backward-compatible for as long as possible, but the long-term
   solution is better introductory and update tutorials for our
   instructors.

6. *How much we know about how to teach.* Online instruction's roots
   [go back decades][teaching-machine], but new technologies really do
   change what's possible.  Each time we help our instructors create a
   course, we learn more about how the next set of courses should be
   created.  In the long run, we would like something like [this
   catalog of exercises types][exercise-types]; for now, our priority
   is to develop ways for instructors to share their insights with
   each other without increasing the burden on them.

[This upcoming paper][collab-lesson] describes some approaches we hope
to learn from; if you know of others, please point us at them.

[collab-lesson]: https://arxiv.org/abs/1707.02662
[exercise-types]: http://third-bit.com/2017/10/16/exercise-types/
[jupyter]: https://jupyter.org/
[swc]: https://software-carpentry.org
[teaching-machine]: http://teachingmachin.es/timeline.html
