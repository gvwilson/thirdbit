---
date: 2010-09-15
original: swc
title: Testing Scientific Software
---
<p>Yesterday, Michael Feathers tweeted that, "The hardest bit of  TDD [test-driven development] for ppl in scientific computation is that they often don't know  what their intermediate results should be." I'd go further: if the average scientist or engineer knew what the output of their program was supposed to be, they wouldn't need to run the program. And if you don't know what answer is right, what do you compare your tests' output to?</p>
<p>Coincidentally, one of our readers sent us this a couple of days ago:</p>
<blockquote><p><em>Forgive my ignorance, but I have just watched all the lectures on testing, and I'm a little fuzzy on how I can put all this knowledge to use for me.</em></p>
<p><em>I do CFD programming to solve fluid flow and heat transfer problems.  I write in Fortran, code that solves an entire problem start to finish (obviously a collection of subroutines and modules). Then I use Python as a "driver" to set the values of my input variables, create input files, run the compiled code, write output files and gnuplot files to create some plots. I loosely follow the logic in <a href="http://www.amazon.com/gp/product/3540739157">Hans Petter Langtangen's book</a>.</em></p>
<p><em>Most of your lectures pertained to testing functions.  I hardly ever use them–should I be?  And how can I independently test a subroutine–or should I be?  Lets say that I run the code to solve a known problem–should I use the same pass/fail criteria that you talk about in the lecture?</em></p>
<p><em>What about testing to find the right values for variables–i.e. grid resolution studies.  Should I automate these?</em></p>
<p><em>I really would like to get these concepts clear, because I don't do ANY regression testing right now, and I know (as you point out) how dangerous that can be.<br />
</em></p></blockquote>
<p>I have some answers, but before I post them, I'd be interested in hearing from other readers: what do you do? What do you expect others to have done when you're reviewing their papers?</p>
<p>Note: readers interested in this subject might enjoy Rebecca Sanders and Diane Kelly's paper, "Dealing with Risk in Scientific Software Development" (<em>IEEE Software</em>, 25(4), July 2008).</p>
