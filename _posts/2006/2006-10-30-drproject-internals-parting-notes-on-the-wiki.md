---
title: "DrProject Internals: Parting Notes on the Wiki"
date: 2006-10-30 07:13:03
year: 2006
---
I promised in the last article to move on to DrProject's ticketing system, but there are still a couple of issues around its wiki that need further description.  The first is how wiki text is transformed into HTML; the second is why this is harder to do in batch mode than you'd think.

Ward Cunningham created the first wiki in 1994-95 so that people could easily edit hypertext over the web.  The only input widget he trust browsers to support was the text input box.  Since editing HTML tags by hand is tedious and error-prone, he adopted and modified the notational conventions that people were using for email and other plain-text documents:
<table cellpadding="1" border="1">
<tr>
<td valign="middle"><code>== Level 2 ==</code></td>
<td valign="middle">
<h2>Level 2</h2>
</td>
</tr>
<tr>
<td valign="middle"><code>''emphasis''</code></td>
<td valign="middle"><em>emphasis</em></td>
</tr>
<tr>
<td valign="middle"><code>ThirdBit</code></td>
<td valign="middle">ThirdBit</td>
</tr>
<tr>
<td valign="middle"><code>[http://third-bit.com home]</code></td>
<td valign="middle">home</td>
</tr>
</table>
If wikis had been invented later, these text notations might not have been adopted, since it's now straightforward to nest a WYSIWYG HTML editor written in Javascript in a web page.  On the other hand, there are a lot of out-of-browser cases where systems like DrProject want users to be able to create hyperlinked text, such as comments on check-ins to version control and the bodies of email messages, so perhaps ASCII styling would have arisen after all.

Wiki markup simplifies input, but creates a new problem: somehow, pages have to be parsed, then transformed into HTML for display.  The parser that DrProject inherited from <a href="http://trac.edgewall.com">Trac</a> used a pile of regular expressions to match and extract bits of text.  This worked well enough, but was difficult to extend—every time we tried to add a new feature, we found our new regexp conflicted with some of the existing ones, or made some piece of formatting ambiguous.

A graduate student named <a href="http://www.cs.toronto.edu/~liam/">Liam Stewart</a> (now with <a href="http://www.ideeinc.com">Idée</a>) therefore wrote an entirely new parser using <a href="http://www.cosc.canterbury.ac.nz/greg.ewing/">Greg Ewing</a>'s <a href="http://www.cosc.canterbury.ac.nz/greg.ewing/python/Plex/">Plex</a> toolkit.  Like <a href="http://dinosaur.compilertools.net/">yacc</a> and (many) other parser generators, <a href="http://www.cosc.canterbury.ac.nz/greg.ewing/python/Plex/">Plex</a> takes a grammar specification as input, and compiles it into executable code that will parse the language that grammar specifies. Developers can embed instructions in the grammar to create a parse tree as a side effect of analyzing input.  Here's a bit of our grammar (<code>Bol</code> means "beginning of line", <code>Eol</code> means "end of line", and—well, the details aren't important):
<pre>newline = Str("\n", "\r\n")
h1 = Alt(Bol + Rep(Any(" \t")) + Str("="),
Str("=") + Rep(Any(" \t")) + Alt(Eol,newline))
h2 = Alt(Bol + Rep(Any(" \t")) + Str("=="),
Str("==") + Rep(Any(" \t")) + Alt(Eol,newline))
hr = Bol + Str("—-") + Rep(Str("-"))
br = re('\[\[BR\]\]')
ital = re("''")
bold = re("'''")
boldital = re("'''''")
under = re("__")
...
rules = [
(h1, (HEADING, H1)),
(h2, (HEADING, H2)),
(hr, (HR, None)),
(ital, (STYLE, ITALIC)),
(bold, (STYLE, BOLD)),
(boldital, (STYLE, BOLDITALIC)),
(under, (STYLE, UNDERLINE)),
...
]</pre>
The entire parser came in at 459 lines of Python, including blank lines and comments.  We were pretty pleased—until we noticed that DrProject had slowed down a <em>lot</em> after we introduced it.  An undergraduate student named Billy Chun looked into the problem over the summer, and discovered that <a href="http://www.cosc.canterbury.ac.nz/greg.ewing/python/Plex/">Plex</a> was re-generating the parser every time it was called.  More specifically, <a href="http://www.cosc.canterbury.ac.nz/greg.ewing/python/Plex/">Plex</a> was spending 1.9 seconds translating a nondeterministic finite state automaton (NFA) into its deterministic equivalent (a DFA) each time DrProject rendered a wiki page.

This isn't a bug in <a href="http://www.cosc.canterbury.ac.nz/greg.ewing/python/Plex/">Plex</a>, but rather a misconception on our part.  <a href="http://dinosaur.compilertools.net/">Yacc</a> and similar tools produce C code that can be compiled into an application; we therefore assumed that <a href="http://www.cosc.canterbury.ac.nz/greg.ewing/python/Plex/">Plex</a> was doing the same, i.e., that the parser was being produced once and stored somewhere for re-use.  When that turned out not to be the case, we were stymied: we went as far as trying to serialize the byte codes that <a href="http://www.cosc.canterbury.ac.nz/greg.ewing/python/Plex/">Plex</a> generated before deciding that we were creating more complexity than we had eliminated by switching to a parser generator in the first place.

Our eventual "solution" to this problem was to let another change to the system—the switch from pure CGI to <a href="http://www.mems-exchange.org/software/scgi/">SCGI</a>—take care of it for us.  While pure CGI forks a fresh Python interpreter to handle each HTTP request, <a href="http://www.mems-exchange.org/software/scgi/">SCGI</a> relies on a single interpreter running in parallel with the web server.  That long-lived interpreter only needs to generate the parser once; the second and subsequent times it has to render a wiki page, it can re-use the parser it generated the first time.

As Billy was starting his investigation of DrProject's performance problems, two other students named Apple Viriyakattiyaporn and David Scannell were ramping up as well.  We'd hired them to spend the summer doing development on the system; as a warm-up exercise, I asked them to write a standalone wiki formatter.  The idea was to have a command-line tool that would transform the text of a wiki page into HTML, so that people could check their formatting when editing offline, batch process pages for printing, and so on.

It turned out to be a harder job than I'd expected.  Some of the difficulty was simply tangled code: for example, the wiki processor expected an HTTP request object as input, but we obviously wouldn't have one when running from the command line in batch mode.  No problem—Python's <a href="http://en.wikipedia.org/wiki/Duck_typing">duck typing</a> makes it easy to create objects that implement just enough of an interface to get a particular job done.

The real problem—what Fred Brooks Jr. would call the "intrinsic complexity", as opposed to the "accidental complexity"—was how to format links.  In order to decide whether to format a particular CamelCaseWord as a link or not, the wiki processor needed to know what other pages the system contained.  That information was stored in DrProject's database.  Should the standalone wiki processor depend on access to a database?  That would be inconvenient; it would also require us to give users read privileges for the database, which would be a big security risk.

What about decoupling the wiki processor from the database?  If the wiki processor only ever called a function <code>get_page_names</code>, we could import a database-specific version in DrProject, and something else in the standalone wiki processor.  That "something else" could read from a file, take a bunch of page names as command-line arguments, or anything else.

That sounded sensible—until we started thinking about wiki macros.  A macro is a piece of Python code that generates HTML.  If <code>copyright.py</code> is saved in the right directory, for example, and contains a function called <code>copyright()</code> that returns the string <code>"Copyright © 2006 University of Toronto"</code> then putting <code>[[copyright()]]</code> in a wiki page will insert the copyright notice.  <a href="http://trac.edgewall.com">Trac</a>'s <a href="http://trac.edgewall.org/wiki/MacroBazaar">Macro Bazaar</a> lists dozens of macros for navigation, inclusion, charts, and much else.

How is the standalone wiki processor supposed to handle macros? Loading the Python code that implements a particular macro isn't (much of) a problem; the problem is that there's no way of knowing what data a particular macro is going to want.  Something that displays the last time a wiki page was edited, for example, is going to need access to an actualy DrProject database. (Either that, or we create a mock object that has all the features of such a database, which seems a little silly...)

In the end, we punted: after working on the standalone wiki processor for more than a week, Apple and David had learned enough about DrProject's internals to start fixing bugs and implementing new features, so we put set the standalone wiki processor aside.  I'd like to return to it some day, though; being able to batch process wiki pages and tickets (particularly for printing) is still an attractive idea.
