---
layout: teaching
permalink: /teaching/performance.html
title: "How to Teach Programming (and Other Things): Teaching as a Performance Art"
---

# Teaching as a Performance Art

**Objectives**

* **Learners can define *jugyokenkyu* and lateral knowledge transfer
  and explain their relationship to each other.**
* **Learners can describe and enact at least three techniques for
  giving and receiving feedback on teaching performance.**
* **Learners can explain at least two ways in which using a rubric
  makes feedback more effective.**

Many people assume that teachers are born, not made. From politicians
to researchers and teachers themselves, reformers have designed
systems to find and promote those who can teach and eliminate those
who can't. But as Elizabeth Green explains
[[Green2014](biblio.html#green-babt)], that assumption is wrong, which is
why educational reforms based on it have repeatedly failed.

The book is written as a history of the people who have put that
puzzle together in the US. Its core begins with a discussion of what
James Stigler discovered during a visit to Japan in the early 1990s:

> Some American teachers called their pattern "I, We, You": After
> checking homework, teachers announced the day's topic, demonstrating
> a new procedure (I)… Then they led the class in trying out a
> sample problem together (We)… Finally, they let students work
> through similar problems on their own, usually by silently making
> their way through a worksheet (You)…
>
> The Japanese teachers, meanwhile, turned "I, We, You" inside
> out. You might call their version "You, Y'all, We." They began not
> with an introduction, but a single problem that students spent ten
> or twenty minutes working through alone (You)… While the
> students worked, the teacher wove through the students' desks,
> studying what they came up with and taking notes to remember who had
> which idea. Sometimes the teacher then deployed the students to
> discuss the problem in small groups (Y'all). Next, the teacher
> brought them back to the whole group, asking students to present
> their different ideas for how to solve the problem on the
> chalkboard… Finally, the teacher led a discussion, guiding
> students to a shared conclusion (We).

It's tempting but wrong to think that this particular teaching
technique is some kind of secret sauce. The actual key is a practice
called _[jugyokenkyu](gloss.html#jugyokenkyu)_, which means "lesson
study":

> *Jugyokenkyu* is a bucket of practices that Japanese teachers use to
> hone their craft, from observing each other at work to discussing
> the lesson afterward to studying curriculum materials with
> colleagues. The practice is so pervasive in Japanese schools that it
> is…effectively invisible.
>
> In order to graduate, [Japanese] education majors not only had to
> watch their assigned master teacher work, they had to effectively
> replace him, installing themselves in his classroom first as
> observers and then, by the third week, as a wobbly…approximation of
> the teacher himself.  It worked like a kind of teaching relay. Each
> trainee took a subject, planning five days' worth of lessons… [and
> then] each took a day. To pass the baton, you had to teach a day's
> lesson in every single subject: the one you planned and the four you
> did not… and you had to do it right under your master teacher's
> nose. Afterward, everyone–the teacher, the college students, and
> sometimes even another outside observer–would sit around a formal
> table to talk about what they saw.

Putting work under a microscope in order to improve it is commonplace
in sports and music.  A professional musician, for example, will
dissect half a dozen different recordings of "Body and Soul" or
"Smells Like Teen Spirit" before performing it. They would also expect
to get feedback from fellow musicians during practice and after
performances.  Many other disciplines work this way too: the Japanese
drew inspiration from [Deming's ideas on continuous improvement in
manufacturing][wikipedia-deming], while the adoption of code review
over the last 15 years has done more to improve everyday programming
than any number of books or websites.

But this kind of feedback isn't part of teaching culture in the US,
the UK, Canada, or Australia.  There, what happens in the classroom
stays in the classroom: teachers don't watch each other's lessons on a
regular basis, so they can't borrow each other's good ideas. The
result is that *every teacher has to invent teaching on their
own*. They may get lesson plans and assignments from colleagues, the
school board, a textbook publisher, or the Internet, but each teacher
has to figure out on their own how to combine that with the theory
they've learned in education school to deliver an actual lesson in an
actual classroom for actual students.

Demonstration lessons, in which one teacher is in front of a room full
of students while other teachers observe, seem like a way to solve
this.  However, Fincher and her colleagues studied how teaching
practices are actually transferred using both a detailed case study
[[Fincher2007](biblio.html#fincher-warrens-questions)] and analysis of
change stories [[Fincher2012](biblio.html#fincher-stories-change)].  The
abstract of the latter paper sums up their findings:

> Innovative tools and teaching practices often fail to be adopted by
> educators in the field, despite evidence of their effectiveness.
> Naïve models of educational change assume this lack of adoption
> arises from failure to properly disseminate promising work, but
> evidence suggests that dissemination via publication is simply not
> effective… We asked educators to describe changes they had made to
> their teaching practice… Of the 99 change stories analyzed, only
> three demonstrate an active search for new practices or materials on
> the part of teachers, and published materials were consulted in just
> eight… Most of the changes occurred locally, without input from
> outside sources, or involved only personal interaction with other
> educators.

<!--| \noindent |-->
Barker et al found something similar
[[Barker2015](biblio.html#barker-practice-adoption)]:

> Adoption is not a "rational action," however, but an iterative
> series of decisions made in a social context, relying on normative
> traditions, social cueing, and emotional or intuitive processes…
> Faculty are not likely to use educational research findings as the
> basis for adoption decisions… Positive student feedback is taken as
> strong evidence by faculty that they should continue a practice.

This phenomenon is sometimes called _[lateral knowledge
transfer](gloss.html#lateral-knowledge-transfer)_: someone sets out to
teach X, but while watching them, their audience actually learns Y as
well (or instead). For example, an instructor might set out to show
people how to do a particular statistical analysis in R, but what her
learners might take away is some new keyboard shortcuts in RStudio.
Live coding makes this much more likely because it allows learners to
see the "how" as well as the "what", and *jugyokenkyu* works because
it creates more opportunities for this to happen.

## Feedback

As the cartoon below suggests, sometimes it can be hard to receive
feedback, especially negative feedback.  The process is easier and
more productive when the people involved share ground rules and
expectations. This is especially important when they have different
backgrounds or cultural expectations about what's appropriate to say
and what isn't.

![Feedback Feelings (copyright (c) Deathbulge 2013)](fig/deathbulge-jerk.jpg)

You can get better feedback on your work from other people using
techniques like these:

1.  *Initiate feedback.* It's better to ask for feedback than to
    receive it unwillingly.

2.  *Choose your own questions*, i.e., ask for specific
    feedback. It's a lot harder for someone to answer, "What do you
    think?" than to answer either, "What is one thing I could have
    done as an instructor to make this lesson more effective?"  or "If
    you could pick one thing from the lesson to go over again, what
    would it be?"

    Directing feedback like this is also more helpful to you.  It's
    always better to try to fix one thing at once than to change
    everything and hope it's for the better.  Directing feedback at
    something you have chosen to work on helps you stay focused, which
    in turn increases the odds that you'll see progress.

3.  *Use a feedback translator.* Have a fellow instructor (or other
    trusted person in the room) read over all the feedback and give an
    executive summary. It can be easier to hear "It sounds like most
    people are following, so you could speed up" than to read several
    notes all saying, "this is too slow" or "this is boring".

4.  Most importantly, *be kind to yourself*.  Many of us are very
    critical of ourselves, so it's always helpful to jot down what we
    thought of ourselves *before* getting feedback from others.
    That allows us to compare what we think of our performance with what
    others think, which in turn allows us to scale the former more
    accurately.  For example, it's very common for people to think that
    they're saying "um" and "err" all the time, when their audience
    doesn't notice it.  Getting that feedback once allows instructors to
    adjust their assessment of themselves the next time they feel that
    way.

<!--| \newpage |-->

You can give feedback to others more effectively as well:

1.  *Balance positive and negative feedback.* One method is a
    "compliment sandwich" made up of one positive, one negative, and
    a second positive observation.

2.  *Organize your feedback using a rubric.* Most people are more
    comfortable giving and receiving feedback when they feel that they
    understand the social rules governing what they are allowed to say
    and how they are allowed to say it.  A facilitator can then
    transcribe items into a shared document (or onto a whiteboard)
    during discussion.

> **Two by Two**
>
> The rubric we find most useful for feedback on teaching is a 2x2
> grid whose vertical axis is labelled "positive" and "negative", and
> whose horizontal axis is labelled "content" (what was said) and
> "presentation" (how it was said).  Observers write each of their
> comments in one of the grid's four squares as they are watching the
> demonstration.

Whatever methods are used, the most important thing to remember is
feedback on teaching is meant to be formative: its goal is to help
people figure out what they are doing well and what they still need to
work on.

> **Studio Classes**
> 
> Architecture schools often include studio classes, in which students
> solve small design problems and get feedback from their peers right
> then and there.  These classes are most effective when the
> instructor critiques both the designs and the peer critiques, so
> that participants are learning not only how to make buildings, but
> how to give and get feedback
> [[Schön1984](biblio.html#schon-practitioner)].  Master classes in music
> serve a similar purpose, and a few people have experimented with
> using live coding at conferences or online in similar ways.

<!-- comment needed to separate blockquotes -->

> **Tells**
> 
> Everyone has nervous habits. For example, many of us become "Mickey
> Mouse" versions of ourselves when we're nervous, i.e., we talk more
> rapidly than usual, in a higher-pitched voice, and wave our arms
> around more than we usually would.
> 
> Gamblers call nervous habits like this "tells".  While these are
> often not as noticeable as you would think, it's good to know
> whether you pace, fiddle with your hair, look at your shoes, or
> rattle the change in your pocket when you don't know the answer
> to a question.
>
> You can't get rid of tells completely, and trying to do so can make
> you obsess about them.  A better strategy is to try to displace
> them, e.g., to train yourself to scrunch your toes inside your shoes
> instead of cracking your knuckles.

If you are interested in knowing more about giving and getting
feedback, you may want to read
[[Gormally2014](biblio.html#gormally-teaching-feedback)] and discuss ways
you could make peer-to-peer feedback a routine part of your teaching.
You may also enjoy [[Gawande2011](biblio.html#gawande-personal-best)],
which looks at the value of having a coach.

## How to Practice Teaching

One of the key elements of instructor training is recording trainees
and having them, and their peers, critique those recordings. We were
introduced to this practice by UBC's Warren Code, who got it from the
Instructional Skills Workshop [[ISW2017](biblio.html#isw-resources)],
and it has evolved to the following:

1.  Split into groups of three.

2.  Each person rotates through the roles of instructor, audience, and
    videographer.  As the instructor, they have two minutes to explain
    one key idea from their research (or other work) as if they were
    talking to a class of interested high school students. The person
    pretending to be the audience is there to be attentive, while the
    videographer records the session using a cellphone or similar
    device.

3.  After everyone in the group of three has finished teaching, watch the
    videos as a group. Everyone gives feedback on all three videos, i.e.,
    people give feedback on themselves as well as on others.

5.  After everyone has given feedback on all of the videos, return to the
    main group and put all of the feedback into the notes.  Again, try to
    divide positive from negative and content from presentation.  Try
    also to identify each person's tells: what do they do that betrays
    nervousness, and how noticeable is it?

It's important to record all three videos and then watch all three: if
the cycle is teach-review-teach-review, the last person to teach runs
out of time. Doing all the reviewing after all the teaching also helps
put a bit of distance between the teaching and the reviewing, which
makes the exercise slightly less excruciating.

In order for this exercise to work well:

*   Let people know at the start of the class that they will be asked to
    teach something so that they have time to choose a topic.  (In our
    experience, telling them this in advance of the class can be
    counter-productive, since some people will fret over how much they
    should prepare.)

*   Groups must be physically separated to reduce audio cross-talk
    between their recordings. In practice, this means 2-3 groups in a
    normal-sized classroom, with the rest using nearby breakout spaces,
    coffee lounges, offices, or (on one occasion) a janitor's storage
    closet.

*   People must give feedback on themselves, as well as giving feedback
    on each other, so that they can calibrate their impressions of their
    own teaching according to the impressions of other people. (We find
    that most people are harder on themselves than others are, and it's
    important for them to realize this.)

*   Try to make at least one mistake during the demonstration of live
    coding so that trainees can see you talk through diagnosis and
    recovery, and draw attention afterward to the fact that you did
    this.

The announcement of this exercise is often greeted with groans and
apprehension, since few people enjoy seeing or hearing themselves.
However, it is consistently rated as one of the most valuable parts of
the class, and also serves as an ice breaker: we want pairs of
instructors at actual workshops to give one another feedback, and
that's much easier to do once they've had some practice and have a
rubric to follow.

> **Setting Up Your Teaching Environment**
>
> If the room setup allows it, try to [set up your
> environment](practices.html#setting-up-your-own-environment) to mimic
> what you would use in an actual classroom: have a glass of water
> handy, stand instead of sitting, and so on.

## Challenges

### Give Feedback (20 minutes)

1.  Watch [[Wilson2016](biblio.html#wilson-bad-teaching-live)] as a
    group and give feedback on it. Organize feedback along two axes:
    positive vs. negative and content vs. presentation.

2.  Have each person in the class add one point to a 2x2 grid on a
    whiteboard (or in the shared notes) without duplicating any points
    that are already up there.

What did other people see that you missed?  What did they think that
you strongly agree or disagree with?

### Practice Giving Feedback (45 minutes)

Use the process described above to practice teaching in groups of
three.  When your group is done, the instructor will add one point of
feedback from each participant to a 2x2 grid on the whiteboard or in
the shared notes, without accepting duplicates.  Participants should
not say whether the point they offer was made by them, about them, or
neither: the goal at this stage is primarily for people to become
comfortable with giving and receiving feedback, and to establish a
consensus about what sorts of things to look for.

[wikipedia-deming]: https://en.wikipedia.org/wiki/W._Edwards_Deming
