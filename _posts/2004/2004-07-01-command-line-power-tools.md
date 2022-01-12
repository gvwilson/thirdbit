---
title: "Command-Line Power Tools"
date: 2004-07-01 11:18:48
year: 2004
---
<p>Harald Koch just pointed me at <a href="http://xmlstar.sourceforge.net/">XMLStarlet</a>, a command-line toolset for manipulating XML.  This isn't the first beast of its ilk --- Sean McGrath built similar tools several years ago in Python, for example --- but it seems to be more mature than others.</p>

<p>Clicking through the documentation, I'm struck yet again by the disconnect between programming's two approaches to handling "odd jobs".  The first is the Unix command-line filter model; the second, scripting.  The second is more powerful, primarily because it gives programmers access to richer data structures, and a wider set of control constructs.  (I talk about this more in <a href="http://www.third-bit.com/~gvwilson/xmlprog.html">this article</a> on extensible programming systems.)</p>

<p>Why then has the command-line model proved so durable?  According to Irving Reid, the main reason is that you get more bang for your keystroke: an experienced Unix geek can do wonderful things in a five-filter pipe.  Once you add a few simple control constructs (like <code>while read var</code>, which I only discovered last fall), you have a lot of power at your fingertips.</p>

<p>Which brings me back to the problem of supporting batch operations in Helium. One of the biggest differences between it and existing systems like <a href="http://www.sf.net">SourceForge</a> and <a href="http://www.gforge.org">GForge</a> is that Helium administrators have to be able to operate on dozens or hundreds of users and projects at once.  Every project in <a href="http://www.sf.net">SourceForge</a> is a separate entity; so is every user.  In Helium, on the other hand, projects are grouped by course, users are registered in courses, and so on.  If someone has a class list for <a href="http://www.cs.utoronto.ca/~csc207h">CSC207</a>, they must be able to create a new project for each student in the course, and make the student a developer in that project, without clicking through a web interface for several hours.</p>

<p>The three options we have considered were discussed in an earlier post: web services, a library of bindings, or using a Java-friendly scripting language like <a href="http://www.jython.org">Jython</a>.  A fourth possibility, though, is to provide a set of command-line tools that talk directly to Helium's database.  The downside is that we lose the consistency checks that our data model classes implement; the upside is that administrators can then do small things quickly by combining our tools with others they already know.</p>

<p>I'd be interested in hearing from people who have done things like this with other systems.</p>
