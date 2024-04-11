---
title: "What I Need in a Static Site Generator"
date: 2024-04-11
year: 2024
---

I want to create lessons and books rather than blogs,
so my needs for a static site generator (SSG) are different from most people's.
Based on what I've built or customized over the past 15 years,
here are some of the things I need:

1.  Translate Markdown files into HTML and copy other resources into the right places.
    The translation should rely on templates,
    which should support loops, conditionals, parameterized inclusions, and so on
    (but see the next point).

1.  Access to a complete programming language for templating.
    One of the many frustrating things about [Jekyll][jekyll] is that
    its templating language only provides a limited subset of Ruby's features:
    you can't, for example, get the index at which an element appears in an array
    without writing a template-level loop,
    which is *really* clumsy.
    Tools like [EJS][ejs] are much, much better in this regard,
    and reliance on limited templating tools like [Jinja][jinja]
    is one of my few grumbles about [Ark][ark].

1.  Built-in shortcodes for things like:
    -   glossary references,
    -   index entries,
    -   bibliographic citations,
    -   numbered cross-references to figures, tables, and headings
        (both within and between files),
    -   figure and table inclusions (so that they're formatted in consistent ways)

1.  Mechanisms for formatting things like bibliographies, glossaries, and indexes.
    For example,
    [McCole][mccole] has an extension that uses [pybtex][pybtex]
    to turn a [BibTeX][bibtex]-formatted bibliography into HTML
    and another that turns a [Glosario][glosario]-formatted YAML file
    into a human-readable glossary page.

1.  A standard way to include fragments of source code and other files.
    This requirement is why I don't use computational notebooks for my writing:
    I always want to include sections of code (e.g., a class header and two of its methods)
    rather than entire pieces of (i.e., the entire class definition),
    but [Jupyter][jupyter] and its ilk don't support that.
    [McCole][mccole] provides two mechanisms:
    one uses specially-formatted comments
    ("include everything from `# [mark]` to `# [/mark]`")
    and the other relies on program structure
    ("parse the code, walk the AST, find the function `example`, and unparse it to text).
    I have other hacks to (for example) show the first *and* last five lines of a CSV file
    in a single inline code block and so on;
    needs like this are why extensibility (discussed below) is so important.

1.  Allow one subdirectory per topic to keep files manageable.
    For example, [McCole][mccole] (which is built on [Ark][ark])
    had a subdirectory <code>src/<em>slug</em></code> for each chapter or appendix,
    where <code><em>slug</em></code> is a short unique identifier.
    And while we're here,
    I always want topic order defined by configuration rather than by cross-references.
    This requirement may seem like nit-picking,
    but having to edit half a dozen files when you change the order of two chapters
    is a real pain.
    [McCole][mccole] defines two lists of slugs in `config.py` called `chapters` and `appendices`,
    and everything else refers to that.

1.  Titles, summaries, key points for the syllabus, and everything else in the frontmatter of each topic page.
    All of the information about a chapter or appendix should be in its frontmatter
    rather than in the configuration file or a separate data file.
    (I've done it both ways in the past;
    everything in one place is less error-prone.)

1.  Conversely,
    the SSG should collect all of the frontmatter data
    and make it available for extensions to use in rendering.
    For example,
    each chapter of [*Software Design by Example*][sdxpy] starts with
    a list of the terms defined in that chapter.
    These are collected by a pre-rendering hook that scans the chapter for glossary reference shortcodes;
    the template has to parse every chapter itself to get that information,
    which adds a couple of seconds to the build.

1.  Extensibility.
    Using [McCole][mccole] as an example again,
    it defines 27 extensions to [Ark][ark] to handle things like
    bibliographic citations,
    glossary references,
    figure inclusions,
    and so on.
    Even if an SSG ships with all of these,
    every user is going to need one more.

[ark]: https://www.dmulholl.com/docs/ark/main/
[bibtex]: https://en.wikipedia.org/wiki/BibTeX
[ejs]: https://ejs.co/
[glosario]: https://glosario.carpentries.org/
[jekyll]: https://jekyllrb.com/
[jinja]: https://jinja.palletsprojects.com/en/3.0.x/templates/
[jupyter]: https://jupyter.org/
[mccole]: https://github.com/gvwilson/mccole
[pybtex]: https://pypi.org/project/pybtex/
[roc-book]: https://github.com/roc-lang/book-of-examples/
[sdxpy]: {{ '/sdxpy/' | relative_url}}
