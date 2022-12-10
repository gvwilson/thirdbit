---
title: "DrProject Architecture"
date: 2007-02-10 14:55:37
year: 2007
---
I posted a picture of <a href="http://www.drproject.org">DrProject</a>'s database schema a while ago.  Last week, I found myself drawing its architecture on the blackboard in class, so I figured I should post that too.  (It would have been up two hours ago, but my Mac died again...)

<img alt="architecture1.png" id="image833" src="{{'/files/2007/02/architecture1.png' | relative_url}}" />
Here are the key elements:
<ul>
	<li>Apache forwards HTTP requests for DrProject pages to SCGI; it also handles traffic from other Subversion clients (such as the command line or Eclipse).</li>
	<li><a href="http://www.mems-exchange.org/software/scgi/">SCGI</a> runs the Python that makes up DrProject.  This is a long-running process, so that we don't pay the cost of repeated forking and loading.</li>
	<li>A command-line tool called drproject-admin uses the same Python code; administrators can use it in shell scripts, or in other Python programs, to do batch operations (like setting up one project for each pair of students in a course).</li>
	<li>(Almost) everything that isn't in a Subversion repository is stored in a PostgreSQL database.</li>
	<li>When mail intended for a DrProject project lands on the machine, Postfix drops it in a spool directory.  Whenever DrProject runs, it pulls messages out of that directory, archives them in the database, indexes them, and forwards them to project members.</li>
	<li>The "mail strobe" was written because DrProject <em>only</em> forwards mail when it runs. This means that if no-one visits the site for three days, mail will just pile up in the spool directory.  The strobe is just a cron job that pokes the server every minute or so.  DrProject 2.0 will pull mail handling out of the CGI, and have it run every time mail is delivered (or alternatively, have Postfix poke SCGI --- we haven't decided yet).</li>
	<li>The "service check" is another small program that polls all of the DrProject installations on a machine every few minutes to make sure they're still up, and sends the admins email if they're not.  We've always had occasional lockups, but they've been growing more common as load on the server increases; the folks at <a href="http://www.engcorp.com">Engenuity</a> are looking into this right now.</li>
	<li>A program called validate, which checks user IDs and passwords against a password file.  We took user management out of the PostreSQL database so that we could piggyback on top of the departmental lab's user provisioning system; since we don't want a process running as www-data (the dummy user set up for Apache) to have access to password information, we use an external program that runs under setuid.</li>
	<li>The password file that validate checks, which is stitched together periodically from (a) the server's own password file, (b) a subset of the user information from the departmental lab's password file, and (c) a mock password file for external users who don't have shell accounts, but who need access to projects.</li>
	<li>DrProject's own configuration files.  I say "files" because each installation of DrProject has its own configuration (although they all share code).  Again, we'll fix this by the time 2.0 comes out...</li>
</ul>
(I left out the Apache and Postfix configuration files, both of which have to be edited as well as part of an installation.)

I have two observations about this diagram:
<ol>
	<li>DrProject is actually a fairly simple system compared to many in widespread use today.  An equivalent diagram for <a href="http://www.sf.net">SourceForge</a> would probably have three times as many boxes on it; Indigo's order tracking system wouldn't fit onto your screen (I don't care how big your screen is, it wouldn't fit).  While we're making progress on debugging programs (even multithreaded ones---see Zeller's book), I haven't seen any substantive work on debugging configurations: if you don't get it write, all you can do is tweak and pray.  Anyone who wants to be rich, famous, and popular should consider tackling this problem.</li>
	<li>This diagram combines several of <a href="http://www.win.tue.nl/~mchaudro/sa2004/Kruchten4+1.pdf">Kruchten's 4+1 views</a> into one: it shows a logical view of the system's components, a process-level view of the system's concurrency, and a development view of which code relies on which. It equally shows elements from all the major divisions in <a href="http://www.softwarepractice.org/">John Reekie's</a> system (which I've been using in class, and have been finding very useful).  I see this whenever I try to explain any system's architecture to anyone: I always want to mix entities of different types in my pictures, because every sensible narrative about the system incorporates them all.</li>
</ol>
I'd be interested in seeing pictures of other applications' architectures if anyone has pointers --- I rather suspect that everyone else is making up notations on the fly to fit their needs as well.
