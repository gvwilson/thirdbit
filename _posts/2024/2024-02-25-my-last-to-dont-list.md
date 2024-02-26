---
title: "My Last To-Don't List"
date: 2024-02-25
year: 2024
---

The best productivity tip I ever got
was to keep a "to don't" list of
things that you are *not* going to do
because life is too short
and you already have too much on the go.
The ones I would most have liked to do were:

- [Sex and Drugs and Guns and Code]({{ '/ideas/sdgc/' | relative_url }})
- [Leadership Skills for Open Science]({{ '/ideas/leadership/' | relative_url }})
- [Software Engineering: Compassion, Evidence, Process, and Tools]({{ '/ideas/secept/' | relative_url }})
- [Harper-Lite: Simple Lesson Discovery and Aggregation]({{ '/ideas/harper/' | relative_url }})
- [Software Engineering Research Ideas]({{ '/ideas/research/' | relative_url }})

Others are described below and in [my list of unwritten books][unwritten];
if you ever have a chance to tackle any of them,
I hope they bring you joy.

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

[Browsercast][browsercast].
:   This tool would replay an HTML slideshow in sync with a voiceover.
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
    in a pure functional language,
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
[svg-replay]: https://wasimlorgat.com/tils/how-to-share-terminal-demos-as-razor-sharp-animated-svg.html
[tidyblocks-post]: {{'/2021/07/22/whatever-happened-to-tidyblocks/' | relative_url}}
[tidyblocks-repo]: https://github.com/tidyblocks/tidyblocks
[tidynomicon]: https://tidynomicon.github.io/tidynomicon/
[to-dont-post]: {{'/2018/11/28/to-dont-list/' | relative_url}}
[unwritten]: {{'/not-on-the-shelves/' | relative_url}}
[use-case-maps-post]: {{'/2018/12/27/use-case-maps/' | relative_url}}
[vignette-post]: {{'/2022/08/14/ese-vignette/' | relative_url}}
[yahoo-pipes]: https://en.wikipedia.org/wiki/Yahoo!_Pipes
