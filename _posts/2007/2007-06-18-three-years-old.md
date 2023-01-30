---
title: "Three Years Old"
date: 2007-06-18 12:39:29
year: 2007
---
Today marks the third anniversary of this blog.  As I near my thousandth post, I figured I'd bore you all with a look back.
<h2>DrProject</h2>
Unsurprisingly, DrProject has been the blog's single biggest topic (under several different names):
<ul>
  <li>2004-06-22: the first mention of Helium (a Java-based predecessor of DrProject that we intended to build from scratch).</li>
  <li>2004-07-26: my first gripe about Python having too many half-finished web frameworks.  I've taken some flak for saying this, but I still think that by failing to unite behind one, the Python community gave the game away to Rails.  Speaking of which, this post, from August 10, is my first mention of Ruby, and this one, from December 14, is my first mention of <a href="http://trac.edgewall.org">Trac</a>, the system from which today's DrProject is descended.</li>
  <li>2004-08-04: Helium was over-engineered in many ways; this post discussed some of the tricky problems created by the user-and-project model I foisted on it.</li>
</ul>
We abandoned Java and the Hippo code base early in 2005.  The main reasons were (a) the XML configuration files that tools like <a href="http://www.hibernate.org">Hibernate</a> depend on aren't debuggable, and (b) it took students so long to set up a working environment that they couldn't make much progress in a term.  This post from September 14, 2004, was the first sign of trouble; things went downhill from there.

But back to DrProject: Chris Lenz did some cleanup on Trac for us in the spring of 2005, in exchange for which I mentored a Google Summer of Code project for him (where "mentored" means "stayed out of his way and was awed by his productivity").  The project picked up speed after that, thanks in no small part to generous donations from <a href="http://www.jonahgroup.com">the Jonah Group</a> and Perforce:
<ul>
  <li>2005-08-22: after a summer of hard work, our fork of <a href="http://trac.edgewall.org">Trac</a> (which at the time we were calling Argon) was up and running, but very slow.  The cause turned out to be the fifty million calls to a Unicode end-of-line marker Python was making each time we ran the CGI.  Those N<sup>2</sup> algorithms will get you every time…</li>
  <li>January 2006: Sean Dawson, Jason Montojo, and Chris Lenz started working full-time on DrProject.  A new version went live on January 13.</li>
  <li>2006-02-20: we switched to <a href="http://kid-templating.org/">Kid</a> as a templating engine.  Progress was slow (as was DrProject itself for a while), but steady.</li>
  <li>2006-03-29: Sean Dawson wrote a piece about processes hanging in DrProject.  It turned out to be a taste of things to come…</li>
  <li>2006-04-16: Igor Foox, Greg Lapouchnian, and Pat Smith produced the first screencast of DrProject in action.  Greg won a Google Summer of Code award that year, and built us a web administration interface.</li>
  <li>2006-06-26: 98% of the tickets for DrProject 1.0 were closed.  I thought we were almost done…</li>
  <li>…but then Billy Chun figured out why DrProject was running so slowly, and it turned out we weren't done after all.</li>
  <li>The first screenshots of Version 1 went on the web on July 15; we did the final release on July 17, and updated the screencast on August 14.</li>
  <li>2006-10-23: I started a series of posts about DrProject's internals, largely to get them clear in my own head.  I later used these posts in my Software Architecture course.  They got me wondering whether users would prefer an IDE-based interface to DrProject.</li>
  <li>2007-01-07: the first release candidate for DrProject 1.2 went up on the web. It had grown quite complex, but we still managed to get the final release out on February 6.</li>
  <li>2006-03-08: after a meeting with people from several local companies, I posted a proposal for a new ticketing system.  A month later, DrProject got its first ticket spam.</li>
</ul>
<h2>Software Carpentry</h2>
Improving scientists' software development skills is the reason I got interested in software engineering in the first place:
<ul>
  <li>2004-12-30: the <a href="http://www.python.org/psf">Python Software Foundation</a> gave me a grant to develop an open source course on software development for scientists and engineers called Software Carpentry.</li>
  <li>2005-07-08: I put an alpha version of the notes on the web.  (Calling them "alpha" is pretty generous…)</li>
  <li>2005-07-29: <a href="http://www.nature.com"><cite>Nature</cite></a> ran a short blurb about the course.</li>
  <li>2005-08-22: <a href="http://www.osl.iu.edu/~lums">Andy Lumsdaine</a> decided to offer Software Carpentry at <a href="http://www.cs.indiana.edu">Indiana University</a>.</li>
  <li>2005-09-14: the Toronto edition of the course met for the first time.  (This was actually the second time I'd taught the course at <a href="http://www.utoronto.ca">U of T</a>, but the first time it was on the books and for credit.)  There were initially 93 people in the course (!), of whom about half stuck with it to the end.</li>
  <li>2005-12-09: <a href="http://www.americanscientist.org">American Scientist</a> ran an <a href="http://www.americanscientist.org/template/AssetDetail/assetid/48548?&print=yes">article</a> I wrote about the motivation for the course called "Where's the Real Bottleneck in Scientific Computing?".  It was later republished in German in <a href="http://www.spektrum.de/artikel/852747">Spektrum</a> magazine.</li>
  <li>2006-02-17: I ran a workshop about the course at the annual meeting of the <a href="http://www.aaas.org">AAAS</a>.</li>
  <li>2006-03-26: I got angry about a report from <a href="http://research.microsoft.com">Microsoft Research</a> called <a href="http://research.microsoft.com/towards2020science/"><cite>2020 Science</cite></a> that gushed about the future of scientific computing without any more than passing mention of the problem of making sure scientists' programs actually work.</li>
  <li>2006-04-28: all the minor corrections to the notes were finished.</li>
  <li>2006-06-25: the course notes moved to their permanent home on one of <a href="http://www.enthought.com">Enthought</a>'s servers.</li>
  <li>2006-07-14: Version 2.0 of the course notes went up on the web.</li>
  <li>2006-08-04: <a href="http://www.hpcwire.com">HPCWire</a> <a href="http://www.hpcwire.com/hpc/771596.html">interviewed me</a> about the course.</li>
  <li>2006-08-17: I gave a talk at <a href="http://www.scipy.org/SciPy2006">SciPy'06</a> on selling Python to scientists and engineers.  (Hint: don't.  Instead, sell them solutions to their problems that happen to use Python, then wait.)</li>
  <li>2006-10-31: a result published in <a href="http://www.nature.com"><cite>Nature</cite></a> was retracted because the code used to produce it had been flaky. Five months later, scientists from the <a href="http://www.scripps.edu">Scripps Institute</a> had to retract five papers published in various prestigious journals because of a sign error in a computer program.  Stories like these are making the course easier to sell…</li>
  <li>2006-11-28: <a href="http://cise.aip.org/"><cite>Computing in Science and Engineering</cite></a> ran an article I wrote about the course.</li>
  <li>2007-04-02: <a href="http://ivory.idyll.org/">Titus Brown</a> got a contract to teach the course at <a href="http://www.llnl.gov">Lawrence Livermore National Laboratory</a>.</li>
</ul>
<h2>49X</h2>
I've been supervising undergraduate student projects under the CSC494 and CSC495 headings since 2002. We've accomplished quite a bit:
<ul>
  <li>2004-08-28: my student teams scored 5 (or 6) out of 12 on the Joel Test.  Today, the good ones score 8.</li>
  <li>The summer student teams have always worked well together.  As I noted on 2004-09-14, social activities are a large part of the reason.</li>
  <li>Managing student projects via auto-generated blogs was a revelation when I first tried it in January 2005.  Even then, I was wondering how to integrate instant messaging into software engineering as well.</li>
  <li>I used to be very sceptical about Extreme Programming and other agile methodologies.  Discussions with Peter Hansen and others have since convinced me that it's a valuable tool in some contexts, and worth teaching.</li>
  <li>The <a href="http://psiphon.civisec.org/">Psiphon</a> project made the Globe and Mail in February 2006.</li>
  <li>I've always run post-mortems on 49X projects, and learned a lot from this results.</li>
</ul>
<h2>Research Projects</h2>
<ul>
  <li>I first thought of Bayesian filtering to detect duplicate posts in newsgroups in October 2004; Helen Bretzke and Jonathan Lung looked into it in 2005-06, but it didn't seem to lead anywhere.</li>
  <li>Quantifying the learning curve for tools and languages (2005-01-02): this was briefly fashionable in the 1970s and 1980s (look up a conference called "Empirical Studies of Programmers"); I think it'd be worth revisiting now that software engineering has a clearer idea of how to do empirical studies.</li>
  <li>What does an entry-level requirements tool look like?  I started wondering back in May 2005, prompted partly by discussions with <a href="http://www.cs.toronto.edu/~sme">Steve Easterbrook</a> and <a href="http://www.cs.toronto.edu/~jaranda">Jorge Aranda</a>, and partly by the realization that none of the widely-used software project management portals (like <a href="http://www.sourceforge.net">SourceForge</a>) offer any help with requirements.  In December 2005, I believed a (the?) solution would be to treat requirements as conversations to be searched, rather than documents to be assembled, but I'm still open to suggestions; <a href="http://www.cs.toronto.edu/~jaranda">Jorge</a>, <a href="http://www.cs.toronto.edu/~sme">Steve</a>, and I are now studying how small companies actually manage requirements in the real world in order to get more ideas.  The simplest so far is to allow hierarchical organization of tickets.</li>
  <li>Many unhappy experiences have convinced me that the world really needs someone to figure out a "debugger" for configuration files ought to work.  Do this, and every <a href="http://ant.apache.org">Ant</a>, <a href="http://httpd.apache.org">Apache</a>, <a href="http://www.hibernate.org">Hibernate</a>, and <a href="http://tomcat.apache.org">Tomcat</a> user in the world will be your new best friend.  (I keep coming back to this topic; one attempt to build a UML model debugger is now on SourceForge.)</li>
  <li>A library's API is the set of functions it allows others to call. Why don't we also care about the functions a library (or application) <em>needs</em> to call (which I dubbed its XPI in December 2005)?</li>
  <li>Your version control system is only as good as your diffs, but sadly, after forty years, the only things we can diff reliably are plain ol' text files.  There's research waiting to happen here…</li>
  <li>Or if that seems too mundane, how about looking at ways to express temporal information about variables as part of their types?</li>
  <li>Or maybe you'd like to measure the value of modeling?  (Hint: I don't think it's that useful…)</li>
</ul>
<h2>Books</h2>
<ul>
  <li><cite>Data Crunching</cite> appeared on Amazon in April 2005.  Jon Udell liked it; so did <cite>Focus on Java</cite> and <cite>StickyMinds</cite>.</li>
  <li>I first asked the web for pointers to good programmers in April 2006.  At SIGCSE'07, Grady Booch let the cat out of the bag by telling the world about <cite>Beautiful Code</cite>.  I posted a table of contents on March 27.</li>
</ul>
<h2>Miscellaneous</h2>
<ul>
  <li>I first mentioned code review, and the problem of making it a normal part of the undergraduate curriculum, on 2004-06-26. I tripped over the issue again in March 2005.  In 2006, <a href="http://www.cs.toronto.edu/~campbell">Jennifer Campbell</a> and I got a grant from <a href="http://www.utoronto.ca">U of T</a> to hire two students full-time to develop OLM.  The first screencast of their work went up on the web on 2006-08-29, and we've been using OLM in courses ever since.</li>
  <li>Women are under-represented in computing, and the situation is steadily deteriorating.  Michelle Levesque and I looked at why the gender ratio in open source is so much worse than in the industry as a whole (2004-10-08).</li>
  <li>: I was HP's rep on the <a href="http://groovy.codehaus.org">Groovy</a> JSR for three months in the summer of 2004 before giving up.  These posts from September 7 and September 11 explain why.  Groovy 1.0 finally appeared in January 2007; interest was…muted.</li>
  <li>I really liked Joel Spolsky's <a href="http://www.joelonsoftware.com/articles/Unicode.html">explanation of Unicode</a>.  I've asked twice (2004-11-22 and 2006-04-04) for someone to write a similar explanation of calendars, time zones, and the like, but to no avail.</li>
  <li>My post on interviewing at Google from 2005-01-19 is still the most popular in the blog.  Michelle Levesque's description of life at Google from October 2006 explains why ;-).</li>
  <li>I first realized in May 2005 that Javascript has a real chance to become the dominant scripting language.  I haven't put any money into it, though… ;-)</li>
  <li>I started redesigning <a href="http://www.cs.toronto.edu">U of T</a>'s software engineering courses in July 2006. I posted the new syllabus in March 2007.</li>
  <li>I've been a mentor for Google's Summer of Code every year that it's run.  I think it's a great program, but as I said in August 2006, I think it could be better.</li>
  <li><a href="http://kanushu.uwaterloo.ca/~tveldhui/">Todd Veldhuizen</a>'s paper <a href="http://endoprogramming.livejournal.com/1257.html"><cite>Software Libraries and the Limits of Reuse: Entropy, Kolmogorov Complexity, and Zipf's Law</cite></a> keeps prompting new ideas.  In January 2007, for example, I wondered whether his ideas imply an intrinsic tradeoff between abstraction and debuggability.</li>
  <li>I wrote an article on <a href="http://delivery.acm.org/10.1145/1040000/1039534/p48-wilson.pdf?key1=1039534&key2=1446697711&coll=&dl=&CFID=15151515&CFTOKEN=6184618">extensible programming</a> for <a href="http://www.acmqueue.org/"><cite>ACM Queue</cite></a> in 2004.  In March 2007, I saw the first signs that it was actually happening.</li>
</ul>
<h2>And Then</h2>
Our daughter Madeleine was born on March 31, 2007.  Suddenly, all my other projects seemed a lot less important.
