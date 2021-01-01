---
title: "Explanation-Oriented Programming"
date: 2017-12-27 05:20
year: 2017
---

I'm trying to write a small program in a language I don't yet know well.
Each step forward takes two or three tries as I stumble over things I don't know about the language,
things I don't know about my data,
and things I don't know about the problem I'm trying to solve.
I'm learning as I go,
but most of what I learn won't be obvious to whoever comes next.
They will see,
for example,
that when I get a list of names matching `*.txt`,
I check that each is a file before trying to read it.

I could add a comment to the code to say,
"Believe it or not, somebody named a bunch of directories `a.txt`, `b.txt`, and so on,
so this check is actually necessary,"
but even that is inadequate.
I'm overwriting early attempts with more informed ones as my problem teaches me how best to solve it.
I think that understanding those early attempts–those plausible failures–is essential
to understanding the "why" of the program as it finally is,
but by the time this code ships,
they will exist nowhere but in my head.

I've gone through this with every program I've ever built.
As Imre Lakatos pointed out many years ago
in [a book that completely changed how I see the world](https://www.amazon.com/Proofs-Refutations-Mathematical-Discovery-Philosophy/dp/1107534054/),
every made thing,
from a hammer to a mathematical proof,
is just the last slice in a long history of trial and error:
looking at them is like looking at the blunt end of a cylinder and thinking it's a circle.

I don't know of any design discipline that captures and conveys "why" adequately.
What I do know is that more than half of the chapters in
*[The Architecture of Open Source Applications](http://aosabook.org)*
explained the state of their chosen program by recapitulating its history.
Rather than obsessing about type systems,
perhaps language designers would do well to look for ways to capture this information
so that we don't all have to painstakingly retrace the steps of so many of our peers.
