---
title: "Software Design by Example in Python 4: Matching Patterns"
date: 2024-04-05
year: 2024
---

As I wrote [last year][sdxjs_pattern_matching],
every piece of technical writing I've ever done has been shaped by the work of
[Brian Kernighan][kernighan].
His books didn't just teach me how to design software;
the clarity of his explanations gave me a model to imitate and a standard to strive for.

It was therefore one of the proudest moments of my life
when Kernighan agreed to contribute a chapter on matching regular expressions to [*Beautiful Code*][bc] in 2006.
His short C program only matched the patterns shown below,
but as Kernighan wrote,
"This is quite a useful class;
in my own experience of using regular expressions on a day-to-day basis,
it easily accounts for 95 percent of all instances."

<div align="center" markdown="1">

| Meaning | Character |
| ------- | --------- |
| Any literal character *c* | *c* |
| Any single character | . |
| Beginning of input | ^ |
| End of input | $ |
| Zero or more of the previous character | * |

</div>

After teaching this material last spring,
I decided that [this chapter][sdxpy_glob] would cover the patterns use in globbing filenames
rather than the subset of regular expressions for text in [the JavaScript version][sdxjs_regex].
Re-implementing this still turned out to be
a natural way to introduce the [Open-Closed Principle][open_closed],
the [Chain of Responsibility][chain] and [Null Object][null_object] design patterns,
some refactoring steps,
and the idea of test-driven development,
which isn't bad for a one-hour lesson.

<img class="centered" src="{{'/sdxpy/glob/concept_map.svg' | relative_url}}" alt="Concept map for pattern matching"/>

> Terms defined: Chain of Responsibility pattern, child class, Extract Parent Class refactoring, globbing, greedy matching, helper method, inheritance, lazy matching, literal (in parsing), Null Object pattern, refactor, regular expression, signature, technical debt, test-driven development.

<img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">

[bc]: https://www.oreilly.com/library/view/beautiful-code/9780596510046/
[chain]: https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern
[kernighan]: https://www.cs.princeton.edu/~bwk/
[null_object]: https://en.wikipedia.org/wiki/Null_object_pattern
[open_closed]: https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle
[sdxjs_regex]: {{'/sdxjs/pattern-matching/' | relative_url}}
[sdxjs_pattern_matching]: {{'/2023/01/09/sdxjs-pattern-matching/' | relative_url}}
[sdxpy]: {{'/sdxpy/' | relative_url}}
[sdxpy_glob]: {{'/sdxpy/glob/' | relative_url}}
