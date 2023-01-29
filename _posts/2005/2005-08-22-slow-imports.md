---
title: "Slow Imports"
date: 2005-08-22 09:28:29
year: 2005
---
Argon (our re-worked <a href="http://projects.edgewall.com/trac">Trac</a>) is now up and running on the <a href="http://www.cdf.utoronto.ca">CDF</a> lab machines, but it's very, very slow: 5-10 seconds per request at best.  We've tracked the problem down to the <code>import</code> statements, which are taking 3.5 seconds or more each time the CGI is executed (we're running as a pure CGI for now).  This is puzzling, because (a) they take less than half a second on Chris Lenz's Powerbook (slower processor and less memory than the CDF servers), and (b) Bin Liang's installation on his hosted Debian service in Dallas, Texas takes 1-2 seconds per page request max.  Something's seriously confused here, and we need to track it down.

On the bright side, we seem to be over the last of the many ownership/permission hurdles that have bedevilled us for the past two weeks, and Keir Mierle says that email is finally working too.  Greg Lapouchnian has been doing a lot of testing, finding problems of various sizes, and filing some very professional bug reports; hopefully, the other 49X alumni who volunteered to help will be able to kick in this week as well.

Twenty person-days left to get this one baked and on the table…
