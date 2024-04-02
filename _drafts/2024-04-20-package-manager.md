---
title: "Software Design by Example in Python 20: A Package Manager"
date: 2024-04-20
year: 2024
---

I had to learn almost as much to write [Chapter 20: A Package Manager][sdxpy_pack]
as I did to write [the chapter on databases][sdxpy_db].
Recursively enumerating all possible combinations of packages
to find ones that were compatible with each other
was relatively straightforward
(by which I mean that
someone taught me how to do it so long ago
that it seems like I've always known).
Using a theorem prover to do this more efficiently,
on the other hand,
was brand new.
I worked on a theorem prover for modal logics for my master's degree,
but it used a completely different approach and was thirty-nine years ago.
I almost gave up on [Z3][z3] several times—its documenation is terrible—but
then I stumbled across [this talk by Andreas Zeller][zeller_talk]
and things started to make sense.
I don't know if my exposition does the subject justice,
but I'm grateful to have had an excuse to dive into it.

<img class="centered" src="{{'/sdxpy/pack/concept_map.svg' | relative_url}}" alt="Concept map for a package manager"/>

> Terms defined: accumulator, backward-compatible, Boolean value, combinatorial explosion, cross product, model, patch, Recursive Enumeration pattern, scoring function, search space, semantic versioning.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[sdxpy_db]: {{'/sdxpy/db/' | relative_url}}
[sdxpy_pack]: {{'/sdxpy/pack/' | relative_url}}
[z3]: https://en.wikipedia.org/wiki/Z3_Theorem_Prover
[zeller_talk]: https://www.fuzzingbook.org/html/AcademicPrototyping.html
