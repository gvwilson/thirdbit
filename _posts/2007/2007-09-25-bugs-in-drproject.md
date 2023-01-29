---
title: "Bugs in DrProject"
date: 2007-09-25 06:56:17
year: 2007
---
DrProject 2.0 has been in use for almost a month now, and we've tripped over some ugly bugs.  The worst one isn't our fault: we've discovered that <a href="https://stanley.cdf.toronto.edu/csc49x/drproject/DrProject/mail/3482">Firefox sometimes sends two identical HTTP requests to the server when a link or button is clicked once</a>, so that two identical transactions are launched just milliseconds apart.  We're going to deal with it (for now) by simply ignoring the database exception thrown by the second transaction, but apparently <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=316731#c6">we're</a> <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=370868#c1">not</a> <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=384364">the</a> <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=61363">first</a> to trip over this.  (Thanks to <a href="http://cs.senecac.on.ca/~david.humphrey/">David Humphrey</a> for the pointers.) Shawn K. tells me the same thing has been seen in IE; how do other people cope with it?

There are also problems with the admin interface—the portal for CSC301 had to be rebuilt yesterday because of one of them.  It all reminds me of something my boss at BNR told me in 1985: "When there's one bug in a release, it's the developer's fault. When there are lots, it's the manager's."  I should have insisted that we switch to 2.0 for internal use early in August, before going on vacation, so that we would trip over these things <em>before</em> students were exposed to them. *sigh*

On the bright side, David, Alex, and Alan the heroic sys admin are turning problems around very quickly.  I hope we'll have 2.0b ready in a couple of weeks, and 2.1 (with the snazzy new ticketing system, and a REST API) looks like it's on track for December or January.  Fingers crossed...
