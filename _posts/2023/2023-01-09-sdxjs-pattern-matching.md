---
title: "Software Design by Example 7: Pattern Matching"
date: 2023-01-09
year: 2023
---

Every piece of technical writing I've ever done has been shaped by the work of
[Brian Kernighan][kernighan].
*The Elements of Programming Style*,
*Software Tools in Pascal*,
*The Unix Programming Environment*,
and *The C Programming Language*
didn't just teach me how to design software (as opposed to just writing code);
the clarity of Kernighan's explanations gave me a model to imitate and a standard to strive for.

It was therefore one of the proudest moments of my life
when Kernighan agreed to contribute a chapter to [*Beautiful Code*][bc] in 2006.
The subject he chose was matching regular expression—more specifically,
the very first regular expression matcher that [Rob Pike][pike] wrote for Unix in the early 1970s.
It only matched the patterns shown below,
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

Re-implementing this in JavaScript turned out to be
a natural way to introduce the [Open-Closed Principle][open_closed] in object-oriented design
and the [Chain of Responsibility][chain] design pattern.
However,
the chapter was also very frustrating:
a couple of simple animations would have been much easier to understand
than the diagrams and prose I created,
but (a) I didn't have an easy way to create what I wanted,
(b) maintaining animations as examples change is a lot of work, and
(c) they don't really work in print.
I use tools like [PythonTutor][pythontutor] every time I teach live,
and while I'm concerned about the accessibility gap they create,
I am certain that they make hard things much easier.
Perhaps one day someone will define a programming language
whose elements have standard, animatable graphic representations that are supported by IDEs.
Until then,
the best we can do is try to meet the standard that Kernighan set for us forty years ago.

<figure id="pattern-matching-greedy-failure" class="center">
  <img src="{{'/sdxjs/pattern-matching/greedy-failure.svg' | relative_url}}" alt="Overly-greedy matching fails" class="centered">
  <figcaption>Figure 7.4: Why overly greedy matching doesn't work.</figcaption>
</figure>

> Terms defined: base class, Chain of Responsibility pattern, child (in a tree), coupling, depth-first, derived class, Document Object Model, eager matching, eager matching, greedy algorithm, lazy matching, node, Open-Closed Principle, polymorphism, query selector, regular expression, scope creep, test-driven development.

[bc]: https://www.oreilly.com/library/view/beautiful-code/9780596510046/
[chain]: https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern
[kernighan]: https://www.cs.princeton.edu/~bwk/
[open_closed]: https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle
[pike]: https://en.wikipedia.org/wiki/Rob_Pike
[pythontutor]: https://pythontutor.com/
