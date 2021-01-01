---
title: "Python, Typing, and the Scientific Spirit"
date: 2005-01-16 22:11:49
year: 2005
---
<p>There's been a minor blog storm over the last few weeks about Guido
van Rossum's proposal to add optional type declarations to Python [<a href="#1">1</a>].  Guido believes it will help catch errors before
code is run (or in sections of code that aren't exercised by unit
tests), but other people say no, the extra clutter and complexity will
spoil Python's clean lines.</p>

<p>The problem is, neither side has any real data to back up their
arguments.  Will optional static typing catch 1% of errors?  10%?
50%?  90%?  And how cost-effective will it be?  If it takes twice as
long to write code, but 50% of errors that would otherwise not show up
until run-time are caught on load, is that a net win or not?</p>

<p>Four and a half years ago, when Python's developers were arguing
over the syntax for multi-list iteration, I ran <a href="http://mail.python.org/pipermail/python-dev/2000-July/006427.html">an
experiment</a> to find out how well users would understand some of the
proposals.  In the same spirit, I'd like to see the advocates and
opponents of optional static typing put their heads together and
design an experiment to gauge its costs and benefits.  I'd be very
happy to run that experiment here in Toronto, and I'm sure others
would do the same in their user communities.  Best case, the results
convince all but a few die-hards that it is or isn't worth doing.
Worst case, figuring out how to tell if optional static typing is a
win or not will clarify the debate, and we'll all have the
satisfaction of knowing that we at least tried to be scientific about
programming language design.</p>

<p>[<a name="1">1</a>] See these <a href="http://www.artima.com/weblogs/viewpost.jsp?thread=85551">two</a>
<a href="http://www.artima.com/weblogs/viewpost.jsp?thread=86641">articles</a>
and many follow-ups on the <a href="http://www.pythonware.com/daily/">Daily Python URL</a>.</p>
