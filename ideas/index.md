---
title: "Ideas"
layout: page
---

The best productivity tip I ever got
was to keep a "to don't" list of
things that you are *not* going to do
because life is too short
and you already have too much on the go.
The ones I'd like to tackle most would be fun to do
and would make the world a better place:

- [Sex and Drugs and Guns and Code](./sdgc/)
- [Leadership Skills for Open Science](./leadership/)
- [Software Engineering: Compassion, Evidence, Process, and Tools](./secept/)
- [Harper-Lite: Simple Lesson Discovery and Aggregation](./harper/)

Others are listed below
and in [my list of unwritten books][unwritten]
and [this summary of software engineering research ideas][se-ideas-post].
If you are already working on any of these,
please let me know.

## What I Won't Build

A browser-based drag-and-drop tool for data analytics.
:   The [TidyBlocks][tidyblocks-repo] project [ground to a halt][tidyblocks-post]
    due to a lack of funding and some difficult technical challenges.
    I still believe in the idea, though,
    and think that using [Node-RED] as a starting point instead of [Blockly][blockly]
    would circumvent the technical challenges,
    give non-programmers an interface they could use immediately,
    *and* be a natural successor to [Yahoo! Pipes][yahoo-pipes].

A WYSIWYG computational notebook.
:   In [a better universe than ours][notebook-post]
    someone has already built a plugin for [LibreOffice][libreoffice]
    that leverages the [the Jupyter messaging protocol][jupyter-protocol],
    and the 99% of our species who prefer WYSIWYG to Markdown plus YAML plus compilation
    can create the reports they want the way they want to.
    It's not too late…

[Browsercast][browsercast],
:   which would replay an HTML slideshow in sync with a voiceover.
    Tools like Wasim Lorgat's [SVG replay][svg-replay] and [Scrimba][scrimba]
    have made me more certain than ever that
    we shouldn't turn text and HTML into video streams:
    we should share them in their original form
    so that people can search them, style them, copy and paste them,
    and feed them to screenreaders and other accessibility aids.

[Use case maps][use-case-maps-post].
:   Given an SVG diagram showing the elements of your system that produce log entries,
    be they classes or microservices,
    and UUIDs to identify the descendents of initiating messages,
    this tool would draw the diagram we all eventually wind up creating by hand
    to show what happens when and where.

A [Journal of Comprehensible Explanations][jce-post].
:   We've been writing reviews of software engineering research results
    at [It Will Never Work in Theory][nwit]
    for years
    with no noticeable impact on what practitioners believe
    or how the subject is taught.
    The lightning talks we organized in 2022 were popular,
    but I think a set of [research vignettes][vignette-post] could help as well.
    The trick would be getting people tenure points for writing them;
    I think a journal (or a track at a major software engineering conference)
    might do the trick.

A superset of [Elm][elm] for systems programming.
:   I've been fascinated by pure functional programming
    since I first encountered it in the mid-1980s.
    I'd really like to do a version of [*Software Design by Example*][sdxjs]
    in a pure functiona language,
    but want one that is to [Haskell][haskell] what Pascal was to Algol-68:
    smaller, simpler, and more accessible.
    I think a superset of Elm with libraries for creating files and directories
    would be just about perfect.

Diff and merge for SVG, CSV, and office documents.
:   While we're talking about drawing,
    I think developers would be much (much) more likely to include diagrams in their documentation
    if they could diff and merge those diagrams as easily as they do text.
    GitHub has supported a [split-pane view][github-svg-diff] for years,
    but it doesn't automatically highlight differences or help you merge them
    the way punchard emulators (i.e., programmers' other editing tools) have done for decades.
    I'd be almost as grateful for a tool to diff and merge CSV files
    that understood columns as well as rows,
    and for one that would handle [LibreOffice][libreoffice] documents.

A portfolio of [learner personas][learner-personas].
:   Good lessons are written for specific learners;
    I think it would be really helpful to create a set
    that gave us shorthand names for people who want to learn programming and/or data science.

A portfolio of [concept maps][concept-maps].
:   A good lesson helps the learner build a mental model of a problem or problem domain.
    I think it would be really helpful to create a set
    that encapsulated a consensus view of the core concepts in particular topics.

A caravan defense game.
:   [*Kingdom Rush: Frontiers*][kingdom-rush-frontiers] is my favorite game
    of the last ten years,
    but I'm increasingly uninterested in killing monsters.
    I want a game where I build towers to *defend* the travelers
    from bandits, predators, natural disasters, swindlers, and other threats.
    It has nothing to do with software engineering,
    but I think it would be a lot of fun.

## What I Won't Study

I never had the patience or diligence to be a good researcher,
but I still have lots of questions.

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

[blockly]: https://developers.google.com/blockly/
[browsercast]: {{site.links.browsercast}}
[concept-maps]: {{'/ideas/concept-maps/' | relative_url}}
[draw-io]: https://app.diagrams.net/
[elm]: https://elm-lang.org/
[github-svg-diff]: https://github.blog/2014-10-06-svg-viewing-diffing/
[harper-lite]: {{'/ideas/harper/' | relative_url}}
[haskell]: https://www.haskell.org/
[jce-post]: {{'/2022/11/20/journal-of-comprehensible-explanations/' | relative_url}}
[jupyter-protocol]: https://jupyter-client.readthedocs.io/en/latest/
[kingdom-rush-frontiers]: https://www.ironhidegames.com/Games/kingdom-rush-frontiers
[learner-personas]: {{'/ideas/learner-personas/' | relative_url}}
[libreoffice]: https://www.libreoffice.org/
[node-js]: https://nodejs.org/
[node-red]: https://nodered.org/
[notebook-post]: {{'/2022/11/13/the-notebook-not-taken/' | relative_url}}
[nwit]: https://neverworkintheory.org/
[scratch]: https://scratch.mit.edu/
[scrimba]: https://scrimba.com/
[sdxjs]: {{'/sdxjs/' | relative_url}}
[se-ideas-post]: {{'/2022/08/30/research-topics/' | relative_url}}
[svg-replay]: https://wasimlorgat.com/tils/how-to-share-terminal-demos-as-razor-sharp-animated-svg.html
[tidyblocks-post]: {{'/2021/07/22/whatever-happened-to-tidyblocks/' | relative_url}}
[tidyblocks-repo]: https://github.com/tidyblocks/tidyblocks
[tidynomicon]: https://tidynomicon.github.io/tidynomicon/
[to-dont-post]: {{'/2018/11/28/to-dont-list/' | relative_url}}
[unwritten]: {{'/not-on-the-shelves/' | relative_url}}
[use-case-maps-post]: {{'/2018/12/27/use-case-maps/' | relative_url}}
[vignette-post]: {{'/2022/08/14/ese-vignette/' | relative_url}}
[yahoo-pipes]: https://en.wikipedia.org/wiki/Yahoo!_Pipes
