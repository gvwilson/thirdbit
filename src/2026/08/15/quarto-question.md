---
title: "A Quarto Question (or Six)"
date: 2026-08-15
category: education
---
I am converting the notes for "Managing Research Software Projects" from McCole to Quarto.
Most of the changes have gone smoothly, but I'm stuck on a few things and would appreciate guidance.
For reference, the materials are in [this repository][repo] and you can view the rendered version [here][ghp].

1.  The landing page shows the contents of `index.qmd` (which is good)
    but that page shows up as entry #1 in the table of contents (which is bad).
    I have tried using a `# Title` heading in `index.qmd` instead of a `title` field in the YAML frontmatter,
    and/or adding`.unnumbered`, `.toc-ignore`, and other classes to that H1 heading,
    but those don't achieve what I want.

1.  Each page that has bibliographic citations lists references at the bottom of that page
    (see for example the [Project Health][mrsp-health] page).
    I don't want this: I want all citations to link to the appropriate entry in the bibliography page
    (e.g., [this page][mrsp-bib] in the example project).

1.  Each chapter in the tutorial is in a subdirectory of the root,
    e.g., `./intro/index.qmd` is rendered as `./docs/intro/index.html`.
    I want to have a slide deck alongside each chapter so that (for example)
    `./intro/slides.qmd` would generate `./docs/intro/slides.html`.
    (Each subdirectory is going to contain images, code fragments, and other artefacts
    that will be included in both the `index.qmd` prose and the `slides.qmd` slides.
    I find it easier to manage these if the two Markdown files are siblings.)
    I've tried setting this up a couple of different ways, but nothing has worked.
    What do I add to the frontmatter of `slides.qmd` to tell Quarto "these are slides",
    where do I put a custom template for those slides,
    and what do I add to the `_quarto.yml` file to create a "Slides" section in the table of contents
    with links to these files?
    Or am I going about this in completely the wrong way?

1.  When Quarto renders the tutorial, it create a 1.1Mbyte directory called `./docs/site_libs`
    with various supporting files (JavaScript, CSS, fonts, etc.).
    Can I configure Quarto to (a) stop it from creating this directory
    and (b) have HTML files refer to some absolute URL to find those files instead?
    I want to do this because I'm going to put the generated files here in the Third Bit site,
    and want to share one copy of the supporting files rather than have one per workshop.
    (I'm likely to have seven or eight workshops served from Third Bit once I'm done converting,
    and 8Mbyte of redundant files makes me squeamish.)

1.  I don't like the way Quarto's default CSS lays out description lists;
    for accessibility reasons I'd like notes to be rendered at the same size as main text,
    and there are probably several other small changes to layout that I'm going to want as well.
    What's the best way to manage custom CSS given that I'm going to generate HTML separately
    for several different projects,
    but then serve them all from one site as siblings as described above?
    (I'm less worried about duplication here because the custom CSS will only be a few kilobytes,
    so this is much less urgent than the `site_libs` issue.)

1.  Finally, the glossary for the workshop is in `./glossary/index.qmd`,
    and I use a little bit of custom Lua in `./bin/g.lua` to handle the rendering.
    I'd like to store the glossary in [Glosario][glosario] format instead,
    and generate HTML from that.
    I think I know how to do this,
    but if anyone has already built what I'm after,
    I'd be grateful for a pointer.

If you have solutions to any of these problems, please [give me a shout][email];
thanks in advance for your help.

[email]: mailto:gvwilson@third-bit.com
[ghp]: https://gvwilson.github.io/mrsp/
[glosario]: https://glosario.carpentries.org/
[mrsp-bib]: https://gvwilson.github.io/mrsp/bibliography/
[mrsp-health]: https://gvwilson.github.io/mrsp/health/
[repo]: https://github.com/gvwilson/mrsp
