---
title: "Provenance Revisited"
date: 2023-02-26
year: 2023
---

I've been thinking recently about how best to help the data scientists I work with,
and I think the thing they stumble over most is *provenance*,
i.e.,
keeping track of exactly what code was used to produce each result and what data it depends on.
There were some attempts starting in the 00's to address this (see <https://openprovenance.org/>),
but none of them saw significant uptake:
unless every tool in the chain (including legacy tools like 'grep', ad hoc shell scripts, and so on) is instrumented,
there will be gaps in the chain of provenance that undermine the whole exercise.
(If I recall the results of
[the original provenance bakeoff](https://onlinelibrary.wiley.com/doi/10.1002/cpe.1233) correctly,
the only group that had a solution to this problem
instrumented the underlying operating system instead of the individual tools.
That "worked",
but most scientists aren't going to install a new OS on their laptop
just to get a record of exactly which data files they've processed.)

One of my colleagues recently put together a script that tackles this problem in a way I hadn't seen before.
Whenever the scientist runs an analysis, her script uploads a record with:

1. The most recent Git hash of the repo the scientist is working in.

2. A patch of all the files that have been changed in the repo since that hash.

3. The command-line parameters used to run the task.

This seems to give a high degree of reproducibility,
particularly if the data files are stored in something like [DVC](https://dvc.org/).
What it has made me realize is that
the environment around scientific work has changed in useful ways since 2006-07:
for example,
I think it's safe to assume today that scientists are using Git.
I realize that the topic isn't as fashionable as blockchain or machine learning,
but I think a solution *that scientists would actually adopt*
would have a lot of impact.
