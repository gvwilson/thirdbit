---
title: "Snailz"
date: 2024-12-14
---

Earlier this year I put together notes for
a companion to the [JavaScript][sdxjs] and [Python][sdxpy] versions of *Software Design by Example*
aimed at [research software engineers][rse].
I shelved [the project][rsdx] because the (lack of) reaction to the first two books
convinced me that this isn't what most people are looking for,
but I still hope that one of the software packages I built along the way might be useful.

[Snailz][snailz-package] is a set of [synthetic data generators][synthetic]
that simulate the collection, storage, and analysis of data related to
snails in the Pacific Northwest
that are growing unusually large as a result of exposure to pollution.

-   One or more *surveys* are conducted at one or more *sites*.
-   Each survey collects *genomes* and *sizes* of snails.
-   A *grid* at each site is marked out to show the presence or absence of pollution.
-   *Laboratory staff* perform *assays* of the snails' genetic material.
-   Each assay plate has a *design* showing the material applied and *readings* showing the measured response.
-   Plates may be *invalidated* after the fact if a staff member believes it is contaminated.

The first diagram below shows the schema of the database that holds the results;
the second shows how various scripts and parameter files interact
to create that database.
Along the way,
the scripts also create CSV files describing the designs of genomic assay plates
and both messy and tidy versions of readings for those plates.
The whole process is documented on [the package site][snailz-site],
and all the code is open source.

<figure>
  <img src="@root/files/2024/snailz-schema.svg" alt="Database schema of snailz data">
  <figcaption>Snailz database schema</figcaption>
</figure>

<figure>
  <img src="@root/files/2024/snailz-workflow.svg" alt="Workflow for generating snailz data">
  <figcaption>Snailz data generation workflow</figcaption>
</figure>

[rsdx]: https://gvwilson.github.io/rsdx/
[rse]: https://en.wikipedia.org/wiki/Research_software_engineering
[sdxjs]: @root/sdxjs/
[sdxpy]: @root/sdxpy/
[snailz-package]: https://pypi.org/project/snailz/
[snailz-site]: https://gvwilson.github.io/snailz/
[synthetic]: https://en.wikipedia.org/wiki/Synthetic_data
