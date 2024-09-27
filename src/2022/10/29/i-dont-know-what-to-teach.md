---
title: "I Don't Know What to Teach"
date: 2022-10-29
---

I've been working with biologists and bioinformaticians for a year now,
and the more time I spend with them,
the more I question what I've been teaching and preaching for the past dozen years.
For example,
one of my colleagues has several hundred Jupyter notebooks in a Git repo,
each of which analyses one or a few datasets.
When a lab scientist sends him new data
he makes a copy of one of the notebooks,
tweaks it (a process which can take anywhere from minutes to days),
and then runs it to produce the plots and tables the scientist needs.

"Why don't you just have one parameterized notebook?" I asked.
"Because every single analysis is different," he said,
patiently and somewhat wearily.
The scientists are exploring new compounds, new experimental methods, new everything.
He's already refactored the shared bits of code into a library,
but if he adds enough options and configuration parameters to those functions
to handle every case,
he will essentially have moved his file structure into an untraceable tangle
of if/else statements
and overridden methods.

I described this to a fellow programmer a few days ago,
and she said,
"Oh come on: there *has* to be a way."
That's when I realized that I don't know how to teach even more than I thought.
The mindset, methods, and tools that software engineer have developed
to solve their problems
aren't automatically a fit for researchers and data analysts.
We're manufacturing t-shirts in standard sizes;
they're tailoring bespoke suits,
and it's wrong in a very self-centered way for us to say
that what they're doing *must* somehow fit into our paradigm.
I therefore need to find things to teach to researchers that are a better fit to their needs,
*and* find ways to convince software engineers
that those needs really are different
and really do need different kinds of support.

*Later:
a data scientist DM'd me to ask why there isn't a `git cp` command
to record the fact that file X is a copy-with-modifications of file Y.
They've seen tools that draw the branch-and-merge structure of Git commits,
and want something similar to show the genealogy of files
that coexist simultaneously in the same branch.
I'm going to have to think about this one…*
