---
layout: default
permalink: /ideas/
title: "Ideas"
redirect_from: "/not-on-the-shelves/2017.html"
---

# Ideas

These ideas are things I might have done if I hadn't done [Software Carpentry](http://carpentries.org).
Many are presented as [descriptions of books that don't yet exist]({{site.github.url}}/not-on-the-shelves/)
because I still believe that a good book can change the world.
If you'd like to help with any of them or take one on yourself, please let me know.

## Software Tools in JavaScript

*[Software Tools](http://www.amazon.com/Software-Tools-Brian-W-Kernighan/dp/020103669X/)*
and its sequel *[Software Tools in Pascal](http://www.amazon.com/Software-Tools-Pascal-Brian-Kernighan/dp/0201103427/)*
introduced a whole generation of programmers to the Unix philosophy of tool-based computing.
This book's starting point is the observation that JavaScript, HTTP, and JSON have taken the place of C, ASCII strings, and standard I/O.
It presents a "new standard model" based on syndication of distributed streams of events,
and shows readers how the tools they use are built,
and how to build tools of their own.

## Merely Useful: An Introduction to Research Computing

Based on the workshops run by [Software Carpentry](http://software-carpentry.org) and [Data Carpentry](http://datacarpentry.org),
this book is a hands-on introduction to practical computing skills
aimed at graduate students and professionals in research-intensive disciplines.
The core topics–data management, structured programming, task automation, and version control–are introduced
through a series of short tutorials,
then elaborated with further lessons on using the web to share data,
creating reproducible workflows,
cleaning data,
and testing software when the right answer isn't actually known.
While it necessarily glosses over many fine points,
it gives readers a useful toolkit and a sense of where to go next.

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
(Derek Jones' *[Empirical Software Engineering Using R](http://www.knosof.co.uk/ESEUR/)*
is headed in this direction.)

### Sex and Drugs and Guns and Code: What Everyone in Tech Needs to Know About Politics, Economics, and Power

Inspired by
*[Economics for Everyone](https://www.amazon.com/Economics-Everyone-Second-Short-Capitalism/dp/0745335780/)*
and
*[The Imposter's Handbook](https://bigmachine.io/products/the-imposters-handbook)*,
this book is aimed at people in tech who want to understand how the world works,
but have limited time in which to do it.
It introduces ideas and methods that are commonplace in the social sciences,
and shows that "the way things are" is neither inevitable nor accidental.
From the reasons racial discrimination persists despite its illogical economic inefficiency
to the ways in which "flat" organizations actually operate and how cognitive biases affect us all,
it gives readers [a toolbox for thinking about society]({{site.github.url}}/reading/)
and how tech is reshaping it for both better and worse.

## Software Architecture by Example

Architects study hundreds of buildings during their training;
writers read hundreds of novels,
and mathematicians study at least that many proofs.
In contrast,
most software engineers only explore a handful of medium-sized programs during their training.
This book corrects that by contrasting alternative implementations of key features of open source applications.
Whether it's the undo/redo stacks of Vim and Emacs,
how Apache and Nginx manage user plugins,
or the way that React and Angular decide what to re-render,
each paired example serves as a springboard for larger discussion of how software is designed
and how tradeoffs are made.
The book draws material from *[The Architecture of Open Source Applications](http://aosabook.org)*,
but is a tutorial rather than a survey.

## A Catalog of Errors

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
the *[one notable exception](http://www.amazon.com/Why-Programs-Fail-Second-Edition/dp/0123745152/)*
is an excellent read,
but too advanced for most undergraduates.
This book fills that gap by combining an exploration of how debugging tools actually work
with dozens of case studies showing how to apply them to real-world problems.
Along the way,
it presents examples of what programmers can do to handle errors gracefully,
from data structure repair to automatically restarting servers.

## The Undergraduate Operator's Manual

What effect does pulling an all-nighter have on the quality of your work?
How do people absorb and retain knowledge?
What are some good ways to run a project meeting,
and how can you get people to actually pull their weight?
Every undergraduate has to deal with these issues and a hundred others,
but most of the time,
they are expected to rediscover or reinvent methods themselves.
This textbook for a one-semester course puts solutions in one place,
and by doing so teaches a lot about physiology, psychology, and organizational behavior.

## Computing and the Law: A Guide for the Perplexed

The legal aspects of software have always been complicated;
the web has done nothing to make them simpler.
This book seeks to help programmers understand the rules (or lack thereof)
they have to live with
by tracing the historical development of patents, copyrights, privacy, and professional liability
from the Industrial Revolution to the present day.
Aimed squarely at people with no prior exposure to legal terminology,
it explains concepts clearly and provides examples for each.

## Numerical JavaScript

Ten years from now,
I believe that JavaScript (or a derivative like TypeScript)
will have supplanted Python and R
as the language of choice for people doing leading-edge open scientific computing,
because no matter what else programmers use,
they eventually have to learn JavaScript.
More specifically,
I expect that the 5-15% of scientists who are early adopters of new technology
will bypass single-purpose languages like Julia
in favor of the one they already have to master
to create websites and use things like [D3](https://d3js.org/).
And with major players like Microsoft, Google, and Facebook all working hard
to make general-purpose JavaScript faster,
it will be harder and harder for niche players to keep up.
