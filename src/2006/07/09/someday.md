---
title: "Someday"
date: 2006-07-09
---
For more than a year now, we've had a milestone called 'someday' in DrProject, so that we could group all our "wouldn't it be nice if…" ideas together. What about adding an IRC channel for each project? Someday. How about authenticating against LDAP? Someday.

Prior to 1.0, "someday" was represented by putting ``null`` in the ticket's ``milestone`` column.  The two problems with that were (a) we needed special code to translate ``null`` to ``"someday"`` for display, and (b) it messed up sorting. To fix both, we modified the setup script to create a milestone called ``"someday"`` for each project upon creation.

Which of course brought up a new problem of its own: what date should be associated with "someday"? SQL doesn't have a standard way to represent "a date that is greater than all actual dates" (i.e., a ceiling for the type ``DATE``).  We've settled on <a href="http://www.gsp.com/2038/">January 19, AD 2038</a>, which is the largest legal date in Unix, but we're not happy with it—when we put this in classrooms this fall, we ''know'' that some students are going to look at it and (quite reasonably) think it's a bug.

So, what should we do?  Eliminate "someday" entirely?  Go back to using ``null`` (and just eat the maintenance cost of more convoluted sorting and translation code)?  Do something else (suggestions welcome)?
