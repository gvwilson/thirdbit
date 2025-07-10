---
title: Grades
date: 2025-01-10
---

Many organizations make the mistake of focusing on outputs rather than on outcomes
[[Perri2018][Perri2018]].
In software companies,
this usually takes the form of measuring progress by the number of features added to a product
rather than by whether changes to the product are actually making people's lives easier.
The equivalent mistake in a project course is to focus on writing lots of code
instead of on what the grading scheme will actually reward,
so once you have [formed a team][forming-teams] and figured out [who's doing what][division-of-labor],
it's time to figure out how the work will be assessed.

Courses with names like "Senior Thesis Project" or "Computer Science Capstone"
generally share three characteristics [[Fincher2001][Fincher2001],[Scharlau2023][Scharlau2023]]:

1.  Learning how to work in a team is an explicit goal
    (versus courses in which
    you work in a team but are not taught how to do so).

2.  Your grade depends on how you work as well as what you build.

3.  You are supposed to work as if you were trying to meet the needs of a real customer.
    You might start with a blank sheet of paper
    or have to fix and extend an existing application,
    but you and your team are responsible for some or all of
    requirements analysis,
    design,
    implementation,
    testing,
    documentation,
    packaging,
    deployment,
    handoff,
    and review.

<div class="callout" markdown="1">
**Move along**

One goal of project courses is to move learners from left to right in
the learning model shown below.
The instructor's job is to mentor rather than to lecture;
most of the learning will take place in the team or on your own.
Putting it another way,
a project course is where your school starts treating you like a competent practitioner
rather than like a novice.

<img src="@root/files/2025/four-models-of-instruction.svg" alt="four models of instruction">
</div>

Your grade in a project course is typically based on:

The software you produce.
:   Does it build and run?
    Does it meet the customer's requirements (or the instructor's specifications if you don't have a real customer)?
    Is the source code readable?
    Is the program efficient?
    (Using an exponential algorithm instead of one that runs in linear time certainly *ought* to cost you marks…)

The process you followed.
:   Some instructors insist you use a traditional analyze-design-code-test methodology.
    Others structure the course around short sprints (typically a couple of weeks long)
    during which you refactor the application,
    extend it,
    test your changes,
    and deploy the new version.

A final report.
:   This may be a handoff report
    (i.e., documentation to help whoever inherits the software from you get up to speed),
    a summary of your experiences,
    or some combination thereof.

A final exam.
:   This may focus on the theoretical side of the course
    ("Describe the four main functions of Quality Assurance…")
    but smart instructors will include some questions to test your understanding of the project
    in order to determine who actually did the work and who was just along for the ride.

<div class="callout" markdown="1">
**Give me good news—lie if you have to**

As pointed out previously,
[time management][time-management] is harder for students than for professionals in industry
because students typically have four or five bosses who don't coordinate deadlines with each other.
Asking students to follow a particular process like waterfall or agile
is therefore functionally equivalent to asking them to lie:
they simply aren't going to be able to spend a couple of hours every day on this project
*and* meet their other commitments.
A fair grading scheme should take that into account.
</div>

Here are some of the things that students might be required to produce:

Requirements analysis
:   What the problem is, who the stakeholders are (i.e., who wants the problem
    solved), and what their needs are.

Design
:   What the user interface should look like, how data will flow through the
    system, what its major modules will be, and how they'll interact.

Application code
:   The software that will be delivered to the end user.  This is inextricably
    entangled with:

Test code
:   Coding and testing should not be separate activities: doing them
    concurrently greatly improves your project's chances of success.

Documentation
:   Human-readable explanations of the software's structure and use.  The first
    is intended for whoever inherits the software from you; the second, for its
    users.  It is almost always a mistake to try to combine the two or to write
    them as if they were going to be read by the same people.

Packaging
:   A program is a piece of software that runs for you on your machine.  A
    product is a piece of software that will run for anyone on *their* machine.
    Products take longer to build than programs: the packaging needed to let
    someone else download, install, configure, and run the program has often not
    been covered in software engineering courses, but good instructors will
    insist that you create it.

Deployment
:   These days the project's aim might not be to create something that can be
    downloaded and installed.  Instead, its aim might be to create a web site or
    web service or make something else directly available to users.  Like
    packaging, deployment can be a major development issue in its own right, and
    the effort required to do it is almost always underestimated.

Handoff
:   If you don't put effort into passing the project on to whoever comes after
    you, your hard work will almost certainly count for nought.  While it isn't
    usual for undergraduate projects to be handed on from one term to another,
    some courses require teams to swap code mid-term.  If this happens,
    instructors may grade you on how complete and up-to-date your wiki pages,
    bug database, and build scripts are at the time of handoff.

Review
:   The only way to get better at something is to reflect on how you've done and
    what you could have done better.  Every project should therefore end with a
    postmortem in which team members talk about what went right and what went
    wrong.  As mentioned earlier, this may then be the subject of the final
    report.

It's a long list,
and in my experience it isn't practical to try to grade all of these,
since you wind up with things being worth just a few percent of the overall result.
In the past,
students have found something more granular works better:

Warmup exercise (0%)
:   The warmup exercise takes up the first week; its purpose is to give students a
    chance to familiarize themselves with the problem domain, tools, and
    software they'll be using for the rest of the term, and to propose a grading
    scheme for the rest of their work. This exercise isn't graded in itself,
    but lays the foundation for everything that is.

Code (20%)
:   Yes, that's right: the code is only worth 20% of the final grade, even
    though it's where students spend the bulk of their time.  I do this because
    (1) if you don't know how to program you shouldn't be in this course and (2)
    if you don't create some code you can't test, do a demo, or write your final
    report.

Testing (20%)
:   Testing is just as important as coding, so it's given the same weight.
    Note, though, that only automated tests count: if I can't check the project
    out of version control and re-run the tests (possibly after editing a
    configuration file) then as far as I'm concerned, the code hasn't been
    tested.

Demos (20%)
:   I used to require students to prepare a 20-minute lecture on a topic of
    their choosing and deliver it to their coursemates or a junior class.  It
    was a valuable experience, but it ate up a lot of time, so I switched to
    having students do 10-minute demos instead.  I usually give students two
    shots at this: one after which their peers give them feedback, and a second
    that's actually graded.  This is valuable practice for job interviews and a
    good reality check on how much progress has actually been made.

Teamwork (20%)
:   Everyone starts with 10 out of 10; marks come off if you always do your work
    at the last moment, check in code that breaks the build, or are
    disrespectful.

Final state of project (20%)
:   Most of my projects carry forward from term to term and team to team, so I
    award one fifth of the overall mark based on the state each team leaves the
    project in.  Does everything build?  Have issues been filed for all known
    bug?  Does the README explain how to install the code, and do those
    instructions actually work?

[Fincher2001]: https://isbnsearch.org/isbn/9781852333577
[Perri2018]: https://isbnsearch.org/isbn/9781491973790
[Scharlau2023]: https://leanpub.com/teachingteamcollaboration
[Spinellis2007]: https://doi.org/10.1109/MS.2007.121
[division-of-labor]: @root/2025/01/08/division-of-labor/
[forming-teams]: @root/2025/01/07/forming-teams/
[time-management]: @root/2025/01/03/time-management/
