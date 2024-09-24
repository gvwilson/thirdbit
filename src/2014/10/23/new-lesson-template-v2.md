---
title: "A New Lesson Template, Version 2"
date: 2014-10-23
original: swc
---

*Update: this post now includes feedback from participants in the
instructor training session run at TGAC on Oct 22-23, 2014.
Please see the bottom of this page for their comments.*

Thanks to everyone for their feedback on
the first draft
of our new template for lessons.
The major suggestions were:

-   We need to explain how this template supports student experience,
    quality lesson planning, etc.  It's not clear now how compliance
    with these Markdown formatting rules will help improve teaching
    and learning.
-   The template needs to be much simpler.  As Andromeda Yelton said,
    "It just looks to me like a minefield of ways to get things
    wrong–things that have <em>nothing to do with pedagogy</em>…"
-   There needs to be a validator that authors can run locally before
    submitting changes or new lessons.  (The proposal did mention
    that `make check` would run `bin/check.py`,
    but this point needs to be more prominent.
-   Every topic should have at least one challenge, and challenges
    should be explicitly connected to specific learning objectives.
-   We need a clearer explanation of the difference between the
    reference guide (which is meant to be a cheat sheet for learners
    to take away) and the instructor's guide (which is meant to be
    tips and tricks for teaching).  We should also suggest formatting
    rules for both.
-   The instructor's guide should explicitly present each lesson's
    "legend", i.e., the story that ties it together which instructors
    gradually reveal to learners.
-   We need to decide whether the instructor's guide is a separate
    document, or whether there are call-out sections in each topic for
    instructors.  The former puts the whole story in one place, and
    helps updaters to see the whole thing when making changes; the
    latter puts it in context, and helps updaters check that the
    instructor's material is consistent with the lesson material.
-   Every topic should explicitly list the time required to teach it.
    (We should do this for topics, rather than for whole lessons,
    because people often don't get through all of the latter, which
    makes timing reports difficult to interpret.)
-   We need to make it clear that lessons must be CC-BY licensed to
    permit remixing.

With all that in mind, here's another cut at the template–as
before, we'd be grateful for comments.  Note that this post mingles
description of "what" with explanation of "why"; the final guide for
people building lessons will disentangle them to make the former
easier to follow.

Note also that Trevor Bekolay has drafted an implementation at
https://github.com/tbekolay/swc-template
for people who'd like to see what the template would look like in
practice.  There's still work to do (see below), but it's a great
start.  Thanks to Trevor, the other Trevor, Erik with a 'k', Molly,
Emily, Karin, Rémi, and Andromeda for their feedback.

## To Do

-   Some people suggested getting rid of the `web/` folder
    and have lessons load CSS, Javascript, and standard images from
    the web.  This would reduce the size of the repository, and help
    ensure consistency, but (a) a lot of people write when they're
    offline (I'm doing it right now), and (b) people may not want
    their lessons' appearance to change outwith their control.
-   We need to figure out how example programs will reference data
    files (i.e., what paths they will use).  See the notes under
    "Software, Data, and Images" below for full discussion.
-   Trevor Bekolay writes:
    <br>
    I took a stab at implementing a minimal motivation slides.
    Unfortunately this isn't very clean right now; I just included the
    &lt;section&gt; and &lt;script&gt; tags in the Markdown, which I know
    we want to avoid. I initially had the slides in a separate
    Markdown file, which is possible with reveal.js. There are a few
    weird things with this though, which we may or may not be able to
    fix, since we're limited in what we can do with Jekyll. Briefly,
    we can have the `slides.html` layout do something like
    this:
    <pre>&lt;div class="slides"&gt;&lt;section data-markdown="{% raw %}{{page.path}}{% endraw %}" data-separator="^\n\n\n" data-vertical="^\n\n"&gt;&lt;/section&gt;&lt;/div&gt;</pre>
    The only wart with this is that the Markdown file
    (i.e., `page.path`) doesn't get copied
    to `_site`. I couldn't figure out a way to do it using
    vanilla Jekyll, but it might be possible. Even if it does get
    copied, however, we might have to strip out the YAML header.

## Terms

-   A <em>lesson</em> is a complete story about some subject, typically
    taught in 2-4 hours.
-   A <em>topic</em> is a single scene in that story, typically 5-15
    minutes long.
-   A <em>slug</em> is a short identifier for something, such
    as `filesys` (for "file system").

## Design Choices

-   We define everything in terms of Markdown. If lesson authors want to
    use something else for their lessons (e.g., IPython Notebooks), it's
    up to them to generate and commit Markdown formatted according to
    the rules below.
-   We avoid putting HTML inside Markdown: it's ugly to read and
    write, and error-prone to process. Instead, we put things that
    ought to be in &lt;div&gt; blocks, like the learning objectives
    and challenge exercises, in blocks indented with
    `&gt;`, and do a bit of post-processing to attach
    the right CSS classes to these blocks.
-   Whatever Markdown-to-HTML converter we use must
    support `{.attribute}` syntax for specifying anchors
    and classes rather than the clunky HTML-in-Markdown syntax our
    current notes have to use to be compatible with Jekyll.
-   Any "extra" metadata (e.g., the human language of the lesson) will
    go into the YAML header of the lesson's index page rather than
    into a separate configuration file.

## Justification and Tutorial

The main Software Carpentry website will contain a one-page tutorial
explaining (a) how to create and update lessons and (b) how the
various parts of the template support better teaching.  A sketch of
the second of these is:

-   A standard layout so that:
    -   Lessons have the same look and feel, and can be navigated in
        predictable ways, even when they are written by different (and
        multiple) people.
    -   Contributors know where to put things when they are extending
        or modifying lessons.
    -   Content can more easily be checked.  For example, we want to
        make sure that every learning objective is matched by a
        challenge, and that every challenge corresponds to one or more
        learning objectives.
    In the longer term, a standard format will help us build tools,
    but the format <em>must</em> be justifiable in terms of short-term
    gains for instructors and learners.
-   One short page per topic: to show each learning sprint explicitly,
    and to create small chunks for recording timings.  The cycle we
    expect is:
    -   Explain the topic's objectives.
    -   Teach it.
    -   Do one or more challenges (depending on time).
-   Introductory slides: to give learners a sense of where the next
    couple or three hours are going to take them.
-   Reference guide: because everybody wants a cheat sheet.  This
    includes a glossary of terms to help lesson authors think through
    what they expect learners to be unfamiliar with, and to make
    searching through lessons easier.
-   Instructor's guide: our collected wisdom, and solutions to the
    challenge exercises.  Once lessons have been reformatted, we will
    ask everyone who teaches for us to review and update the
    instructor's guide for each lesson they taught after each
    workshop.  Note that the instructor's guide (including challenge
    solutions) will be on the web, both because we believe in
    openness, and because it's going to be publicly readable anyway.
-   Tools: because machines should check formatting rules, not people.

## Overall Layout

Each lesson is stored in a directory laid out as described
below. That directory is a self-contained Git repository (i.e.,
there are no submodules or clever tricks with symbolic links).

-   `index.md`: the home page for the lesson. (See "Home
    Page" below.)
-   `dd-slug.md`: the topics in the lesson. `dd`
    is a sequence number such as `01`, `02`, etc.,
    and `slug` is an abbreviated single-word mnemonic for the
    topic. Thus, `03-filesys.md` is the third topic in this
    lesson, and is about the filesystem. (Note that we use hyphens
    rather than underscores in filenames.) See "Topics" below.
-   `motivation.md`: slides for a short introductory
    presentation (three minutes or less) explaining what the lesson is
    about and why people would want to learn it. See "Introductory
    Slides" below.
-   `reference.md`: a cheat sheet summarizing key terms and
    commands, syntax, etc., that can be printed and given to learners.
    See "Reference Guide" below.
-   `instructors.md`: the instructor's guide for the
    lesson. See "Instructor's Guide" below.
-   `code/`: a sub-directory containing all code samples. See
    "Software, Data, and Images" below.
-   `data/`: a sub-directory containing all data files for
    this lesson. See "Software, Data, and Images" below.
-   `img/`: images (including plots) used in the lesson. See
    "Software, Data, and Images" below.
-   `tools/`: tools for managing lessons. See "Tools" below.
-   `_layouts/`: page layout templates. See "Layout" below.
-   `_includes/`: page inclusions. See "Layout" below.

## Home Page

`index.md` must be structured as follows:

```
---
layout: lesson
title: Lesson Title
keywords: ["some", "key terms", "in a list"]
---
Paragraph of introductory material.

> ## Prerequisites
>
> A short paragraph describing what learners need to know
> before tackling this lesson.

## Topics

* [Topic Title 1](01-slug.html)
* [Topic Title 2](02-slug.html)

## Other Resources

* [Introduction](intro.html)
* [Reference Guide](reference.html)
* [Instructor's Guide](guide.html)
```

<strong>Notes:</strong>

-   The description of prerequisites is prose for human consumption,
    not a machine-comprehensible list of dependencies. We may
    supplement the former with the latter once we have more experience
    with this lesson format and know what we actually want to do.  The
    block must be titled "Prerequisites" so we can detect it and style
    it properly.
-   Software installation and configuration instructions
    <em>aren't</em> in the lesson, since they may be shared with other
    lessons.  They will be stored centrally on the Software Carpentry
    web site and linked from the lessons that need them.

## Topics

Each topic must be structured as follows:

```
---
layout: topic
title: Topic Title
minutes: MM
---
> ## Learning Objectives {.objectives}
>
> * Learning objective 1
> * Learning objective 2

Paragraphs of text mixed with:

~~~ {.python}
some code:
    to be displayed
~~~
~~~ {.output}
output
from
program
~~~
~~~ {.error}
error reports from program (if any)
~~~

and possibly including:

> ## Callout Box {.callout}
>
> An aside of some kind.

> ## Challenge Title {.challenge}
>
> Description of a single challenge.
> There may be several challenges.
```

<strong>Notes:</strong>

-   The "expected time" heading is called minutes to encourage people
    to create topics that are short (10-15 minutes at most).
-   There are no sub-headings inside a topic other than the ones
    shown: if a topic needs sub-headings, it should be broken into two
    or more topics.
-   <em>
      We need to figure out how to connect challenges back to learning
      objectives.  Markdown doesn't appear to allow us to
      add `id` attributes to list elements, or to create
      anchors that challenges can refer back to.
    </em>

## Introductory Slides

Every lesson must include a short slide deck suitable for a short
presentation (3 minutes or less) that the instructor can use to
explain to learners how knowing the subject will help them. Slides
are written in Markdown, and compiled into HTML for use
with <a href="http://lab.hakim.se/reveal-js/">reveal.js</a>.

<strong>Notes:</strong>

-   <em>We should provide an example.</em>

## Reference Guide

The reference guide is a cheat sheet for learners to print, doodle
on, and take away.  The format of the actual guide is deliberately
unconstrained for now, since we'll need to see a few before we can
decide how they ought to be laid out (or whether they need to be
laid out the same way at all).

The last thing in it must be a Level-2 heading called "Glossary"
followed by definitions of key terms Each definition must be
formatted as a separate blockquote indented with &gt; signs:

```
---
layout: reference
---
…commands and examples…

## Glossary

> **Key Word 1**: the definition
> relevant to the lesson.

> **Key Word 2**: the definition
> relevant to the lesson.
```

Again, we use blockquotes because standard [sic] Markdown doesn't
have a graceful syntax for &lt;div&gt; blocks.  If definition lists
become part of CommonMark, or if we standardize on Pandoc as our
translation engine, we can use definition lists here instead of
hacking around with blockquotes.

## Instructor's Guide

Many learners will go through the lessons outside of class, so it
seems best to keep material for instructors in a separate document,
rather than interleaved in the lesson itself.  Its structure is:

```
---
title: Instructor's Guide
---
## Overall

One or more paragraphs laying out the lesson's legend.

## General Points

* Point
* Point

## Topic 1

* Point
* Point

## Topic 2

* Point
* Point
```

<strong>Notes:</strong>

-   The topic headings must match the topic titles.  (Yes, we could
    define these as variables in a configuration file and refer to
    those variables everywhere, but in this case, repetition will be a
    lot easier to read, and our validator can check that the titles
    line up.)
-   The points can be anything: specific ways to introduce ideas,
    common mistakes learners make and how to get out of them, or
    anything else.

## Software, Data, and Images

All of the software samples used in the lesson must go in a
directory called `code/`.  Stand-alone data files must go
in a directory called `data/`. Groups of related data
files must be put together in a sub-directory of `data/`
with a meaningful (short) name.

Images used in the lessons must go in an `img/`
directory. We strongly prefer SVG for line drawings, since they are
smaller, scale better, and are easier to edit. Screenshots and other
raster images must be PNG or JPEG format.

<strong>Notes:</strong>

-   This mirrors the layout a scientist would use for actual work (see
    Noble's
    "<a href="http://www.ploscompbiol.org/article/info%3Adoi%2F10.1371%2Fjournal.pcbi.1000424">A
    Quick Guide to Organizing Computational Biology Projects</a>" or
    Gentzkow and Shapiro's
    "<a href="http://faculty.chicagobooth.edu/jesse.shapiro/research/CodeAndData.pdf">Code
    and Data for the Social Sciences: A Practitioner's
    Guide</a>").
-   However, it may cause novice learners problems. If
    `code/program.py` includes a hard-wired path to a data
    file, that path must be either `datafile.ext`
    or `data/datafile.ext`. The first will only work if the
    program is run with the lesson's root directory as the current
    working directory, while the second will only work if the program
    is run from within the `code/` directory. This is a
    learning opportunity for students working from the command line,
    but a confusing annoyance inside IDEs and the IPython Notebook
    (where the tool's current working directory is less obvious). And
    yes, the right answer is to pass filenames on the command line,
    but that requires learners to understand how to get command line
    arguments, which isn't something they'll be ready for in the first
    hour or two.
-   We have removed the requirement for an index file in
    the `code/` and `data/` directories.
    It is tempting to require code fragments in topics to have an
    extra attribute `src="code/filename.ext"` so that we
    can prune files that are no longer used as lessons change, but
    that may be more effort than authors are willing to put in.

## Tools

The `tools/` directory contains tool to help create and
maintain lessons:

-   `tools/check`: make sure that everything is formatted
    properly, and print error messages identifying problems if it's
    not.
-   `tools/build`: build the lesson website locally for
    previewing.  This assumes `tools/check` has given the
    site a clean bill of health.
-   `tools/update`: run the right Git commands to update
    shared files (e.g., layout templates).

## Layout

The template still contains `_layouts/`
and `_includes/` directories for page layout templates
and standard inclusions.  These are needed to support lesson
preview.

## Major Changes

-   We no longer rely on Make.  Instead, the two key tools are scripts
    in the `tools/` directory.
-   There is no longer a separate glossary page.  Instead, the
    glossary is part of the reference guide given to learners.
-   The index page no longer lists overall learning objectives, since
    learning objectives should all be paired with challenges.
-   Topic pages no longer have key points: anything that would have
    gone here properly belongs in the reference guide.

## Feedback from TGAC Instructor Trainees

Participants in the instructor training session run at TGAC on Oct
22-23 gave us feedback on the content shown above.  Their points are
listed below; we'll try to factor them into the final template.

<div class="row">
  <div class="col-4">
    <p><strong>Good</strong></p>
    <ul>
      <li>Details +2</li>
      <li>Lots of technical detail</li>
      <li>Enables flexibility - adding contents</li>
      <li>Markdown</li>
      <li>Helps to structure / think about content</li>
      <li>Good outline of what you want to do</li>
      <li>Good organisation</li>
      <li>Enough detail for somebody who doesn't have much experience</li>
      <li>Uncomplicated visually</li>
      <li>Required variables section</li>
      <li>Proper highlighting for the syntax part</li>
      <li>Clearly listed variables</li>
    </ul>
  </div>
  <div class="col-4">
    <p><strong>Bad</strong></p>
    <ul>
      <li>Assumed knowledge (keywords) +2</li>
      <li>Not much introduction +2</li>
      <li>Overwhelming</li>
      <li>Some terms jargon unclear</li>
      <li>Not live yet so you can't check if works</li>
      <li>Mixed instructions (website + Jekyll info) </li>
      <li>Text on the lesson template needs reordering (restucturing)</li>
      <li>See Markdown rendered so that it's easier to review</li>
      <li>Key info down at the bottom</li>
      <li>More visual info</li>
      <li>No "Get it touch" info</li>
      <li>Customizing lessons badly explained</li>
      <li>Which md and translators to use</li>
      <li>Colours (background + foreground)</li>
      <li>example.edu for email</li>
    </ul>
  </div>
  <div class="col-4">
    <p><strong>Questions/Suggestions</strong></p>
    <ul>
      <li>Maybe two different overviews (depending on the audience) +2</li>
      <li>Why these engineering choices were made? (if that was supposed to be simple)</li>
      <li>Troubleshooting?</li>
      <li>Shortcut to the "how to set it up and skip the whole info"?</li>
      <li>How is feedback to lessons made available to others?</li>
      <li>Metasection on each lesson - which audience it is particularly working well with?</li>
      <li>Why should we create our own website?</li>
    </ul>
  </div>
</div>
