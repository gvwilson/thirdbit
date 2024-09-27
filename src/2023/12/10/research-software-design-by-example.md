---
title: "Research Software Design by Example"
date: 2023-12-10
---

I'm thinking about running a 12-week course online next year,
tentatively called "Research Software Design by Example",
to raise money for [Rainbow Railroad][rr].
My plan is to take the same approach as
the [JavaScript][sdxjs] and [Python][sdxpy] versions of
*Software Design by Example*,
i.e.,
to show people how to think about the design of medium-sized programs
by working through scaled-down examples of real applications,
and to introduce some useful computer science-y ideas along the way.
I would be grateful for [feedback][mailto:gvwilson@third-bit.com]
on the very (very) tentative outline below.

Introduction: an overview of where we're going and why.
:   The best way to learn design is to study examples, and the best programs to use as examples are ones like those you want to create. These lessons therefore build small versions of tools that research software engineers build and use every day to show how experienced software designers think. Along the way, they introduce some fundamental ideas in computer science that many self-taught programmers haven't encountered. The lessons assume readers can write small programs and want to write larger ones, or are looking for material to use in software design classes that they teach.

Parsing: convert some messy CSV data files with geocoded pollution measurements into tidy CSV.
:   Research data is often stored in idiosyncratic formats, or must be extracted from documents that were written for people to read rather than for machines to process. Our first lesson therefore shows how to build a parser that can handle several variations of a single data format and how to write command-line tools that respect [Taschuk's Rules][taschuk]
.

Plugin Architecture: find the center point of each polluted region and visualize it.
:   Research data may come from files, databases, websites, and many other sources. Instead of rewriting a program each time a new source becomes available, we can build a plugin architecture that loads data handlers dynamically so that users can extend our program without modifying its internals. Doing this gives us an opportunity to look at how to query a SQL database and at the problem of testing visualizations.

Refactoring: refactor a student-quality Python script that uses invasion percolation to model pollution spread.
:   Computational notebooks are a great tool for exploratory work, but research software engineers must also be able to create software libraries that can be re-mixed and re-used. This lesson therefore critiques and refactors a script that uses invasion percolation to simulate to model the spread of pollution to show how to break code up into comprehensible chunks and how to validate implementations against one another.

Testing: use mocks to test programs that rely on pseudo-randomness.
:   Testing research software is hard: the algorithms are often subtle, and we often don't know what the correct output is supposed to be except in a handful of trivial cases. This lesson introduces several tools that can make the problem tractable, including the use of mock objects to make randomness less random and the use of coverage tools to determine what is and isn't being tested.

Profiling: compare the performance of grid implementations empirically.
:   Some pieces of research software have to be fast in order to be useful. This lesson therefore explores how profiling can help us figure out which parts of our program are worth optimizing. Along the way, it alos looks at how to capture program parameters in reproducible ways and why tuning code can't solve fundamental algorithmic issues.

A Lazy Algorithm: create a lazy implementation of invasion percolation that's much faster.
:   Simple algorithms are easy to implement and test, but often have poor performance. More complex algorithms—particularly lazy algorithms that don't perform calculations until they're sure the results are needed—are harder to write and test, but can improve performance by orders of magnitude. This lessons demonstrates this idea by implementing a better algorithm for invasion percolation, and along the way shows how to refactor code as needs and ideas evolve.

Scaling Up: generate fractals using a workflow runner and store them remotely.
:   Once we have an algorithm that's worth scaling up, we need to actually scale it up. This lesson shows how to describe a workflow as an acyclic graph, how to express that workflow in code to take advantage of cloud computing, and how support tools like logging frameworks and remote data storage can help.

Packaging: navigating the confusion of creating a simple Python package.
:   Creating an installable package is the best way to share your code with other people, but Python's packaging tools are a complex mess. This lesson therefore introduces key ideas such as virtual environments and package manifests while avoiding as much of the complexity as it can.

Synthetic Data Generation: analyze snail genomes to see if a single mutation accounts for size differences.
:   In this lesson we pivot from simulation to data analysis and build a simple pipeline to find out whether a single nucleotide polymorphism can explain differences in the sizes of snails in polluted regions. We also build a synthetic data generator to help us test our analysis pipeline, and use it to show how data analyses can be tested more generally.

Building a Static Site: build a static site to display research results using Ark and Jinja.
:   Sharing knowledge is as much a part of research as asking good questions and getting correct answers. This lesson therefore shows how to use a static site generator to create a website that displays research findings, and how to extend such a tool to handle the idiosyncratic needs of a particular research project.

Scraping Data: pull data from web pages using requests and Beautiful Soup.
:   Some researchers make their data easy to access and use, but in many other cases, the only way to get information is to scrape it off the web. This lesson therefore explains how the web's basic protocols work, how web pages are represented inside programs, and how to build a tool that can extract information from someone else's HTML.

Building a Web Site: build a small Flask web server to display plate data.
:   As a counterpart to the previous lesson, this one shows how web servers handle requests and generate dynamic HTML pages. Understanding how this works will help research software engineers design services of their own and debug them when things go wrong.

Conclusion: what we've covered and where readers might like to go next.
:   Software is usually critiqued by asking if it does what it's supposed to do and if it's pleasurable to use. What is often missing is discussion of whether its design makes it easy to manufacture, test, and maintain. We hope these lessons will help you ask and answer that question about the things you build.

Some of the tools these lessons will use are listed below,
but the goal *isn't* to teach those tools:
it's to use them to teach research software engineers
how to build software that is modular, reusable, testable, comprehensible, and shareable,
and that those five virtues all arrive together or not at all.

-   [Ark](https://www.dmulholl.com/docs/ark/main/) as a static site generator
-   [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/) because of course I would
-   [DVC](https://dvc.org/) for version control of large data files
-   [Faker](https://faker.readthedocs.io/) for generating test data.
-   [Flask](https://flask.palletsprojects.com/) for building a web server
    (because it will return HTML pages—I'd use [FastAPI](https://fastapi.tiangolo.com/)
    if the lesson was about building a web service)
-   [Jinja2](https://jinja.palletsprojects.com/) for templating
-   [Metaflow](https://metaflow.org/)
    (which seems to be the best-supported workflow tool with a pure-Python syntax)
-   [Pandas](https://pandas.pydata.org/)
    (I'd rather use [Polars](https://pola.rs/)—there is
    so much less to explain away—but not enough other tools interoperate with it yet).
-   [Plotly Express](https://plotly.com/python/plotly-express/)
-   [Pony ORM](https://ponyorm.org/)
    (go ahead—read the first answer to [this question](https://stackoverflow.com/questions/16115713/how-pony-orm-does-its-tricks)
    and tell me you aren't impressed)
-   [`requests`](https://requests.readthedocs.io/) for getting data from the web
    and [`geopy`](https://geopy.readthedocs.io/) for handling geocoded data.
-   Several Python library modules, including
    [`coverage`](https://coverage.readthedocs.io/),
    [`dataclasses`](https://docs.python.org/3/library/dataclasses.html),
    [`logging`](https://docs.python.org/3/library/logging.html),
    [`profile`](https://docs.python.org/3/library/profile.html),
    and [`pytest`](https://docs.pytest.org/).

[rr]: https://donate.rainbowrailroad.org/team/515984
[sdxjs]: @root/sdxjs/
[sdxpy]: @root/sdxpy/
[taschuk]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005412
