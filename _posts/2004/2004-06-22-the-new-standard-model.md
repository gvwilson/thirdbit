---
title: "The New Standard Model"
date: 2004-06-22 10:14:57
year: 2004
---
The
<a href="http://particleadventure.org/particleadventure/frameless/standard_model.html">Standard Model</a>
is modern physics' baseline explanation of How It All Works.
It encompasses pretty much everything there is, except gravity.  From
subatomic physics to cosmology, everyone builds their theory in its
image, hoping to create a new standard to supplant today's.

For the developers of my generation, the Standard Model of
programming took shape in the early 1980s.  It consisted of:
<ul>
	<li>C (which has mutated [<a href="#1">1</a>] into C++);</li>
	<li>a character-oriented editor like Vi or Emacs;</li>
	<li>Make for automating the complexities of rebuilding code;</li>
	<li>the standard [<a href="#2">2</a>] Unix command-line tools like
<code>cat</code> and <code>grep</code>;</li>
	<li>CVS for version control;</li>
	<li>character streams as a data exchange format; and</li>
	<li>"power tools" like Yacc and Awk for more complex tasks.</li>
</ul>
By the late 1980s, Microsoft had developed an alternative.  It was
also based on C, but presented developers with an IDE instead of a
character-oriented editor, and gave users uncomposable GUIs instead of
command-line filters.  Visual Basic was the standard for scripting,
and COM was how programmers glued components together.

Microsoft's offerings were well engineered (more so than most Open
Source advocates would like to admit). However, many programmers
disliked the complexity of Microsoft's offerings, and its business
model---so much so that they were willing to adopt a new language
instead.  The result has been a New Standard Model---a morally
respectable replacement for the venerable Unix toolset.  As evidenced
by a slew of recent books [<a href="#3">3</a>], this environment consists
of:
<ul>
	<li>Java</li>
	<li><a href="http://www.eclipse.org">Eclipse</a> and its many plugins</li>
	<li><a href="http://ant.apache.org">Ant</a> (for building) and
<a href="http://www.junit.org">JUnit</a> (for testing);</li>
	<li>XML as a data exchange format;</li>
	<li>some form of scripting language [<a href="#4">4</a>];</li>
	<li>reflection, and technologies built on top of it like JavaBeans, for managing components; and</li>
	<li>a web presence for everything (e.g. a project dashboard, a searchable mailing list archive, and so on
).</li>
</ul>
One of the most interesting things about the New Standard Model is
how much of it is open source.  Java itself is the glaring exception,
but good implementations are freely available and (unusually for free
software) very well documented.  Most [<a href="#5">5</a>] North American
universities have already switched to Java as a first teaching language.

However, most schools have not updated the rest of their curriculum.
Few instructors, for example, require students to submit JUnit tests
with exercise solutions in upper-year courses, or take XML and
reflection as givens.  <a href="http://www.cs.utoronto.ca/~csc207h">CSC207</a>, a new course at
the <a href="http://www.cs.utoronto.ca">University of Toronto</a>, is
an attempt to get the individual-oriented bits of this model into the
curriculum.

The goal of the <a href="http://pyre.third-bit.com/helium">Helium</a> project is
to make it easy for instructors to
teach the team-oriented bits of the New Standard Model.
In order to do this, we are building a web application that is
inspired by <a href="http://www.sf.net">SourceForge</a>,
but tailored for the particular needs of classroom instruction.
Using this, instructors will be able to create batches of team
programming projects, while students will gain experience with
version control, issue tracking, and so on.

This
blog will record our progress as we figure out what <a href="http://pyre.third-bit.com/helium">Helium</a> should do (most
importantly, what it should do <em>differently</em> from
industrial-strength systems like <a href="http://www.sf.net">SourceForce</a>), and as we discover how to
build it.  Comments and pointers are very welcome.

Notes:

[<a name="1"></a>1] I use the word in its science fiction "meddling
with what ought not be meddled with" sense.

[<a name="2"></a>2] By which I mean those defined in Kernighan and
Pike's <a href="http://www.amazon.com/exec/obidos/tg/detail/-/013937681X">The
Unix Programming Environment</a>, rather than those defined by
some after-the-fact standards committee trying to produce a facade of
unity by kitchen-sinking every feature any of them had ever
shoe-horned into their clumsy, crippled implementations of---sorry,
sorry, got carried away there.

[<a name="3"></a>3] See <a href="http://www.amazon.com/exec/obidos/tg/detail/-/0596003870">Java
Extreme Programming Cookbook</a>, <a href="http://www.amazon.com/exec/obidos/tg/detail/-/0764556177">Professional
Java Tools for Extreme Programming</a>, <a href="http://www.amazon.com/exec/obidos/tg/detail/-/1932394192">Explorer's
Guide to Java Open Source Tools</a>, and many others.

[<a name="4"></a>4] As much as I like <a href="http://www.python.org">Python</a>'s syntax, <a href="http://www.jython.org/">Jython</a> and its ilk are crippled by
the impedance mis-match between the semantics of their native data
structures, and Java's.  For example, if you want to create a list in
<a href="http://www.jython.org/">Jython</a>, and pass it into some
Java code, you must either translate <a href="http://www.jython.org/">Jython</a>'s type to a Java List, or use
a Java List in the first place---in which case, you lose much of the
ease-of-use that makes scripting languages attractive in the first
place.  On the other hand, while <a href="http://groovy.codehaus.org/">Groovy</a> uses native Java types,
it doesn't actually work at the moment...

[<a name="5"></a>5] 85%, according to one large textbook publisher;
I've heard others quote 90% or more.
