---
title: "Why DrProject Is Slow"
date: 2006-06-27
---
Billy Chun has been investigating why DrProject is so slow (5.1 seconds per request).  As regular readers will know, we're running it as a pure CGI: a new Python interpreter is forked for every request.  The fork itself costs about half a second, and importing all the libraries takes about the same, but the real culprit turns out to be the 1.9 seconds (yes, 1.9 seconds) spent in Plex.nfa_to_dfa.  <a href="http://www.cosc.canterbury.ac.nz/~greg/python/Plex/">Plex</a> is the parser generator we used to create a parser for our wiki pages; according to internal documentation, the nfa_to_dfa translates non-deterministic finite automata into deterministic ones.  In plain English, we're recompiling our wiki syntax parser <em>every single time a page is requested</em>.

Oops.

So how much improvement can we expect? Well, when Billy ran DrProject with <a href="http://www.mems-exchange.org/software/scgi/">SCGI</a>, the time per request dropped from 5.1 seconds per request to 0.6 seconds: no fork, no re-import, no regeneration of the wiki parser, and a few other things as well. That's a factor of eight, and will get us well within our target performance range. He's writing up an installation guide right now, and will then look at whether we can cache the <a href="http://www.cosc.canterbury.ac.nz/~greg/python/Plex/">Plex</a>-generated parser somehow. These changes won't be in this week's release candidate, but ought to make it into the final 1.0.

Onward!
