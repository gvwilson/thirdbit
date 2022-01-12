---
title: "The Design of Fossil"
date: 2010-01-07 08:15:11
year: 2010
---
Partly in response to my post about building something <a href="http://www.fossil-scm.org/">Fossil</a>-like on a NoSQL data store, Richard Hipp has written <a href="http://www.fossil-scm.org/fossil/doc/tip/www/theory1.wiki">a brief discussion of Fossil's design</a> that tackles two questions:
<ol>
	<li>Why is Fossil based on SQLite instead of a distributed NoSQL database?</li>
	<li>Why is Fossil written in C instead of a modern high-level language?</li>
</ol>
His answer to the first is that Fossil <em>is</em> a NoSQL database---its use of SQLite to store metadata and other stuff is an implementation detail. His answer to the second is, "Fossil does use a modern high-level language for its implementation, namely SQL." He goes on to say:
<blockquote>Much of the "heavy lifting" within the Fossil implementation is carried out using SQL statements.  It is true that these SQL statements are glued together with C code, but it turns out that C works surprisingly well in that role.  Several early prototypes of Fossil were written in a scripting language (TCL).  We normally find that TCL programs are shorter than the equivalent C code by a factor of 10 or more.  But in the case of Fossil, the use of TCL was actually making the code longer and more difficult to  understand. And so in the final design, we switched from TCL to C in order to make the code easier to implement and debug.</blockquote>
I'm sceptical: I earned my living as a C/C++ programmer for almost 15 years, but believe these days that other languages give better bang for the buck in almost all cases. On the other hand, Richard has shipped much more high-quality software than I have. I wish I had time to dig into this deeper... *sigh*
