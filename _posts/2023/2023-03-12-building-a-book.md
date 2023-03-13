---
title: "Building a Book"
date: 2023-03-12 19:00:00
year: 2023
---

In response to a question about [today's first post][rethinking],
I use [Ivy][ivy] with some custom extensions to create the HTML versions of my books,
and then translate the HTML to LaTeX and compile that to produce PDFs.

-   *Why not use [GitHub Pages][ghp]?*
    Because [Jekyll][jekyll] doesn't support things I need.
    Even if I learned enough Ruby to write extensions,
    I couldn't run them directly on GitHub:
    I'd have to set up an action of some sort.
    If I'm going to do that,
    I might as well build the HTML on my own machine and commit it.
    (I'm also tired of trying to keep yet another package manager and virtual environment manager up to date.)

-   *Why not [Jupyter Book][jb], [Bookdown][bookdown], or [Quarto][quarto]?*
    For the same reasons.
    For example, I frequently need to include sections of source code rather than entire semantic units,
    such as two methods from a class without the rest of the class,
    and none of them cater for this.
    They do handle bibliographies,
    but link tables, syllabi, and other things would still be on me.
    (I'm also really, really tired of having to wrestle with PDF formatting issues
    when I use these tools:
    we did [*Research Software Engineering with Python*][py-rse] with [Bookdown][bookdown],
    and honestly, it would have been faster and easier to just write the LaTeX ourselves.)

-   *So you translate HTML to LaTeX yourself?*
    Yup:
    thanks to [Beautiful Soup][bs],
    the whole translation script is only 534 lines (including blank lines, comments, and docstrings).
    I put time and money into [Paged.js][paged] last year in the hope that I could go directly from HTML+CSS to PDF,
    but it's simply not ready yet.

-   *Why [Ivy][ivy] rather than [Nikola][nikola], [Pelican][pelican], [Sphinx][sphinx], or…?*
    Because [Ivy][ivy] is still so small that I can understand how it works.
    The extensions I need are now 1500 lines of Python;
    they might have been shorter if I'd used another framework,
    but I think it would have taken me longer to figure out what to write.

So what are these extensions I keep referring to?

-   Insert credits and acknowledgments based on metadata in a configuration file.
-   Create bibliographic citations and build a bibliography from them.
-   Copy source files referenced by chapters into the right output directory.
-   Number figures and manage cross-references to them.
-   Mark and collate FIXME items.
-   Create glossary references and build a glossary from them.
-   Number headings and manage cross-references to them.
-   Manage source code inclusions,
    including ones that select only a few lines from a file
    or include several files that match a pattern.
-   Create an index of special terms.
-   Manage external links and create a table of them in an appendix.
-   Extract information about the syllabus from each chapter and format it.
-   Number tables and manage cross-references to them.

Is this sustainable?
I.e., could someone else step in and maintain it?
Or could it handle other people's needs?
I don't know,
but the Python version of [*Software Design by Example*][sdxjs]
will be my fourteenth technical book,
and so far it's hurting less than any of the others.

[bookdown]: https://bookdown.org/
[bs]: https://beautiful-soup-4.readthedocs.io/
[ghp]: https://pages.github.com/
[ivy]: https://www.dmulholl.com/docs/ivy/main/
[jb]: https://jupyterbook.org/
[jekyll]: https://jekyllrb.com/
[nikola]: https://www.getnikola.com/
[paged]: https://pagedjs.org/
[pelican]: https://getpelican.com/
[py-rse]: https://merely-useful.tech/py-rse/
[quarto]: https://quarto.org/docs/books/
[rethinking]: {{'/2023/03/12/rethinking-design-examples/' | relative_url}}
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sphinx]: https://www.sphinx-doc.org/
