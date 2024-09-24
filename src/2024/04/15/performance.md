---
title: "Software Design by Example in Python 15: Performance Profiling"
date: 2024-04-15
---

After previous chapters on webbish things,
[Chapter 15: Performance Profiling][sdxpy_perf] sets off in a new direction.
There are basically two ways to store a dataframe:
as heterogeneous rows or as homogeneous columns.
Which one performs better depends on the mix of operations in your program.
If you are filtering records,
row-wise storage saves you the cost of assembling values scattered across several columns.
If you are selecting columns,
on the other hand,
the column-wise representation imposes almost no overhead at all.

This chapter builds on earlier exposition of the difference between interface and implementation
to create two simple dataframe classes with identical interfaces,
then shows how to use a synthetic benchmark to compare their performance
on a mix of operations.
The answer isn't surprising:
row-wise is better if you're doing a lot of row-oriented operations
and column-wise if you're doing column-oriented ones.
What *has* surprised my students,
though,
is that software performance can be studied empirically.
Many didn't know that profilers exist;
most had never used one,
and none had ever benchmarked different implementations against each other before.
I've complained many times that universities don't offer courses on debugging;
if I was in charge of curriculum,
I would also try to add a senior undergraduate course on performance profiling and optimization
because of what can be learned about computers by doing it.

<img class="centered" src="@root/sdxpy/perf/concept_map.svg" alt="Concept map for performance profiling"/>

> Terms defined: batch processing, benchmark, column-wise storage, data engineer, dataframe, docstring, immutable, index (a database), join (tables), online analytical processing, online transaction processing, parameter sweeping, profiling, row-wise storage.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[sdxpy]: @root/sdxpy/
[sdxpy_perf]: @root/sdxpy/perf/
