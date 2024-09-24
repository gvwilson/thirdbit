---
title: "Building a Book"
date: 2021-02-10
---

I have written or edited five technical books in the last 11 years
and have three more in various stages of production.
Every single one has been built differently
because none of the tools I can find
do the things I want:

1.  **Numbered cross-references.**
    I want to assign logical names to sections, figures, and tables
    so that I can refer to them from other places
    and have those cross-references filled in with the correct numbers.
    LaTeX does this,
    but the Jekyll setup used by GitHub Pages doesn't.

1.  **Citations.**
    LaTeX (plus BibTeX) turns `\cite{Able,Baker}` into `[Able 2000, Baker 2011]`
    and generates a bibliography.
    Bookdown and Jupyter Book do this too,
    but Jekyll doesn't know what citations are—without plugins,
    I have to write something like `[[Able 2000](../bib/#Able), [Baker 2011](../bib/#Baker)]`
    and then filter my bibliography myself.

1.  **A glossary.**
    If you want to know what a document is about,
    look at the terms it defines.
    LaTeX has packages for tagging glossary definitions,
    but Bookdown and Jupyter Book don't;
    [Glosario](https://github.com/carpentries/glosario/) is trying to fix this.

1.  **Code fragments.**
    Bookdown, Jupyter Book, and other notebook-based systems
    let me embed runnable code chunks and their output in a document.
    The problem is,
    that's almost never what I want when I write a book.
    Instead,
    what I usually want is a fragment of that code—a couple of methods out of a class,
    for example,
    or the first and last few lines of output with vertical ellipses between them.
    Purist literate programming systems support this via transclusion,
    but none of the widely-used notebooks do.

1.  **Automatic regeneration of output.**
    This is the greatest strength of computational notebooks
    and one of the major deficiencies of LaTeX and site generation tools like Jekyll.
    I have Makefiles… Lots of Makefiles…

1.  **Support for multiple languages.**
    [*Software Design by Example Using JavaScript*](@root/sdxjs/)
    has examples in Node.js, Python, and the Bash shell;
    other books have an even greater diversity.
    Today's computational notebooks handle this reasonably well;
    for LaTeX and static site generators I have to trust my Makefiles.

1.  **No dependence on Pandoc.**
    Every time I have used Pandoc I have had to write some customization scripts,
    whether as pre- and post-processors or as embedded filters.
    (I learned the little bit of Lua I know in order to do the latter.)
    In theory I'm sure I could learn enough about its templating language to solve my problems,
    but I'm tired of investing my time in single-use technologies,
    and if doing that is a prerequisite for contributing to a project,
    that's going to exclude a lot of people.
    I'm not proud of having written several text-to-text translators in Python and Node.js,
    but my collaborators can fix and extend them using the knowledge they already have.

1.  **No escape characters.**
    I don't have to type backslashes or the punctuation in `![](./logo.png)`
    when I'm writing in Word or a Google Doc,
    so I resent every time my tools require me to.
    This is one of the reasons I don't write in LaTeX and then translate to HTML:
    not only has "the FORTRAN of scientific publishing" become increasingly brittle over the years
    as packages pile on packages pile on packages,
    but it's grown harder to persuade people that its arcane syntax is justified.
    Markdown hurts less—until you need notations for numbered cross-references,
    citations, glossary entries, partial code inclusions, and so on.

1.  **Diff and merge.**
    This is non-negotiable for me,
    and is one of the reasons I don't use Jupyter notebooks.
    If I can't diff and merge contributions from other people,
    I can't collaborate with them effectively.
    (And yes, there are ways to diff and merge Jupyter notebooks now,
    but no, they aren't usable enough to persuade me.)

1.  **No mandated editor.**
    So far this week I have edited in Emacs, the RStudio IDE, and Microsoft Visual Code.
    My co-authors on *[JavaScript for Data Science](@root/js4ds/)*
    and *[Research Software Engineering with Python](@root/py-rse/)*,
    and the team translating *[Teaching Tech Together](https://teachtogether.tech/)*
    into [Spanish](http://teachtogether.tech/es/index.html),
    use another half-dozen editors between them.
    I don't think people should have to switch tools to work with me,
    so any solution that mandates a particular editor, operating system, or online service
    is a non-starter.

1.  **HTML and PDF.**
    This is the point of it all: something people can read online
    and something that can be printed and bound.
    They don't need to look like one another—fonts that work well on the web
    may not be the best choice on paper—but all of the indexing and cross-referencing *must* be consistent.
    They must also come from a single source so that updates are automatically consistent as well,
    and that's a problem:
    forced page breaks and "put it here" directives are always needed for print,
    but can be invalidated by even small changes to content
    and make no sense for HTML.

All of this has led me to build and re-build a succession of tools
to convert Markdown to HTML and HTML to LaTeX.
It's a horrible "solution":
while I am dissatisfied with the tools mentioned above,
they are all well-documented and well-maintained,
neither of which is true of my home-made scripts.
I'd give a lot for a WYSIWYG editor with *in situ* drawing,
re-execution of transcluded code,
and built-in user-level diffing and merging,
but I no longer believe I'm going to see it in my lifetime.
