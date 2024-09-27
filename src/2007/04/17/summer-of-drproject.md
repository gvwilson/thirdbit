---
title: "Summer of DrProject"
date: 2007-04-17
---
As noted previously, we have quite a team working for us this summer, four of whom are full-time on DrProject.  Two of the students (Jeff Balogh and David Cooper) will be rebuilding the ticketing system, but we still have to figure out what Alex Krizhevsky and David Wolever should do.  Options include:
<ol>
  <li>General bug fixes.  and small extensions (no shortage of work here). Useful, but not particularly exciting for the students.</li>
  <li>Integrate the dashboard display that Ali and Adam built this term to show stats on project size, tickets filed/closed over time, etc.  This is a must-have, but it's not a full summer.</li>
  <li>Add a continuous integration (build 'n' smoke) subsystem (using Xen, Qemu, or some other virtualization layer for security)—would be a *very* nice feature to have, but it's not 100% essential.</li>
  <li>Add continuous documentation (i.e., rebuild a project's JavaDoc/PyDoc/whatever every time there's a check-in, and integrate the results seamlessly into the project's wiki).  Again, it'd be nice to have, but continuous integration is more important.</li>
  <li>Add a chat relay that understands wiki syntax, and archives all conversations for later searching.  There's genuine novelty here, and I've been convinced by students that at least some of them would use it, but I have no idea how challenging it is.</li>
  <li>Sort out authentication—we want self-registration and admin-approved registration; problem is, we need to make sure that Subversion is authenticating against exactly the same identities, and when we tried it last summer, it proved much harder than we'd expected.</li>
  <li>Internationalization, so that someone can easily produce a French language version (federal funding agencies would smile upon us more readily).  The long-overdue Unicode audit would be a first step.</li>
  <li>Wiki extensions, including hierarchical page names and "personal" pages that aren't associated with particular projects.</li>
  <li>Make DrProject a lot easier to install—very useful, but this one is probably best left to the folks at <a href="http://www.engcorp.com">Engenuity</a>.</li>
  <li>Convert to TurboGears, Pylons, or one of the other standard frameworks—tempting in theory, but I'm not sure how much value there would be in practice, and again, I'm not sure that undergrads have enough background to take it on.</li>
</ol>
Votes?  Others?

Later: some others have been suggested.
<ol start="11">
  <li>Modify a WYSIWYG in-browser HTML editor to generate wiki syntax to make it easier for people to enter wiki pages.  It would have to generate wiki text (rather than HTML) in the background so that people could still use wiki syntax in check-in comments, email, etc.</li>
  <li>Integrate with Eclipse, so that users can edit wiki pages, view and modify tickets, etc., without leaving their IDE.  As noted previously, Xiaoyang Guan is going to be working toward this; it's a big job, but will be made simpler if we—</li>
  <li>—create a web services API for DrProject to support remote scripting.  We thought about doing this two years ago, instead of a Python library-style API; I can now see that both would be useful.</li>
  <li>Create a human-content blog for each project.  Right now, each project's blog only contains automatically-generated listings of check-in comments, ticket changes, wiki edits, and so on; there's no way for a human being to write something (such as a release announcement, or a description of how a particularly nasty bug was fixed).  Human-content blog entries should show up as wiki pages as well, as in Martin Fowler's "<a href="http://www.martinfowler.com/bliki/">bliki</a>".  However, all of this will only be useful if we can—</li>
  <li>—sort out the authentication problems for blogs.  As noted before, we can't allow student teams to read each other's event blogs, but there's no standard for storing and forwarding credentials in the blogging world.  We have therefore disabled RSS feeds for most course projects, which I think is a big loss.  <a href="http://openid.net/">OpenID </a>seems to be gathering strength—maybe this summer we'll be able to fix this one. (And yes, this does tie in to #6 above; I'm just not sure how.)</li>
</ol>
Others?
