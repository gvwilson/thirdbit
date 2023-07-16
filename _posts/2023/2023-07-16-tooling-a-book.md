---
title: "Tooling a Book"
date: 2023-07-16
year: 2023
---

Shortly after I announced [the beta release of *Software Design by Example (Python edition)*][announce-beta]
a couple of people reached out to ask why I hadn't used [Quarto][quarto] to build it.
I pointed them at [the list of extensions I had to build][extensions]
to turn source code and Markdown into something publishable
and asked how much work Quarto would have saved me.
Neither has replied,
so I'd like to throw the question out to a wider audience.
I'm pretty sure Quarto (and other tools) can do these things:

-   Convert a BibTeX-formatted bibliography into Markdown
    and turn shortcodes into hyperlinked citations.

-   Extract headings to support numered cross-references to sections.

-   Copy the example files mentioned in each chapter into the output directory
    *without* trying to expand macros in them.

-   Insert the build date.

-   Insert figures with proper labels (including alt text)
    and resolve shortcode references to them.

-   Insert tables with proper labels
    and resolve `[%t some-key %]` shortcode references to them.

I'm pretty sure I'd have to write Lua extensions and/or wrestle with Pandoc
to do the following:

-   Include sections of example code files.
    The "sections" part is necessary for teaching purposes:
    I often want to show one or two methods from a class in one place,
    another method or two in another,
    and so on.
    As far as I can tell,
    computational notebooks and tools derived from them
    don't support code fragments like this in a maintainable way.

-   Convert a [Glosario][glosario]-formatted glossary into Markdown,
    turn glossary reference shortcodes into hyperlinked references,
    and display a list of terms defined in a chapter at the top of the chapter.

-   Turn shortcodes into index entries so readers can find out
    which chapters say something interesting about which key subjects.

-   Append links from a YAML-formatted link directory to each file
    so that all chapters and appendices can refer to a single source of truth for external links
    and use it to build a single-page directory of all the external links in the book.

-   Turn a list of people who've helped in some way
    into a Markdown-formatted paragraph of acknowledgments.

-   Compare the inclusions in the long-form prose for chapters
    with inclusions in those chapters' slide decks
    to make sure they're consistent.
    
-   Build a page with links to the slide decks for each chapter.

-   Extract syllabus entries from the header of each chapter
    to format as a callout box at the top of its page
    and as a consolidated learning guide in an appendix.

-   Check the sizes of SVG diagrams and the fonts they use.

-   Extract inter-chapter dependencies and use them to create
    [a curriculum roadmap][curriculum].

-   Compare word counts, number of slides, number of figures, etc.
    against targets and produce a status report
    showing how close the book is to being finished.

-   Run a dozen different checks to make sure that (for example)
    glossary terms are defined before they are used,
    section IDs are formatted consistently, etc.

[announce-beta]: https://third-bit.com/2023/07/12/sdxpy-beta/
[curriculum]: https://third-bit.com/2019/03/30/curriculum-roadmap/
[extensions]: https://third-bit.com/2023/06/12/book-extensions/
[glosario]: https://glosario.carpentries.org/
[quarto]: https://quarto.org/
