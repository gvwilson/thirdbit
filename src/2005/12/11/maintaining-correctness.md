---
title: "Maintaining Correctness"
date: 2005-12-11
---
I'm re-thinking the lectures in the Software Carpentry course based on feedback from this term's students.  I'm going to merge the three lectures on different development processes into one, and use the space that frees up to talk in more detail about programming style and software design—assuming, of course, I can think of something to say that isn't banal.

I also want to talk about the material in an article by Paul Dubois in the May/June 2005 issue of <a href="http://cise.aip.org/cise/">Computing in Science &amp; Engineering</a> called "Maintaining Correctness in Scientific Programs".  Here are a few key lines from the introduction:

<blockquote>The more frequently a program is changed, the more difficult it is to maintain its correctness… Most programmers can reasonably tell when their programs are incorrect, but for scientific programmers, this is not the case.  A bug that doesn't cause the program to fail in an obvious way could be indistinguishable from an error in modeling the real world with equations… Solving this problem must be the focus of our methodology, be it for a single person writing a 10,000-line program [or] a team of 20 or more writing half a million lines.</blockquote>

Paul then outlines a strategy based on <em>defense in depth</em> which has the following layers:

<ul>
  <li>a protocol for source control;</li>
  <li>use of language-specific safety tools;</li>
  <li>design by contract;</li>
  <li>verification;</li>
  <li>reusing reliable components;</li>
  <li>automating testing;</li>
  <li>unit testing (which requires automation to be effective);</li>
  <li>to-main testing policy (i.e., code must be tested before being integrated from a branch into the main line);</li>
  <li>regression testing;</li>
  <li>release management; and</li>
  <li>bug tracking.</li>
</ul>

This immediately struck me as an excellent way to organize and motivate several important parts of the course.  It also points out some holes that I'll need to fill.  Oh, to have more hours, and more hands…
