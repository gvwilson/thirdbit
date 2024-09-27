---
date: 2018-12-06
title: "Three Courses"
---

People who've known me for a while will have heard all this before,
but since some of you haven't,
here's what I would put in the core of a modern undergraduate software engineering curriculum.
Each proposed course is one semester (13 weeks).

- **Year 1**
  - **CS1** and **CS2**,
    i.e., standard two-course introduction to programming.
  - **Statistics** (a computational approach).
  - **Psychology**,
    because nothing in software development makes sense except in light of human psychology.

- **Year 2**
  - **Software Development I and II**,
    which I envisage as a two-course sequence in which students build small versions of classic software tools,
    such as a baby Git,
    a little profiler,
    a unit testing harness,
    and so on.
    This is where they'll start to think about design, testing, and teamwork;
    I also hope that building small versions of these tools will encourage them to use the real things.
  - **Data Structures & Algorithms**:
    again, pretty standard stuff.
  - **Hardware**:
    controlling small devices using C will make everything else seem less like magic.

- **Year 3**
  - **Software Analytics**,
    in which they get, clean, analyze, and interpret data from real software engineering projects.
    Are long functions actually buggier than short ones?
    Do lots of short releases actually make for more reliable software?
    As I've argued before,
    teaching young software developers a little bit of data science (which I think of as operationalized skepticism)
    will do our field a world of good.
  - **Distributed Systems**,
    which would cover all the fun things you can do with HTTP,
    a little bit of queueing theory for performance modeling,
    and fault tolerance.
  - **Verification**,
    using tools like TLA+ and Alloy
    (because after a semester building distributed systems, they'll be ready).
  - **Sex and Drugs and Guns and Code** (note: working title),
    in which they would work through case studies in privacy,
    intellectual property,
    and the like.

This is 2/5 of 3/4 of a standard Canadian undergraduate degree,
leaving 70% of their course load for subjects ranging from HCI and operating systems
to calculus, computational complexity, and humanities electives.
It isn't radically different from what some schools do today:
the course on Software Analytics is probably the biggest departure from the norm,
while the focus in the two-course Software Development sequence on re-creating tools is unusual but not remarkable.
I imagine the inclusion of Psychology in the first year will raise some eyebrows,
but I find I'm basing more and more of my choices and design decisions on what the hardware between our ears is capable of,
and I think some cognitive psychology will help students understand coding guidelines,
while some social psychology will prepare them for working in teams.
