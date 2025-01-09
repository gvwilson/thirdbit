---
title: Thinking
---

We know as much about teaching and learning as we do about public health. The
problem is, while university professors are experts in their own fields, many of
them don't know what we know.  Most people in the tech industry don't either,
which means many of us learn more slowly and less reliably than we could.  This
chapter will give you a short overview of a few key facts that can help fix
that.

## Different Kinds of Learners

Research starting in the 1980s showed that most neurotypical[%i "neurotypical" %] adults undergo a series of fairly
predictable [%g cognitive_transition "cognitive transitions" %][%i "cognitive transition" %] on their way from being a novice to being an expert in any
domain [%b Benner2000 %]. (We say "most" and "neurotypical" because as
with anything involving people, there will be outliers.)

For our purposes, we will say that people are [%g novice "novices" %][%i "novice" %], [%g competent_practitioner "competent practitioners" %][%i "competent practitioner" %], or [%g expert "experts" %][%i "expert" %]. Some characteristics that most novices share include
doing things by rote (i.e., following a series of steps without understanding
why they work), asking questions that don't make sense ("What color is the
database?") and not being able to tell what is and isn't relevant—for example,
using their own filenames or variable names when searching for help online
because they don't yet have a clear distinction between what belongs to the
library and application and what is specific to their code.

What ties these things together is that novices don't have a mental model[%i "mental model" %] of the problem. A mental
model is a simplified representation of something that's good enough for present
needs. One example is the ball-and-spring models used to represent molecules in
chemistry classes: real atoms aren't marbles and atomic bonds aren't springs,
but this model is good enough to explain why burning methane produces carbon
dioxide and water and a host of other things.

What about experts? They can typically solve problems at a glance, and are
usually much better at debugging than competent practitioners because they are
better able to reason backward from effects to causes. They also tend to be
*less* good as teachers because of [%g expert_blind_spot "expert blind spot" %][%i "expert blind spot" %]: they know their subject so well that they've
forgotten how hard it is for newcomers.

To explain where these differences come from, imagine that the knowledge in your
brain is stored as a graph in which ideas are nodes and the connections between
them are arcs. (Your brain doesn't actually work this way, but it's a useful
metaphor.) A novice's mental model is disconnected: some key facts are missing,
and other pieces don't join up ([%f thinking-models %]). In contrast,
a competent practitioner's mental model is fully connected: given fact `A`, he
can reason his way through `B` and `C` to solution `D`. He might take a wrong
turn to `Y` and `Z` along the way and have to backtrack, but he'll get there
eventually.

What makes an expert different isn't that she has more facts (though she usually
does). What makes the difference is that she has many more connections, so the
distance between any two ideas in her head is usually much less. In fact, in
many cases the problem and its solution will be directly connected so that she
can go from one to the other in a single step. This is what we mean by expert
intuition: rather than *reasoning* their way through problems, they *recognize*
them in the same way that most people recognize human faces. Being able to do
this explains why they can solve problems at a glance, but also why they have
trouble explaining their thinking: they can't tell someone else how they did it
any more than we can explain how we recognize faces.

[% figure
   slug="thinking-models"
   img="thinking-models.svg"
   alt="Mental models"
   caption="The differences between novice, competent, and expert mental models."
%]

<div class="callout" markdown="1">
### Learning styles aren't a thing

You may have heard of "learning styles[%i "learning styles" "pseudoscience!learning
styles" %]", i.e., that some people learn better visually,
while others do so more quickly or more accurately by listening, reading, or
otherwise using language. It's bullshit: while lots of companies make and sell
materials based on this myth, no one has ever shown that tuning what or how we
teach to match people's preferences has any impact on outcomes
[%b DeBruyckere2015 %]. Like Myers-Briggs personality types[%i "Myers-Briggs Type
Indicator" %] ([%x fairness %]),
learning styles belong with healing crystals and astrology.

</div>

This model of learning leaves almost everything discussed in
[%b Kirschner2018 %] and other recent work, but is good enough to start
with.  Novices, competent practitioners, and experts are at different stages of
cognitive development, so they need different kinds of teaching
[%b Kalyuga2003 %]. Novices need to be told what to learn next: since they
don't have yet a mental model of the problem, they don't know what to ask for.
As [%b Kirschner2006 %] and many others have shown, discovery-based learning[%i "discovery-based learning" %] in which people are
told "go figure out how to solve this problem" is less effective for novices
than guided learning because they don't know what to ask next.

Once someone is a competent practitioner, though, being told step-by-step what
to tackle next is both unnecessary and frustrating.  Competent practitioners
should be mentored[%i "mentoring" %] instead of lectured: they should
tackle problems on their own, but have someone at hand to get them unstuck if it
takes them more than a few minutes to figure out what to do next.

Finally, the most effective way to "teach" experts is to have them reflect or
introspect[%i "introspection" %] on their own practice
[%b Schon1984 %]. This usually happens in three stages:

1.  You do some work and get feedback on it.  For example, someone in grade
    school might write an essay about what they did with their summer holiday
    and get feedback from the teacher on their spelling, grammar, and structure.

2.  You give feedback on other people's work and get feedback *on your
    feedback*. This is what most literature courses are about: instead of
    writing new material, people learn how to critique and analyze things.

3.  Once you know how to critique things, you can start to critique your own
    work as you produce it. This is the tightest feedback loop there can be, and
    people who reach this stage start to see continuous improvement in their
    work as a result.

## Formative Assessment

Suppose you are teaching a child how to do addition and you give them this
multiple-choice question:

> What is 37 + 45?
>
> - 82
> - 72
> - 712
> - 73

If they pick the first answer, it shows they know how to add multi-digit
numbers. If they pick the second, it signals that they don't know how to carry:
they add 7 and 5 to get 12, throw away the 1, and then add 3 and 4 to get 7.
(Alternatively, they might write down 12 and then write the 7 on top of the 1.)

If they pick 712 it also signals that they don't understand how to carry, but
it's a different kind of error: instead of throwing away the 1 or overwriting
it, they're treating the problem as two parallel single-digit problems. As for
73, it's a sign that they've learned that they're supposed to add the 1 from 12,
but they're adding it back into the ones column instead of carrying it over to
the tens column.

Each of these wrong answers has [%g diagnostic_power "diagnostic power" %][%i "diagnostic power (of formative assessment)" %]. Like a good unit test, this
multiple choice question doesn't just tell us that something is wrong: it points
us at the source of the problem. Using questions like these in class in order to
diagnose misunderstandings so that they can be corrected is called [%g formative_assessment "formative assessment" %][%i "formative assessment" %]
because it forms (or shapes) the learning as it is taking place.

A good formative assessment question takes 30--60 seconds to do (so that it
doesn't disrupt the flow of the lesson) and has an unambiguous right answer (so
that it scales—if the answers are paragraphs long, it won't be practical to
use in a class of 20 students, much less 200). The most important thing, though,
is that it tells the instructor what to say next. Different learners can
misunderstand things in different ways; a good formative assessment tells the
instructor what misconceptions these particular learners have and therefore what
needs to be corrected.

<div class="callout" markdown="1">
### Recordings can't respond

If an instructor uses a formative assessment in class and then says whatever
they planned to say next instead of responding to the learner's actual
misunderstandings, they're not a good teacher. Unfortunately, that is what
almost all recorded videos do: they always say the same next thing regardless of
what the viewer did or didn't understand.  Good video games provide many paths
around or through each obstacle; recorded courses could in theory do that too,
but in practice the cost is prohibitive.

</div>

Formative assessments have many other benefits. One is that in order to come up
with good ones, the instructor has to build a mental model of all the ways in
which the learner's mental model might be wrong. Doing this helps them write a
better lesson, in the same way that if you think about how your program might
fail you'll write code that prevents or handles those potential failures.

Another benefit is that formative assessments tell the learners what they do and
don't actually understand. It's common for someone to come out of a lesson
believing that they've grasped the key ideas, only to discover when they to do
homework that they didn't understand after all. Formative assessment on its own
won't fill in the gaps in their knowledge, but at least they'll know what they
do and don't actually understand.

Finally, formative assessments can be used pre-emptively. I once had a professor
start a math class by putting up a multiple choice question. It was pretty
easy—I think everyone in the class got it—so he said, "All right, here's
twenty minutes of your life I don't need to waste," and set aside a section of
his slides. He then did it again, and again, enough of us got it right that he
said, "Here's another twenty minutes of your life I don't have to waste," and
set aside the second chunk of slides. It wasn't until his third question that
enough of us were wrong that he started lecturing. He did that with every topic
in the course, and it was great: it meant he wasn't wasting time telling us
things we already knew, which meant he had more time for helping us understand
the things we didn't.

## Cognitive Load

[% figure
   slug="thinking-cognitive-architecture"
   img="cognitive-architecture.svg"
   alt="Cognitive architecture"
   caption="The cognitive architecture of the human mind (simplified)."
%]

[%f thinking-cognitive-architecture %] shows a very (very) simple model of
the cognitive architecture of the human brain. On the left is [%g long_term_memory "long-term memory" %][%i "long-term memory" %] (LTM), which
is where you store things like the spelling of your name and how that awful
clown scared you when you were ten years old. It is very large—you can keep
adding to it as long as you live—but you don't have direct conscious access to
it.

Instead, evolution has given you a second subsystem called [%g short_term_memory "short-term memory" %][%i "short-term memory" %] (STM) or
[%g working_memory "working memory" %][%i "working memory" %]. (More
sophisticated models distinguish between these two concepts, but this simple
model is good enough for our needs.)  You are constantly fetching things from
LTM into STM to use them, then re-encoding them and writing them back to LTM.
This is one of the differences between your brain and a computer: reading data
from a hard drive doesn't alter it, but every time you access something in LTM,
you may write it back in a different or augmented form. We call this "learning".

Here's the problem: STM is
very small[%i "short-term memory!limited capacity of" %].  [%b Miller1956 %] famously estimated that it could
hold 7±2 things at one time; more modern estimates put the number closer to 4±1
[%b Didau2016 %]. This means that STM is a bottleneck for learning: if too
many new ideas are presented too quickly, the new arrivals will knock older ones
out of STM before you have a chance to encode them and store them in LTM, so
learning won't take place.

This realization and others have produced the theory of [%g cognitive_load "cognitive load" %][%i "cognitive load theory" %], which (among other things)
divides the things you have to do while learning into three categories. The
[%g intrinsic_load "intrinsic load" %][%i "intrinsic load" "cognitive load!intrinsic" %] is the thinking that is required by the learning task itself. The
[%g germane_load "germane" %][%i "germane load" "cognitive load!germane" %]
(or relevant) load is the other thinking that the problem requires, but which
isn't the focus of the lesson, while the [%g extraneous_load "extraneous load" %][%i "extraneous load" "cognitive load!extraneous" %] is everything you're
being asked to do that is irrelevant.

For example, suppose you are learning the grammar of Frisian. If I ask you to
translate, "How is her knee today?" then the intrinsic load is the rules of
grammar, but there is also the germane load of recalling vocabulary (which is
necessary, but isn't the main focus of the lesson). If, on the other hand, I
give you the words as shown in [%f thinking-frisian %] and ask you to
rearrange them, I have eliminated the germane load, but have added some
extraneous load by using a mix of fonts. You will solve the problem more quickly
and more accurately if the words are all in the same font, no matter what that
font is, than you will if your brain is wondering whether the difference is
significant.

[% figure
   slug="thinking-frisian"
   img="thinking-frisian.svg"
   alt="Translating a sentence"
   caption="Reducing germane load while increasing extraneous load."
%]

Cognitive load theory explains why tools like [Scratch][scratch][%i "Scratch" %] work so well: they reduce germane load by
getting rid of the commas, curly braces, and other distractions so that learners
can focus on mastering concepts like assignment and loops. It also explains why
working with code written in a mix of styles is so painful: each minor
difference adds extraneous load.

In order to handle larger sets of information, our minds create [%g chunking "chunks" %][%i "chunking" "short-term memory!chunking" %] that only
take up one slot in STM.  For example, most of us remember words as single items
rather than as sequences of letters.  Similarly, the pattern made by five spots
on cards or dice is remembered as a whole rather than as five separate pieces of
information.

Experts have more and larger chunks than non-experts, i.e., experts "see" larger
patterns and have more patterns to match things against.  This allows them to
reason at a higher level and to search for information more quickly and more
accurately.  However, chunking can also mislead us if we mis-identify things:
newcomers really can sometimes see things that experts have looked at and
missed.

Given how important chunking is to thinking, it is tempting to try to teach
design patterns directly to learners as early as possible.  These patterns help
competent practitioners think and talk to each other in many domains, but
pattern catalogs are too dry and too abstract for novices to make sense of on
their own.  However, giving names to a small number of patterns does seem to
help, primarily by giving the learners a richer vocabulary to think and
communicate with [%b Sajaniemi2006 %].

## Learning Strategies

All of this leads to six strategies[%i "learning strategies" %] that
have been proven to help people learn faster and better
[%b Weinstein2018 %].  While researchers still disagree on *why* they
work, everyone now agrees that they *do*.

Spaced practice[%i "spaced practice" "learning strategies!spaced practice" %].
:   Ten hours of study spread out over five days is more effective than two
    five-hour days, and far better than one ten-hour day.  You should therefore
    create a study schedule that spreads study activities over time: block off
    at least half an hour to study each topic each day rather than trying to
    cram everything in the night before an exam [%b Kang2016 %].

    You should also review material after each class, but not immediately
    after—take at least a half-hour break.  Doing this also helps you catch
    any gaps or mistakes in previous sets of notes while there's still time to
    correct them or ask questions.

Retrieval practice[%i "retrieval practice" "learning strategies!retrieval practice" %].
:   The limiting factor for long-term memory is not retention (what is stored)
    but recall (what can be accessed).  Recall of specific information improves
    with practice, so outcomes in real situations can be improved by taking
    practice tests or summarizing the details of a topic from memory and then
    checking what was and wasn't remembered.

    Recall is better when practice uses activities similar to those used in
    testing.  For example, writing personal journal entries helps with
    multiple-choice quizzes, but less than doing practice quizzes.  One way to
    exercise retrieval skills is to solve problems twice.  The first time, do it
    entirely from memory without notes or discussion with peers.  After grading
    your own work against a rubric supplied by the teacher, solve the problem
    again using whatever resources you want.  The difference between the two
    shows you how well you were able to retrieve and apply knowledge.

    Another method is to create flash cards.  Physical cards have a question or
    other prompt on one side and the answer on the other, and many flash card
    apps are available for phones.  If you are studying as part of a group,
    swapping flash cards with a partner helps you discover important ideas that
    you may have missed or misunderstood.

Interleaving[%i "interleaving" "learning strategies!interleaving" %].
:   One way you can space your practice is to interleave study of different
    topics: instead of mastering one subject, then a second and third, shuffle
    study sessions.  Even better, switch up the order: `A-B-C-B-A-C` is better
    than `A-B-C-A-B-C`, which in turn is better than `A-A-B-B-C-C`
    [%b Rohrer2015 %].  This works because interleaving fosters creation
    of more links between different topics, which in turn improves recall.
    Interleaving study will initially feel harder than focusing on one topic at
    a time, but that's a sign that it's working.  If you are using flash cards
    or practice tests to gauge your progress, you should see improvement after
    only a couple of days.

Elaboration[%i "elaboration" "learning strategies!elaboration" %].
:   Explaining things to yourself as you go through them helps you understand
    and remember them.  One way to do this is to follow up each answer on a
    practice quiz with an explanation of why that answer is correct, or
    conversely with an explanation of why some other plausible answer isn't.
    Another is to tell yourself how a new idea is similar to or different from
    one you have seen previously.

    Talking to yourself may seem like an odd way to study, but
    [%b Bielaczyc1995 %] found that people trained in self-explanation
    outperformed those who hadn't been trained.  Similarly, [%b Chi1989 %]
    found that some learners simply halt when they hit a step they don't
    understand when trying to solve problems.  Others pause and generate an
    explanation of what's going on, and the latter group learns faster.  An
    exercise to build this skill is to go through an example program line by
    line with a class, having a different person explain each line in turn and
    say why it is there and what it accomplishes.

    Note-taking[%i "note-taking (as a learning strategy)" %] is a form
    of real-time elaboration: it forces you to organize and reflect on material
    as it's coming in, which in turn increases the likelihood that you will
    transfer it to long-term memory.  Many studies have shown that taking notes
    while learning improves retention [%b Aiken1975 Bohay2011 %].

Concrete examples[%i "concrete examples" "learning strategies!concrete examples" %].
:   One particularly useful form of elaboration is the use of concrete examples.
    Whenever you have a statement of a general principle, try to provide one or
    more examples of its use, or conversely take each particular problem and
    list the general principles it embodies.  [%b Rawson2014 %] found that
    interleaving examples and definitions like this made it more likely that
    learners would remember the latter correctly.

    One structured way to do this is the ADEPT method: give an analogy, draw a
    diagram, present an example, describe the idea in plain language, and then
    give the technical details.  Again, if you are studying with a partner or in
    a group, you can swap and check work: see if you agree that other people's
    examples actually embody the principle being discussed or which principles
    are used in an example that they haven't listed.

Dual coding[%i "dual coding" "learning strategies!dual coding" %].
:   Different subsystems in our brains handle and store linguistic and visual
    information, so if complementary information is presented through both
    channels, they can reinforce one another.  However, learning is less
    effective when the same information is presented simultaneously in two
    different channels, because then the brain has to expend effort to check the
    channels against each other [%b Mayer2009 %].

    One way to take advantage of dual coding is to draw or label timelines,
    maps, family trees, or whatever else seems appropriate to the material.  (I
    am personally fond of pictures showing which functions call which others in
    a program.)  Drawing a diagram without labels and then coming back later to
    label it is excellent retrieval practice.

One powerful finding in learning research is the [%g hypercorrection_effect "hypercorrection effect" %][%i "hypercorrection effect" %] [%b Metcalfe2016 %].  Most people don't like to be told
they're wrong, so it would be reasonable to assume that the more confident
someone is in the answer they've given on a test, the harder it is to change
their mind if they were actually wrong.  It turns out that the opposite is true:
the more confident someone is that they were right, the more likely they are not
to repeat the error if they are corrected.

## Motivation

One of the strongest predictors of whether or not a neurotypical[%i "neurotypical" %] adult will learn something or not is
whether they are intrinsically motivated[%i "intrinsic motivation" "motivation!intrinsic" %] to learn it, i.e., whether
they're learning it to satisfy their own goals.  If someone is extrinsically
motivated[%i "extrinsic motivation" "motivation!extrinsic" %]—for example, if they're taking a course because it's a degree
requirement but they have no real interest in the topic—the learning probably
won't stick [%b Wlodkowski2017 %].  While motivation is deeply personal,
these three factors influence most people:

Self-efficacy[%i "self-efficacy" "motivation!self-efficacy" %].
:   Also called self-determination, this is the degree to which you feel you are
    in control of your own life. People don't enjoy being treated like robots;
    anything the teacher does to put control back in their hands will increase
    engagement, and with it, learning.  This is one of the reasons formative
    assessment works: if the teacher changes course to respond to students'
    answers, it shows students that they have some control over their lives.

Utility.
:   Students will learn more if they think the material is useful, but it has to
    be useful to *them*.  One reason to create learner
    personas[%i "learner persona" %] like the ones in [%x intro %] is to remind
    instructors of the second rule of teaching: "You are not your learners."
    (The first is, "Be kind.")

Community.
:   Most people prefer to learn things that they can share with other people who
    are also learning it.  (I can only dream of inspiring the same enthusiasm
    for programming as I see in baseball forums and fan discussions of *Avatar:
    The Last Airbender*.)

What about demotivation[%i "demotivation" %]? Again, it turns out that
the same few things turn most people off:

Unpredictability.
:   If what you do seems to have no effect on the outcome, you soon learn to
    stop trying.  This is called learned
    helplessness[%i "learned helplessness" %], and anyone who has ever wrestled with an intermittent
    bug or a poorly-written grading rubric is familiar with it.

Unfairness.
:   If people believe that a game is rigged, they will all try less hard:
    the people who are favored will know they can slack off, while everyone
    else will see less point in trying [%b Wilkinson2011 %].

Indifference.
:   Most of us have had a teacher who didn't care whether we learned or not,
    and that kind of apathy is infectious.

These factors, both positive and negative, affect teams and team projects.  You
may not be able to control all of them, but whatever you *can* do will be repaid
many times over.
