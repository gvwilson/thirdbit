---
date: 2019-01-06 03:11
title: "Not on the Shelves (2019 Edition)"
---

I made progress on two book projects last year:
*[Teaching Tech Together](http://teachtogether.tech)* is now "done",
and *[JavaScript versus Data Science](https://software-tools-in-javascript.github.io/js-vs-ds/)*
should be out some time in February.
That means it's time to update my list of
[books that don't yet exist]({{site.github.url}}/talks/not-on-the-shelves/),
which I have found helps me figure out
what gaps exist in the literature that I could usefully fill.

I still believe that a good book can change the world;
If you'd like to help with any of the ideas below or take one on yourself,
please [let me know](mailto:gvwilson@third-bit.com).

## Still Magic: A Guide for Research Software Engineers

This book is a hands-on introduction to practical computing tools and skills
aimed at people who have mastered the material in
[Software Carpentry](http://software-carpentry.org)'s workshops
and are now working as [research software engineers](https://researchsoftware.org/).
The core topics---data management, structured programming, task automation, and version control---are introduced
through hands-on tutorials,
then elaborated with further lessons on using the web to share data,
cleaning data,
and creating reproducible workflows.

Status: [working on it](https://merely-useful.github.io/still-magic/en/).

## Probably Approximately Correct: A Guide to Testing Numerical Software

I know how to test an online store:
put a few things in the shopping cart,
total their prices,
add taxes and shipping,
and check the answer.
But how do you test a simulation of highly-magnetized, rapidly-rotating black holes?
How do you check that your data analysis pipeline is probably approximately correct?
And in general,
how do you test software when you don't know what the right answer actually is,
and how can those tests tell your colleagues what your heuristics and thresholds are?

Status: there are [some interesting tools](http://www.tdda.info/) out there,
and some parts of [this book](https://www.amazon.com/Bad-Data-Handbook-Cleaning-Back/dp/1449321887/) are helpful,
but I think this is the biggest gap in data science and data science training today.

## Software Engineering: An Evidence-Based Approach

Unlike their counterparts in physics, psychology, and engineering,
most students in computer science don't do experiments.
As a result,
they graduate not knowing how to get data,
clean it up,
model it,
and draw conclusions from it.
This innovative textbook corrects that:
it tackles simple real-world problems using basic statistical methods
and data harvested from actual software projects.
Its larger message is that opinions about software should be based on evidence
rather than hearsay and strong opinions.

Status: Derek Jones' *[Empirical Software Engineering Using R](http://www.knosof.co.uk/ESEUR/)*
contains a lot of good material,
but isn't designed as a textbook for undergraduates.
Since I'm now working for [a company that builds data science tools](http://rstudio.com),
and feel that I ought to warm up my out-of-date statistical skills,
this might be the next one I tackle.

## Software Tools in JavaScript

*[Software Tools](http://www.amazon.com/Software-Tools-Brian-W-Kernighan/dp/020103669X/)*
and its sequel *[Software Tools in Pascal](http://www.amazon.com/Software-Tools-Pascal-Brian-Kernighan/dp/0201103427/)*
introduced a whole generation of programmers to the Unix philosophy of tool-based computing.
This book's starting point is the observation that JavaScript, HTTP, and JSON
have taken the place of C, ASCII strings, and standard I/O.
Inspired in large part by Mary Rose Cook's awesome [Git from the inside out](https://maryrosecook.com/blog/post/git-from-the-inside-out),
it shows readers how to build standard software engineering tools
like style checkers, unit testing frameworks, and version control systems
using modern JavaScript.

Status: sidetracked by *[JS vs DS](https://software-tools-in-javascript.github.io/js-vs-ds/)*.

## Sex and Drugs and Guns and Code: What Everyone in Tech Needs to Know About Politics, Economics, and Power

Inspired by *[Freakonomics](https://www.amazon.com/Freakonomics-Economist-Explores-Hidden-Everything/dp/0060731338)*
(which was one of the most influential pieces of propaganda written in my lifetime)
and by *[Economics for Everyone](https://www.amazon.com/Economics-Everyone-Second-Short-Capitalism/dp/0745335780/)*
(which tackles many of the same subjects,
but focuses on social justice instead of justifying and excusing the excesses of the powerful),
this book is aimed at people in tech who want to understand how the world works,
but have limited time in which to do it.
It introduces ideas and methods that are commonplace in the social sciences,
and shows that "the way things are" is neither inevitable nor accidental.
From the reasons racial discrimination persists despite its illogical economic inefficiency
to the ways in which "flat" organizations actually operate and how cognitive biases affect us all,
it gives readers [a toolbox for thinking about society]({{site.github.url}}/reading/)
and how tech is reshaping it for both better and worse.

Status: I tried to get this going in 2017-17, but it didn't take off.
I think it's more urgent than ever.

## The Modern Developer: An Owner's Manual

What effect does pulling an all-nighter have on the quality of your work?
How do people absorb and retain knowledge?
What are some good ways to run a project meeting,
and how can you get people to actually pull their weight?
Everyone involved in software development has to deal with these issues and a hundred others,
but most of the time,
they are expected to rediscover or reinvent methods themselves.
This book,
suitable for self-study or for a one-semester course,
puts solutions in one place,
and by doing so teaches a lot about physiology, psychology, and organizational behavior.

Status: this book would be a natural complement to *Sex and Drugs and Guns and Code*.
I don't think I'll ever know nearly enough to write it myself,
but I would be very (very) happy to edit.

## Unbreaking Software

Most programmers spend a large part of their time debugging,
but most books only show working code,
and never discuss how to prevent, diagnose, and fix errors.
[Most](http://www.amazon.com/Debugging-Indispensable-Software-Hardware-Problems/dp/0814474578/)
[books](http://www.amazon.com/Debugging-Thinking-Multidisciplinary-Approach-Technologies/dp/1555583075/)
[ostensibly](http://www.amazon.com/Debug-It-Prevent-Pragmatic-Programmers/dp/193435628X/)
[about](http://www.amazon.com/The-Developers-Guide-Debugging-Edition/dp/1470185520/)
[debugging](http://www.amazon.com/The-Art-Debugging-GDB-Eclipse/dp/1593271743/)
are high-level handwaving,
user guides for particular debugging tools,
or [out of date](http://www.amazon.com/Find-Bug-Book-Incorrect-Programs/dp/0321223918/);
the [one notable exception](http://www.amazon.com/Why-Programs-Fail-Second-Edition/dp/0123745152/)
is an excellent read,
but too advanced for most undergraduates.
This book fills that gap by combining an exploration of how debugging tools actually work
with dozens of case studies showing how to apply them to real-world problems.
Along the way,
it presents examples of what programmers can do to handle errors gracefully,
from data structure repair to automatically restarting servers.

Status: I'll believe that software engineering takes itself seriously as a profession
when a course based on a textbook like this
is a routine part of every college program on computing.
