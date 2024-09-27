---
title: "Up and to the Right"
date: 2004-07-21
---
<p>I spent a twenty minutes this morning throwing together a couple of <a href="http://www.python.org">Python</a> scripts to measure Helium's progress over time.  The first script checks Helium out of CVS for each day since the project started, and counts the number of lines of source and test code.  The second script takes that data and produces this simple graph.</p>

<p>I built this simple tool for three reasons. First, it's just plain cool ;-).  Second, the five students working on the project all finish at the end of August.  I know how what you <em>didn't</em> accomplish can loom large in your mind toward the end of a project, so I hoped this graph would remind them of how much they've accomplished, and how quickly.</p>

<p>Third, these little scripts are my way of finding out whether a larger tool of this kind would be worthwhile.  One half would periodically gather statistics about a project and store them in a database; the other half would extract that data and create images for display.  The whole thing could then be integrated into Helium itself, so that students and professors could gauge projects' progress over time.</p>

<p><a href="http://www.sf.net">SourceForge</a> already has something like this, of course.  However, its progress meters aren't extensible: you can't create new metrics and plug 'em in.  I was sure someone would have written an open soruce framework for this, but <a href="http://www.google.com">Google</a> hasn't turned anything up.  I therefore have a couple of students from the study group building a prototype. They're using <a href="http://checkstyle.sf.net">Checkstyle</a> to collect information about Java source code; eventually, we'll want to extend it so that people can use other tools, or languages, to gather data.</p>
