---
title: "Software Design by Example 18: Package Manager"
date: 2023-01-24
year: 2023
---

Inspired by the [Comprehensive TeX Archive Network][ctan],
most languages now have an online archive from which developers can download packages.
Each package typically has a name and one or more version(s);
each version may have a list of dependencies,
and the package may specify a version or range of versions for each dependency.

Finding a consistent set of things to install is an intrinsically hard problem.
If A and B require different versions of C,
it might not be possible to use A and B together at all.
On the other hand,
if A and B requires ranges of versions of C and those ranges overlap,
a workable combination might exist.

[Chapter 18][sdxjs_packman] of [*Software Design by Example*][sdxjs]
therefore explores how to search for something legal.
Almost every real package manager does this with some sort of constraint solver,
but I decided not to use one in this chapter because their documentation is mostly awful.
[This tutorial on Z3][z3_tutorial] isn't bad,
but as soon as you need to go deeper,
[the full documentation][z3] seems designed to keep working programmers at bay.
I think that's a shame:
constraint solvers are tremendously powerful tools,
and deserve to be more widely used.

> Terms defined: backward-compatible, combinatorial explosion, heuristic, manifest, patch, prune, SAT solver, scoring function, seed, semantic versioning.

[ctan]: https://www.ctan.org/
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxjs_packman]: {{'/sdxjs/package-manager/' | relative_url}}
[z3]: https://z3prover.github.io/papers/programmingz3.html
[z3_tutorial]: https://microsoft.github.io/z3guide/programming/Z3%20JavaScript%20Examples
