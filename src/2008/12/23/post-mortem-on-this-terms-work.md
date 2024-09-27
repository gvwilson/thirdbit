---
title: "Post-Mortem on This Term's Work"
date: 2008-12-23
---
As I've mentioned several times, we've started rebuilding DrProject on top of <a href="http://www.djangoproject.com">Django</a>.  We had a post-mortem last Tuesday on our first term's work, which <a href="http://weblog.latte.ca/">Blake Winton</a> was kind enough to summarize.  The highlights (good and bad) are listed below.

<strong>Good</strong>
<ul>
  <li>Everybody gave more than expected/requested/paid for.</li>
  <li>The team produced some remarkably clean code in a very short time, especially given its prior lack of exposure to Django.</li>
  <li>Distributed collaboration worked much better than expected.  (The team was spread across four universities in three countries.)</li>
  <li>The dev and commit mailing lists worked well, as did weekly status meetings on IRC.</li>
  <li>Regular, frequent, small commits went well/were a good idea.</li>
  <li><a href="http://divmod.org/trac/wiki/DivmodPyflakes">pyflakes</a> and <a href="http://svn.browsershots.org/trunk/devtools/pep8/">pep8</a> were great tools for checking code and style (but it would have been nice to have a script to run both on all files in one command).</li>
  <li>Code reviews rocked.  (Author's note: this was the best part of the term for me, and something I'm going to want to encourage in my undergrad software engineering class next term.)</li>
</ul>
<strong>Bad</strong>
<ul>
  <li>Tempers were strained occasionally during reviews and design discussions (more considerate language should have been used).</li>
  <li>Too much juggling people from one sub-project to another.  (Author's note: this was my fault.)</li>
  <li><a href="http://www.orcaware.com/svn/wiki/Svnmerge.py">svnmerge</a> was a pain.  (Author's note: one developer was a real fan of distributed version control systems, and kept trying to move us in that direction.  I should have resisted more strongly.)</li>
  <li>The project blog wasn't used effectively—it was never clear what should go in the blog vs. on the mailing lists.</li>
  <li>People sometimes didn't know what they should be working on.  (Author's note: also my fault—next term, the newcomers will be given a couple of short, specific tasks at the start to get them up to speed.)</li>
  <li>The release process kind of fell apart, the code freeze never really happened.</li>
</ul>
