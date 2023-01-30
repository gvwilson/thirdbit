---
title: "Filters, Performance, and Priorities"
date: 2004-08-18 16:57:22
year: 2004
---
<p>Where has the summer gone?  We've written a lot of software (and documentation), but there's still a lot to do before Helium (er, sorry, Hippo—we're renaming it, for reasons that are too silly to go into) is ready to deploy.</p>

<p>Eleven undergraduates from the <a href="http://www.cs.utoronto.ca">Department of Computer Science</a> at the <a href="http://www.utoronto.ca">University of Toronto</a> will be carrying on with the project this fall.  Between now and September 9, we have to decide what we want them to work on.  In order to do that, we have to resolve some technical issues that we've been deferring.</p>

<p>For example, Hippo includes mail management, so that projects can have mailing lists.  We'd like to make use of whatever SMTP server our host is running, but that means we have to find a way to get messages into Hippo.  We also have to put some kind of spam filtering in place.</p>

<p>However, we also want to keep Hippo unilingual if at all possible.  It would be fairly easy for our existing programming team to write a Python script (or even a shell script) to feed Hippo mail, but if we do that, I'm afraid we'll be falling into the same trap that <a href="http://www.sf.net">SourceForge</a> did.  Last time I checked, <a href="http://www.sf.net">SourceForge</a> depended on five (5) different languages (PHP, Perl, Python, Bash, and C), plus more than a dozen major third-party packages and many smaller libraries.  Getting all this stuff installed is hard; keeping it all in synch is harder; and finding programmers who know XYZ when it breaks is a continuing headache.  ("Sorry, dude, if this bit was written in Perl, I could help you…")</p>

<p>So why not write the necessary glue in Java?  Performance.  Write a little shell script that runs a simple "Hello, world" script in Python a thousand times, and see how long it takes to run.  Now do the same in Java.  Make sure you have other applications running on the box, so that you're getting realistic numbers, rather than never-to-be-exceeded everything-in-memory peaks.  On Pyre (the Linux box that's hosting Helium's development), the difference is about 4:1.  It was less (about 3:2) on my souped-up development box at work, but only when I wasn't running anything else.  As soon as the VMs were fighting with other applications for space, Java lost: badly.</p>

<p>We have several ways to deal with this.  One is to bite the bullet and write the smallest possible shell/Python script to move mail from the SMTP server to (for example) a scratch directory, then have a long-running Java daemon do everything from there.  (I'm pretty sure that Java will match Python's performance on the actual processing, though I don't yet have any data to back that up.)  Another would be to throw up our hands and say, "OK, Java's been fun, but this is the N'th time (where N is approximately 3) that we've found a case where Python would have been easier, so maybe we should start over."  Needless to say, I'm less than excited about that…</p>

<p>I'm sure there are other possibilities; I'm also sure that we're not the first development team to bang our heads against this particular wall.  As always, pointers and advice are welcome…</p>
