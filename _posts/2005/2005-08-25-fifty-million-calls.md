---
title: "Fifty… Million… Calls"
date: 2005-08-25 11:19:11
year: 2005
---
"House" and "CSI" (the original) are two of my favorite TV shows.
Partly, it's the characters—Hugh Laurie and Marg Helgenberger are
both brilliant—but I also enjoy watching smart people debugging.
Sure, they're dealing with diseases and crime scenes, but deep down
it's all the same: something's wrong, and you have to figure out
what.

The Argon team spent a lot of the last five days doing exactly
that.  For those of you who haven't been following along, Argon is a
fork of <a href="http://projects.edgewall.com/trac">Trac</a>, a
lightweight web-based project management framework that's implemented
in Python.  We've been working for several months to modify it so that
we can use it to run undergraduate programming projects; the interface
has been redesigned, it now handles multiple projects, we're using
PostgreSQL instead of SQLite (partly for performance, and partly
because SQLite contains a synchronization bug), and so on.

A couple of weeks ago, we finally installed it on CDF, the
Computing Disciplines Facility servers that host undergraduate work
during term.  It took longer than anticipated to find a set of file
ownerships and permissions that would allow students access to their
projects, but <em>only</em> their projects, while giving TAs and
lecturers access to everything.

We got it sorted out eventually, but then we ran into another
problem: our application was really, really slow—it was taking 10
seconds or more to service each CGI request.  There was no way we
could put it into production as it was.

While we were poking around at our end, <a href="http://www.cmlenz.net">Chris Lenz</a> had a look.  The first
thing he told us was that we should map the <code>htdocs</code>
directory (the one containing all the static resources) to some URL
that wouldn't trigger an invocation of the CGI, so that Apache
wouldn't have to invoke Python for each image or icon.

The second thing was that our code ran in under half a second on
his unplugged Powerbook.  He and Keir Mierle (one of the students
working here in Toronto) profiled the code, and found that almost all
the difference lay in the time it was taking the CGI to import the
libraries it needed.  On Chris's machine, this was a few hundred
milliseconds; on ours, it was several seconds.

All right, down a layer we go.  Keir profiled Python itself using
gprof, and found this:
<table cellpadding="3" border="1">
<tr>
<th valign="top" align="left">% time</th>
<th valign="top" align="left">cumulative seconds</th>
<th valign="top" align="left">self seconds</th>
<th valign="top" align="left">calls</th>
<th valign="top" align="left">self s/call</th>
<th valign="top" align="left">total s/call</th>
<th valign="top" align="left">name</th>
</tr>
<tr>
<td>38.46</td>
<td>0.70</td>
<td>0.70</td>
<td>51442563</td>
<td>0.00</td>
<td>0.00</td>
<td><code>_PyUnicodeUCS2_IsLinebreak</code></td>
</tr>
<tr>
<td>15.93</td>
<td>0.99</td>
<td>0.29</td>
<td>28141</td>
<td>0.00</td>
<td>0.00</td>
<td><code>PyUnicodeUCS2_Splitlines</code></td>
</tr>
<tr>
<td>3.85</td>
<td>1.06</td>
<td>0.07</td>
<td>83334</td>
<td>0.00</td>
<td>0.00</td>
<td><code>classify</code></td>
</tr>
<tr>
<td>3.30</td>
<td>1.12</td>
<td>0.06</td>
<td>55512</td>
<td>0.00</td>
<td>0.00</td>
<td><code>PyFrame_New</code></td>
</tr>
<tr>
<td>2.20</td>
<td>1.16</td>
<td>0.04</td>
<td>1233298</td>
<td>0.00</td>
<td>0.00</td>
<td><code>_PyUnicode_New</code></td>
</tr>
<tr>
<td>2.20</td>
<td>1.20</td>
<td>0.04</td>
<td>50779</td>
<td>0.00</td>
<td>0.00</td>
<td><code>list_dealloc</code></td>
</tr>
<tr>
<td>1.65</td>
<td>1.23</td>
<td>0.03</td>
<td>1416785</td>
<td>0.00</td>
<td>0.00</td>
<td><code>app1</code></td>
</tr>
<tr>
<td>1.65</td>
<td>1.26</td>
<td>0.03</td>
<td>660223</td>
<td>0.00</td>
<td>0.00</td>
<td><code>dict_subscript</code></td>
</tr>
<tr>
<td>1.65</td>
<td>1.29</td>
<td>0.03</td>
<td>515599</td>
<td>0.00</td>
<td>0.00</td>
<td><code>PyDict_GetItem</code></td>
</tr>
</table>
That's right: for some reason, each time the CGI ran, it called the
function that sees whether a character is a Unicode end-of-line marker
50 million times.

Hm… If we were parsing XML or some other data files, I could see
why we'd call <code>_PyUnicodeUCS2_IsLinebreak</code>, but this was
happening as we were importing libraries.  Ah, but: each of the source
files we inherited from Trac began with the line:
<pre># -*- coding: iso8859-1 -*-</pre>
This is an Emacsism that recent versions of Python have adopted to
tell the interpreter how the characters in the source file are
encoded.  (If you don't know what that means, please check out Joel
Spolsky's <a href="http://www.joelonsoftware.com/articles/Unicode.html">excellent
article</a>.)  When we took those pragmas out of our files, the number
of calls to <code>_PyUnicodeUCS2_IsLinebreak</code> dropped to 29
million.  That's still a lot, but it was a sign we were on the right
track.

We then got tangled up for a while with .pyc files.  When Python
imports a .py module, it compiles it to bytecode, and then saves the
bytecode to disk.  The next time it's asked to import the module, it
checks the timestamp on the corresponding .pyc; if the .pyc is
fresher, Python slurps that into memory instead of recompiling the
source.  Of course, this only works if the Python interpreter has
permission to write to the directory that the .py file is stored in.
In our case, it couldn't, because the interpreter was running with
the user ID of the web server, and giving it write access to the
source directory would open up a fairly large security hole.

Our solution was to compile all the .py files to .pyc's manually
every time we updated the source code (just as Python does to its
standard library when you install it on a new machine).  For a while,
though, we were running our tests with some .pyc's deleted, but others
still present, which is why we were still getting those 29 million
calls to <code>_PyUnicodeUCS2_IsLinebreak</code>.  Once we got that
cleaned up, the number of calls dropped to zero, and the run time went
from over 10 seconds per hit to 2 or less—well within our comfort
zone.

OK, we'd fixed our problem, but we still didn't really understand
it.  Karen Reid (my co-supervisor) and I have learned the hard way
that just making bugs go away usually isn't enough: if you don't
understand where they came from, they'll probably come back when you
least expect them.

We had Keir post a note to the Python developers' list.  It went
out at 16:10 on Tuesday, August 23.  At 05:45 the next morning, Walter
Dorwald replied to say:
<blockquote>This is caused by the chances to the codecs in 2.4. Basically the codecs
no longer rely on C's readline() to do line splitting (which can't work
for UTF-16), but do it themselves (via unicode.splitlines()).</blockquote>
Half an hour later, Martin v. Lowis followed up with:
<blockquote>That explains why you get any calls to IsLineBreak; it doesn't explain
why you get so many of them.
I investigated this a bit, and one issue seems to be that
StreamReader.readline performs splitline on the entire input, only to
fetch the first line. It then joins the rest for later processing.
In addition, it also performs splitlines on a single line, just to
strip any trailing line breaks.
The net effect is that, for a file with N lines, IsLineBreak is invoked
up to N*N/2 times per character (at least for the last character).</blockquote>
Yup—the reader was invoking
<code>_PyUnicodeUCS2_IsLinebreak</code> N<sup>2</sup> times.  Square
root of fifty million is… carry the three… about seven thousand,
which happens to be about the number of lines of code we were
loading.

There have been over a dozen messages on the Python developers'
list since then about how to fix this.  The most interesting part for
me hasn't been the proposals themselves, but rather the fact that the
first thing Walter and Martin did was write little test programs and
profile them to find out how fast things would actually run.  To put
it another way, good programmers like Walter and Martin automatically
apply the scientific method to problems—they design and run
experiments, collect data, and <em>then</em> formulate a hypothesis
(a.k.a. a bug fix).  It's cool to be able to watch this in action, and
even cooler to have code that runs fast enough to be called
interactive.
