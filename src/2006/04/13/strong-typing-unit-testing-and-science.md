---
title: "Strong Typing, Unit Testing, and Science"
date: 2006-04-13
---
<p>I've doing a technical review of a new book on object-oriented
analysis &amp; design that spends several pages discussing
strongly-typed vs. freely-typed languages (using Java and Ruby as
examples).  The author asserts that unit testing does for FTLs what
static type-checking does for STLs.  I've heard this claim before—in
fact, I may even have made it myself once or twice—but the more I
think about it, the more problematic it seems.</p>

<p>The argument is that programmers don't actually make type errors
very often, so requiring them to specify types all the time slows
initial development down.  Yes, FTL advocates acknowledge, having
explicit types helps with maintenance and extension, but so do unit
tests.  The latter are more flexible (i.e., you can check a lot more
than just variable types in unit tests), and should be written even
for strongly-typed code, so why mandate typing?</p>

<p>What's missing from this, though, is any consideration of
cost-effectiveness.  Which is faster: writing a dozen unit tests, or
declaring the parameter and return types of a dozen methods?  Which
technique catches more errors?  And crucially, which catches more
errors per minute or hour of programmer time?  It's like asking which
is more productive: two programmers writing code and tests
independently, XP-style pair programming, or having one programmer
write code while another writes tests?  I think these questions can
and should be answered <a href="http://www.cs.toronto.edu/~sme/CSC2130/index.html">empirically</a>;
I also think that the fact so many people feel it's OK to have an
opinion one way or the other, without any data to base it on, is one
more sign that "computer science" doesn't yet deserve the second part
of its name.</p>
