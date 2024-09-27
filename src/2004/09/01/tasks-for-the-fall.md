---
title: "Tasks for the Fall"
date: 2004-09-01
---
<p>We've finalized the list of things we want to accomplish between now and December, in order to be ready for beta use in the Winter term:</p>

<p>Bug tracking system: we need to build a simple issue tracking system (like
Neon's) that
integrates with Subversion, the rest of Hippo's user interface, and the
server-side scripting framework.  UI, database work, testing—this has
it all.  3 people needed; one slot spoken for.</p>

<p>Server-side scripting: one of the big differences between Hippo and other
systems (like SourceForge and GForge) is that Hippo has to support dozens
(possibly hundreds) of more-or-less identical projects (for courses like
207, in which each student is working on their own version of each
assignment).  Creating these one at a time through a web interface would
be painfully slow, so we need to build a Python library that can talk
directly to the data model classes in Hippo.  That way, administrators and
profs can write little scripts to create projects, user accounts, bugs,
and so on.  (Why Python?  Because there's a version written in Java,
called Jython, and since we're teaching it in courses, we can reasonably
expect profs to know a little about it.)  2 people needed; both slots
open.</p>

<p>Email system: the Helium team made a good start on an email management
system, but lots more need to be done.  Spam filtering, threading… it's
a long list.  3 people needed, all slots open.</p>

<p>Testing frameworks: this team will *not* be responsible for testing Hippo
(each team will be required to test its own work).  Instead, this team
will integrate and customize some open source testing tools, like HtmlUnit
and HttpUnit, so that everyone else can test the user interfaces they're
building.  I expect that some of the work this team does will be folded
back into the official releases of those tools, so if you're looking for
an extra line on your resume…  2 people needed, both slots open.</p>

<p>Server-side subversion: David James is already at work cleaning up the
Java interface to Subversion, so that we can make it do what we need it to
do on the servr side.  No more bodies are needed for this one.</p>
