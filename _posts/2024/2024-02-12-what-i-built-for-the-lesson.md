---
date: 2024-02-12
year: 2024
title: "What I Built for the Lesson"
---

Earlier today I finished the first complete version of the SQL tutorial I've been working on,
(now called [The Querynomicon][sql-tutorial]).
As [the FAQ][contrib] says,
I built it with [Jekyll][jekyll] because
it's the default for GitHub Pages,
and because if I used something more comfortable like [Ark][ark]
I would have been tempted to fiddle with the template instead of writing content.

I wound up fiddling with the template anyway,
though.
Here's what I had to build:

1.  A glossary in a [Glosario][glosario]-formatted YAML file
    that is included in the body of the lesson.
    The first use of each term in the glossary links to the appropriate entry.
    I *haven't* written a script to check that every glossary entry is referred to exactly once,
    but I did that for my [most][sdxjs] [recent][sdxpy] books.

1.  A list of links with shortcodes, URLs, and titles,
    also stored as YAML.
    All the links in the body of the lesson use these shortcodes
    so that I can keep references consistent.

1.  A Jekyll inclusion that copies a text file into the generated page.
    I use this to include code examples and their corresponding output;
    the Jekyll inclusion can optionally slice a comment-demarcated section of the file
    so that only the interesting parts are shown in the page.
    (This capability is one of the reasons I don't use computational notebooks for lessons:
    it's surprisingly hard to have one display a section from a larger block of code.)

1.  Another Jekyll inclusion that takes a filename stem and includes
    the matching source file and its output.
    This inclusion uses the one above;
    I created it mostly to make sure that I didn't show the output of sample A
    when I should show the output of sample B.

1.  A Makefile that re-runs the code examples and saves their output.
    The Makefile also has a rule that zips up the examples to create a downloadable file
    and other rules to run various linting checks on the site and the examples.

1.  Some more Jekyll inclusions to create numbered section headings,
    exercises,
    and figures.

1.  Yet another Jekyll inclusion to turn boilerplate files like `CODE_OF_CONDUCT.md`
    into pages in the tutorial site.
    Without this,
    I would either have to add Jekyll metadata to the tops of those files
    (which would make them look odd when viewed directly on GitHub)
    or duplicate the information
    (which would inevitably become inconsistent).

1.  A list of SQL keywords taken from the [SQLite][sqlite] site
    and a script that parses my code samples using Andi Albrecht's [sqlparse][sqlparse] module
    to find keywords that the lesson doesn't mention.

1.  A configuration file with settings for [SQLFluff][sqlfluff],
    a SQL linter that was surprisingly difficult to configure
    but which has helped me format my examples consistently.

1.  A YAML-formatted list of people to thank
    and a Jekyll inclusion to insert their names into the generated page.

1.  A `requirements.txt` file that lists the Python packages needed to rebuild the site
    and re-run the examples.

[ark]: https://www.dmulholl.com/docs/ark/main/
[contrib]: https://gvwilson.github.io/sql-tutorial/contributing/
[glosario]: https://glosario.carpentries.org/
[jekyll]: https://jekyllrb.com/
[sql-tutorial]: https://gvwilson.github.io/sql-tutorial/
[sdxjs]: {{"/sdxjs/" | relative_url}}
[sdxpy]: {{"/sdxpy/" | relative_url}}
[sqlfluff]: https://sqlfluff.com/
[sqlite]: https://sqlite.org/
[sqlparse]: https://pypi.org/project/sqlparse/
