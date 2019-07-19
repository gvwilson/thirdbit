---
layout: post
date: 2019-06-05 02:27
title: "Things I Would Do If I Still Did Research"
favorite: true
---

I never had the patience or diligence to be a good researcher,
but I still have lots of questions that I would like answered.

Are programmers who use version control more productive that programmers who don't?
:   This may seem too obvious to be worth investigating,
    but what I really want to do is calibrate and compare different ways to measure productivity.
    If a method *doesn't* find that version control helps,
    there's something wrong with the method.
    This study would compare three or four different approaches,
    and thereby help the research community agree on what to measure and how
    when tackling cases that *aren't* obvious.

Can we assess students' proficiency with tools by watching screencasts of their work?
:   Just before I left the University of Toronto,
    I asked several people to record their desktop while solving a small data analysis problem.
    The result shook me:
    the times ranged from just under four minutes to just under 38 minutes,
    and I would not have been able to tell which was which
    from the code they produced.
    I have wondered ever since if we could use screencasting to implement lab exams for programming classes,
    i.e,
    if having students record *how* they solve problems would allow us to assess verbs as well as nouns.
    I think it's feasible:
    the files are only a few megabytes
    and you can watch a screencast at 5X or even 10X
    and get a good sense of how well its creator is using their tools,
    so 30 minutes of work is less than 5 minutes to grade.
    What I don't know is whether this would help learners,
    or whether it would help more than other things we could have them do.

Does calibrated peer review improve the quality of novices' programmers code?
:   Give a student a one-page program and have them score it using a checklist,
    then grade them on how closely their scoring matches the instructor's.
    (They start with 100%, and lose one mark for each false positive or false negative.)
    After doing this a handful of times,
    they should learn to see code through the instructor's eyes.
    Does this help them write better code?
    If so,
    how quickly and how well?
    (One of Mine Çetinkaya-Rundel's interns
    is exploring the design of this experiment this summer.)

How well do data scientists agree with each other about the correctness of analyses?
:   There's an old joke that physicists worry about decimal places,
    astronomers worry about exponents,
    and economists are happy if they've got the sign right.
    The truth beneath this is that
    every disciplines uses its own implicit heuristics to judge how good is "good enough".
    I suspect that data science doesn't yet have a shared set of heuristics,
    both because it's such a young field
    and because its practitioners come from such varied background.
    This study would put a dozen two-page data analyses in front of a couple of dozen data scientists
    and ask them which ones seem OK and which ones seem dodgy,
    then explore the degree of inter-grader agreement and the reasons behind disagreements.

Do novices learn data science faster or better using blocks or text?
:   Multiple studies have shown that novices learn programming faster using blocks-based tools like Scratch
    than using text-based programming languages.
    Is the same true for data science?
    The study subjects would be high school students preparing for something like the AP Stats exam,
    and the blocks would implement the operations in the tidyverse.
    (One of my summer interns is building a tool so that we can study this.
    If you're a JavaScript programmer and you want to help, please get in touch.)

How much software would pass a Moses Test?
:   Robert Moses reshaped New York City and surrounding areas;
    among other things,
    he deliberately made the bridges over roads leading to public beaches too low for buses
    so that poor people would have a hard time getting there.
    In his dishonor,
    I would like to institute a Moses Test:
    take a real social network or software application,
    and another that has deliberately been designed to be unfair or exclusionary in some way,
    and put them in front of a randomly selected software engineer.
    If they can't tell which is which,
    the real system fails the test.
    This would allow us to gauge how fair systems are without having to define fairness,
    in the same way that the Turing Test does for intelligence.
