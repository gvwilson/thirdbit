---
title: "Ideas"
layout: page
---

Someday I hope I'll have a chance to tackle one of these projects---I think
they would all be fun to do and would make the world a better place:

- [Software Engineering: Compassion, Evidence, Process, and Tools]({{'/ideas/secept/' | relative_url}})
- [Leadership Skills for Open Science]({{'/ideas/leadership/' | relative_url}})
- [Harper-Lite: Simple Lesson Discovery and Aggregation][harper]

I'd like to do a lot of other things as well,
but the best productivity tip I ever got
was to keep a "to don't" list of
things that you are *not* going to do
because life is too short
and you already have too much on the go.
Here's mine:

-   [What I Would Build If I Still Wrote Software](#what-i-would-build-if-i-still-wrote-software)
-   [What I Would Study If I Still Did Research](#what-i-would-study-if-i-still-did-research)
-   [What I Would Write If I Was Smarter Than I Am](#what-i-would-write-if-i-was-smarter-than-i-am)
-   [What Else I Would Like](#what-else-i-would-like)

## What I Would Build If I Still Wrote Software

**A blocks-based tool for data science.**
:   [Scratch][scratch] is the most effective tool we have for teaching programming to newcomers of all ages
    because it reduces [cognitive load][cognitive-load] on learners.
    [TidyBlocks][tidyblocks] was an attempt to replicate its success for data science,
    but we couldn't get funding
    and clickable blocks couldn't represent operations like joins in a natural way.
    A dataflow tool based on [Node-RED][node-red] would probably do better;
    there has been [some preliminary work][node-red-danfo],
    and I think it's very promising.

**A computational notebook that includes a drawing tool.**
:   The workflow for putting hand-drawn (vector) diagrams into notebooks is clumsy:
    open drawing tool, save file, add reference to notebook, render, curse, re-draw, re-render...
    I'd like to be able to click on a diagram in a notebook and edit it in place
    just like I can in Word or Google Doc.
    There are [several][draw-io] [good][excalidraw] open source vector drawing tools out there,
    and the SVG could either be embedded in the notebook document or stored in a side file.

**Diff and merge for SVG and CSV.**
:   While we're talking about drawing,
    I think developers would be much (much) more likely to include diagrams in their documentation
    if they could diff and merge those diagrams as easily as they do text.
    GitHub has supported a [split-pane view][github-svg-diff] for years,
    but it doesn't automatically highlight differences or help you merge them
    the way punchard emulators (i.e., programmers' other editing tools) have done for decades.
    I'd be almost as grateful for a tool to diff and merge CSV files
    that understood columns as well as rows.

**Browsercast.**
:   It's been ten years since I first wanted to be able to add a voiceover to an HTML slideshow.
    I still want it,
    but these days I'd like to be able to replay a computational notebook with commentary as well.
    We came close a couple of times, but never quite got there;
    playback is straightforward,
    but tools to edit and sync the audio require more thought.
    Given recent advances in text-to-speech technology,
    this one may now be moot.

## What I Would Study If I Still Did Research

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

**How much software would pass a Moses Test?**
:   [Robert Moses][robert-moses] reshaped New York City and surrounding areas;
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
that draw on alternatives to the *Freakonomics* view of the world---my
favorites are [listed here]({{ '/reading/' | relative_url }}).
But asking a programmer who has never done a civics course
to read nine thousand pages about something they're not yet sure is real
is functionally equivalent to telling them to piss off.
We need something that tells a story that coders will feel smarter for having heard.
We need what Sarah Kendzior, Zeynep Tufekci, and N.K. Jemisin would write
if they had six months and some great music to listen to.
Call it *Sex and Drugs and Guns and Code: What Everyone in Tech Needs to Know About Politics, Economics, Justice, and Power*,
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

## What Else I Would Like

I'd like to write these, but I'd be just as happy to read 'em...

**A Catalog of Errors**
:   Most programmers spend a large part of their time debugging,
    but most books only show working code,
    and never discuss how to prevent, diagnose, and fix errors.
    [Most](http://www.amazon.com/Debugging-Indispensable-Software-Hardware-Problems/dp/0814474578/)
    [books](http://www.amazon.com/Debugging-Thinking-Multidisciplinary-Approach-Technologies/dp/1555583075/)
    [ostensibly](http://www.amazon.com/Debug-It-Prevent-Pragmatic-Programmers/dp/193435628X/)
    [about](http://www.amazon.com/The-Developers-Guide-Debugging-Edition/dp/1470185520/)
    [debugging](http://www.amazon.com/The-Art-Debugging-GDB-Eclipse/dp/1593271743/)
    are high-level handwaving,
    user guides for particular debugging tools,
    or [out of date](http://www.amazon.com/Find-Bug-Book-Incorrect-Programs/dp/0321223918/).
    The [one notable exception](http://www.amazon.com/Why-Programs-Fail-Second-Edition/dp/0123745152/)
    is an excellent read,
    but too advanced for most undergraduates.
    This book would fill that gap by combining an exploration of how debugging tools actually work
    with dozens of case studies showing how to apply them to real-world problems.
    Along the way,
    it would present examples of what programmers can do to handle errors gracefully,
    from data structure repair to automatically restarting servers.

**Computing and the Law: A Guide for the Perplexed**
:   The legal aspects of software have always been complicated;
    the web has done nothing to make them simpler.
    This book would help programmers understand the rules they have to live with
    by tracing the historical development of patents, copyrights, privacy, and professional liability
    from the Industrial Revolution to the present day.
    Aimed squarely at people with no prior exposure to legal terminology,
    it would explain concepts clearly and provides examples for each.

[cognitive-load]: http://teachtogether.tech/en/index.html#s:architecture-load
[draw-io]: https://app.diagrams.net/
[economics-everyone]: https://isbndb.com/book/9780745335773
[excalidraw]: https://excalidraw.com/
[flyover]: https://isbndb.com/book/9781250189998
[github-svg-diff]: https://github.blog/2014-10-06-svg-viewing-diffing/
[humanizing-economy]: https://www.newsociety.com/Books/H/Humanizing-the-Economy
[lower-ed]: https://isbndb.com/book/9781620974384
[node-red]: https://nodered.org/
[node-red-danfo]: https://www.youtube.com/watch?v=9KToLbF3ZgM
[owning-earth]: https://isbndb.com/book/9781620402917
[peoples-walmart]: https://www.versobooks.com/books/2822-the-people-s-republic-of-walmart
[robert-moses]: https://en.wikipedia.org/wiki/Robert_Moses
[scratch]: https://scratch.mit.edu/
[seeing-like-state]: https://isbndb.com/book/9780300078152
[spirit-level]: https://isbndb.com/book/9781608193417
[tidyblocks]: https://tidyblocks.tech/
[tidynomicon]: https://tidynomicon.github.io/tidynomicon/
[twitter-tear-gas]: https://isbndb.com/book/9780300234176
