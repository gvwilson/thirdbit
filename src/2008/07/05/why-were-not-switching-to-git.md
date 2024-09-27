---
title: "Why We're Not Switching to Git"
date: 2008-07-05
---
I got the following a couple of days ago from a colleague in the US:

<em>Our development teams are debating the use of GIT vs SVN. [Project name] has standardized on SVN, but some of the projects are considering GIT. Do you have an opinion on their relative merits, particularly for computational science and engineering applications?</em>

It's a timely question—two of my best students are keen to switch us from Subversion to Git, and claim the latter makes them much more productive. I've decided we're not going to (not before the end of 2009, anyway) for a couple of reasons:
<ol>
  <li>Documentation: there's a ton of good stuff about SVN, but Git's docs are still spotty in places.  I'm reviewing an early draft of a book about it, and that'll go a long way toward closing the gap, but it's not going to be ready until early 2009.</li>
  <li>Supporting tools: we delayed switching from CVS to SVN until the Eclipse and Visual Studio plugins for the latter were solid, and we're going to delay switching to something else (such as Git) until support for it is as ubiquitous, and as dependable.  Again, that probably means some time in 2009.</li>
  <li>Reality check: we've already had one big snafu due to a developer (a bright one) creating lots of local branches, losing track of his work, then having the hard drive die.  Fans of fully distributed version control don't seem to take this into account when talking about relative productivity, and I think it's easier to fall into bad habits when there isn't the visibility of a central repository.</li>
  <li>Backing the wrong horse: Git seems to be the most popular VCS of its kind right now, but there are several others, and it's not yet clear which is going to dominate.  Having chosen Python for my web programming projects, only to watch Ruby on Rails grow by leaps and bounds, I'm willing to wait a while to see which horse is going to win the race before placing my bet.</li>
</ol>
<em>Later: see also this <a href="http://www.infoq.com/articles/dvcs-guide">guide to distributed version control systems</a>.</em>
