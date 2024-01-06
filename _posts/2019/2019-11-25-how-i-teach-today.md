---
title: "How I Teach Today"
date: 2019-11-25 13:02:00
year: 2019
---

I teach a training class for [RStudio instructors][rstudio-instructors] once a month or so,
and invigilate anywhere from half a dozen to a dozen exams each week.
The mechanics are constantly evolving,
but here's what we use right now:

## Application and Selection

People who want to take part fill in a Google Form that adds them to a spreadsheet.
Every few weeks,
I email applicants about upcoming courses based on their timezones.
(I run separate classes at times suitable for people in the Americas,
in countries between Ireland and the Indian Ocean,
and in East Asia and Oceania.)
Applicants who reply are allocated to classes on a first-come/first-served basis;
the rest are carried over to the next round.

This is the least satisfying part of the whole process.
I've been [looking for a better queueing system since September][queueing],
but so far haven't found anything—pointers would be very welcome.

## Before We Start

The class is two sessions of 4.5 hours on consecutive days.
I send people a reminder a few days before it starts
that includes video conferencing details,
a couple of short readings,
and an invite to a Google Doc for shared note-taking.
I ask them to add a line or two about themselves to the doc before the class starts,
both by way of introduction
and to make sure they have edit permission for the doc.

## During Class

I usually have between half a dozen and two dozen learners at a time.
If some of them are co-located,
I ask them to share one webcam and a decent meeting room microphone
(the microphones built into laptops aren't good for group conversations),
but they should all still be in the Google Doc.

Everyone is muted by default.
If someone wants to ask a question,
they can either type it into the video conference chat channel
or signal that they want to speak and unmute themselves when I call on them.
(Allowing both modes helps people who feel shy or who need more time to compose a question
feel more comfortable.)
We use breakout rooms for small-group discussion and peer teaching exercises.
They work pretty well, though it's easy for groups to lose track of time.

Learners do exercises every 10-30 minutes.
I paste a list of names into the shared doc;
they then write their answers under their names
so that they don't stumble over one another's cursors.
They can also paste in images of things like concept maps;
it's a bit clumsy,
but it works surprisingly well.
They can also screenshare with the rest of the class
whenever they want to demonstrate something,
which is so useful that I've started doing it for in-person programming classes as well.

At the end
I ask learners to make a calendar reminder one month in the future
to mail me and tell me what they still remember or found useful.
About 20% of them send that message,
and it's a useful gauge on what to keep teaching
and what to drop because it hasn't made an impact.

> I don't allow learners to record these online classes:
> it makes a lot of people uncomfortable,
> particularly if they've had to deal with online stalkers or harassment.
> I also don't require people to turn on video,
> though if everyone has it off I may ask two or three people to re-enable it
> so that I'm not teaching to a mosaic of empty rectangles.

## Afterward

People have to pass two exams in order to complete certification:
one on teaching and one on the mechanics of using the Tidyverse.
(They can also certify for Shiny, but they only have to do the teaching exam once.)
I use [Calendly](https://calendly.com/) to manage exam booking:
I have open slots every week,
and people can claim one whenever they want.

I clone and rename a Google Doc for each exam,
then share it with the candidate and send them a zip file with the data they'll need.
Candidates share their screen with me when doing the exam
so that I can watch them present or program.
This lets me jump in right away
if I see someone over-engineering an answer to a question,
but it doesn't scale:
I have to run exams one at a time.

## What I'd Like To Do Next

I have two things on my wish-list for 2020.
The first is a [better signup system][queueing]:
I don't want to build something from scratch,
but Salesforce, Lessonly, and Eventbrite all have gaps for this use case.

My second is to make more intensive use of graphics *with* learners
rather than *at* them (as slides).
Many laptops already have touchscreens;
as soon as Apple produces a MacBook that supports fingerpainting
it will be feasible to add new types of exercises to collaborative online classes,
and I'd like to start playing with that now.

[rstudio-instructors]: http://education.rstudio.com/trainers
[queueing]: {{'/2019/09/27/learning-queue/' | relative_url}}
