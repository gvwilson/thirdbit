---
title: "Software Design by Example 18: Package Manager"
date: 2023-01-24
---

Inspired by the [Comprehensive TeX Archive Network][ctan],
most languages now have an online archive from which developers can download packages.
Each package typically has a name and one or more version(s);
each version may have a list of dependencies,
and the package may specify a version or range of acceptable versions for each dependency.

Finding a consistent set of versions to install is an intrinsically hard problem.
[Chapter 18][sdxjs_packman] of [*Software Design by Example*][sdxjs]
therefore explores how to search for something legal.
Almost every real package manager uses some sort of [SMT solver][smt_solver] to do this,
but I decided not to use one in this chapter because their documentation is mostly impenetrable.
[This tutorial on Z3][z3_tutorial] isn't bad,
for example,
but as soon as you need to go deeper,
[the full documentation][z3] seems designed to keep working programmers at bay.

I think that's a shame:
solvers are tremendously powerful tools,
and deserve to be much more widely used.
The working draft of the Python version of this book re-solves the problem from [this chapter][sdxjs_packman] using [Z3][z3],
and goes on to show how it can be used to generate test data as well
using an example borrowed from [Andreas Zeller's][zeller_andreas] excellent lecture
on [academic prototyping][academic_prototyping].
If you'd like to have a look and let me know if it works,
please [reach out][email].

<figure id="package-manager-allowable" class="center">
  <img src="@root/sdxjs/package-manager/allowable.svg" alt="Allowable versions" class="centered">
  <figcaption>Figure 18.1: Finding allowable combinations of package versions.</figcaption>
</figure>

> Terms defined: backward-compatible, combinatorial explosion, heuristic, manifest, patch, prune, SAT solver, scoring function, seed, semantic versioning.

[academic_prototyping]: https://www.fuzzingbook.org/html/AcademicPrototyping.html
[ctan]: https://www.ctan.org/
[email]: mailto:gvwilson@third-bit.com
[sdxjs]: @root/sdxjs/
[sdxjs_packman]: @root/sdxjs/package-manager/
[smt_solver]: https://en.wikipedia.org/wiki/Satisfiability_modulo_theories
[z3]: https://z3prover.github.io/papers/programmingz3.html
[z3_tutorial]: https://microsoft.github.io/z3guide/programming/Z3%20JavaScript%20Examples
[zeller_andreas]: https://andreas-zeller.info/
