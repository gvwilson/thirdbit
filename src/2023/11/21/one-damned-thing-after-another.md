---
title: "One Damned Thing After Another"
date: 2023-11-21
---

I promised that I wouldn't write another technical book,
but I didn't say I wouldn't create another course.
I've been working up examples for
a one-semester introduction to software design for research software engineers
similar in spirit to [this book in JavaScript][sdxjs] and [this one in Python][sdxpy]
but emphasizing the kinds of problems RSEs are more likely to encounter.

As with [the Cowichan Problems][cowichan],
I'd like to build the course on a series of example that connect with each other
but can be tackled one by one or out of order.
What I have so far is listed below;
I'd be grateful for suggestions about (a) other design challenges to work through
and (b) a narrative (however fanciful) that connects them to the ongoing story.

1.  Convert some messy CSV data files with geocoded pollution measurements into tidy CSV.
    -   Writing command-line tools that respect [Taschuk's Rules][taschuk].
    -   Creating a data manifest (and why you want one).
    -   Using regular expressions if you have to, but an out-of-the-box parser if one is available.

1.  Use the tidy data to try to find the center point of each polluted region and visualize it.
    -   Finding, installing, and figuring out how to use open source packages.
    -   Using [`geopy`][geopy] to handle geocoded data.
    -   Plotting (and the challenge of testing visualization code).

1.  Walk through a student-quality Python script that uses invasion percolation to model pollution spread.
    -   Reading code.
    -   Breaking code into comprehensible chunks.
    -   Writing docstrings and generating documentation pages.

1.  Show how to use mocks to test a program like invasion percolation that relies on pseudo-randomness.
    -   Deciding what tests to write (assume readers have already met [`pytest`][pytest]).
    -   Creating and using mock objects.
    -   Making "random" reproducible.

1.  Refactor that script into classes with two different grid implementations.
    -   Creating classes and class hierarchies.
    -   Deciding what goes where in such a hierarchy.
    -   Validating implementations against one another.

1.  Measure the performance of those two implementations in order to pick one.
    -   Using [`coverage`][coverage] to determine which parts of the code are(n't) being exercised by tests.
    -   Using [`cProfile`][profile] to determine which parts are expensive.

1.  Convert the performance measurement scripts to use a pipeline runner.
    -   Describing workflows as directed acyclic graphs.
    -   Expressing DAGs in code with [Metaflow][metaflow].

1.  Create a lazy implementation of invasion percolation that's much (much) faster.
    -   Estimating algorithm performance with big-oh.
    -   Extending a class hierarchy to accommodate new features.
    -   Adapting tools written earlier to make all of this simpler to run, test, and document.

1.  Use remote storage for large files
    -   Saving fractals created by invasion percolation for analysis.
    -   Using [DVC][dvc] to store those remotely instead of committing to version control.
    -   Using those files to estimate fractal dimension and density vs. distance from centroid.

1.  Analyze genomic data from snails in polluted areas to see if a single mutation accounts for differences in sizes.
    -   Using a statistical model of single nucleotide polymorphisms (SNPs) to synthesize test data.
    -   Building a pipeline to analyze and visualize that data.
    -   *Note: this is a bit of a jump from previous topics—I need a more connected narrative.*

1.  Get data from a SQL database instead of from CSV files on disk.
    -   Connecting to a database from Python.
    -   Embedding SQL queries in Python and reading results.
    -   Safely parameterizing SQL queries.

1.  Use an ORM to interact with the database.
    -   Creating classes with [Pony][pony] to mirror database tables.
    -   Writing queries in Python rather than as embedded SQL strings.

[coverage]: https://coverage.readthedocs.io/
[cowichan]: @root/2010/06/12/the-cowichan-problems/
[dvc]: https://dvc.org/
[geopy]: https://geopy.readthedocs.io/
[metaflow]: https://metaflow.org/
[pony]: https://ponyorm.org/
[profile]: https://docs.python.org/3/library/profile.html
[pytest]: https://docs.pytest.org/
[sdxjs]: @root/sdxjs/
[sdxpy]: @root/sdxpy/
[taschuk]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005412
