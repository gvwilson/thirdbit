---
title: "Preparing for the Next Round"
date: 2004-07-23 14:37:34
year: 2004
---
<p>The team that's going to be working on Helium this fall had its first meeting last night.  If all goes well, eleven of the department's best undergraduate students will build on all the hard work that Michelle, Laurie, Jason, Eric, and Wilfred have put in this summer, and deliver something that we can use in undergraduate classes.</p>

<p>The next step is to determine exactly what they will work on.  The current list (in priority order) is:</p>

<ol>

<li><em>Real <a href="http://subversion.tigris.org">Subversion</a> integration.</em>  We believe we can use applets to give users a complete in-browser interface to <a href="http://subversion.tigris.org">Subversion</a> (rather than a read-only interface, which is what <a href="http://www.sf.net">SourceForge</a> and <a href="http://www.gforge.org">GForge</a> offer).  In order to do this, we must first bring <a href="http://subversion.tigris.org">Subversion</a>'s Java bindings up to date, which is an entire project in itself…</li>

<li>A <em>scripting interface</em>.  We can't require instructors to create hundreds of user accounts, and hundreds of projects, by hand.  Instead, we're hoping to provide a <a href="http://www.jython.org">Jython</a> library that instructors and administrators can use to work directly with Helium's data model.  (The alternative would be to expose the database tables, but that would bypass all the constraints that the model layer enforces.)</li>

<li><em>Testing infrastructure</em>.  Helium's lower layers are exercised by a unit test suite—in fact, there's currently more testing code than application code.  The next step is to adapt <a href="http://httpunit.sf.net">HttpUnit</a>, <a href="http://htmlunit.sf.net">HtmlUnit</a>, or something similar to do end-to-end testing on the whole application.</li>

<li>A <em>progress monitoring framework</em>.  Helium's home page displays a status light (green if all tests are passing, red if there are failures) and a graph showing the growth of the source and test code over time.  Displays like these will help students and instructors see how their projects are doing.</li>

<li><em>Searching</em>.  <a href="http://www.google.com">Google</a> is every programmer's friend; the <a href="http://jakarta.apache.org/lucene">Lucene</a> project puts that search capability into everyone's hands.  We hope that if forums and site content are searchable, fewer students will repeat questions umpteen times.</li>

<li><em>Issue tracking</em>.  Version control and issue tracking are two of the things that distinguish professional programmers from amateurs.  It's easy to show students why they want the former (if nothing else, version control helps them keep their home computers in synch with their accounts on the university's machines), but motivating issue tracking is harder.  Initially, we're going to add it to Helium for our own use (we'd like to be self-hosting by September).  Once it's in place, we hope we'll be able to find ways to work it into courses.</li>

<li><em>Blogging, wikis, project and personal home pages, NNTP integration…</em>  There's a lot more we'd like, but they'll probably have to wait for the Winter 2005 term.</li>

</ol>

<p>It's a lot, but with two or three students per item, we should be able to pull it off.</p>
