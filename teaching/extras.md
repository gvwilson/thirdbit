---
layout: book
permalink: /teaching/extras.html
title: "How to Teach Programming (and Other Things): Extra Material"
---

# Extra Material

This section includes material that doesn't naturally fit anywhere else.

## How to Use This Material

This material has been taught as a multi-week online class, as a
two-day in-person class, and as a two-day class in which the learners
are in co-located groups and the instructor participates remotely.

> **Terminology**
>
> When we talk about workshops, we will try to be clear about whether
> we're discussing ones whose subject is programming, which are aimed
> at general learners, and those whose subject is how to teach, which
> are using this material.

### In-Person

In our experience, this is the most effective way to deliver an
instructor training workshop.

*   Participants are physically together for one or two days.  When they
    need to work in small groups (e.g., for practice teaching), some
    or all of them go to nearby breakout spaces.  Participants bring
    their own tablets or laptops to view and edit online material
    during the class, and use pen and paper and/or whiteboards for
    some exercises.

*   Participants use Etherpad or Google Doc for in-person training, both
    for [shared note-taking](practices.html#take-notes-together) and for
    posting exercise solutions and feedback on recorded lessons.
    Questions and discussion are done aloud.

*   Several times during the training, participants are put in groups of
    three to teach for 2-3 minutes.  The mechanics are described
    [later](performance.html#how-to-practice-teaching), and while
    participants are initially intimidated at first, they routinely
    rank it as the most useful part of the class.

### Two-Day Online With Groups

In this format, learners are in groups of 4-12, but those groups are
geographically distributed.

*   Each class uses an Etherpad or Google Doc for [shared
    note-taking](practices.html#take-notes-together), and more
    importantly for asking and answering questions: having several
    dozen people try to talk on a call works poorly, so in most
    sessions, the instructor does the talking and learners respond
    through the note-taking tool's chat.

*   Each group of learners is together in a room using one camera and
    microphone, rather than each being on the call separately. We have
    found that having good audio matters more than having good video,
    and that the better the audio, the more learners can communicate
    with the instructor and other rooms by voice rather than by using
    the Etherpad chat.

*   We do the video lecture exercise as in the two-day in-person training.

### Multi-Week Online

This was the first format we used, and we no longer recommend it.

*   We met every week or every second week for an hour via web
    conferencing. Each meeting was held twice (or even three times) to
    accommodate learners' time zones and because video conferencing
    systems can't handle 60+ people at once.

*   We used web conferencing and shared note-taking as described above
    for online group classes.

*   Learners posted homework online between classes, and commented on
    each other's work.  (In practice, comments were relatively rare:
    people seemed to prefer to discuss material in the web chats.)

*   We used a WordPress blog for the first ten rounds of training, then
    a GitHub-backed blog, and finally Piazza.  WordPress worked best:
    setting up accounts was tedious, but everything after that ran
    smoothly.  Using a GitHub blog worked so poorly that we didn't try
    it again: a third of the participants found it extremely
    frustrating, and post-publication commentary was awkward.  Piazza
    was better than GitHub, but still not as easy for participants to
    pick up as WordPress. In particular, it was hard to find things
    once there were more than a dozen homework categories.

## Key Terms

_[Educational psychology](gloss.html#educational-psychology)_ is the
study of how people learn. It touches on everything from the
neuropsychology of perception and the mechanisms of memory to the
sociology of school systems and the philosophical question of what we
actually mean by "learning" (which turns out to be pretty complicated
once you start looking beyond the standardized Western
classroom). Within the broad scope of educational psychology, two
specific perspectives have primarily influenced our teaching practices
(and by extension, this instructor training).

The first perspective is _[cognitivism](gloss.html#cognitivism)_,
which treats learning as a problem in neuropsychology. Cognitivists
focus their attention on things like pattern recognition, memory
formation, and recall. It is good at answering low-level questions,
but generally ignores larger issues like, "What do we mean by
'learning'?" and, "Who gets to decide?"

The second perspective is _[situated
learning](gloss.html#situated-learning)_, which focuses on how
_[legitimate peripheral
participation](gloss.html#legitimate-peripheral-participation)_ leads
to people becoming members of a _[community of
practice](gloss.html#community-of-practice)_.  Unpacking those terms,
the situated learning perspective focuses on the transition from being
a newcomer to being accepted as a peer by those who already do the
activity in question. Situated learning is directly relevant to our
learners, many of whom ease into scientific computing by doing small
tasks that experienced practitioners would regard as straightforward,
but who learn how to take on bigger and more novel challenges both
from what they do and from the feedback (and welcome) it elicits. It
is equally relevant to our instructors (i.e., you), who are
approaching evidence-based teaching in the same way.

For example, Software Carpentry aims to serve researchers who are
exploring data management and programming on their own (legitimate
peripheral practice) and make them aware of other people doing that
work (simply by attending the workshop) and the best practices and
ideas of that community of practice, thereby giving them a way to
become members of that community. Situated learning thus describes why
we teach, and recognizes that teaching and learning is necessarily
rooted in a social context. We then depend on the cognitivist
perspective to drive *how* we teach the specific content associated
with the community of practice.

> **Other Perspectives**
>
> There are many other perspectives outside cognitivist theory—see the
> Learning Theories site [[Learning2017](biblio.html#learning-theories)]
> for summaries. Besides cognitivism, those encountered most
> frequently include _[behaviorism](gloss.html#behaviorism)_ (which
> treats education as stimulus/response conditioning),
> _[constructivism](gloss.html#constructivism)_ (which considers
> learning an active process during which learners construct knowledge
> for themselves), and _[connectivism](gloss.html#connectivism)_ (which
> emphasizes the social aspects of learning, particularly those made
> possible by the Internet).  And yes, it would help if their names
> were less similar…

Educational psychology does not tell us how to teach on its own
because it under-constrains the problem: in real life, several
different teaching methods might be consistent with what we currently
know about how learning works. We therefore have to try those methods
in the class, with actual learners, in order to find out how well they
balance the different forces in play.

Doing this is called _[instructional
design](gloss.html#instructional-design)_.  If educational psychology is
the science, instructional design is the engineering.  For example,
there are good reasons to believe that children will learn how to read
best by starting with the sounds of letters and working up to words.
However, there are equally good reasons to believe that children will
learn best if they are taught to recognize entire simple words like
"open" and "stop", so that they can start using their knowledge
sooner.

The first approach is called "phonics", and the second, "whole
language".  The whole language approach may seem upside down, but more
than a billion people have learned to read and write Chinese and
similar ideogrammatic languages in exactly this way.  The only way to
tell which approach works best for most children, most of the time, is
to try them both out.  These studies have to be done carefully,
because so many other variables can have an impact on rules.  For
example, the teacher's enthusiasm for the teaching method may matter
more than the method itself, since children will model their teacher's
excitement for a subject.

Unsurprisingly, effective teaching depends on what the teacher knows,
which can be divided into:

*   _[content knowledge](gloss.html#content-knowledge)_, such as the
    "what" of programming;

*   _[general pedagogical
    knowledge](gloss.html#general-pedagogical-knowledge)_, i.e., an
    understanding of the psychology of learning; and

*   the _[pedagogical content
    knowledge](gloss.html#pedagogical-content-knowledge)_ (PCK) that
    connects the two. PCK is things like what examples to use when
    teaching how parameters are passed to a function, or what
    misconceptions about wildcard expansion are most common.  For
    example, an instructor could write variable names and values on
    paper plates and then stack and unstack them to show how the call
    stack works.

A great example of PCK is [[Gelman2002](biblio.html#gelman-stats)],
which is full of PCK for teaching introductory statistics.  The CS
Teaching Tips site [[Tips2017](biblio.html#cs-teaching-tips)] is
gathering similar ideas for computing.

## Myths

One [well-known scheme][wikipedia-learning-modalities] characterizes
learners as visual, auditory, or kinesthetic according to whether they
like to see things, hear things, or do things. This scheme is easy to
understand, but as de Bruyckere and colleagues point out in *Urban
Myths About Learning and Education*
[[DeBruyckere2015](biblio.html#debruyckere-urban-myths)], it is almost
certainly false.  Unfortunately, that hasn't stopped a large number of
companies from marketing products based on it to parents and school
boards.

This is not the only myth to plague education. The learning pyramid
that shows we remember 10% of what we read, 20% of what we hear, and
so on?  Myth. The idea that "brain games" can improve our
intelligence, or at least slow its decline in old age? Also a myth, as
are the claims that the Internet is making us dumber or that young
people read less than they used to.

Computing education has its own myths. Mark Guzdial's "Top 10 Myths
About Teaching Computer Science"
[[Guzdial2015a](biblio.html#guzdial-top10)] are:

1.  The lack of women in Computer Science is just like all the other
    STEM fields.

1.  To get more women in CS, we need more female CS faculty.

1.  A good CS teacher is a good lecturer.

1.  Clickers and the like are an add-on for a good teacher.

1.  Student evaluations are the best way to evaluate teaching.

1.  Good teachers personalize education for students' learning styles.

1.  High schools just can't teach CS well, so they shouldn't do it at all.

1.  The real problem is to get more CS curriculum into the hands of
    teachers.

1.  All I need to do to be a good CS teacher is model good software
    development practice, because my job is to produce excellent software
    engineers.

1.  Some people are just born to program.

The last of these is the most pervasive and most damaging.  As
discussed in [Motivation](motivation.html), Elizabeth Patitsas and others
have shown that grades in computing classes are *not* bimodal
[[Patitsas2016](biblio.html#patitsas-cs-grades)], i.e., there isn't one
group that gets it and another that doesn't. Many of the participants
in our workshops have advanced degrees in intellectually demanding
subjects, but have convinced themselves that they just don't have what
it takes to be programmers. If all we do is dispel that belief, we
will have done them a service.

## Feedback on Live Coding Demo Videos

The two lists below summarize key feedback on the two videos used
in the discussion of [live coding](live.html).

### Part 1: How Not to Do It

*   Instructor ignores a red sticky clearly visible on a learner's
    laptop.

*   Instructor is sitting, mostly looking at the laptop screen.

*   Instructor is typing commands without saying them out loud.

*   Instructor uses fancy shell prompt in the console window.

*   Instructor uses small font in not full-screen console window with
    black background.

*   The console window bottom is partially blocked by the learner's
    heads for those sitting in the back.

*   Instructor receives a a pop-up notification in the middle of the
    session.

*   Instructor makes a mistake (a typo) but simply fixes it without
    pointing it out, and redoes the command.

### Part 2: How to Do It Right

*   Instructor checks if the learner with the red sticky on her laptop
    still needs attention.

*   Instructor is standing while instructing, making eye-contact with
    participants.

*   Instructor is saying the commands out loud while typing them.

*   Instructor moves to the screen to point out details of commands or
    results.

*   Instructor simply uses `$ ` as shell prompt in the console window.

*   Instructor uses big font in wide-screen console window with white
    background.

*   The console window bottom is above the learner's heads for those
    sitting in the back.

*   Instructor makes mistake (a typo) and uses the occasion to
    illustrate how to interpret error-messages.

## Effecting Change

This guide is aimed primarily at people working in grassroots
organizations, but in order to reach and help as many people as
possible, we must find ways to work with the schools we
have. [[Henderson2011](biblio.html#henderson-facilitating)] discusses
ways to get educational institutions to change what and how they
teach; in our experience, the most important things are:

1.  *Ask, don't tell.*  Teachers know their students and their
    needs much better than you do, so start by asking what they
    think the most pressing needs are.

2.  *Find allies.* Many colleges and universities have teaching and
    learning centers whose staff are keen to improve teaching
    practices, and who also know how to navigate the local
    bureaucracy.  Similarly, there are often tech meetup groups or
    other local organizations whose members are likely helpers.

3.  *Start small.* [[Lang2016](biblio.html#lang-small-teaching)]
    describes evidence-based teaching practices that can be put in
    place with minimal effort and at low cost.  These may not have the
    most impact, but scoring a few early wins helps build support for
    larger and riskier efforts.

[[Brown2007](biblio.html#brown-bpco)] is an excellent guide to building
organizations in and for communities.  You may not need to answer all
of the questions it asks right away, but they are all worth thinking
about.

## Evaluating Impact

A key part of effecting change is to convince people that what you're
doing is having a positive impact.  That turns out to be surprisingly
hard for free-range programming workshops:

1.  *Ask learners if the workshop was useful.* Study after study has
    shown that there is no correlation between how highly learners
    rate a course and how much they actually learn
    [[Uttl2016](biblio.html#uttl-evaluations)], and most people working
    in education are now aware of that.

2.  *Give them an exam at the end of the workshop.*  Doing that
    dramatically changes the feel of the workshop, and how much they
    know at the end of the day is a poor predictor of how much they
    will remember two or three months later.

3.  *Give them an exam two or three months later.*  That's hard enough
    to do in a traditional battery-farmed learning environment; doing
    it with free-range learners is even harder.  In addition:

    *   The people who didn't get anything out of the workshop are
        probably less likely to take part in follow-up, so feedback
        gathered this way will be subject to self-selection bias.

    *   The fact that learners *remember* something doesn't
        necessarily mean it was useful (although they are more likely
        to remember things that are useful than things that aren't).

4.  *See if they keep using what they learned.* This is a good way to
    evaluate employment-oriented skills, but equally useful for things
    people have learned for fun.  The problem is how to do it: you
    probably shouldn't put spyware on their computers, and follow-up
    surveys suffer from the same low return rate and self-selection
    bias as exams.

5.  *See if they recommend the workshop to friends.* This method often
    strikes the best balance between informative and doable: if people
    are recommending your workshop to other people, that's a pretty
    good sign.

There are many other options; the most important thing is to figure
out early on how you're going to know whether you're teaching the
right things the right way, and how you're going to convince potential
backers that you're doing so.

[wikipedia-learning-modalities]: https://en.wikipedia.org/wiki/Learning_styles#Learning_modalities
