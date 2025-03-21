---
title: "Another Static Site Generator for Lessons"
date: 2024-11-30
---

I built a very simple static site generator (SSG) called [McCole][mccole]
to support the lessons I mentioned in [my previous post][unfinished].
I could have stuck with [Ark][ark]
(which I use to build this site and books like [*Software Design in Python*][sdxpy]),
but writing my own helped me figure out what I actually need,
and might someday serve as the basis for a tutorial of some sort.
In no particular order, [McCole][mccole]'s features are:

1.  Read configuration from the project's `pyproject.toml` file.
1.  Convert all the Markdown files in or below the project's root directory to HTML
    using [Jinja][jinja] templates.
1.  Rename a few files along the way:
    -   `README.md` becomes `index.html`
    -   `CODE_OF_CONDUCT.md` becomes `code_of_conduct.html`
    -   `CONTRIBUTING.md` becomes `contributing.html`
    -   `LICENSE.md` becomes `license.html`
1.  Create an HTML page corresponding to every source code file
    so that (for example) `a/b.py` is visible online as `a/b.py.html`.
1.  Replace `@root` at the start of URLs with the relative path to the site's root directory.
1.  Replace links to Markdown files with links to the corresponding HTML files.
    I do this so that links would work properly when people view the Markdown files on GitHub.
1.  Rewrite the URL in something like `[label](b:key)` to `[label](@root/bibliography.html#key)`
    to make it easy for authors to link to bibliographic citations.
    These special links *don't* work when files are viewed on GitHub,
    but it's a lot less typing that the alternative.
    (I use the [shortcodes][shortcodes] package to do this with [Ark][ark] sites,
    but after a bit of experimentation I decided to special-case these links in [McCole][mccole].)
1.  Similarly,
    [McCole][mccole] rewrites `[term](g:key)` to `[term](@root/glossary.html#key)`
    so that authors can easily insert glossary references.
1.  If a page contains any glossary references,
    [McCole][mccole] creates a list of defined terms at the top of the page.
    (In my experience,
    this is the most useful way to tell a would-be instructor what the lesson is actually about.)
1.  I tried using shortcodes to format figures consistently,
    but once I decided not to use them for the glossary and bibliography,
    it didn't seem worth keeping them for figures.
    Instead,
    I check their properties during linting (see below).
1.  My tutorials focus on programming,
    so I need to be able to include snippets of source code in pages.
    "Snippets" makes the problem more complex:
    I often want to include just one function or a couple of methods rather than an entire source file.
    My previous SSG had a couple of hundred lines of code
    to pull sections out of source files in various ways;
    [McCole][mccole] just checks that the text in the Markdown file
    is contained in the source file.
1.  [McCole][mccole] defines a class for each inclusion like `language-py` or `language-sql`
    so that inclusions from different languages can be styled differently.
    I haven't included syntax highlighting,
    partly because I want to keep this SSG simple
    but also because the highlighting rules I choose probably *won't* match what learners see
    in their editor or IDE.
1.  [McCole][mccole] includes a tool for linting sites,
    i.e.,
    for checking that links resolve,
    glossary entries are mentioned somewhere,
    and so on.
    It turned out to be a lot simpler to check for problems
    than to generate correct content automatically,
    at least for small lessons.
    [McCole][mccole] also uses [html5validator][html5validator]
    to check the formatting of the HTML pages it generates;
    specific lessons use tools like [ruff][ruff] to check source code as well.

So what *doesn't* [McCole][mccole] include that a full-featured lesson SSG would?
The most important thing is probably some sort of support for exercises:
styling them,
numbering them,
keeping track of solutions,
and so on.
I could also add CSS styling for various kinds of callouts,
but I'm not trying to reproduce something like [the Carpentries Workbench][workbench]:
[McCole][mccole] is a multi-bit screwdriver,
not a fully-equipped machine shop.

[ark]: https://www.dmulholl.com/docs/ark/main/
[html5validator]: https://pypi.org/project/html5validator/
[jinja]: https://jinja.palletsprojects.com/
[mccole]: https://github.com/gvwilson/mccole
[ruff]: https://docs.astral.sh/ruff/
[sdxpy]: @root/sdxpy/
[shortcodes]: https://github.com/dmulholl/shortcodes
[unfinished]: @root/2024/11/24/unfinished-projects/
[workbench]: https://carpentries.github.io/workbench/
