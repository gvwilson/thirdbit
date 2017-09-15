---
layout: teaching
permalink: /teaching/live.html
title: "How to Teach Programming (and Other Things): Live Coding"
---

# Live Coding

**Objectives**

* **Learners can describe live coding and explain its advantages as a
  teaching practice for programming workshops.**
* **Learners can enact and critique live coding.**

> *Teaching is theater not cinema.*  
> – Neal Davis

Teaching is a performance art, just like drama, music, and athletics.
And as in those fields, we have a collection of small tips and tricks
to make teaching work better.

The first of our recommended teaching practices is so central that it
deserves a chapter of its own: _[live
coding](gloss.html#live-coding)_.  When they are live coding,
instructors don't use slides.  Instead, they go through the lesson
material, typing in the code or instructions, with their learners
following along.  Its advantages are:

1.  Watching a program being written is more compelling than watching
    someone page through slides that present bits and pieces of the same
    code.

2.  It enables instructors to be more responsive to "what if?"
    questions. Where a slide deck is like a railway track, live coding
    allows instructors to go off road and follow their learners'
    interests.

3.  It facilitates lateral knowledge transfer: people learn more than we
    realized we were teaching by watching *how* instructors do
    things.

4.  It slows the instructor down: if she has to type in the program as
    she goes along, she can only go twice as fast as her learners,
    rather than ten-fold faster as she could with slides.

5.  Learners get to see instructors' mistakes *and how to diagnose
    and correct them*. Novices are going to spend most of their time
    doing this, but it's left out of most textbooks.

6.  Watching instructors make mistakes shows learners that it's all
    right to make mistakes of their own.  Most people model the
    behavior of their teachers: if the instructor isn't embarrassed
    about making and talking about mistakes, learners will be more
    comfortable doing so too.

Live coding does have some drawbacks, but with practice, these can be
avoided or worked around:

1.  Instructors can go too slowly, either because they are not good
    typists or by spending too much time looking at notes to try to
    remember what they meant to type.

2.  Typing in boilerplate code that is needed by the lesson, but not
    directly relevant to it (such as library import statements)
    increases the [extraneous cognitive load](load.html) on your
    learners.  Willingham says "Memory is the residue of thought"
    [[Willingham2010](biblio.html#willingham-dont-like-school)], so if you
    spend your time typing boilerplate, that may be what learners will
    take away.

Live coding is an example of the "I/We/You" approach to teaching
discussed in [Performance](performance.html).  It takes a bit of practice
for instructors to get used to thinking aloud while coding in front of
an audience, but most report that it is then no more difficult to do
than talking off a deck of slides.

## Be Seen and Heard

If you are physically able to stand up for a couple of hours, do it
while you are teaching. When you sit down, you are hiding yourself
behind others for those sitting in the back rows. Make sure to notify
the workshop organizers of your wish to stand up and ask them to
arrange a high table, standing desk, or lectern.

Regardless of whether you are standing or sitting, make sure to move
around as much as reasonable. You can for example go to the screen to
point something out, or draw something on the white/blackboard (see
below). Moving around makes the teaching more lively, less monotonous.
It draws the learners' attention away from their screens, to you,
which helps get the point you are making across.

Even though you may have a good voice and know how to use it well, it
may be a good idea to use a microphone, especially if the workshop
room is equipped with one. Your voice will be less tired, and you
increase the chance of people with hearing difficulties being able to
follow the workshop.

## Take It Slow

For every command you type, every word of code you write, every menu
item or website button you click, say out loud what you are doing
while you do it, then point to the command and its output on the
screen and go through it a second time. This not only slows you down,
it allows learners who are following along to copy what you do, or to
catch up, even when they are looking at their screen while doing it.
Whatever you do, *don't* copy and paste code: doing this practically
guarantees that you'll race ahead of your learners.

If the output of your command or code makes what you just typed
disappear from view, scroll back up so learners can see it again -
this is especially needed for the Unix shell lesson.  Other options
are to execute the same command a second time, or to copy and paste
the last command(s) into the workshop's shared notes.

## Mirror Your Learner's Environment

You may have set up your environment to your liking, with a very
simple or rather fancy Unix prompt, colour schemes for your
development environment, keyboard shortcuts etc. Your learners usually
won't have all of this. Try to create an environment that mirrors what
your learners have, and avoid using keyboard shortcuts. Some
instructors create a separate bare-bones user (login) account on their
laptop, or a separate teaching-only account on the service being
taught (e.g., Github).

## Use the Screen Wisely

You will need to enlarge your font considerably in order for people to
read it from the back of the room, which means you can put much less
on the screen than you're used to.  (You will often be reduced to
60-70 columns and 20-30 rows, which basically means that you're using
a 21st Century supercomputer to emulate an early-1980s VT100
terminal.)

To cope with this, maximize your window, and then ask everyone to give
you a thumbs-up or thumbs-down on its readability.  Use a black font
on a lightly-tinted background rather than a light font on a dark
background–the light tint will glare less than a pure white
background.

When the bottom of the projector screen is at the same height, or
below, the heads of the learners, people in the back won't be able to
see the lower parts. Draw up the bottom of your window(s) to
compensate.

Pay attention to the room lighting as well: it should not be fully
dark, and there should be no lights directly on or above the
presenter's screen.  If needed, reposition the tables so all learners
can see the screen.

If you can get a second screen, use it: the extra screen real estate
will allow you to display your code on one side and its output or
behavior on the other.  The second screen may require its own PC or
laptop, so you may need to ask a helper to control it.

> **Multiple Personalities**
>
> If you teach using a console window, such as a Unix shell, it's
> important to tell people when you run an in-console text editor and
> when you return to the console prompt.  Most novices have never seen
> a window take on multiple personalities in this way, and can quickly
> become confused (particularly if the window is hosting an
> interactive interpreter prompt for Python or some other language as
> well as running shell commands and hosting an editor).

## Double Devices

Many instructors now use two devices when teaching: a laptop plugged
into the projector for learners to see, and a tablet beside it on
which they can view their notes and the shared notes that the learners
are taking.  This seems to be more reliable than displaying one
virtual desktop while flipping back and forth to another.  Of course,
printouts of the lesson material are still the most reliable backup
technology…

## Use Illustrations

Most lesson material comes with illustrations, and these may help
learners to understand the stages of the lesson and to organize the
material. What can work really well is when you as instructor generate
the illustrations on the white/blackboard as you progress through the
material. This allows you to build up diagrams, making them
increasingly complex in parallel with the material you are
teaching. It helps learners understand the material, makes for a more
lively workshop (you'll have to move between your laptop and the
blackboard) and gathers the learners' attention to you as well.

## Avoid Distractions

Turn off any notifications you may use on your laptop, such as those
from social media, email, etc. Seeing notifications flash by on the
screen distracts you as well as the learners, and may even result in
awkward situations when a message pops up you'd rather not have others
see.

## Improvise *After* You Know the Material

The first time you teach a new lesson, you should stick fairly closely
to the topics it lays out and the order they're in.  It may be
tempting to deviate from the material because you would like to show a
neat trick, or demonstrate some alternative way of doing
something. Don't do this, since there is a fair chance you'll run into
something unexpected that you then have to explain.

Once you are more familiar with the material, though, you can and
should start improvising based on the backgrounds of your learners,
their questions in class, and what you find most interesting about the
lesson.  This is like a musician playing a new song: the first few
times, you stick to the sheet music, but after you're comfortable with
it, you can start to put your own stamp on it.

If you really want to use something outside of the material, try it
out thoroughly before the workshop: run through the lesson as you
would during the actual teaching and test the effect of your
modification.

## Embrace Mistakes

No matter how well prepared you are, you will be making
mistakes. Typo's are hard to avoid, you may overlook something from
the lesson instructions, etc. This is OK! It allows learners to see
instructors' mistakes and how to diagnose and correct them. Some
mistakes are actually an opportunity to point something out, or
reflect back on something covered earlier. Novices are going to spend
most of their time making the same and other mistakes, but how to deal
with them is left out of most textbooks.

> *The typos are the pedagogy.*  
> – Emily Jane McTavish

Note: if you've given a lesson several times, you're unlikely to make
anything other than basic typing mistakes (which usually aren't
informative). It's worth remembering "real" mistakes and making them
deliberately, but that often feels forced.  A better approach is to
get learners to tell you what to do next in the hope that this will
get you into the weeds.

## Face the Screen–Occasionally

It's OK to *face the screen occasionally*, particularly when you are
walking through a section of code statement by statement or drawing a
diagram, but you shouldn't do this for more than a few seconds at a
time.  Looking at the screen for a few seconds can help lower your
anxiety levels, since it gives you a brief break from being looked at.

A good rule of thumb is to treat the screen as one of your learners:
if it would be uncomfortable to stare at someone for as long as you
are spending looking at the screen, it's time to turn around and face
your audience.

## Have Fun

Teaching is performance art and can be rather serious business. On the
one hand, don't let this scare you - it is much easier than performing
Hamlet. You have an excellent script at your disposal, after all! On
the other hand, it is OK to add an element of play, i.e. use humor and
improvisation to liven up the workshop. How much you are able and
willing to do this is really a matter of personality and taste - as
well as experience. It becomes easier when you are more familiar with
the material, allowing you to relax more. Choose your words and
actions wisely, though. Remember that we want the learners to have a
welcoming experience and a positive learning environment - a misplaced
joke can ruin this in an instant. Start small, even just saying `that
was fun' after something worked well is a good start. Ask your
co-instructors and helpers for feedback when you are unsure of the
effect your behavior has on the workshop.

## Challenges

### The Bad and the Good (20 minutes)

Watch the video of live coding done poorly
[[Nederbragt2016a](biblio.html#live-coding-bad)] and then the video of
live coding done well [[Nederbragt2016b](biblio.html#live-coding-good)]
as a group and then summarize your feedback on both using the usual
2×2 grid.  These videos assume learners know what a shell variable is,
know how to use the `head` command, and are familiar with the contents
of the data files being filtered.

### See Then Do (30 minutes)

Teach 3-4 minutes of a lesson using live coding to a fellow trainee,
then swap and watch while that person live codes for you. Don't bother
trying to record the live coding sessions–we have found that it's
difficult to capture both the person and the screen with a handheld
device–but give feedback the same way you have previously (positive
and negative, content and presentation).  Explain in advance to your
fellow trainee what you will be teaching and what the learners you
teach it to are expected to be familiar with.

*   What felt different about live coding (versus standing up and
    lecturing)? What was harder/easier?

*   Did you make any mistakes? If so, how did you handle them?

*   Did you talk and type at the same time, or alternate?

*   How often did you point at the screen? How often did you highlight
    with the mouse?

*   What will you try to do differently next time?
