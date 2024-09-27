---
date: 2018-07-05
title: Performance Curves, Curriculum Design, and Trust Revisited
---

Suppose you have a processing pipeline with three stages,
each of which takes one second to run.
What's its overall performance?
As Roger Hockney pointed out in the 1980s, that question isn't well formed.
What we really need to ask is how its performance changes as a function of the size of its input.
It takes 3 seconds to process one piece of data,
4 to process two,
5 to process three, and so on.
Inverting those numbers,
its rate is 1/3 result per second for one piece of data,
1/2 result/sec for two, and so on:

![Throughput as a Function of Data Size](@root/files/2012/03/curve.png)

A curve like this can be characterized by two values: *r<sub>&infin;</sub>*,
which is its performance on an infinitely large data set,
and *n<sub>&frac12;</sub>*,
which is how much data we have to provide to get half of that theoretical peak performance.
Deep pipelines tend to have high *r<sub>&infin;</sub>* (which is good),
but also high *n<sub>&frac12;</sub>* (which is bad);
shallow pipelines have the reverse,
i.e.,
they don't get you as far,
but they get you there sooner.

Something like this idea underpins my approach to teaching computing.
My goal isn't to increase *r<sub>&infin;</sub>*,
but to minimize *p<sub>&frac12;</sub>*,
i.e.,
to help people get some useful results as early as possible so that they'll think it's worth learning more.
What makes this challenging is the fact that learners' performance over time actually looks like this:

![Glass's Law](@root/files/2012/03/final.png)

That dip is due to Glass's Law: every new tool or practice initially slows you down.
If the dip is too deep,
or if it takes too long to recover from it,
most people go back to doing things the way they're used to, because that's the safest bet.

So here's my question:
are there meaningful equivalents to *n<sub>&frac12;</sub>* and *r<sub>&infin;</sub>* for programming tools?
Informally,
what I want is "how long it takes you to become reasonably productive with a tool"
and "how productive you are in absolute terms once you've mastered it".
I suspect "low church" tools like R are better by the first measure,
which might explain why they're increasingly popular for teaching,
while "high church" tools like Smalltalk are better by the second,
which is why professionals building large, complex systems tend to like them.
(I'm also thinking about Hadley Wickham's recently invented distinction,
between "early-worry" and "late-worry" tools,
but I don't think that's quite the same split.)

But what about Scratch?
It won't ever do well on a measure of absolute productivity measured against general programming tasks
because there are things it just can't do,
but on the other hand that's as unfair as asking how good MATLAB is for writing operating systems.

My current thinking is this:

- *p<sub>1/2</sub>* is how long it takes you to reach the point where you can correctly trace and explain the operation of
  a one-page program selected at random from your community's repository (e.g., GitHub or the Scratch site) half of the time.
  Using the community's code repository as an oracle is intended to scale the measure automatically and impartially.

- *n<sub>&infin;</sub>* is how many randomly-selected one-page programs you can successfully reproduce in a day
  given a description of their inputs, outputs, and behaviors.
  (Alternatively, this could be "given a description *and* having read the source code the day before".)
  Again, basing this on the community's code repository is intended to scale the measure
  against the things the language is actually used for.

I'm not happy with either of these;
I'd welcome comments or suggestions about how to improve them,
or an explanation of why this whole idea is wrong-headed.
