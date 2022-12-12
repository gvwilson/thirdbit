---
title: "Ideas"
layout: page
---

Someday I hope I'll have a chance to tackle these projects---they would be fun to do
and would make the world a better place:

- [Sex and Drugs and Guns and Code](./sdgc/)
- [Leadership Skills for Open Science](./leadership/)
- [Software Engineering: Compassion, Evidence, Process, and Tools](./secept/)
- [Harper-Lite: Simple Lesson Discovery and Aggregation](./harper/)

I'd like to do a lot of other things as well,
but the best productivity tip I ever got
was to keep a "to don't" list of
things that you are *not* going to do
because life is too short
and you already have too much on the go.
Parts of mine are below;
the rest are in [my list of unwritten books]({{'/not-on-the-shelves/' | relative_url}}).

## What I Would Build

**A drag-and-drop tool for teaching data science.**
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

**Diff and merge for SVG, CSV, and office documents.**
:   While we're talking about drawing,
    I think developers would be much (much) more likely to include diagrams in their documentation
    if they could diff and merge those diagrams as easily as they do text.
    GitHub has supported a [split-pane view][github-svg-diff] for years,
    but it doesn't automatically highlight differences or help you merge them
    the way punchard emulators (i.e., programmers' other editing tools) have done for decades.
    I'd be almost as grateful for a tool to diff and merge CSV files
    that understood columns as well as rows,
    and for one that would handle [LibreOffice][libreoffice] documents.

**Browsercast.**
:   It's been over ten years since I first wanted to be able to add a voiceover to an HTML slideshow.
    I still want it,
    but these days I'd like to be able to replay a computational notebook with commentary as well.
    We came close a couple of times, but never quite got there;
    playback is straightforward,
    but tools to edit and sync the audio require more thought.

## What I Would Study

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

[cognitive-load]: http://teachtogether.tech/en/index.html#s:architecture-load
[draw-io]: https://app.diagrams.net/
[excalidraw]: https://excalidraw.com/
[github-svg-diff]: https://github.blog/2014-10-06-svg-viewing-diffing/
[libreoffice]: https://www.libreoffice.org/
[node-red]: https://nodered.org/
[node-red-danfo]: https://www.youtube.com/watch?v=9KToLbF3ZgM
[scratch]: https://scratch.mit.edu/
[tidyblocks]: https://tidyblocks.tech/
[tidynomicon]: https://tidynomicon.github.io/tidynomicon/
