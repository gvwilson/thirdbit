---
title: "Software Design by Example in Python 15: Performance Profiling"
date: 2024-04-15
year: 2024
---

After previous chapters webbish things,
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
as noted above,
row-wise is better for row-oriented operations
and column-wise for column-oriented ones.
What *has* surprised my students,
though,
is that software performance can and should be studied empirically.
Some didn't know that profilers exist;
most had never used one,
and none had ever benchmarked different implementations against each other before.
I've complained many times that universities don't offer courses on debugging;
if I was in charge of curriculum,
a senior undergraduate course on performance profiling and optimization would be my second addition
because of what can be learned about computers by doing it.

<img class="centered" src="{{'/sdxpy/perf/concept_map.svg' | relative_url}}" alt="Concept map for performance profiling"/>

> Terms defined: batch processing, benchmark, column-wise storage, data engineer, dataframe, docstring, immutable, index (a database), join (tables), online analytical processing, online transaction processing, parameter sweeping, profiling, row-wise storage.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[sdxpy]: {{'/sdxpy/' | relative_url}}
[sdxpy_perf]: {{'/sdxpy/perf/' | relative_url}}
