---
title: "Next… Design by Contract?  (Please)"
date: 2006-06-27
---
I was pleasantly surprised a few years ago when programmers (particularly open source programmers) actually started writing unit tests.  <a href="http://www.extremeprogramming.org">XP</a> is usually given the lion's share of the credit, but I think that <a href="http://www.junit.org">JUnit</a> was the real reason: it was just enough structure to get people in, and had a perfect balance between simplicity and extensibility.

What I'd like to see catch on next is <a href="http://en.wikipedia.org/wiki/Design_by_contract">design by contract</a>. Most people who've encountered it think it's about enforcing modularity, or about making sure that derived classes respect the rules of their parents.  What I like, though, is its temporal application: making sure that Version 3.1.2 of a class has the same externally-visible behavior as Version 3.1.1, so that upgrading is guaranteed not to break things.  I'd particularly like this <em>right now</em>, as we're banging our heads once more against  "slight" differences between successive versions of what's supposed to be the same damn library. The release notes for 3.1.2 of—let's call it "Fred", shall we?—don't mention any backward-incompatible changes, but somewhere eight levels down in the call stack, something is passing an Element where it should be passing a string, and everything after that is blowing up.

Given pre- and post-conditions (a big given, I'll grant you), a tool that checks an RPM, JAR file, or Egg against an existing installation, and reports discrepancies, shouldn't be all that hard to build—the general problem may be undecidable, but even something conservative, that draws human attention to possibly problematic mutations, would go a long way toward making lives like mine a little better.

<strong>Update</strong>: Aaron Bingham's <a href="http://indico.cern.ch/contributionDisplay.py?contribId=83&sessionId=41&confId=44">presentation</a> from EuroPython 2006.
