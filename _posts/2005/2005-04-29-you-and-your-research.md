---
title: "You and Your Research"
date: 2005-04-29 10:43:25
year: 2005
---
Richard Hamming was one of the early greats of information science.
After working on the Manhattan Project at Los Alamos, he spent thirty
years at Bell Labs; he received the ACM Turing Prize in 1968, and in
1987, the IEEE named its Hamming Medal after him.

In 1986, he gave a lecture called <a href="http://www.cs.virginia.edu/~robins/YouAndYourResearch.html">"You
and Your Research"</a>, in which he talked about what makes great
researchers great.  A few passages show signs of old-fashioned views,
and others are frankly egotistical, but for the most part, it's a very
thought-provoking look at what you can (and have to) do if you really
want to make an impact.

Among points like "Great researchers are comfortable with
ambiguity" and "Great researchers know how to sell an idea" was one
that particularly struck me:
<blockquote><em>
If you do not work on an important problem, it's unlikely you'll do
important work...  Great scientists have thought through, in a careful
way, a number of important problems in their field, and they keep an
eye on wondering how to attack them.  Let me warn you, 'important
problem' must be phrased carefully.  The three outstanding problems in
physics, in a certain sense, were never worked on while I was at Bell
Labs.  By important I mean guaranteed a Nobel Prize and any sum of
money you want to mention.  We didn't work on (1) time travel, (2)
teleportation, and (3) antigravity.  They are not important problems
because we do not have an attack.  It's not the consequences that
makes a problem ipmortant, it is that you have a reasonable attack...
When I say that most scientists don't work on important problems, I
mean it in that sense.  The average scientist, so far as I can make
out, spends almost all of his time working on problems which he
believes will not be important and he also doesn't believe that they
will lead to important problems.
</em></blockquote>
and later:
<blockquote><em>
Many great scientists know many important problems.  They have
something between 10 and 20 important problems for which they are
looking for an attack.  And when they see a new idea come up, one
hears them say, "Well that bears on this problem."  They drop all the
other things and get after it.
</em></blockquote>
In 1995, after completing a Ph.D., doing post-docs in several
countries, and writing a book on parallel programming, I decided that
I wasn't cut out to be a researcher.  I was pretty sure that I could
jump through the hoops required to get a tenured position somewhere or
other, but the idea left me cold.  As far as I could tell, the whole
point of being a professor was to think Big Thoughts.  Since I didn't
seem to have any, I felt I should go and do something else.

Ten years and several micro-careers later, I think I've finally
figured out a way to find big ideas (and important problems):
<ol>
	<li>Look at how people (especially people in their teens and twenties)
are actually using computers.</li>
	<li>Draw up a list of things that software developers find
frustrating, time-consuming, or error-prone.</li>
	<li>See if anything from the first list can be used to solve problems
in the second.</li>
</ol>
For example, a growing number of students are using <a href="http://www.codingmonkeys.de/subethaedit/">SubEthaEdit</a> to <a href="http://www.insanecats.com/cgi-bin/single.py?month=apr05&msg=26">take
notes collaboratively</a> during lectures.  Questions:
<ol>
	<li>How do editing patterns compare with those of multi-author
wikis?  Classroom notes are taken in real time, by people who are
more likely to have direct contact; will we see the same <a href="http://opensource.mit.edu/papers/viegaswattenbergdave.pdf">patterns
of collaboration and competition that researchers have found at </a><a href="http://www.wikipedia.org">Wikipedia</a> and elsewhere?</li>
	<li>Are notes taken this way more useful to students?  To
instructors (as feedback on what students are actually getting out
of lectures)?  Either way, how can we enhance or customize
collaborative editors to improve the student experience?</li>
	<li>What other tasks can collaborative note-taking be applied to?
<a href="http://www.cs.utoronto.ca/~sme">Steve Easterbrook</a>
suggested using it in requirements analysis sessions, so that
customers could see the analyst's impression of what they'd said
evolving on a shared screen; how well would that work in
practice?</li>
</ol>
Here's another: a lot of empirical research in <a href="http://www.google.ca/search?q=social+network+theory">social
network theory</a> analyzes intra-group email traffic to discover who
actually shares information with, or makes commitments to, whom.  Now,
almost everyone has some kind of spam filter set up on their mailbox.
Suppose you were to compare the filter settings of group members:
would you find role-related patterns, e.g., that people in QA are
reading and ignoring the same kinds of things?  Could you
automatically uncover common interests that group members might not be
aware of?  I don't think it would help much on small projects, but
what about the Windows development group (several hundred people) or
IBM's DB2 group (ditto)?

Closer to home, Modern IDEs, like <a href="http://www.eclipse.org">Eclipse</a>, include <a href="http://www.amazon.com/exec/obidos/ASIN/0201485672">refactoring</a>
tools to help programmers rearrange and clean up their code.
Recently, researchers at the <a href="http://www.cs.colorado.edu">University of Colorado</a> have
taken to recording refactorings of one body of code, and <a href="http://www-plan.cs.colorado.edu/diwan/icse2005.pdf">replaying
them</a> against other code.  If I modify a library's API, for
example, you can take what I did, and apply it to your application, to
bring your app into line with my new API.  So, suppose you have two
pieces of code "A" and "B"; can you use heuristic search to turn "A"
into "B" using only well-defined refactorings?  If so, I can think of
several applications:
<ol>
	<li>When a student hands in an assignment, run the tool in order to
provide marking assistance: "Class XYZ ought to be split, and method
M made abstract, in order to conform with the instructor's
solution."</li>
	<li>When looking at two snapshots from a version control repository,
see if you can reverse engineer a sequence of refactorings to
account for the changes, in the spirit of Parnas and Clements'
famous paper <a href="http://objectz.com/columnists/parnas&clements/09152003.asp">"A
Rational Design Process: How and Why to Fake It"</a>.</li>
</ol>
I'm also interested in the fact that a growing number of software
development teams use some kind of web portal to manage their
projects.  <a href="http://www.sf.net">SourceForge</a> is the most
famous of these, but there are many others.  Each one combines a
version control browser with mailing lists, bug tracking, blogs,
release management, and other collaboration tools.  So far, this stuff
isn't part of the standard undergraduate curriculum, but <a href="http://www.cs.utoronto.ca/~reid">Karen Reid</a> and I are hoping
to change that by modifying <a href="http://projects.edgewall.com/trac">Trac</a> to provide the
features that we need to run courses.  Once we do that, we'll have a
way to collect data on how students actually do group assignments.  We
were surprised in the summer of 2004 that we couldn't
find any correlation between the way students used CVS
repositories in a second-year course, and the grades they were given.
So:
<ol>
	<li>What's the correspondence between student use of the web portal,
and how students actually program?</li>
	<li>What are the differences between the way students use
collaborative tools, and the way professional programmers
(particularly those working on open source projects) use them?
Should we try to close that gap?  If so, how?</li>
</ol>
Last but not least are three accelerating trends:
<ul>
	<li>giving programmers more ways to express abstraction in
programs;</li>
	<li>building applications as extensible frameworks; and</li>
	<li>using XML-based markup, rather than arbitrary text formats, to
store data.</li>
</ul>
I believe the logical endpoint of this convergence is extensible
programming systems, in which "programs" are mixed-media
representations of application code, meta-code for tools such as
compilers and debuggers, and meta-data such as class diagrams and
pictures of the dev team.  Pretty much everyone else is already
there---just take a look at what's into Word documents, CAD diagrams,
or the web site of your favorite band.  Sooner or later, programmers
are going to join the future too, which opens up a host of research
problems.

If you're interested in pursuing any of these, or already are, I'd
enjoy hearing from you.
