---
title: "They're All Eighth Bolts"
date: 2004-09-06 13:36:07
year: 2004
---
<p>Years ago, I was putting together a pine futon frame I'd purchased from Ikea.  It was a pretty simple thing---just four uprights and some crosspieces.  The whole thing was held together by eight bolts hidden in pre-drilled recesses.</p>

<p>The first seven bolts went in easily, but the eighth bolt took more than half an hour.  The problem was getting the bolt to thread through the nut when both pieces were hidden from sight inside the aforementioned recesses.  I got up and did odd jobs three times to calm myself down while trying to get the damn thing seated.</p>

<p>There are a lot of eighth bolts in software development---things that should take a couple of minutes, but instead chew up an entire afternoon.  Most of them have to do with getting third-party software (i.e., stuff you didn't write yourself) to play nicely.  Never mind algorithms (which is what my computer science courses taught me life was about), or pushing data around, or user interface design, or analyzing requirements, or anything else: anyone building a real modern grown-up application is going to spend days---days!---trying to make sense of out-of-date documentation and idiosyncratic configuration files.</p>

<p>As you've probably guessed by now, I'm knee-deep in exactly this process.  I've been trying to set up two PCs (my girlfriend's desktop machine, and my laptop) so that I can do Hippo development.  I'm logging the process, and am starting to worry that my description will frighten students away.  Did you know that <a href="http://www.eclipse.org">Eclipse</a> sometimes pays attention to some environment variables, but only some, and only sometimes?  Or that if you install Tomcat on Windows XP with Service Pack 2, it can fail <em>silently</em> because Windows decides that running it would be a security risk?  If you reboot after the install, Windows will put up a dialog telling you what it's doing, but nothing in the install process tells you that you have to do this.</p>

<p>And then there are databases.  I'm sure relational databases have to be as complex as they are.  Right? They have to be, because otherwise I'd have to believe that database developers are all cruel misanthropes.  <a href="http://www.hibernate.org">Hibernate</a>'s developers recommend <a href="http://hsqldb.sourceforge.net/">HSQLDB</a> (formerly Hypersonic), a pure-Java RDBMS, but only one process can connect to it at once, which means that if you want to check what your servlet has done to the database, you have to shut Tomcat down, fire up a viewer, take a peek, then shut down the viewer and re-start Tomcat.  It isn't difficult, but it makes debugging even more painful than it normally is.</p>

<p>OK, so what about <a href="http://postgresql.org">Postgres</a>?  We're planning to use it as our production server, so why not download the <a href="http://pgfoundry.org/projects/pginstaller">beta version of the Postgres Windows installer</a>, run it, and carry on?  Well, Postgres insists on creating a new user account for security reasons... And then the <a href="http://www.cygwin.com/">Cygwin</a> version of Postgres has trouble talking to the version you just downloaded... and then, and then, and then.  I'm sure it's all doable, but jeez, does it really have to hurt this much?</p>

<p>So, two observations.  First, it isn't just Hippo; the Select Access product that I've worked on for the past four and a half years has run into the same issues over and over again.  (Anecdote: at the first Select Access training course, I apologized to the sales engineers for the product's complexity.  They all laughed.  "You have no idea how much simpler this is to install than anything else we've ever worked with," one of them said.  "It only takes a day to get it going.")</p>

<p>Second, where is academic computer science in all of this?  When and where are we teaching students that <em>this is important</em>, and that getting it right (or at least not getting it wrong) matters more than adding any number of WYSIWYG peer-to-peer object-oriented voice-activated features to a project.</p>

<p>Back to it...</p>
