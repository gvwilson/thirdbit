---
date: 2011-09-20
original: swc
title: I'm Not Normally Lost for Words
---
<p>I mentioned last week that I'm trying to put together a lecture on packaging and installation. It's proving harder than I expected: I'm not normally lost for words, but I'm struggling to get these ones to come together. My goal is to help people understand what happens when they install software on a computer, so that they can:</p>
<ol>
<li>diagnose and fix problems when things go wrong;</li>
<li>understand why the things that are in packaging tools are there, and how to use them.</li>
</ol>
<p>After a few false starts, I think the best way to do this will be challenge/response, i.e., trace the evolution of a typical scientific software package from a single Python file shared by email to a mix of Python and C that plays nicely with distutils2. Steps I've identified are:</p>
<ol>
<li>A single-file Python script that I email to my labmates whenever I make changes to it.</li>
<li>Adding a version number to that file so that I can keep track of which copy someone has (see the essay on provenance for details).</li>
<li>Splitting that file into multiple Python files and putting them in a directory with an __init__.py file to make a package, and distributing the result as a gzip'd tar file (again, by email).</li>
</ol>
<p>What are the next steps? At some point this lecture will have to explain PATH and PYTHONPATH, what .so and .dll files are, what /etc, .rc files, and the Windows registry are… How do I get there from here?  What steps have <em>your</em> projects gone through, and in what order?</p>
<p><em>Later: just to clarify, challenge/response is a teaching style in which you introduce a simple problem, demonstrate a simple solution, point out a flaw or shortcoming in that solution, show how a slightly more complex solution addresses the flaw, and repeat. It's similar to Lakatos' "<a href="http://www.amazon.com/Proofs-Refutations-Logic-Mathematical-Discovery/dp/0521290384">proofs and refutations</a>", and I find it a good way to help people understand why complex things are complex.</em></p>
