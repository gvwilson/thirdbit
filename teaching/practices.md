---
layout: teaching
permalink: /teaching/practices.html
title: "How to Teach Programming (and Other Things): Teaching Practices"
---

# Teaching Practices

> **Objectives**
>
> * Learners can name, describe, and enact four teaching practices that
>   are appropriate to use in programming workshops for adults, and
>   give a pedagogical justification for each.
> * Learners can explain why instructors should *not* introduce new
>   pedagogical practices in a short workshop.

Just as domain expertise is often a matter of [pattern
recognition](load.html#pattern-recognition), teaching expertise often
comes down to using good practices consistently.  None of the
practices described below are essential (except having a code of
conduct), but each will improve lesson delivery.

## Have a Code of Conduct

An important part of making a class productive is to treat everyone
with respect.  We therefore strongly recommend that every group
offering classes based on this material adopt a Code of Conduct like
[this one](conduct.html), and require people taking part in the
class to abide by it.

We believe equally strongly that your actual programming classes
should also have and enforce a Code of Conduct.  Programming is a
scary topic for many novices, and workshops are meant to be a judgment
free space to learn and experiment. The behavior of the instructor and
other participants may make more of an impression on a novice learner
than any "technical" topic you teach.

If you do this, hosts should point people at it during registration,
and instructors should remind attendees of it at the start of the
workshop. The Code of Conduct doesn't just tell everyone what the
rules are: it tells them that there *are* rules, and that they can
therefore expect a safe and welcoming learning experience.

If you are an instructor, and believe that someone in a workshop has
violated the Code of Conduct, you may warn them, ask them to
apologize, and/or expel them, depending on the severity of the
violation and whether or not you believe it was intentional.  Whatever
you do:

*   Do it in front of witnesses.  Most people will tone down their
    language and hostility in front of an audience, and having someone
    else present ensures that later discussion doesn't degenerate into
    conflicting claims about who said what.

*   Contact the organizer or host of your class as soon as you can and
    describe what happened.  Remember, a Code of Conduct is
    meaningless without a procedure for enforcing it.

A Code of Conduct cannot stop people from being offensive, any more
than laws against theft stop people from stealing. What it *can* do is
make expectations and consequences clear.  In our experience, people
rarely violate the Code of Conduct in person, though some are more
likely to online, where they feel less inhibited.  And remember, a
Code of Conduct is *not* an infringement on free speech.  People have
a right to say what they think, but that doesn't mean they have a
right to speak wherever and whenever they want.  If someone wishes to
say something disparaging about someone else, they can go and find a
space of their own in which to say it.

## Starting Out

To begin your class, the instructors should give a brief introduction
that will convey their capacity to teach the material,
accessibility and approachability, desire for student success, and
enthusiasm. Tailor your introduction to the students' skill level so
that you convey competence (without seeming too advanced) and
demonstrate that you can relate to the students. Throughout the
workshop, continually demonstrate that you are interested in student
progress and that you are enthusiastic about the topics.

Students should also introduce themselves (preferably verbally). At the
very least, everyone should add their name to the Etherpad, but its also
good for everyone at a given site to know who all is in the group. Note:
this can be done while setting up before the start of the class.

## Overnight Homework

In a two-day class, have learners read the operations checklists as
overnight homework and do their demotivational story just before
lunch on day 2: it means day 2 starts with *their* questions
(which wakes them up), and the demotivational story is a good
lead-in to lunchtime discussion.

## Never a Blank Page

Programming workshops (and other kinds of classes) can be built around
a set of independent exercises, develop a single extended example in
stages, or use a mixed strategy.  The main advantages of independent
exercises are that people who fall behind can easily re-synchronize,
and that lesson developers can add, remove, and rearrange material at
will.  A single extended example, on the other hand, will show
learners how the bits and pieces they're learning fit together: in
educational parlance, it provides more opportunity for them to
integrate their knowledge.

Whichever approach you take, learners should never start with a blank
page (or screen), since they often find this intimidating or
bewildering.  Modifying existing code instead of writing new code from
scratch doesn't just give them structure: it is also more realistic.
Keep in mind, however, that starter code may increase cognitive load,
since learners can be distracted by trying to understand it all before
they start their own work.

## Take Notes Together

Many studies have shown that taking notes while learning improves
retention [[Aiken1975](biblio.html#aiken-note-taking)],
[[Bohay2011](biblio.html#bohay-note-taking)].  As discussed in
[Memory](memory.html), this happens because taking notes forces you to
organize and reflect on material as it's coming in, which in turn
increases the likelihood that you will transfer it to long-term memory
in a usable way.

Our experience, and some recent research findings, lead us to believe
that taking notes *collaboratively* helps learning even more
[[Orndorff2015](biblio.html#orndorff-note-taking)], even though taking
notes on a computer is generally less effective than taking notes
using pen and paper [[Mueller2014](biblio.html#mueller-note-taking)].
Taking notes collaboratively:

*   It allows people to compare what they think they're hearing with
    what other people are hearing, which helps them fill in gaps and
    correct misconceptions right away.

*   It gives the more advanced learners in the class something useful to
    do.  Rather than getting bored and checking Twitter during class,
    they often take the lead in recording what's being said, which
    keeps them engaged, and allows less advanced learners to focus
    more of their attention on new material.  Keeping the more
    advanced learners busy also helps the whole class stay engaged
    because boredom is infectious: if a handful of people start
    updating their Facebook profiles, the people around them will
    start checking out too.

*   The notes the learners take are usually more helpful *to them* than
    those the instructor would prepare in advance, since the learners
    are more likely to write down what they actually found new, rather
    than what the instructor predicted would be new.

*   Glancing at the notes as they're being taken helps the instructor
    discover that the class didn't hear something important, or
    misunderstood it.

We usually use [Etherpad][etherpad] or [Google Docs][google-docs] for
collaborative note-taking.  The former makes it easy to see who's
written what, while the latter scales better and allows people to add
images to the notes.  Whichever is chosen, classes also use it to
share snippets of code and small datasets, and as a way for learners
to show instructors their work (by copying and pasting it in).

Shared note-taking is almost always mentioned positively in
post-workshop feedback.  However, it's also common for participants to
report that they find it distracting, as it's one more thing they have
to keep an eye on.  We believe the positives outweigh the negatives,
but think that some careful controlled studies would tell us whether
we're right, and how to use it better.

## Assess Motivation and Prior Knowledge

Most formal educational systems train people to treat all assessment
as summative, i.e., to think of every interaction with a teacher as an
evaluation, rather than as a chance to shape instruction.  For
example, we use a short pre-assessment questionnaire to profile
learners before workshops to help instructors tune the pace and level
of material. We send people this questionnaire out after they have
registered rather than making it part of the sign-up process because
when we did the latter, many people concluded that since they couldn't
answer all the questions, they shouldn't enrol. We were therefore
scaring off many of the people we most wanted to help.

Instead of asking people how easily they could complete specific
tasks, we could just ask them to rate their knowledge of various
subjects on a scale from 1 to 5. However, self-assessments of this
kind are usually inaccurate because of the [Dunning-Kruger
effect][wikipedia-dunning-kruger]: the less people know about a
subject, the less accurate their estimate of their knowledge is.

That said, there *are* things we can do:

*   Before running a workshop, communicate its level clearly to everyone
    who's thinking of signing up by listing the topics that will be
    covered and showing a few examples of exercises that people will
    be asked to complete.

*   Provide multiple exercises for each teaching episode so that more
    advanced learners don't finish early and get bored.

*   Ask more advanced learners to help people next to them. They'll
    learn from answering their peers' questions (since it will force
    them to think about things in new ways).

*   The helpers and the instructor who aren't teaching the particular
    episode should keep an eye out for learners who are falling behind
    and intervene early so that they don't become frustrated and give
    up.

The most important thing is to accept that no class can possibly meet
everyone's individual needs. If the instructor slows down to
accommodate two people who are struggling, the other 38 are not being
well served.  Equally, if she spends a few minutes talking about an
advanced topic because two learners are bored, the 38 who don't
understand it will feel left out. All we can do is tell our learners
what we're doing and why, and hope that they'll understand.

It's important to design lessons with a particular audience in mind.
It's equally important to find out who's in each specific audience,
since this will influence how you introduce yourself, motivate topics,
and pace the lessons.  Before the start of a Software Carpentry
instructor training class, we ask people to fill in a short
questionnaire like the one below.  It doesn't tell us everything we
might want to know, but it does give trainers a pretty clear idea of
who they're speaking to.

1.  Have you ever participated in a Software Carpentry workshop?
    *   Yes, as a learner.
    *   Yes, as a helper.
    *   Yes, as an organizer.
    *   Yes, as an instructor.
    *   No, but I am familiar with what is taught at a workshop.
    *   No, and I am not familiar with what is taught.

1.  Which of these describes your teaching experience?
    *   I have none.
    *   I have taught a workshop or other informal course.
    *   I have been a teaching assistant for a college-level course.
    *   I have been the instructor for a college-level course.
    *   I have taught at the K-12 level.

1.  Which of these describes your previous formal training in teaching?
    *   None
    *   A few hours
    *   A workshop
    *   A certification or short course
    *   A full degree

1.  How frequently do you work with the tools that Software Carpentry
    teaches, such as R, Python, MATLAB, Perl, SQL, Git, and the Unix
    Shell?
    *   Every day
    *   A few times a week
    *   A few times a month
    *   A few times a year
    *   Never or almost never

1.  How often would you expect to teach a Software Carpentry workshop
    after this training?
    *   Not at all
    *   Once a year
    *   Several times a year

1.  Why do you want to take this training course?

## Sticky Notes as Status Flags

Give each learner two sticky notes of different colours, e.g., red and
green. These can be held up for voting, but their real use is as
status flags. If someone has completed an exercise and wants it
checked, they put the green sticky note on their laptop; if they run
into a problem and need help, the put up the red one. This is better
than having people raise their hands because:

*   it's more discreet (which means they're more likely to actually do
    it),

*   they can keep working while their flag is raised, and

*   the instructor can quickly see from the front of the room what state
    the class is in.

Sometimes a red sticky involves a technical problem that takes a bit
more time to solve. To prevent this issue from slowing down the whole
class too much, you could use the occasion to take the small break you
had planned to take a bit later, giving the helper(s) time to fix the
problem.

## Sticky Notes to Distribute Attention

Sticky notes can also be used to ensure that the instructor's
attention is fairly distributed.  Have each learner write their name
on a sticky note and put it on their laptop.  Each time the instructor
calls on them or answers one of their questions, their sticky note
comes down.  Once all the sticky notes are down, everyone puts theirs
up again.

This technique makes it easy for the instructor to see who they
haven't spoken with recently, which in turn helps them avoid the
unconscious trap of only interacting with the most extroverted of
their learners.  It also shows learners that attention is being
distributed fairly, so that when they *are* called on, they won't feel
like they're being picked on.

## Never Touch the Learner's Keyboard

It's often tempting to fix things for learners, but when you do, it
can easily seem like magic (even if you narrate every step).  Instead,
talk your learners through whatever they need to do.  It will take
longer, but it's more likely to stick.

## Minute Cards

We frequently use sticky notes as _[minute
cards](gloss.html#minute-cards)_: before each break, learners take a
minute to write one positive thing on the green sticky note (e.g., one
thing they've learned that they think will be useful), and one thing
they found too fast, too slow, confusing, or irrelevant on the red
one. They can use the red sticky note for questions that haven't yet
been answered. While they are enjoying their coffee or lunch, the
instructors review and cluster these to find patterns. It only takes a
few minutes to see what learners are enjoying, what they still find
confusing, what problems they're having, and what questions are still
unanswered.

## One Up, One Down

We frequently ask for summary feedback at the end of each day. The
instructors ask the learners to alternately give one positive and one
negative point about the day, without repeating anything that has
already been said. This requirement forces people to say things they
otherwise might not: once all the "safe" feedback has been given,
participants will start saying what they really think.

Minute cards are anonymous; the alternating up-and-down feedback is
not.  Each mode has its strengths and weaknesses, and by providing
both, we hope to get the best of both worlds.

## Pair Programming

_Pair programming_ is a software development practice in which two
programmers share one computer.  One person (called the driver) does
the typing, while the other (called the navigator) offers comments and
suggestions.  The two switch roles several times per hour.

Pair programming is a good practice in real life, and also a good way
to teach [[Hannay2009](biblio.html#hannay-pairing)],
[[Porter2013](biblio.html#porter-what-works)]. Partners can not only help
each other out during the practical, but can also clarify each other's
misconceptions when the solution is presented, and discuss common
research interests during breaks. To facilitate this, we strongly
prefer flat (dinner-style) seating to banked (theater-style) seating;
this also makes it easier for helpers to reach learners who need
assistance.

When pair programming is used it's important to put *everyone* in
pairs, not just the learners who are struggling, so that no one feels
singled out. It's also useful to have people sit in new places (and
hence pair with different partners) after each coffee or meal break.
It's also important to have people switch roles within each pair three
or four times per hour, so that the stronger personality in each pair
doesn't dominate the session.

> **Confidence is Not Knowledge**
>
> The [Dunning-Kruger Effect][wikipedia-dunning-kruger] can easily
> come into play in pair programming: whoever *thinks* they know the
> most can dominate the session regardless of how much they *actually*
> know.

<!-- comment needed to separate blockquotes -->

> **Switching Partners**
>
> Instructors have mixed opinions on whether people should be required
> to change partners at regular intervals.  On the one hand, it gives
> everyone a chance to gain new insights and make new friends.  On the
> other, it is uncomfortable for introverts, and moving computers and
> power adapters to new desks several times a day is disruptive.

## Have Learners Make Predictions

Research has shown that people learn more from demonstrations if they
are asked to predict what's going to happen
[[Miller2013](biblio.html#miller-predictions)].  Doing this fits naturally
into live coding: after adding or changing a few lines of a program,
ask someone what is going to happen when it's run.

## Collaborative Debugging

If you are live coding and your program doesn't work, explain the
symptoms to your learners.  The underlying cause often then becomes
clear; if it doesn't, have them take turns suggesting things to try
next.  Be careful not to let one or two people dominate the
discussion.

## Peer Instruction

No matter how good a teacher is, she can only say one thing at a time.
How then can she clear up many different misconceptions in a
reasonable time?

The best solution developed so far is a technique called _[peer
instruction](gloss.html#peer-instruction)_. Originally created by
Eric Mazur at Harvard, it has been studied extensively in a wide
variety of contexts, including programming
[[Porter2013](biblio.html#porter-what-works)]. Peer instruction combines
formative assessment with student discussion and looks something like
this:

1.  Give a brief introduction to the topic.

1.  Give students an MCQ that probes for misconceptions (rather than
    simple factual knowledge).

1.  Have all the students vote on their answers to the MCQ.
    *   If the students all have the right answer, move on.
    *   If they all have the same wrong answer, address that specific
        misconception.
    *   If they have a mix of right and wrong answers, give them
        several minutes to discuss those answers with one another in
        small groups (typically 2-4 students) and then reconvene and
        vote again.

As [[Avanti2013](biblio.html#video-peer-instruction)] shows, group
discussion significantly improves students' understanding because it
forces them to clarify their thinking, which can be enough to call out
gaps in reasoning. Re-polling the class then lets the instructor know
if they can move on, or if further explanation is necessary. A final
round of additional explanation and discussion after the correct
answer is presented gives students one more chance to solidify their
understanding.

Peer instruction is essentially a way to provide one-to-one mentorship
in a scalable way. Despite this, we usually do not use it in either
programming workshops or instructor training workshops because it
takes people time to adapt to a new way of learning–time that we
typically don't have in our compressed two-day format.

> **Taking a Stand**
>
> Note that it is important to have learners record their votes so
> that they can't change their minds afterward and rationalize it by
> making excuses to themselves like "I just misread the question".
> Much of the value of peer instruction comes from the jarring
> experience of having their answer be wrong and having to think
> through the reasons why.

## Setting Up Your Learners

Adult learners tell us that it is important to them to leave
programming workshops with their own machine set up to do real
work. We therefore strongly recommend that instructors be prepared to
teach on all three major platforms (Linux, Mac OS, and Windows), even
though it would be simpler to require learners to use just one.

To aid in this, put detailed setup instructions for all three
platforms on the workshop's website, and email learners a couple of
days before the workshop starts to remind them to do the setup.  Even
with this, a few people will always show up without the right
software, either because their other commitments didn't allow them to
go through the setup or because they ran into problems.  To detect
this, have everyone run some simple command as soon as they arrive and
show the instructors the result, and then have helpers and other
learners assist people who have run into trouble.

> **Common Denominators**
> 
> If you have participants using several different operating systems,
> avoid using features which are OS-specific, and point out any that
> you *do* use.  For example, some shell commands take different
> options on Mac OS than on Linux, while the "minimize window"
> controls and behavior on Windows are different from those on other
> platforms.

<!-- comment to separate blockquotes -->

> **Virtual Machines**
> 
> We have experimented with virtual machines (VMs) on learners'
> computers to reduce installation problems, but those introduce
> problems of their own: older or smaller machines simply aren't fast
> enough, and learners often struggle to switch back and forth between
> two different sets of keyboard shortcuts for things like copying and
> pasting.
> 
> Some instructors use VPS over SSH or web browser pages instead. This
> solve the installation issues, but makes us dependent on host
> institutions' WiFi (which can be of highly variable quality), and
> has the issues mentioned above with things like keyboard shortcuts.

## Setting Up Tables

You may not have any control over the layout of the desks or tables in
the room in which your programming workshop takes place, but if you
do, we find it's best to have:

<!--| \newpage |-->

*   all tables on the same level (rather than banked seating),

*   four people per table (so that each table can have two pairs if
    you choose to use pair programming), and

*   in-floor power outlets (so that you don't have to run power cords
    across the floor that people can trip over).

Whatever layout you have, try to make sure the seats have good back
support, since people are going to be in them for an extended period,
and check that every seat has an unobstructed view of the screen.

## Setting Up Your Own Environment

Setting up your environment is just as important as setting up your
learners', but more involved.  As well as having all the software that
they need, and network access to the tool they're using to take notes,
you should also have a glass of water, or a cup of tea or coffee.
This helps keep your throat lubricated (as discussed in the next
section), but its real purpose is to give you an excuse to pause for a
couple of seconds and think when someone asks a hard question or you
lose track of what you were going to say next.

You will probably also want some whiteboard pens and a few of the
other things described in the [travel kit
checklist](checklists.html#travel-kit).

## Cough Drops

If you talk all day to a room full of people, your throat gets raw
because you are irritating the epithelial cells in your larynx and
pharynx.  This doesn't just make you hoarse–it also makes you more
vulnerable to infection (which is part of the reason people often come
down with colds after teaching).

The best way to protect yourself against this is to keep your throat
lined, and the best way to do that is to use cough drops early and
often.  The right ones will also help delay the onset of coffee
breath, for which your learners will probably be grateful.

## Think-Pair-Share

Think-pair-share is a lightweight technique that helps refine their
ideas and compare them with others'.  Each person starts by thinking
individually about a question or problem and jotting down a few notes.
Participants are then paired to explain their ideas to each another,
and possibly to merge them or select the more interesting ones.
Finally, a few pairs present their ideas to the whole group.

Think-pair-share works because, to paraphrase Oscar Wilde's Lady
Windermere, people often can't know what they're thinking until
they've heard themselves say it.  Pairing gives people new insight
into their own thinking, and forces them to think through and resolve
any gaps or contradictions *before* exposing their ideas to a larger
group.  We used think-pair-share in several of the challenges in
[our discussion of motivation](motivation.html#challenges).

## Humor

Humor should be used sparingly when teaching: most jokes are less
funny when written down, and become even less funny with each
re-reading.  Being spontaneously funny while teaching usually works
better, but can easily go wrong: what's a joke to your circle of
friends may turn out to be a serious political issue to your audience.
If you do make jokes when teaching, don't make them at the expense of
any group, or of anyone except possibly yourself.

## Challenges

### Create a Questionnaire (20 minutes)

Using the questionnaire shown earlier as a template, create a short
questionnaire you could give learners before teaching a class of your
own.  What do you most want to know about their background?

[etherpad]: http://etherpad.org
[google-docs]: https://docs.google.com
[wikipedia-dunning-kruger]: https://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect
