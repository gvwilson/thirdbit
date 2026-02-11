---
title: "Thirty Years of Python"
template: slides
date: "2026-02-19"
---

## Why Should You Listen to Me?

-   Fellow of the Python Software Foundation
    -   I wrote the PEP for sets
-   I've been using Python for 30 years
    -   Teaching it for 28 of those
    -   Including writing a few books


--

-   Much better at teaching than graphic design

---

## Are Some Languages Better?

Stefik2013: "An Empirical Investigation into Programming Language Syntax"

-   Measured how easily novices could read:
    -   Perl
    -   Quorum: the language their team is building
    -   Randomo: syntax "designed" by rolling D&D dice

--

-   Perl is as hard for novices to learn as a language with a randomly-designed syntax

---

## Are Some Languages Better?

-   Second study
    -   More subjects
    -   Multiple assessment strategies
-   Languages in the C family are as hard for novices to learn to read as a randomly-designed language
-   Ruby and Python are easier
-   <a href="https://quorumlanguage.com/">Quorum</a> is easier still

---

## Show Me the Data

-   Gao2017: Strong typing catches about 15% of bugs

<div class="row">
  <div class="col-12 center">
    <img src="typescript-features.png" alt="Typescript feature adoption" width="90%">
    <br>
    From Scarsbrook2023
  </div>
</div>

---

## In the Beginning…

-   …there was Perl
-   Every page of the O'Reilly Pocket Guide included at least one use of "except", "unless", or "however"
-   Hm: there's this new language called Python



--

-   Indentation? Really? Bleh

---

## It Was More Teachable

-   Ran classes at Los Alamos National Laboratory and elsewhere
    -   Scientists turned programmers
-   More learnable than Bash, Perl, C++, or Java
    -   And cheaper than MATLAB

--

-   I should say "appeared to be more learnable"

---

## The Golden Age

-   Python 2 was better than its predecessors

--

-   Raise your hand if you're old enough to remember this:

```python
while True:
    line = reader.readline()
    if not line:
        break
    …process the line…
```

---

## The Golden Age

-   Python 2 was also better than its successors



--

-   Type hints
-   `yield` *and* `async`/`await`
-   `match`
-   Meta-your-name-goes-here
-   Walrus operator

--



-   If I wanted to write Java, I'd write Java

---

## Old Man Shakes Fist At Clouds

-   The problem is *learnability*
-   "You don't have to teach [X] to beginners"
-   But they're going to see it in examples
    -   And be told to use it by LLMs



--

-   [Lua](https://www.lua.org/) proves that boundless growth is not inevitable
-   [Project Oberon](https://www.projectoberon.net/) proved that it's not necessary

---

## Conclusion

-   I write Python code five or six days a week
    -   Even though I'm unemployed :-)
-   Every feature that's there is there for a good reason
-   But the cumulative effect has (in my opinion) been harmful
-   Or maybe just changed the audience



--

1.  Do you know which parts of your software your users are actually using?
2.  Does your project have a complexity budget?

---

<div align="center">
  <h2>Thank You</h2>
  <p><img src="@root/files/cv/gvwilson-gage-2019.png" width="40%"></p>
  <p><a href="http://third-bit.com">Greg Wilson</a></p>
  <p><a href="mailto:gvwilson@third-bit.com">gvwilson@third-bit.com</a></p>
  <p><a href="http://third-bit.com/talks/py30/">http://third-bit.com/talks/py30/</a></p>
</div>
