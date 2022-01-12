---
title: "Integration Irony"
date: 2008-04-15 09:06:49
year: 2008
---
We've been having a problem recently with self-registration in the new version of <a href="http://www.drproject.org">DrProject</a>. Would-be users fill an oh-so-familiar form (preferred ID, email address, password); their data is then held in queue for an admin to approve.  However, when the admin clicks "approve", <a href="http://www.drproject.org">DrProject</a> reports "user already exists in password file".

Yesterday, David Wolever managed to track it down.
<ol>
	<li>Two users are being confirmed at once (i.e., there are two or more requests pending, the admin has selected "approve" for both, then clicks "submit" on the form).</li>
	<li>One works fine.</li>
	<li>The other triggers an exception for some reason (usually missing information).</li>
	<li>The exception causes the database transaction to roll back (good), but the first user's ID and password are in the external password file (bad).</li>
</ol>
Yes, we will improve pre-transaction validation so that #3 happens less frequently, but we're still left with the basic problem: we can't make operations across two things (in this case, the database and the file system) atomic. We could make up a list of file operations to be undone in case of a database transaction failure (i.e., roll our own transaction system---bleah), or do the file operations first and proceed to the database transaction only if the file op succeeds (more code, which means more places where developers could forget to do things), or move passwords for self-registered users into the database (which makes administration of large portals harder: managing credentials in multiple credential stores is a project unto itself).

I'm sure we'll come up with something, but until we do, I'm just going to savor the irony of it all. Four years ago, when we forked from <a href="http://trac.edgewall.org">Trac</a>, we faced a similar problem. Should each of a portal's projects have its own database and version control repository, or should we use one DB for all projects (but separate repositories), or one DB and one repository? We eventually realized that one DB shared by all projects was the only option that made sense, even though it meant more hacking on the tables inherited from <a href="http://trac.edgewall.org">Trac</a>, because multiple DBs would require us to build our own atomicity layer.  It's ironic that trying to keep all the user credentials in one place (a file on disk, accessed only by a setuid validation program), has gotten us back to the same point.

<em>Later</em>: at Alan Rosenthal's suggestion, David Wolever has "solved" this particular problem by making operations on the credentials file idempotent: if <a href="http://www.drproject.org">DrProject</a> tries to add data that's already there, nothing happens and no error is reported.  It's not a general solution---in fact, I'm sure that one day someone somewhere will curse us for special-casing this---but it's good enough to get 3.0.1 out the door.
