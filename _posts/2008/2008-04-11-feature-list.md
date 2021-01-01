---
title: "Feature List"
date: 2008-04-11 20:11:26
year: 2008
---
I skipped an important step in my <a href="http://pyre.third-bit.com/blog/archives/1487.html">previous post</a>: I wasn't explicit about the features something had to have to qualify (in my mind, if no one else's) as a "software project portal".  Here are my current thoughts, sorted in order of importance.
<ol>
	<li>Identity management and access control (i.e., accounts, privileges, and all that jazz).
<ul>
	<li>Bonus marks if privileges are organized into roles for easier administration.</li>
	<li>More bonus marks if administrators can define new roles.</li>
	<li>Still more if it integrates with <a href="http://www.openid.org">OpenID</a> or the like.</li>
</ul>
</li>
	<li>Issue tracking (a.k.a. "ticketing"), or some other kind of to-do list.
<ul>
	<li>...with a query interface that lets users filter and sort.
<ul>
	<li>Bonus marks if F&amp;S settings can be saved and shared, so that users can set up things like "all the high-priority items assigned to me that are due within a week".</li>
</ul>
</li>
	<li>More bonus marks if fields in tickets can be customized without rewriting any code.</li>
	<li>Still more bonus marks if this is combined with a calendar so that users can group tickets by release or due date.
<ul>
	<li><a href="http://www.drproject.org">DrProject</a>'s "milestones" have been inherited from <a href="http://trac.edgewall.org">Trac</a>, and are just as lame.</li>
</ul>
</li>
</ul>
</li>
	<li>Version control repository browser (browser only because there's no safe and easy way to do a commit through a browser).</li>
	<li>Mailing list management (even though <a href="http://trac.edgewall.org">Trac</a> doesn't have this, and I still consider it a portal).</li>
	<li>A wiki.
<ul>
	<li>Marks taken off if the wiki's grammar <em>doesn't</em> have shortcuts for linking to tickets, code revisions, mail messages, and the like.</li>
</ul>
</li>
	<li>Cross-component search.</li>
	<li>A plugin or extension system.
<ul>
	<li><a href="http://www.drproject.org">DrProject</a>'s needs a major overhaul...</li>
</ul>
</li>
	<li>Some kind of over-the-web API (REST, SOAP, or RPC doesn't matter, just so long as it allows remote scripting, automation, and integration).</li>
	<li>An integrated view of the project's history.
<ul>
	<li>This should be available as an RSS feed as well as in the browser.</li>
	<li>Users should be able to get more immediate notification of selected events (e.g., email when tickets they care about are created or changed).</li>
	<li>There should also be a separate, more detailed event log for auditing and administrative purposes.</li>
	<li>Plus charts and other analytic tools.
<ul>
	<li>We're going to try again this summer to build something like this for <a href="http://www.drproject.org">DrProject</a>.</li>
</ul>
</li>
</ul>
</li>
	<li>Project blogs.</li>
	<li>Continuous integration.
<ul>
	<li>Most systems rely on external tools like <a href="http://cruisecontrol.sourceforge.net/">CruiseControl</a>, in which case this becomes "integrate with continuous integration".</li>
</ul>
</li>
	<li>Test case management.
<ul>
	<li>Actually, most don't bother to do this separately (<a href="http://www.rallydevelopment.com/test_defect_management.jsp">Rally</a> being a notable exception).  I'm still trying to figure out why nobody has integrated with <a href="http://fitnesse.org/">FitNesse</a> yet...</li>
</ul>
</li>
	<li>Requirements management.
<ul>
	<li>A lot of systems, including <a href="http://www.drproject.org">DrProject</a>, just use tickets for this, but <a href="http://studios.thoughtworks.com/mingle-project-intelligence">Mingle</a> and other agile-oriented portals support user story cards or the like.</li>
	<li>As an aside, I think it's pretty telling that nothing smaller than <a href="http://www-306.ibm.com/software/awdtools/clearcase/">ClearCase</a> offers, or even integrates with, a "classic" requirements management tool like <a href="http://www.telelogic.com/Products/doors/doors/index.cfm">DOORS</a>.</li>
</ul>
</li>
	<li>Time tracking.
<ul>
	<li>This comes near the bottom of my list because I believe most people input random numbers.</li>
</ul>
</li>
	<li>Integration with IRC, instant messaging, VoIP, and other communication tools.
<ul>
	<li>Anyone?</li>
</ul>
</li>
	<li>Support for internationalization and localization.</li>
	<li>Forums or some other kind of bulletin board system.
<ul>
	<li>I personally think this is redundant given mailing lists and a wiki, but a lot of portals offer them, and we regularly get requests to add them to <a href="http://www.drproject.org">DrProject</a>.</li>
</ul>
</li>
</ol>
One more consideration is that a portal should be installable, rather than a hosted service: not every project is open source, and many universities aren't allowed to store student information out of their own jurisdiction.
