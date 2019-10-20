---
title: "Is This a Notional Machine for R?"
date: 2019-07-15 04:30
---

A year ago,
I wrote [a description of a notional machine for Python]({{site.github.url}}/2018/04/12/notional-machine-for-python.html),
i.e.,
the mental model of how Python programs execute that I want to convey to learners when I'm teaching.
I didn't get much feedback on it at the time,
so I still don't know how well it corresponds to other people's notional machines,
but it was apparently mentioned in
[a recent workshop on notional machines](https://www.dagstuhl.de/de/programm/kalender/semhp/?semnr=19281),
so I thought it might be worth following up by describing my notional machine for
the tidyverse in R
(the programming framework I've learned most recently).

1. When code is loaded,
   R converts it to a sequence of instructions
   that are stored in memory just like any other data.

1. When code is executed,
   R steps through the instructions,
   doing what each tells it to in turn.

1. A program manipulates three basic types of data:
   numbers, text, and Booleans.

1. A program stores data in vectors,
   each of which contains zero or more values of the same type.

1. Vectors may contain the special values `NA` (for missing data)
   and `NaN` (for illegal numbers, like the result of dividing by zero).

1. Basic operations like addition work on corresponding elements of vectors.

1. A scalar like `3.14` or `"hello"` is just a vector of length 1.
   Its value is repeated as necessary when it's combined with a longer vector
   (which is why `1 + X` works).

1. Vectors are usually not used on their own.
   Instead, they are combined into tables,
   each of which is a list of named vectors of the same length (but possibly different types).

1. We think of the columns (vectors) in a table as statistical variables,
   and the rows (corresponding elements) as observations of those variables.

1. Vectors are not modified after they are created.
   Instead,
   a program calculates new vectors and adds them to existing tables,
   or uses them to create entirely new tables.

1. A program can do different calculations depending on the values in vectors,
   or keep only a subset of results to produce a vector of a different length than the original.

1. We make programs easier to understand by writing functions,
   which are recipes that give a name to a series of calculations.

1. When a function is called,
   a new stack frame is pushed on the call stack.

1. When a variable is used,
   R looks for it in the top stack frame.

1. When the function completes or returns,
   R switches from its blob of instructions
   back to the blob it was executing beforehand.
   If there isn't a "beforehand",
   the program has finished.

1. The functions that operate on tables are usually combined to create pipelines.
   A pipeline starts with a table (or with a function that reads a table);
   the output of each function is used as the input of the next in the pipeline,
   and only the output of the last function in the pipeline is displayed.

A few notes:

1. This notional machine overlaps with that for Python in many ways,
   which is unsurprising given that they are both dynamically-typed, interactive, and garbage-collected.
1. The elements in this notional machine *aren't* presented in the order in which I would teach them;
   this description is the model I want learners to have at the end of an introductory course.
1. It doesn't include loops or conditionals,
   since modern R is a mostly-functional language.
1. It also doesn't include [non-standard evaluation]({{site.github.url}}/2018/11/16/non-standard-evaluation.html),
   or try to explain that you can pass column names to functions as if they were variables.
   In my (so far limited) teachinge experience,
   questions about this don't come up:
   I suspect that people who are new to programming don't know enough to realize how weird this is,
   but that's just a guess.
   If NSE is part of your notional machine for novices,
   I'd really like to hear what form it takes.
