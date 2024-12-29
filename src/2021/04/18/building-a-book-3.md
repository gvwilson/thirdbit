---
title: "Building a Book (Part 3)"
date: 2021-04-17
---

The [previous post in this series](@root/2021/03/10/building-a-book-2/)
described the template I'm using for [*Software Design by Example Using JavaScript*][sdxjs]
and *Building Tech Together*.
Here's more detail on the helper scripts I had to write
to work around Jekyll's inadequacies,
in the order in which they run during a full build.
All in all they are 2600 lines of Python;
rebuilding some of them would be a rich source of exercises
for a second-year course on software design and testing.

1.  `make-bib.py`:
    convert the YAML-format bibliography in `_data/bibliography.yml`
    to a Markdown file `bibliography/index.md`.
    I used YAML rather than BibTeX because it's easier to read and process;
    I'm surprised this isn't already common practice.

1.  `make-index.py`:
    extract index keys from Markdown source to create `_data/index.yml`,
    which is then processed by Jekyll to create an index page.

1.  `make-numbering.py`:
    generate serial numbers for chapters and appendices, figures, and tables,
    and put them in `_data/numbering.yml`.

1.  `make-terms.py`:
    find all glossary definitions and store them in `_data/terms.yml`
    so that each chapter can start with a list of the terms it defines.

1.  `check-bib.py`:
    check that all citations resolve and all bibliography entries are used.

1.  `check-gloss.py`:
    check that all glossary entries resolve (including cross-references within the glossary)
    and that all existing entries are referenced.
    The glossary is stored in [Glosario](https://glosario.carpentries.org/) format,
    and the entries are mix of some cherry-picked from Glosario itself
    and some I've written for these books.

1.  `check-chunk-length.py`:
    look for text inclusions (e.g., sample programs) that are too long to fit on a single printed page.
    [*SDXJS*][sdxjs] has several of these;
    if I stick with this template,
    I'll modify this script and some of the others
    so that directives in the Markdown source will turn off warnings for specific inclusions.

1.  `check-code-blocks.py`:
    check that all code blocks have a recognized language type.
    (I can't train my hands to be consistent about `txt` versus `text` or `py` versus `python`.)

1.  `check-dom.py`:
    check that the generated HTML only uses expected tags and attributes.

1.  `check-links.py`:
    compare the link definitions in `_config.yml`
    with the `[name][link]` references in the Markdown source files
    to make sure that all definitions are used and all references to links resolve.
    I'd really like to put link definitions in an external YAML file in the `_data` directory,
    but Jekyll doesn't support that;
    as explained [here][yaml-bug],
    they have to go in a single YAML-formatted string in `_config.yml`.

1.  `check-numbering.py`:
    make sure that all cross-references to chapters/appendices, figures, and tables resolve.

1.  `prep-spelling.py` and `check-spelling.py`:
    the first strips code blocks from the generated HTML,
    which is then piped to `aspell` to create a list of unknown words;
    the second compares that list with the one stored in `_data/spelling.txt`
    and produces a list of unknown words.

1.  `html2tex.py`:
    convert the generated HTML to LaTeX, which is then used to produce a PDF.
    I've used Pandoc for several previous projects;
    500 lines of Python that does exactly what I want and produces comprehensible error messages
    is a lot easier for me to maintain.

I also have:

1.  `show-chapters.py`:
    show the number of words in each chapter along with the total word count.

1.  `show-dom.py`:
    print a list of all tags and attributes in the generated HTML.

1.  `show-fixme.py`:
    display all the embedded to-do items along with a count of how many there are.

1.  `show-index.py`:
    display all index terms and the locations of all references to them.
    (This helps me catch things like singular-vs.-plural inconsistencies in index terms.)

1.  `show-pages.py`:
    display the number of pages in each chapter of the final PDF.

[sdxjs]: @root/sdxjs/
[yaml-bug]: https://stackoverflow.com/questions/66320774/how-to-pre-define-links-in-jekyll-config-yml-using-kramdown-links-def-options
