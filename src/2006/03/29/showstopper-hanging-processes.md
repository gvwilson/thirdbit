---
title: "Showstopper: Hanging Processes"
date: 2006-03-29
---
We've run into a rather annoying bug in DrProject. I've been keeping some brief notes in this ticket, but I'll try to organize my thoughts better here.

First, some background.  DrProject is run as a cgi script under Apache and is backed by PostgreSQL.  Every so often (almost daily), we notice that a number of python/postgres processes are hung:
<blockquote>
<pre>www-data 32016  0.0  1.1 18112 12344 ?       S    06:24   0:02 python2.4 drproject.cgi postgres 32017  0.0  0.6 17880 7148 ?        S    06:24   0:00 postgres: www-data drprojectdb-svn 127.0.0.1 idle in transaction www-data 32203  0.0  1.1 18112 12344 ?       S    06:31   0:02 python2.4 drproject.cgi postgres 32204  0.0  0.6 17880 7160 ?        S    06:31   0:00 postgres: www-data drprojectdb-svn 127.0.0.1 idle in transaction www-data 32279  0.0  1.1 18112 12344 ?       S    06:38   0:02 python2.4 drproject.cgi postgres 32281  0.0  0.7 17916 7476 ?        S    06:38   0:00 postgres: www-data drprojectdb-svn 127.0.0.1 idle in transaction www-data 32340  0.0  1.1 18112 12340 ?       S    06:44   0:02 python2.4 drproject.cgi postgres 32341  0.0  0.7 17916 7316 ?        S    06:44   0:00 postgres: www-data drprojectdb-svn 127.0.0.1 idle in transaction www-data 32410  0.0  1.1 18112 12344 ?       S    06:52   0:02 python2.4 drproject.cgi postgres 32411  0.0  0.6 17880 7148 ?        S    06:52   0:00 postgres: www-data drprojectdb-svn 127.0.0.1 idle in transaction www-data 32466  0.0  1.1 18112 12344 ?       S    06:57   0:02 python2.4 drproject.cgi postgres 32467  0.0  0.7 17916 7308 ?        S    06:57   0:00 postgres: www-data drprojectdb-svn 127.0.0.1 idle in transaction www-data 32533  0.0  1.1 18112 12344 ?       S    07:04   0:02 python2.4 drproject.cgi postgres 32534  0.0  0.6 17880 7160 ?        S    07:04   0:00 postgres: www-data drprojectdb-svn 127.0.0.1 idle in transaction …</pre>
</blockquote>
As these processes build up, eventually the number of active postgres connections exceeds the number of allowable non-superuser connections, requiring us to manually kill these processes.

I have been unable to find a sequence of steps to reproduce the frozen processes, but I've been able to run a few short tests when it has occurred:
<ul>
  <li>When the process hangs, it is due to a long timeline query (ie, 30+ days back)</li>
  <li>You can access other sections of DrProject when the timeline is locking up (ie, the Wiki)</li>
  <li>The DrProject log for the hanging request cuts off while the timeline is gathering events for the Ticket system.  Note that there are 5 subsystems that the timeline gathers events for, and the Ticket system is the last of these.</li>
  <li>Multiple requests for the same URL will cause the process to hang at the same point during collection!</li>
</ul>
After some time, DrProject will stop locking up for these timeline requests and the service returns to normal, albeit with a number of hung processes/connections on the server.

I tried an experiment whereby I inserted a manual <code>gc.collect()</code> call into the timeline code.  I verified that with the manual cleanup, the timeline would process normally, and that without the cleanup, it would continue to hang (I switched between these two multiple times, so as to rule out an accidental solution ;))

Continuing in this vein, I started to investigate whether there were any objects not being collected properly (in particular, leftover database connection objects would worry me).  Sure enough, a number of PooledConnection objects are classified as uncollectable by the Python garbage collector.  In the simplest form, the problem seems to be isolated to the 'select' function in our generic <code>Record</code> class.  This class is the base class in our custom Object/Relational mapping framework, and implements the basic SELECT functionality for every object.  The following example shows the problem:
<blockquote>
<pre>from drproject.env import Environment from drproject.project import Project import gc gc.set_debug(gc.DEBUG_LEAK)  env = Environment('/tmp/drproject') for obj in Project.select(env, 'All'): print str(obj)</pre>
</blockquote>
Which results in the following output:
<blockquote>
<pre>… &lt;Project name='All'&gt; … gc: collectable &lt;EntryPoint 0x1256f50&gt; gc: collectable &lt;dict 0x125c030&gt; gc: collectable &lt;tuple 0x1256e70&gt; gc: collectable &lt;list 0x434fa8&gt; gc: collectable &lt;cell 0x43f770&gt; gc: collectable &lt;cell 0x43f870&gt; gc: collectable &lt;cell 0x43f710&gt; gc: collectable &lt;function 0x41c630&gt; gc: collectable &lt;tuple 0x1251cd8&gt; gc: collectable &lt;tuple 0x43f510&gt; gc: uncollectable &lt;PooledConnection 0x434e18&gt; gc: uncollectable &lt;dict 0x4a5ed0&gt;</pre>
</blockquote>
<strong>Note:</strong> The dict that is uncollectable is actually the __dict__ object for the PooledConnection that is uncollectable.

My working theory is that during a long timeline request, these uncollectable PooledConnection objects accumulate to the point where Python will hang unless a manual collection is done.  This fails to explain, however, why the timeline is locking up in rare occasions, and not all the time.

My next step will be attaching GDB to one of the frozen processes to see exactly what is going on.  As I've never done this before, it should be a good learning experience ;)

— Sean Dawson
