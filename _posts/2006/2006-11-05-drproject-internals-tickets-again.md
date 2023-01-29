---
title: "DrProject Internals: Tickets Again"
date: 2006-11-05 10:40:02
year: 2006
---
So that's tickets taken care of, right?  If only...  Versioning is far from being the only thorny issue in building a ticketing system.  To understand some of the others, it helps to know a little about how DrProject evolved from <a href="http://trac.edgewall.org">Trac</a>.

When we first started using <a href="http://trac.edgewall.org">Trac</a> in January 2005, each installation of the software managed one, and only one, project: a single ticket database, a single set of wiki pages, and (most importantly) a single Subversion repository.  Each installation needed its own stanza in Apache's configuration file, and users had to be added to each installation separately (Figure 1).

That model made sense for one-of-a-kind open source hobby projects, but broke down in larger settings.  Even a small company, for example, would usually have several projects going on at once; setting up and managing each one completely independently would be (to quote a former colleague) "nuthin' but overhead".  And in a classroom setting, <a href="http://trac.edgewall.org">Trac</a>'s model didn't work at all, since instructors need to start twenty or more nearly-identical projects every term.

There were several ways we could fix this:
<ol>
  <li>Put a facade in front of a collection of <a href="http://trac.edgewall.org">Trac</a>s to route HTTP and Subversion traffic to the right place (Figure 2).</li>
  <li>Partition the database by adding a project ID column to each table, and use Subversion access control files to give each user access to only part of a common repository (Figure 3).</li>
  <li>Partition the database as above, but give each project its own Subversion repository (Figure 4).</li>
</ol>
We discarded the first option fairly quickly, since it would make integration (particularly configuring the web server) a lot more complicated than it already was, and would be very difficult to test and debug.  Option 2 seemed attractive for a while, but then we stumbled across this scenario:
<ul>
  <li>Hamdan is a member of project H; Tong is a member of project T.</li>
  <li>So Hamdan has read/write access to <code>/svn/drp/H</code>, and Tong has read/write access to <code>/svn/drp/T</code>.  Neither has any kind of access to any other part of the repository.</li>
  <li>Hamdan creates <code>/svn/drp/H/README.txt</code> and adds it to the repository.  This becomes changelist 1.</li>
  <li>Tong creates <code>/svn/drp/T/design.html</code> and adds it to the repository.  This becomes changelist 2.  Tong says, "Huh?"</li>
  <li>Hamdan modifies <code>/svn/drp/H/README.txt</code>, checks in his changes, and is told that he has created changelist 3.  Hamdan says, "Huh?"</li>
</ul>
At first, the non-consecutive numbering of changelists within projects sounds like it would just be an annoyance, but it's more than that.  Suppose we want to display the history of a project: we have to filter out all the changelists that refer to portions of the repository that the user requesting the history isn't allowed to see. And what happens when an instructor adds <code>start.java</code> to every team's repository, and checks them all in at once (instead of checking in one copy at a time)?  What do we show then?  What do we let people revert to?

There's a much larger point here than just how we divvied up students' files among repositories.  The phrase "<a href="http://www.mcs.vuw.ac.nz/comp/Publications/archive/CS-TR-02/CS-TR-02-9.pdf">postmodern</a> programming" refers to the observation that people don't build programs any more: they assemble them by re-mixing the work of others.  99% of the bits in the last big <a href="http://h20229.www2.hp.com/products/select/">product</a> I worked on were bought or downloaded; our part, as complex as it was, was "just" the glue holding it all together.  It's the only way to build large systems, but it means you have to know early on—at design time—what assumptions and limitations are built into the systems you're going to be assembling.  Like other architects, we must always design <em>toward</em> the materials at hand.

Here's another instance of the same problem.  How do you identify tickets?  Every system I've ever worked with numbers them: as Kronecker said, "God created the integers; all else is the work of man."  That maps pretty cleanly to a database table:
<table border="1">
<tr>
<td>id</td>
<td>summary</td>
<td>author</td>
<td>creationtime</td>
<td>...</td>
</tr>
</table>
But what if you want to store multiple projects in a single database?  You can't use a separate table for each project (well, you could, but it would be a lousy design for reasons that I hope are obvious).  What about this:
<table border="1">
<tr>
<td>id</td>
<td>project</td>
<td>summary</td>
<td>author</td>
<td>creationtime</td>
<td>...</td>
</tr>
</table>
Seems like it would work: to get a project's tickets, just add <code>WHERE project=whatever</code> to the <code>SELECT</code> statement.  Once again, though, we have a sequentiality problem: if people are filing tickets in different projects over the same period of time, a particular project's ticket IDs will seem to have gaps.

All right, why don't we just use the project's name, and the ticket's ID within the project, as a <a href="http://en.wikipedia.org/wiki/Composite_key">composite key</a> to uniquely identify each ticket?  Our <code>SELECT</code>s are no more complicated than they were—but then every other table that wants to refer to tickets has to use a two-column composite as a <a href="http://en.wikipedia.org/wiki/Foreign_key">foreign key</a>, instead of a single-column integer value.

Things like this are why I'm sceptical about the most extreme interpretations of <a href="http://www.extremeprogramming.org/">Extreme Programming</a>. "Don't design it 'til you need it" is great if changes don't have long-range ripple effects, but in my experience, the harder the problem, the more likely it is to send shock waves through the whole system.
<h2>Tags</h2>
Here's another example.  Over the summer, Apple Viriyakattiyaporn added tagging to DrProject, so that keywords can be attached to wiki pages, tickets, email messages, and just about everything else. She had two independent decisions to make: how to store the tag values, and how to index them.  Options for storing the tag values were:
<ol>
  <li>Store each tag separately, one per database record.</li>
  <li>Store all the tags together in a delimited list (e.g., <code>"bug fix|concurrency|GUI"</code>) in a single record.</li>
</ol>
The first wins hands-down: if she had used the second, searching for things with particular tags would have required us to delve into the stored values, which requires more code than a simple <code>WHERE</code>, and is less efficient.

What about indexing?  If we only wanted to tag tickets, the table could be:
<table border="1">
<tr>
<td>project id (text)</td>
<td>ticket id (int)</td>
<td>tag value (text)</td>
</tr>
</table>
i.e., a set of unique triples.  But we also want to tag wiki pages, whose unique identifiers are strings, not integers.  Oh, and email messages (integer keys).  And other things that we haven't though of yet, that might use some other type (such as dates) as an index.

Choices:
<ol>
  <li>a separate table for each module (such as tickets or the wiki);</li>
  <li>one table for each type of index value (such as string or int); or</li>
  <li>convert everything into strings.</li>
</ol>
In the first option, the thing the tag belongs to is implicit in the table: only ticket tags appear in the ticket tag table, for example.  In the second and third option, the tag tables need an extra column to keep track of this information.

We hemmed and hawed over this for a while, then finally went with option 3.  We thought that everything we'd ever want to index tags by would be representable as text somehow, and options 1 and 2 might require us to add new tables (i.e., change the database schema) when adding new components in the future.  Changing the schema is always a Bad Thing, since it means upgrading existing installations; "everything is text" seemed like the lesser of the available evils.
<h2>Attachments</h2>
One final note on tickets.  People often want to attach screen shots, configuration files, and other odds and ends to them.  Like <a href="http://trac.edgewall.org">Trac</a>, DrProject stores attachments in the file system in an <code>attachments</code> sub-directory of its working directory. <code>attachments</code> has two sub-directories, <code>wiki</code> and <code>ticket</code>, which store the wiki and ticket attachments respectively.

Each of these has sub-directories whose names correspond to the wiki page's name or the ticket's number; the attached files are put into these directories.  Thus, the attachment <code>attach.txt</code> for ticket #222 would be located at <code>/drp/attachments/ticket/222/attach.txt</code>, while the attachment <code>attach.txt</code> for the wiki page <code>MyWiki</code> would be located at <code>/drp/attachments/wiki/MyWiki/attach.txt</code>.

Attachments aren't versioned (there's that word again): if a user attaches a fresh screenshot to a ticket that has the same name as the old screenshot, the old screenshot is lost.  What's worse, attachments aren't segregated by project, either: if someone attaches a file called <code>pic.png</code> to ticket #22 in the project <code>Venus</code>, it will overwrite the file with the same name that's attached to ticket #22 in the <code>Mars</code> project.

We're going to fix this as soon as we can find the time.  What we should really do, though, is store attachments as <a href="http://en.wikipedia.org/wiki/BLOB">BLOB</a>s (Binary Large OBjects) in database we're using to store the tickets themselves, or backtrack even further and put everything under version control.
