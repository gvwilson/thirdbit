---
title: "Six for the To-Don't List"
date: 2022-12-28
year: 2022
---

I was a professor from 2007 to 2010.
My grad students had a pretty rough time:
all five of the grant proposals I made in those 40 months were turned down,
which meant none of the projects I'd envisioned for them ever got off the ground.
I've thought occasionally about going back and trying again,
but every time I bring it up my spouse's response is,
"Look, if you want a divorce, just say that you want a divorce."

I can't stop thinking about things I want to build,
though,
both because they'd be useful and so that we could study their use and impact.
I have put the <s>six</s> <s>seven</s> <s>eight</s> nine below on [my to-don't list][to-dont-post],
but if you're minded to tackle any of them,
please give me a shout.

1. **[A lesson aggregation system][harper-lite]**.
   Instead of building yet another repository for lessons,
   let's draw inspiration from RSS
   (which I think is right up there with "view source" as an example of what the web *could* be)
   and create a way to find and aggregate lessons.

2. **A browser-based drag-and-drop tool for data analytics**.*
   The [TidyBlocks][tidyblocks-repo] project [ground to a halt][tidyblocks-post]
   due to a lack of funding and some difficult technical challenges.
   I still believe in the idea, though,
   and think that using [Node-RED] as a starting point instead of [Blockly][blockly]
   would circumvent the technical challenges,
   give non-programmers an interface they could use immediately,
   *and* be a natural successor to [Yahoo! Pipes][yahoo-pipes].

3. **A WYSIWYG computational notebook**.
   In [a better universe than ours][notebook-post]
   someone has already built a plugin for [LibreOffice][libreoffice]
   that leverages the [the Jupyter messaging protocol][jupyter-protocol],
   and the 99% of our species who prefer WYSIWYG to Markdown plus YAML plus compilation
   can create the reports they want the way they want to.
   It's not too late…

4. **[Browsercast][browsercast],**
   which would replay an HTML slideshow in sync with a voiceover.
   Tools like Wasim Lorgat's [SVG replay][svg-replay] and [Scrimba][scrimba]
   have made me more certain than ever that
   we shouldn't turn text and HTML into video streams:
   we should share them in their original form
   so that people can search them, style them, copy and paste them,
   and feed them to screenreaders and other accessibility aids.

5. **[Use case maps][use-case-maps-post]**.
   Given an SVG diagram showing the elements of your system that produce log entries,
   be they classes or microservices,
   and UUIDs to identify the descendents of initiating messages,
   this tool would draw the diagram we all eventually wind up creating by hand
   to show what happens when and where.

6. A **[Journal of Comprehensible Explanations][jce-post]**.
   We've been writing reviews of software engineering research results
   at [It Will Never Work in Theory][nwit]
   for years
   with no noticeable impact on what practitioners believe
   or how the subject is taught.
   The lightning talks we organized in 2022 were popular,
   but I think a set of [research vignettes][vignette-post] could help as well.
   The trick would be getting people tenure points for writing them;
   I think a journal (or a track at a major software engineering conference)
   might do the trick.

7. **A superset of [Elm][elm] for systems programming.**
   I've been fascinated by pure functional programming
   since I first encountered it in the mid-1980s.
   I'd really like to do a version of [*Software Design by Example*][sdxjs]
   in a pure functiona language,
   but want one that is to [Haskell][haskell] what Pascal was to Algol-68:
   smaller, simpler, and more accessible.
   I think a superset of Elm with libraries for creating files and directories
   would be just about perfect.

8. **Diff and merge for SVG, CSV, and office documents.**
   I think developers would be much (much) more likely to include diagrams in their documentation
   if they could diff and merge those diagrams as easily as they do text.
   GitHub has supported a [split-pane view][github-svg-diff] for years,
   but it doesn't automatically highlight differences or help you merge them
   the way punchard emulators (i.e., programmers' other editing tools) have done for decades.
   I'd be almost as grateful for a tool to diff and merge CSV files
   that understood columns as well as rows,
   and even more so for one that would handle [LibreOffice][libreoffice] documents.

9. **A caravan defense game**.
   [*Kingdom Rush: Frontiers*][kingdom-rush-frontiers] is my favorite game
   of the last ten years,
   but I'm increasingly uninterested in killing monsters.
   I want a game where I build towers to *defend* the travelers
   from bandits, predators, natural disasters, swindlers, and other threats.
   It has nothing to do with software engineering,
   but I think it would be a lot of fun.

[blockly]: https://developers.google.com/blockly/
[browsercast]: {{site.links.browsercast}}
[elm]: https://elm-lang.org/
[github-svg-diff]: https://github.blog/2014-10-06-svg-viewing-diffing/
[harper-lite]: {{'/ideas/harper/' | relative_url}}
[haskell]: https://www.haskell.org/
[jce-post]: {{'/2022/11/20/journal-of-comprehensible-explanations/' | relative_url}}
[jupyter-protocol]: https://jupyter-client.readthedocs.io/en/latest/
[kingdom-rush-frontiers]: https://www.ironhidegames.com/Games/kingdom-rush-frontiers
[libreoffice]: https://www.libreoffice.org/
[node-js]: https://nodejs.org/
[node-red]: https://nodered.org/
[notebook-post]: {{'/2022/11/13/the-notebook-not-taken/' | relative_url}}
[nwit]: https://neverworkintheory.org/
[scrimba]: https://scrimba.com/
[sdxjs]: {{'/sdxjs/' | relative_url}}
[svg-replay]: https://wasimlorgat.com/tils/how-to-share-terminal-demos-as-razor-sharp-animated-svg.html
[tidyblocks-post]: {{'/2021/07/22/whatever-happened-to-tidyblocks/' | relative_url}}
[tidyblocks-repo]: https://github.com/tidyblocks/tidyblocks
[to-dont-post]: {{'/2018/11/28/to-dont-list/' | relative_url}}
[use-case-maps-post]: {{'/2018/12/27/use-case-maps/' | relative_url}}
[vignette-post]: {{'/2022/08/14/ese-vignette/' | relative_url}}
[yahoo-pipes]: https://en.wikipedia.org/wiki/Yahoo!_Pipes
