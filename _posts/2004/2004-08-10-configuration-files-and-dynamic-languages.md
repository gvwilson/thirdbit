---
title: "Configuration files and dynamic languages"
date: 2004-08-10 07:48:13
year: 2004
---
<p>A few months ago, Carlos Perez <a href="http://www.manageability.org/blog/stuff/mildly-complex-web-app-in-2-man-months/view">blogged</a> about someone else's claim to have built a mildly complex web app using <a href="http://www.ruby-lang.org/en/">Ruby</a> in just two months.  Perez argued that one reason <a href="http://www.ruby-lang.org/en/">Ruby</a>-based development was so much faster than Java-based development would have been was:</p>

<ol>

<li>Java web app frameworks typically use lots of configuration files.</li>

<li>These are effectively dynamically-typed (i.e. checking is done at runtime, rather than during a compilation phase).</li>

<li>If you're going to use dynamic typing, you're better off going all the way, rather than trying to weld dynamically-typed configuration onto a statically-typed language.</li>

</ol>

<p>Perez offers no evidence to back up his argument, but it's an interesting one nonetheless.  <a href="http://www.hibernate.org">Hibernate</a>, <a href="http://www.tapestry.org">Tapestry</a>, <a href="http://jakarta.apache.org/tomcat">Tomcat</a> itself, and many other current-generation Java tools require XML configuration files that are so complex that users are effectively doing bilingual programming, without having a debugger for one of the two languages.</p>

<p>In contrast, dynamic languages like <a href="http://www.ruby-lang.org/en/">Ruby</a> and <a href="http://www.python.org">Python</a> allow users to type in complex data structures directly, and make it easy to include calculated values.  This is (in my opinion) the main reason why <a href="http://scons.sourceforge.net/">SCons</a> (a build system written in Python) is easier to use than <a href="http://ant.apache.org">Ant</a>: one language, with a debugger, and you don't have to jump through hoops to say "for each" or "only do this if A and B are true, but C isn't".  Even <a href="http://ant.apache.org">Ant</a>'s inventor agrees: a few months ago, James Duncan Davidson wrote:</p>

<blockquote><p><em>
If I knew then what I know now, I would have tried using a real scripting language, such as JavaScript via the Rhino component or Python via JPython, with bindings to Java objects which implemented the functionality expressed in todays tasks. Then, there would be a first class way to express logic and we wouldn't be stuck with XML as a format that is too bulky for the way that people really want to use the tool.
</em></p></blockquote>

<p>Now that <a href="http://www.oreilly.com/catalog/bfljava/">entire books</a> are being written to decry the complexity of Java application frameworks, and urge us to return to simpler code, it'll be interesting to see whether more programmers switch to dynamic languages, or whether the continuing backwardness of those languages' application frameworks drives programmers back to Java and .Net.</p>
