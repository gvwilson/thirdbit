---
title: "Python 3.0 is Out (But We're Not Using It Yet)"
date: 2008-12-04
---
<a href="http://www.python.org/download/releases/3.0/">Python 3.0 (final) has been released</a>—yay, and congratulations to everyone who helped build it.  It includes a lot of welcome changes [1], and I'm looking forward to switching—but not yet.  Our "intro to CS in Python" textbook (<a href="http://pragprog.com/titles/gwpy/practical-programming">now in beta at Pragmatic</a>) and our port of DrProject to <a href="http://www.djangoproject.com/">Django</a> are both going to stick to 2.*, at least until mid-2009.  It's no reflection on Py3K—we're just juggling enough other balls that adding more technical novelty to the mix would greatly increase the risk that everything would come crashing down. It's the same argument I've had with students who want to switch from Subversion to Git/Arch/Bazaar/Mercurial/whatever: sometimes, it's better to concentrate on the task at hand and let other people find the potholes for you.

Congratulations once again to the whole Py3K team!

[1] Very glad they added literals for sets, like {1, 2, "three"}; still disappointed that people still have to write the empty set as set() (because {} means "empty dictionary").  Maybe in 4.0… :-)
