---
date: 2018-12-14
title: "No Straight Pipeline"
---

Most people will probably read
[*JavaScript versus Data Science*](@root/js4ds/) online for free,
but I like having printed copies of books.
Getting this one out the door gave me a chance to revisit the pipeline I built for
*[Teaching Tech Together](http://teachtogether.tech)*
and to think some more about [accessible lesson templates](@root/2018/12/12/twelve-percent/).
The constraints I chose to work under are:

-   All content is written in [GitHub Flavored Markdown](https://github.github.com/gfm/)
    and processed using [Jekyll](https://jekyllrb.com/) without any special plugins
    so that the book's website can be regenerated simply by committing files to its GitHub repository.
    Yes, [Hugo](https://gohugo.io/) and [Bookdown](https://bookdown.org/yihui/bookdown/) are probably nicer to use,
    but to paraphrase Knuth,
    Jekyll is everybody's second favorite choice.

-   LaTeX for generating a PDF suitable for printing and binding.
    There really isn't another choice for this:
    the only question is how to get there from Markdown.

So what does our setup look like?

1.  All of the Markdown source files are stored in a directory called `./_en`.
    The "en" stands for "English" (we want to allow for translations in future),
    and the leading underscore tells Jekyll that we want these files to be turned into a collection,
    i.e.,
    that inside our templates,
    `site.en` should be a list containing all of the pages.
    We have to add a few lines to `./_config.yml` (the Jekyll configuration file) to enable this as well.

1.  `./_config.yml` also contains a list that specifies the order of the files;
    each file is specified by its permalink,
    so files can be added, removed, or reordered without editing their content.
    Various template snippets in `./_includes` loop over this list and the collection contents
    to create a table of contents,
    summarize all the motivating questions and key points,
    and so on.

1.  `jekyll build` translates all the Markdown to HTML and puts it in `_site/en`.
    These files are *not* committed to Git;
    instead, each time changes to the Markdown are pushed to GitHub,
    it regenerates the site automatically.

1.  However, a server-side compilation step *is* needed
    to create an all-in-one-page version of the site,
    which in turn is used to create a PDF (about which more below).
    A little JavaScript utility called `./bin/stitch.js` extracts content from the generated pages
    and rewrite inter-page links so that they'll resolve within that single page.
    This could and should be done inside the client's browser
    (as it is in [the current Carpentries template](https://github.com/carpentries/lesson-example/blob/gh-pages/aio.md));
    if anyone wants to put it together,
    please [get in touch](mailto:gvwilson@third-bit.com).

1.  We use [Pandoc](https://pandoc.org/) to convert the single-page HTML version of the book to LaTeX.
    However, since Pandoc doesn't handle some of our Markdown the way we want,
    the command to do this is prefixed and suffixed with a few lines of text wrangling via `sed`.
    We could probably write a Pandoc extension to do this instead,
    or modify the template,
    but those approaches feel brittle:
    there aren't a lot of people out there who are familiar enough with Pandoc to maintain custom work.

1.  When it comes to diagrams,
    we use the desktop version of [draw.io](https://www.draw.io/) to create them,
    then export as both SVG (for the browser) and PDF (for LaTeX).
    We experimented with automatically generating PDF from SVG as needed,
    but the results were unsatisfying:
    draw.io's SVG contains some artefacts that [CairoSVG](https://cairosvg.org/) doesn't know how to handle,
    and since diagrams change fairly infrequently,
    exporting twice seemed easier than anything else.

1.  In order for all this to work,
    authors have to respect a few formatting conventions:
    -   Section headings need IDs with names like <code>s:<em>chapter</em>-<em>slug</em></code>.
    -   Figures need IDs with names like <code>f:<em>chapter</em>-<em>slug</em></code>.
    -   Glossary entries need IDs with names like <code>g:<em>slug</em></code>.
    -   Bibliography entries need IDs with names like <code>b:<em>slug</em></code>.
    -   All chapters go into their own sub-directories
        (e.g., the introduction lives in `./_site/en/intro/index.html`),
	so inter-file links have to be formatted as <code>../<em>chapter</em>/</code>
	and links to specific targets (like glossary entries) as <code>../<em>chapter</em>/#<em>id</em></code>.

There are a few utility scripts in `./bin` inherited from earlier projects
to do things like check the consistency of glossary entries,
look for non-ASCII characters in files, and so on.
It's simpler than the process for *[T3](http://teachtogether.tech)*,
but there are still more moving parts than I'd like:
in particular,
having to stitch all the files in a multi-file Jekyll site together feels like something that
should have already existed.
If you're interested in helping to streamline it,
or in contributing to the content,
[we'd like to hear from you](mailto:gvwilson@third-bit.com).
