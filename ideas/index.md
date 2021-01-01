---
title: "Ideas"
layout: page
---

The most effective productivity strategy I ever learned was
to keep a "to don't" list of things that would be fun and worthwhile
but which you are *not* going to do because life is too short
and you already have too much on the go.
Here's mine.

-   [What I Would Do If I Still Did Research](#what-i-would-do-if-i-still-did-research)
-   [What I Would Build If I Still Wrote Software](#what-i-would-build-if-i-still-wrote-software)
-   [What I Would Write If I Was Smarter Than I Am](#what-i-would-write-if-i-was-smarter-than-i-am)
-   [What Else I Would Write](#what-else-i-would-write)
-   [What I Would Organize If I Still Organized Things](#what-i-would-organize-if-i-still-organized-things)

## What I Would Do If I Still Did Research

I never had the patience or diligence to be a good researcher,
but I still have lots of questions that I would like answered.

**Are programmers who use version control more productive that programmers who don't?**
:   This may seem too obvious to be worth investigating,
    but what I really want to do is calibrate and compare different ways to measure productivity.
    If a method *doesn't* find that version control helps,
    there's something wrong with the method.
    This study would compare three or four different approaches,
    and thereby help the research community agree on what to measure and how
    when tackling cases that *aren't* obvious.

**Can we assess students' proficiency with tools by watching screencasts of their work?**
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

**Does calibrated peer review improve the quality of novices' programmers code?**
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

**How well do data scientists agree with each other about the correctness of analyses?**
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

**Do novices learn data science faster or better using blocks or text?**
:   Multiple studies have shown that novices learn programming faster using blocks-based tools like Scratch
    than using text-based programming languages.
    Is the same true for data science?
    The study subjects would be high school students preparing for something like the AP Stats exam,
    and the blocks would implement the operations in the tidyverse.
    (One of my summer interns is building a tool so that we can study this.
    If you're a JavaScript programmer and you want to help, please get in touch.)

**How much software would pass a Moses Test?**
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

## What I Would Build If I Still Wrote Software

**A computational notebook for blocks-based programming.**
:   R Markdown, Stencila, and the Jupyter notebook are great ways to tell dynamic stories with and about code.
    I'd really like a notebook whose code sections were built with blocks rather than text.

**A computational notebook that includes a drawing tool.**
:   And while we're at it, the workflow for putting hand-drawn (vector) diagrams into notebooks is pretty clumsy.
    Open drawing tool, save file, add reference to notebook, render, curse, re-draw, re-render...
    I'd like to be able to click on a diagram in a notebook and edit it in place
    just like I can in Word or Google Doc.
    There are several good open source JavaScript vector drawing tools out there,
    and the SVG could either be embedded in the notebook document or stored in a side file.

**[Browsercast]({{ '/browsercast/' | relative_url }}).**
:   It's been almost ten years since I first wanted to be able to add a voiceover to an HTML slideshow.
    I still want it,
    but these days I'd like to be able to replay a computational notebook with commentary as well.
    We came close a couple of times, but never quite got there;
    playback is straightforward,
    but tools to edit and sync the audio require more thought.

**A lightweight lesson aggregation tool.**
:   Instead of building yet another repository for lessons or trying to get people to use a single template,
    it would probably be more useful to
    [aggregate metadata about the lessons they already have](https://github.com/gvwilson/harper).

**Tutorial implementations of common software tools.**
:   *[Software Tools](http://www.amazon.com/Software-Tools-Brian-W-Kernighan/dp/020103669X/)*
    and *[its sequel](http://www.amazon.com/Software-Tools-Pascal-Brian-Kernighan/dp/0201103427/)*
    taught my generation how to design software
    by showing us how to create small versions of the very tools we were using.
    I'd like to do the same exercise using JavaScript, JSON, and HTTP
    instead of C, ASCII strings, and standard I/O.
    Mary Rose Cook's [Gitlet](http://gitlet.maryrosecook.com/) is a beautiful example of what this might look like;
    I want to do the same thing for eslint, NPM, and the like
    and then use them to teach software architecture.

**A single-pass LaTeX compiler.**
:   Because we can fit an entire encyclopedia into memory these days
    and I am *so* done with writing Makefiles to run LaTeX two or three times
    to update numbered cross-references.

## What I Would Write If I Was Smarter Than I Am

Everything above is less important than what I would write if I was smarter than I am.
Most of the young programmers I know have only ever been exposed to one worldview:
the toxic strain of neoliberal capitalism favored by venture capitalists and their gushing fans in the tech media.
As inequality widens,
as white nationalism comes roaring back on stage,
as we do everything in our power to make climate change *worse*,
and as companies like Twitter, Facebook, and Shopify tie themselves in ever-more-contorted knots
to avoid taking responsibility for their actions,
most programmers don't have the intellectual tools needed
to understand what's gone wrong and how we might fix it.
Why do gender and racial discrimination persist despite their economic inefficiency?
Why do "flat" organizations make power imbalances worse rather than better?
How does regulatory capture work?
Why do Americans keep shooting one another?
And why is Boris Johnson?

Lots of books give cogent answers to these questions
that draw on alternatives to the *Freakonomics* view of the world---my favorites are [listed here]({{ '/reading/' | relative_url }}).
But asking a programmer who has never done a civics course
to read nine thousand pages about something they're not yet sure is real
is functionally equivalent to telling them to piss off.
We need something that tells a story that coders will feel smarter for having heard.
We need what Sarah Kendzior, Zeynep Tufekci, and N.K. Jemisin would write
if they had six months and some great music to listen to.
Call it *Sex and Drugs and Guns and Code: What Everyone in Tech Needs to Know About Politics, Economics, and Power*,
get *Wired* to tell everyone it's the new new thing,
and you just might change the world.

See also:

-   [Positive and Negative Openness]({{ '/2019/05/11/positive-and-negative-openness/' | relative_url }})
-   [Afraid of Change]({{ '/2018/11/24/afraid-of-change/' | relative_url }})
-   [Cigarettes and Shopify]({{ '/2018/05/06/cigarettes-and-shopify/' | relative_url }})

But more importantly, please read:

1. Tressie McMillan Cottom: *[Lower Ed][lower-ed]: The Troubling Rise of For-Profit Colleges in the New Economy*.
   Describes how a large part of the educational sector in the US exists
   to translate government grants into personal debt for the poor and private profit for the rich.

1. Sarah Kendzior: *[The View From Flyover Country][flyover]*.
   Essential reading about the rise of authoritarian kleptocracy in the United States.

1. Andro Linklater: *[Owning the Earth][owning-earth]*.
   The idea that individuals can own land is a lot younger than most people realize,
   and its emergence holds a lot of lessons for today's debates over intellectual property.

1. Leigh Phillips and Michal Rozworski: *[The People's Republic of Walmart][peoples-walmart]*.
   Most of the world's economic activity occurs within large companies like Walmart and Amazon.
   They all use central planning:
   why doesn't the economy as a whole,
   and can we make the efficiencies of planning democratically accountable?

1. John Restakis: *[Humanizing the Economy][humanizing-economy]*.
   A history of the co-operative movement and a blueprint for its future.

1. James C. Scott: *[Seeing Like a State][seeing-like-state]*.
   Explains why large organizations always prefer uniformity over productivity,
   and the price people pay for this.

1. Jim Stanford: *[Economics for Everyone][economics-everyone]*.
   A useful antidote to the abstract, unquestioning way that neoliberal economics is usually presented.

1. Zeynep Tufekci: *[Twitter and Tear Gas][twitter-tear-gas]*.
   A nuanced look at how social media is and isn't changing politics and protest.

1. Richard Wilkinson and Kate Pickett: *[The Spirit Level][spirit-level]*.
   An evidence-based exploration of how and why greater equality is better for everyone.

## What Else I Would Write

### A Catalog of Errors

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

### The Undergraduate Operator's Manual

What effect does pulling an all-nighter have on the quality of your work?
How do people absorb and retain knowledge?
What are some good ways to run a project meeting,
and how can you get people to actually pull their weight?
Every undergraduate has to deal with these issues and a hundred others,
but most of the time,
they are expected to rediscover or reinvent methods themselves.
This textbook for a one-semester course puts solutions in one place,
and by doing so teaches a lot about physiology, psychology, and organizational behavior.

### Computing and the Law: A Guide for the Perplexed

The legal aspects of software have always been complicated;
the web has done nothing to make them simpler.
This book seeks to help programmers understand the rules (or lack thereof)
they have to live with
by tracing the historical development of patents, copyrights, privacy, and professional liability
from the Industrial Revolution to the present day.
Aimed squarely at people with no prior exposure to legal terminology,
it explains concepts clearly and provides examples for each.

## What I Would Organize If I Still Organized Things

*Please see [this post from December 2019]({{ '/2019/12/30/method-motive-opportunity/' | relative_url }}) for ideas about a precursor to this workshop.*

### Background

Many people in open communities have technical knowledge, enthusiasm, and good intentions,
but no experience engineering structural change in organizations.
Pushing through changes to the curriculum,
nurturing a user group that can sustain itself,
and removing bias from hiring practices
all require skills that most scientists and programmers have never learned.
Fortunately, we do not have to invent these skills ourselves:
many groups before us have made the kinds of changes we now seek
and can teach us how to be more effective.

### Proposal

We propose a four-day workshop.
In the first three days,
participants rotate through six half-day training sessions;
on the final day they work in small groups to plan their next steps.
The topics listed below give the flavor of the workshop topics;
the final list would be put together in consultation with community leaders
and the participants themselves:

-   Strategies for institutional change (e.g., Manns & Rising's *[Fearless Change][fearless-change]*)
    to give people a toolbox for acting on what they know.

-   Community organization (e.g., Brown's *[Building Powerful Community Organizations][bpco]*),
    which lays out the steps needed to build an effective grassroots organization.

-   Marketing (e.g., based on Kuchner's *[Marketing for Scientists][marketing-for-scientists]*)
    so that people learn how to match what they want with what decision makers think they need.

-   Leadership skills (e.g., the [Raw Signal Group][raw-signal]'s training)
    so that they can get people pulling in the same direction.

-   How to be a good ally (e.g., [Aurora's workshop on ally skills][ally-skills])
    so that they can use their power and influence to support people who are targets of discrimination.

-   Personal digital security (e.g., [the Electronic Frontier Foundation's training materials][security]),
    because online harassment is unfortunately now a fact of life,
    and people in visible roles need to safeguard themselves against it.

Participants would be selected based on:

1.  A previously-demonstrated commitment to inclusive open communities.
2.  Career stage: we would give preference to people who are likely to be able to act on what they learn
    in the 1-2 years following the workshop.
3.  Reach: we would give preference to people who live and work outside existing hotbeds of open activity.

### Benefits

Many people share a vision of a better kind of open:
one that is inclusive *and* effective.
The more skills they have for organizing and leading,
the sooner that vision will be realized.

### Budget

1.  Each instructor would teach for half a day (either morning or afternoon)
    and have the other half of the day off
    for three consecutive days.
2.  Each class would have 20 participants at a time,
    so the entire workshop would have 60 participants.
3.  The budget assumes $6,000 for 3 days of training plus $2,000 in expenses per instructor.
4.  Most organizing will be done by volunteers,
    but the budget includes 20 days of paid support staff time as well.
5.  Participants will be charged $500
    and will be required to cover their own travel and accommodation costs
    as well as breakfast and dinner.
6.  One third of participants will be offered partial financial support
    and will not be charged registration.

<table class="table table-striped">
<tr>
  <td><strong>Item</strong></td>
  <td align="right"><strong>Each</strong></td>
  <td align="right"><strong>Number</strong></td>
  <td align="right"><strong>Total</strong></td>
</tr>
<tr>
  <td>Venue (per day)</td>
  <td align="right">$1,500</td>
  <td align="right">4</td>
  <td align="right">$6,000</td>
</tr>
<tr>
  <td>Instructors</td>
  <td align="right">$8,000</td>
  <td align="right">6</td>
  <td align="right">$48,000</td>
</tr>
<tr>
  <td>Lunch/snacks (per person per day)</td>
  <td align="right">$30</td>
  <td align="right">4 &times; 60</td>
  <td align="right">$7,200</td>
</tr>
<tr>
  <td>Support/admin staff (per day)</td>
  <td align="right">$500</td>
  <td align="right">20</td>
  <td align="right">$10,000</td>
</tr>
<tr>
  <td>Travel scholarships</td>
  <td align="right">$800</td>
  <td align="right">20</td>
  <td align="right">$16,000</td>
</tr>
<tr>
  <td><em>Registration fee (per person)</em></td>
  <td align="right"><em>- $500</em></td>
  <td align="right">40</td>
  <td align="right"><em>- $20,000</em></td>
</tr>
<tr>
  <td colspan="3"><strong>Total</strong></td>
  <td align="right"><strong>$67,200</strong></td>
</tr>
</table>

I think a workshop like this is a logical and necessary follow-on
to things like [the Carpentries' instructor training][carpentries-training]
and the [AAAS community engagement program][aaas-program].
Almost without exception,
we think and act as if we're always going to be outside the room where decisions are made,
waving our placards or trying to get someone's attention long enough to explain that better is possible
and we're already built it
and could they please give it a try.
If we truly want a better world,
we need to be *inside* the room when the vote is called.

Training like this is,
I believe,
a necessary step toward getting advocates of openness elected
to school boards and city councils and professional societies.
Creationists, gunaholics, fossil fuel addicts, and anti-choicers have been doing it for many years to great effect;
do we really care so much less about our issues that we're not willing to do it too?

See also [Maciej Ceglowski's work to secure political campaigns in the US][ceglowski],
which is a great example of how to engage with power.
And please note that
I would be happy to run an online one-day training class on [how to teach][t3]
for people who are organizing and running workshops on digital self-defense.
Please [email me](mailto:gvwilson@third-bit.com) if you're interested.

[aaas-program]: https://www.aaas.org/programs/community-engagement-fellows
[ally-skills]: https://frameshiftconsulting.com/ally-skills-workshop/
[bpco]: https://isbndb.com/book/0977151808
[carpentries-training]: https://carpentries.github.io/instructor-training/
[ceglowski]: https://idlewords.com/2019/05/what_i_learned_trying_to_secure_congressional_campaigns.htm
[fearless-change]: https://fearlesschangepatterns.com/
[marketing-for-scientists]: https://islandpress.org/books/marketing-scientists
[raw-signal]: https://www.rawsignal.ca/
[security]: https://sec.eff.org/
[t3]: http://teachtogether.tech

[lower-ed]: https://isbndb.com/book/9781620974384
[flyover]: https://isbndb.com/book/9781250189998
[owning-earth]: https://isbndb.com/book/9781620402917
[peoples-walmart]: https://www.versobooks.com/books/2822-the-people-s-republic-of-walmart
[humanizing-economy]: https://www.newsociety.com/Books/H/Humanizing-the-Economy
[seeing-like-state]: https://isbndb.com/book/9780300078152
[economics-everyone]: https://isbndb.com/book/9780745335773
[twitter-tear-gas]: https://isbndb.com/book/9780300234176
[spirit-level]: https://isbndb.com/book/9781608193417
