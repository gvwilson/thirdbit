---
title: "And Now We Are Three"
date: 2015-03-17
original: swc
---
<p>
  The four core topics that every Software Carpentry workshop is supposed to teach are
  automating tasks using the Unix shell,
  structured programming in Python, R, or MATLAB,
  version control using Git or Mercurial,
  and data management using SQL.
  In practice,
  many workshops omit the fourth,
  either because instructors want to put more time into the first three,
  or because they don't think SQL is relevant to their learners.
</p>
<p>
  The Steering Committee has therefore voted to take SQL out of the core.
  This <em>doesn't</em> mean that it can't or shouldn't be taught:
  it's still useful for many researchers to know,
  and the best way we've found to introduce key ideas in data management
  like atomic values, keys, and how to handle missing information.
  However,
  if instructors and learners would rather cover something else,
  they can do so.
</p>
<p>
  One candidate for that "something else" is quality assurance,
  i.e.,
  the things we do to ensure that our code actually works.
  We talked last October about
  why we don't include testing in the core,
  but some instructors still do cover testing and debugging using
  this material
  from the Hacker Within,
  these notes
  from one of last year's WiSE workshops,
  or our Version 4 notes
  from five years ago.
  I think we should try once again to combine this with material on code review
  to create a half-day lesson on QA for the working scientist.
  I still believe that lesson will only stick if it includes examples showing
  how to decide what tests to run for actual scientific problems,
  and what tolerances to use for "right" answers,
  but Ian Hawke has put together <a href="https://github.com/IanHawke/close-enough-balloons">some IPython Notebooks</a>
  (which you can <a href="http://nbviewer.ipython.org/github/IanHawke/close-enough-balloons/tree/master/">view here</a>)
  to get that ball rolling.
</p>
<p>
  Another candidate for "something else" is
  how to use Make
  to create a reproducible paper.
  Make's syntax is famously opaque,
  and that lesson moves far too quickly for most of our audience,
  but again,
  those are things we can fix.
</p>
<p>
  Writing a usable half-day lesson takes me a week:
  it's one day per hour of class time to put the first version together,
  then another couple of days to revise it after its first delivery.
  Crowdsourcing doesn't help much with the first part,
  but definitely does with the second.
  If you're interested in taking a run at either of these,
  or at some other topic,
  please <a href="mailto:gvwilson@third-bit.com">get in touch</a>:
  I'll group interested parties together and get a new lesson repository rolling.
</p>
