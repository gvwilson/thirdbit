---
title: "Misdirection and Javascript"
date: 2005-05-04 16:26:32
year: 2005
---
<p>When I was twelve, I spent $3.95 on a book that promised to teach
me how to do magic tricks that would astound my friends.  I didn't
make it past the second chapter ("No way---I have to
<em>practice</em>!?"), but I still remember the way the word
"misdirection" was set in bold face every time it appeared.  The key
to making a trick work, the book said, was to get the audience to
focus their attention on something else.  That way, by the time they
realized the trick was happening, the hard part would already be
over.</p>

<p>A similar effect seems to have played a key role in the success of
some of today's biggest software technologies.  Unix, DOS, Perl, the
web---they all just kind of grew while the grownups were worrying
about something else, until one day, everyone turned around and said,
"Hey, this is huge!"</p>

<p>So, as a follow-on to last week's post about <a href="http://pyre.third-bit.com/blog/archives/000230.html">you and
your research</a>, here's another idea that I think has at least a
fighting chance of going through that same cycle of stealthy growth
followed by overnight success.  I think there's at least an even money
chance that Perl, Python, and Ruby will all turn out to have been
also-rans, and that the dynamic language that eventually succeeds in
going mainstream will be (wait for it) Javascript.  Here's why:</p>

<ol>

<li>It has a clean, C-like syntax, and a very conventional imperative
programming model, so there are no immediate obstacles to
adoption.</li>

<li>It offers everything that have dynamic languages popular,
including free typing, first-class everything, garbage collection, and
a rich set of built-in tools.</li>

<li>Thanks to IE, Firefox, and Safari, it's available everywhere;
thanks to <a href="http://www.xml.com/pub/a/2005/02/09/xml-http-request.html">XMLHttpRequest</a>,
it can now deliver everything that Java applets were supposed to back
in the 1990s.  <a href="http://maps.google.com/">Google Maps</a> is
the most famous example of the AJAX (Asynchronous Javascript And XML)
architecture that XMLHttpRequest permits, but many others are starting
to appear.</li>

<li>Most importantly, anyone who wants to build a professional-looking
web site these days <em>has to learn it</em>, which means that
hundreds of thousands of programmers are using it every day.  (I'm
willing to bet that more people are writing Javascript at this instant
than are writing Perl, Python, Ruby, and Tcl put together.)</li>

</ol>

<p>Of course, there's a ton of things missing: I wouldn't use
Javascript for command-line <a href="http://www.amazon.com/exec/obidos/ASIN/0974514071">data
crunching</a><sup><a href="#1">1</a></sup>, for example, since it
lacks the thousand and one libraries for LDAP, database connectivity,
process control, and what have you that are the real key to those
other languages' power.  It also lacks IDE support (although projects
like <a href="http://JSEditor.sourceforge.net/">jseditor</a> are
already addressing this.)  Set those against its ubiquity, though, and
they seem like small change.</p>

<p>Javascript has one other thing going for it, at least in my eyes:
it may be the first widely-used language to include direct syntactic
support for XML, via <a href="http://weblog.infoworld.com/udell/2004/09/29.html">E4X</a>.
Whether you like XML or not, it's as much a part of the modern web as
HTTP.  Ubergeeks might scoff and say, "You can do all that with
libraries," but my guess is that any language that treats XML as a
first-class native data type is going to look awfully attractive to
the other 95% of programmers.</p>

<p>(For more information about Javascript, see <a href="http://www.mozilla.org/js/">Mozilla's Javascript page</a>, which
has links to open source implementations in both <a href="http://www.mozilla.org/rhino/">Java</a> and <a href="http://www.mozilla.org/js/spidermonkey/">C</a>.)</p>

<p><a name="1"><sup>1</sup></a>Shameless plug.</p>
