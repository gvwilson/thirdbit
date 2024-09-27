---
title: "Book Extensions"
date: 2023-06-12
---

I use a static site generator called [Ark][ark] (formerly Ivy) to build my books
(see [this post][building-a-book] for my reasons).
I've built several extensions for it over the past year
to do what books need that plain old websites don't,
which includes:

-   Turn a list of people who've helped in some way
    into a Markdown-formatted paragraph of acknowledgments.

-   Convert a BibTeX-formatted bibliography into Markdown
    and turn `\\[%b Key1,Key2 %]` shortcodes into hyperlinked citations.

-   Copy the example files mentioned in each chapter into the output directory
    *without* trying to expand macros in them.

-   Insert the build date.

-   Insert figures with proper labels (including alt text)
    and resolve `\\[%f some-key %]` shortcode references to them.

-   Convert a [Glosario][glosario]-formatted glossary into Markdown
    and turn `\\[%g key "text" %]` shortcodes into hyperlinked references.

-   Extract headings to support numered cross-references to sections.

-   Include example files or sections of example files.
    The "sections" part is necessary for teaching purposes,
    and is one of the reasons I can't write books using [Quarto][quarto],
    [Jupyter notebooks][jupyter], or other tools.

-   Convert a YAML-formatted directory of links into Markdown link footers
    and into a single-page directory of all the external links in the book.
    
-   Build a page with links to the slide decks for each chapter.

-   Extract syllabus entries from the header of each chapter
    to format as a callout box at the top of its page
    and as a consolidated learning guide in an appendix.

-   Insert tables with proper labels
    and resolve `\\[%t some-key %]` shortcode references to them.

It's a lot of text wrangling,
and for a while I hoped that [paged.js][paged] would make it unnecessary,
but for now,
maintaining 1700 lines of code is simpler than anything else I know of.

[ark]: http://www.dmulholl.com/docs/ark/master/
[building-a-book]: @root/2023/03/12/building-a-book/
[glosario]: https://glosario.carpentries.org/
[jupyter]: https://jupyter.org/
[paged]: https://pagedjs.org/
[quarto]: https://quarto.org/
