---
title: "Never Mind the Concurrency, What About the Math?"
date: 2009-11-01 12:10:01
year: 2009
---
Lots of people are touting functional programming (FP) as a solution to the problem of ever-increasing concurrency. I think the case is "<a href="http://en.wikipedia.org/wiki/Not_proven">not proven</a>": I have never seen any trustworthy studies comparing the productivity or post-release fault rate of developers using FP with those using more popular approaches.

What I find more interesting right now is the possibility that wider adoption of FP will help turn software engineering into a real engineering discipline—one whose practitioners routinely <em>use</em> complex mathematics rather than doing proofs <em>about</em> that mathematics. Formal verification tools like <a href="http://en.wikipedia.org/wiki/SPIN_model_checker">SPIN</a> and <a href="http://en.wikipedia.org/wiki/Alloy_Analyzer">Alloy</a> are becoming both more powerful and more usable with every passing year; meanwhile, a growing number of developers are learning the hard way that they can't "code and fix" their way to reliable concurrent software. I wouldn't be surprised if programmers start adopting functional languages because they are a better target for analysis and proof tools than imperative languages, rather than any intrinsic productivity difference when used traditionally.
