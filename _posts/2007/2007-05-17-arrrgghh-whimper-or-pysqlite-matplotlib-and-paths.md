---
title: "Arrrgghh *whimper* (or, PySqlite, Matplotlib, and paths)"
date: 2007-05-17 16:41:15
year: 2007
---
Muhammad Ali and Adam Foster prototyped a dashboard display for DrProject as a term project this winter. It collects information on the number of tickets in various states, and the number of check-ins, then uses <a href="http://matplotlib.sourceforge.net/">Matplotlib</a> to construct time-series charts. It's pretty cool, so Ali agreed to spend a week integrating into DrProject for deployment.

In order to make it work, DrProject has to load <a href="http://matplotlib.sourceforge.net/">Matplotlib</a>  and  <a href="http://initd.org/tracker/pysqlite">PySqlite</a> (the Python wrappers for <a href="http://www.sqlite.org">SQLite</a>) at the same time. After a day of wrestling with versions, packages, LD_LIBRARY_PATH, and other junk, Ali can get it to load one or the other, but never both.  The symptoms are described here:

<ul>
  <li>message to SQLite list</li>
  <li>message to Matplotlib list</li>
</ul>

Basically, if LD_LIBRARY_PATH is left empty, Matplotlib will load, but PySqlite won't. If LD_LIBRARY_PATH is set to /usr/local/lib (where the sqlite .so file is located), PySqlite is  happy, but Matplotlib fails to load.  If the directory containing the .so's that Matplotlib needs are added to LD_LIBRARY_PATH, well, you can read Ali's message, but it's still broken.

We'd welcome help or guidance; we'd also be grateful if someone would come up with a packaging and deployment strategy that makes these problems just not happen :-(.

<hr />

Later: Ali writes, "The problem was that I had an incompatible version of one the packages that matplotlib needs to import (libcairo), installed in /usr/local/lib. By adding usr/local/lib to LD_LIBRARY_PATH, the system loaded up the incompatible libcairo, instead of its regular one. The fix was 'uninstalling' all incompatible packages (libcairo and libpango in my case) from /usr/local/lib. I've also learnt that in Linux terminology uninstalling is the same as 'rm -f'."
