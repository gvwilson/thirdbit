---
title: "Teaching Code Review"
date: 2020-04-06
---

I have taught code review a few times to computer science students (but not yet to data scientists).
The method I've used is:

1.  Give learners a half-page program and a short checklist (6-8 points) of things to look for.

2.  They have 5 minutes to go through the code and mark it up with numbers from the checklist
    ("this line violates rules 5 and 8").

3.  We then go through it as a class so that they compare their evaluation with mine.
    This helps them understand how to interpret the points in the checklist.

4.  Repeat the exercise with another piece of code and the same checklist.
    Hopefully there will be closer agreement between their evaluation and mine
    now that they've seen how to interpret the checklist items.

5.  Give them a homework exercise with a larger piece of code (a full page, maybe longer)
    and a longer checklist (12-15 items).

Some of the items in the checklist can come straight from sources like
Python's [PEP-8 style guide](https://www.python.org/dev/peps/pep-0008/)
or the [tidyverse style guide](https://style.tidyverse.org/).
Others should require higher-level thinking,
e.g.,
"function should be split" or "functions should be combined".
For example,
this short Python program is supposed to count stop words in a list of strings:

```
stops = ['a', 'A', 'the', 'The', 'and']

def count(ln):
    n = 0
    for i in range(len(ln)):
        line = ln[i]
        stuff = line.split()
        for word in stuff:
            # print(word)
            j = stops.count(word)
            if (j > 0) == True:
                n = n + 1
    return n

import sys

lines = sys.stdin.readlines()
# print('number of lines', len(lines))
n = count(lines)
print('number', n)
```

I expect learners to say that:

-   We should use two blank lines before the function definition on line 3 and after it on line 15.
-   Using `== True` or `== False` is redundant
    (because `x == True` is the same as `x`
    and `x == False` is the same as `not x`).
-   The `import` on line 15 should be at the top of the file.
-   The commented-out `print` statements should be removed.
-   The variables `ln`, `i`, and `j` should be given clearer names.
-   The outer loop in `count` loops over the indices of the line list rather than over the lines.
    It should do the latter (which will allow us to get rid of the variable `i`).
-   There's no reason to store the result of `line.split` in a temporary variable:
    the inner loop of `count` can use it directly.
-   Since the set of stop words is a global variable,
    it should be written in upper case.
-   We should use `+=` to increment the counter `n`.

I would probably also point out that:

-   Rather than reading the input into a list of lines and then looping over that,
    we can give `count` a stream and have it process the lines one by one.
-   Since we might want to use `count` in other programs some day,
    we should put the two lines at the bottom that handle input into a conditional
    so that they aren't executed when this script is imported.
-   Rather than counting how often a word occurs in the list of stop words with `stops.count`,
    we can turn the stop words into a set and use `in` to check words.
    This will be more readable *and* more efficient.

The last thing I do is show them what code looks like after problems have been fixed:

```
import sys


STOPS = {'a', 'A', 'the', 'The', 'and'}


def count(reader):
    n = 0
    for line in reader:
        for word in line.split():
            if word in STOPS:
                n += 1
    return n


if __name__ == '__main__':
    n = count(sys.stdin)
    print('number', n)
```

I haven't (yet) had learners do code reviews with checklists on GitHub,
but it seems like a natural next step.
