---
title: "Building a Book (Part 2)"
date: 2021-03-10
year: 2021
---

As a follow-up to [last month's post about building a book]({{ '/2021/02/10/building-a-book/' | relative_url }}),
here's a rundown of what the template for [*Software Design by Example Using JavaScript*]({{'/sdxjs/' | relative_url}})
and my other book projects does right now.

1.  **Jekyll with GitHub Pages' settings.**
    I don't like Jekyll,
    but since it is well documented and no other tool does what I want either,
    I might as well stick to it.

1.  **Use HTML tags for simple extensions.**
    Glossary references are written as `<span g="label">text</span>`,
    cross-references to chapters and appendices as `<span x="label"></span>`,
    and so on.
    A previous template used Jekyll inclusions like `{% raw %}{% include g key="label" text="text" %}{% endraw %}`,
    but I find the spans much easier to read.
    They're copied verbatim into the generated pages like any other HTML
    and I use a little bit of JavaScript to convert them to links (more about this below).

    *Note: I can't use special tags like `<g key="label">text</g>`
    since the Kramdown parser doesn't transcribe non-standard tags in some cases.
    After working as a programmer for almost 40 years,
    I still don't know where to document insights like this
    so that the next person can find them.*

1.  **Pre-processing.**
    I need a global lookup table to make cross-references to chapters, sections, figures, and other things work.
    While Jekyll will give me a list of posts or collection items,
    there's no way (with GitHub Pages' settings)
    to add my own counted objects.
    I therefore have a bunch of little Python scripts driven by a Makefile
    to produce *chapter.number*-style IDs for things.
    These are saved in YAML files in the `_data` directory
    so that they're accessible to Jekyll while it's building pages,
    and transcribed as JSON in each page's header
    so that the little bits of JavaScript mentioned above can do their job.

1.  **Jekyll inclusions for code fragments.**
    One of the reasons I don't use computational notebooks is that
    they don't give me a way to transclude excerpts from programs,
    i.e.,
    I can't show some methods of a class but not others,
    or interleave a few lines of a function with a few lines of prose.
    I therefore put specially-formatted comments in my source code to mark regions,
    then use Jekyll inclusions to slice those files into pieces during page compilation.
    It's not elegant,
    but it does the job,
    and it gives me an opportunity to check during the build
    that every snippet of code I mention actually exists.

1.  **Checks. Lots of checks.**
    The Makefile includes these targets to make sure things will build:
    -   `check`: run all checks
    -   `check-bib`: compare citations and definitions
    -   `check-chunk-length`: see whether any inclusions are overly long
    -   `check-code-blocks`: check inline code blocks
    -   `check-gloss`: compare references and definitions
    -   `check-links`: make sure all external links resolve
    -   `check-numbering`: make sure all internal cross-references resolve
    -   `check-spelling`: check for misspelled words

1.  **Structured exercises.**
    Every exercise is in a sub-directory whose name starts with `x-`,
    such as `x-glob-patterns`,
    so that I can find them easily using wildcards.
    Each sub-directory contains files called `problem.md` and `solution.md`
    and has an entry in Jekyll's `_config.yml` file with metadata like its title
    (to ensure consistency between problems-in-the-chapter
    and solutions-in-the-appendix).
    It's clumsy,
    but so is everything else I've tried.

1.  **Link definitions in the configuration file.**
    I want to be sure that external references resolve consistently.
    I used to do this by including a file called `links.md` in each page
    (in each page rather than in the template because Jekyll's order of operations prevents the latter from working).
    I then discovered Kramdown's `link_defs` option and was briefly excited.
    What I *want* to be able to put in `_config.yml` is:
    ```
    kramdown:
      link_defs: _data/link_defs.yml
    ```
    I'd settle for:
    ```
    kramdown:
      link_defs:
        - acorn:
          - https://github.com/acornjs/acorn
          - acorn.js
        - alloy:
          - https://alloytools.org/
          - Alloy
        - antlr:
          - https://www.antlr.org/
          - ANTLR
        …
    ```
    To get around [this bug](https://stackoverflow.com/questions/66320774/how-to-pre-define-links-in-jekyll-config-yml-using-kramdown-links-def-options),
    though,
    I need to write YAML that contains a string that can be parsed as YAML:
    ```
    kramdown:
      syntax_highlighter_opts:
        disable: true
      link_defs: >
      {
        "acorn": ["https://github.com/acornjs/acorn", "acorn.js"],
        "alloy": ["https://alloytools.org/", "Alloy"],
        "antlr": ["https://www.antlr.org/", "ANTLR"],
        …
      }
    ```
    I can then write `{% raw %}[Acorn][acorn]{% endraw %}` everywhere in my pages,
    but have to do some messy string operations in a Jekyll inclusion
    to print a table of links in an appendix.

1.  **Figures saved as PDF as well as SVG.**
    I draw all of my diagrams with [diagrams.net](https://www.diagrams.net/) and save them as SVG;
    all screenshots are done using [SVG Screenshot](https://chrome.google.com/webstore/detail/svg-screenshot/nfakpcpmhhilkdpphcjgnokknpbpdllg).
    I need PDFs for the print version: since SVG is only 22 years old, LaTeX doesn't support it yet.
    Unfortunately,
    I can't use off-the-shelf SVG-to-PDF tools because diagrams.net's SVG includes extra fields
    to support things like smart connectors,
    and since diagrams.net doesn't have a command-line API,
    I can't script the translation.

1.  **Custom HTML-to-LaTeX conversion.**
    My template depends on Jekyll, Python, Make, CSS, and JavaScript;
    adding [Pandoc](https://pandoc.org/) to the mix seemed like a step too far, even for me.
    I therefore have a 440-line Python script that turns the HTML generated by Jekyll into LaTeX,
    which I then compile to produce a PDF.
    I translate the generated HTML rather than the original Markdown
    to ensure consistent interpretation of the latter (Python's Markdown processors don't work exactly like Kramdown)
    and so that I don't have to write Python equivalents of my Jekyll inclusions;
    I use Jekyll for this and my other scripts rather than Ruby
    because neither I nor the researchers I work with speak the latter.

It's a mess,
but it's reasonably fast,
reasonably flexible (I'm using it for three projects right now),
and I've learned a lot from assembling it.
As I said in my note on point #2 above,
though,
I still don't know where to document my insights so that the next person can find them.
"Write it down" doesn't work:
it rusts very quickly
and it's hard to make material findable.
Solve this problem,
and you'll have given us a way to start sharing software design insights at scale.
