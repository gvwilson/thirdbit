---
title: "Structural Programming and Rational Metaprogramming"
date: 2008-01-15
---
I keep trying to put extensible programming aside, but it just won't let me let go.  (Yes, I know, the eighties want their lyrics back…)  Most recently, Michael Feathers posted <a href="http://beautifulcode.oreillynet.com/2008/01/structuring_tests_with_operato_1.php">this piece</a> about what he calls <em>structural programming</em>.  As he says:
<blockquote>A structural program (or program snippet) is a program that is essentially a data structure on a page. The structure both dominates and conveys the semantics.</blockquote>
I realized years ago that this was the real difference between agile languages (like Python and Scheme) and sturdy ones (like C++ and Java): the former let you type in your data structures pretty much verbatim, and allows those data structures to include functions as easily as integers and strings.  As a result, you really can work in the Turing Paradise in which programs are data and vice versa.

What's holding us back now is our unwillingness to do more than overload operators.  I can, if I try very hard, abuse this to create a mini-language that lets me type in things that look like decision tables—but Alan help me when I have to debug it.  There's a ton of good research waiting to happen here, and dozens of innovative products waiting to be built…

Coincidentally, I just saw a post from Diomidis Spinellis about <a href="http://www.spinellis.gr/blog/20080113/index.html">rational metaprogramming</a>. It has to lie at the heart of any extensible programming system; there are some interesting comments around his article that are worth following up.
