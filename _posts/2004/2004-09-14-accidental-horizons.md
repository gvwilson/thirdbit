---
title: "Accidental Horizons"
date: 2004-09-14 10:04:24
year: 2004
---
<p>A quarter of a century ago, in <a href="http://www.amazon.com/exec/obidos/tg/detail/-/0201835959">The Mythical Man Month</a>, Fred Brooks pointed out the difference between intrinsic complexity and accidental complexity.  Intrinsic complexity is how hard a problem really is; accidental complexity is how much harder we make it by creating inconsistent APIs, fragile configuration files, or GUIs that don't accurately reflect the state of the world.</p>

<p>Over the past couple of years, I've realized there's a similar difference between intrinsic horizons and accidental horizons.  A "horizon" defines what you can see from where you're standing; in a technical field, it is the boundary between problems you know how to solve, and ones you don't.  There are therefore two ways a field can make progress: by inventing new ways to solve problems, or by pushing out the horizons of the ways they already have.  When we do the latter, we often discover that the horizon was accidental.  There was never anything to stop us from solving those problems before---we just didn't think to try.</p>

<p>Which brings me to <a href="http://www.hibernate.org">Hibernate</a>, the object/relational mapping package we're using in Hippo.  A <a href="http://www.hibernate.org">Hibernate</a>-based application has three parts:</p>

<ul>
<li>the Java classes representing things you want stored in a database;</li>
<li>an XML configuration file describing the mapping between those classes and your database tables; and</li>
<li>the rest of your program, which works with Java objects, and trusts <a href="http://www.hibernate.org">Hibernate</a> talk to the database on its behalf.</li>
</ul>

<p>When everything is working as it should, this is an excellent division of labor.  The problem is that when things <em>aren't</em> working, there is no easy way to figure out why not [<a href="#1">1</a>].  I have <a href="http://www.hibernate.org">Hibernate</a>'s log messages, but they don't tell me why my attempt to create a session object throws an exception.  I have <a href="http://www.hibernate.org">Hibernate</a>'s source, so I could step into the session's constructor and trace the fault if I wanted to, but I don't think I should have to.  <a href="http://www.hibernate.org">Hibernate</a> is supposed to abstract away the details of working with databases directly; as far as I'm concerned, it should also abstract away the details of <em>debugging</em> my interactions with the database.</p>

<p>Which brings us back to the notion of an accidental horizon.  The IDE I'm using, <a href="http://www.eclipse.org">Eclipse</a>, is really just a framework for hosting plugins.  Some of these (like the syntax-aware Java editor) come bundled with it, but many others (like the <a href="http://eclipse-cs.sourceforge.net/">Checkstyle plugin</a>) have been developed by third parties.  The <a href="http://www.apache.org/httpd">Apache</a> web server is built in a similar way: its core only knows how to load plugins, and route message traffic through them.  All the stuff we use it for---resolving paths, launching CGI scripts, and so on---is implemented in a plugin that ships with the distribution, but hundreds of others exist as well.</p>

<p>So why aren't debuggers built this way?  When I something as complex as <a href="http://www.hibernate.org">Hibernate</a>, why can't I also create a debugging plugin to help <a href="http://www.eclipse.org">Eclipse</a> show me what <a href="http://www.hibernate.org">Hibernate</a> is doing?  There are no intrinsic technical obstacles [<a href="#2">2</a>]; as far as I can see, the only reason it isn't supported is that, well, no-one else supports it either.  It is a purely accidental horizon, and the sooner it's eliminated, the more productive we will all be [<a href="#3">3</a>].</p>

<p>Now, if you'll excuse me, I have some <a href="http://www.hibernate.org">Hibernate</a> source code to step through...</p>

<p>[<a name="1">1</a>] See also Joel Spolsky's article on <a href="http://www.joelonsoftware.com/articles/LeakyAbstractions.html">leaky abstractions</a>.</p>

<p>[<a name="2">2</a>] Which isn't to say that it wouldn't take a lot of thoughtful design and hard work to create the right hooks in <a href="http://www.eclipse.org">Eclipse</a> for developers to plug into.  Master's thesis, anyone?</p>

<p>[<a name="3">3</a>] See also my article on <a href="http://www.third-bit.com/~gvwilson/xmlprog.html">extensible programming systems</a>.</p>
