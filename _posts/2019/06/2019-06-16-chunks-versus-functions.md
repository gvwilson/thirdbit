---
layout: post
date: 2019-06-16 12:27
title: "Chunks versus Functions"
---

I have now done two multi-page analyses in R Markdown,
and one thing I've noticed is that I'm writing fewer functions than I normally would.
A command-line script that I put together this morning to check a book I'm working on,
for example,
has 8 functions in 76 lines of code,
or 9.5 lines of code per function.
The analysis script I wrote for a recent paper,
on the other hand,
has 12 functions for 640 lines of code,
which is 53 lines per function.

The difference is that most of the code in the analysis script
is in code blocks rather than functions.
Most of the functions in my command-line scripts are only called from one place;
I use them to decompose work into comprehensible pieces
rather than to eliminate redundancy.
Code chunks give me another way to do that,
albeit a less structured one:
I've been bitten several times by removing or renaming a variable in one chunk
that another chunk further down relies on.
I suspect this means that code chunks are going to acquire some kind of modularization
equivalent to parameters and return values.
If you want to work at the intersection of HCI and language design,
there would be worse places to start than this...
