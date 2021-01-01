---
title: "Git as GOTO"
date: 2015-07-20 06:00
year: 2015
---
<p>
  I am not a fan of Git.
  While <a href="https://twitter.com/jiffyclub/status/622622918854381568">some people may find it intuitive</a>,
  I consider it one of the most complicated programs I have ever tried to teach.
  Some of that complexity comes from its inconsistent command syntax and
  <a href="http://git-man-page-generator.lokaltog.net/">needless jargon</a>,
  but I realized a few days ago that there's a deeper cause.
</p>
<p>
  To explain it,
  I have to go all the way back to March of 1968,
  when Edsger Dijkstra's article "<a href="https://en.wikipedia.org/wiki/Considered_harmful">Go To Statement Considered Harmful</a>"
  appeared in <em>Communications of the ACM</em>.
  In it,
  Dijkstra argued that arbitrary use of the GOTO statement
  led to programs that were hard for both human beings and compilers to understand,
  and that we should instead restrict ourselves to a handful of control structures
  like for loops, if/else statements, and subroutines.
</p>
<p>
  That might seem like an obvious truth today,
  but it wasn't at the time.
  It took a decade for structured programming to become dogma,
  i.e.,
  for programmers to agree to limit themselves to
  a small subset of all possible flows of control
  when building software.
</p>
<p>
  We haven't had that collective epiphany yet when it comes to distributed version control systems like Git.
  At its core,
  Git is a way to construct and manipulate a directed acyclic graph of changes to a project.
  Git allows programmers to make almost any change to that graph they can imagine,
  and the results can be just as hard to understand
  as the tangled flowcharts of patched and re-patched assembly code.
</p>
<p>
  In practice,
  though,
  most of us manipulate the change graph in a small number of stereotyped ways,
  just as most FORTRAN and assembly language programmers used GOTO to build things
  that are recognizable as nested loops and conditionals.
  That makes me wonder when version control will have its structured revolution&mdash;when
  <a href="http://nvie.com/posts/a-successful-git-branching-model/">today's best practices</a>
  will be enforced rather than encouraged.
  When it happens,
  I'm certain that the old guard will point out useful things it doesn't allow,
  and optimizations it doesn't permit,
  just as they did in Dijkstra's day.
</p>
