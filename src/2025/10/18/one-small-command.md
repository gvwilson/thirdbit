---
title: One Small Command
date: 2025-10-18
---

> Please note that I am suffering from jet lag and recovering from a bad cold while writing this,
> which means my proposal may well be garbage.

I've had a lot of conversations over the years about
the differences in how software engineers and data scientists work.
One example is how they manage software:

-   Software engineers regard duplicated code as sinful and refactor to avoid it.

-   Data scientists routinely copy a notebook or a script and make small changes to do a new data analysis.
    After many years,
    I have accepted that they are right to do so:
    their analyses are often exploratory one-offs,
    so copy-and-modify is more efficient than generalize-and-parameterize.

The problem is that software engineers build tools for software engineers,
which means they don't automatically support data scientists' workflows.
Continuing the refactor-versus-copy example,
Git doesn't have a way to explicitly say "this file started as a copy of that one".
Git has a way to say "this file was moved or renamed" (`git mv`),
but there isn't a corresponding `git cp` command
because software engineers believe that you shouldn't be doing that.
You can ask Git to guess which files were copied in each commit:

```
git log --find-copies --diff-filter=C --stat
```

but (a) you probably didn't know this existed,
(b) you're not going to remember it,
and (c) Git's heuristics often produce incorrect answers.

So let's add `git cp` so that the log records copying events explicitly.
That will allow us to trace the lineage of copied-and-modified notebooks and scripts
(and the copied-and-modified configuration files that software engineers create
because they don't think of YAML and TOML as code).
Doing this won't solve all our traceability problems,
but I think it will solve some of them,
and we'll learn something useful from its failure if it doesn't.
