---
title: "Wait, Not That Bit!"
date: 2011-07-20 01:17:20
year: 2011
---
We all do it.  We start fixing something over here, in this file, then notice something unrelated ten lines above in a different method that should be cleaned up as well, so we make that little change, but then we have to change the three calls to that method, and while changing one of them we see an opportunity to combine two methods, and so when it's time to check in, our commit message is a bullet-point list of unrelated changes.  Yes, the right thing to do is to make notes for ourselves about those other changes, then defer work on them until we've finished the first change, but few of us are that disciplined 100% of the time.

But wait: why can't our version control system help us here?  When I commit, why do I have to commit all or none of a file?  Wouldn't it be cool if I could say, "I want to commit these lines of this file, and those lines of that other file, but not inflict my other changes on my teammates just yet?"  Well, there's at least one good reason why it would be a bad idea: we almost certainly won't have tested the exact combination of lines that we're checking in.

But what if we could pull the changes we <em>don't</em> want to commit out and save them, then re-run our tests, commit (assuming the tests pass), and then put the pulled-out changes back in place?  It doesn't seem like a particularly hard thing to build, though the user interface would have to be thought through carefully.  I suspect it would make the check-in history of many projects cleaner...
