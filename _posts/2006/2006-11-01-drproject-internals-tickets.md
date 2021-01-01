---
title: "DrProject Internals: Tickets"
date: 2006-11-01 13:46:51
year: 2006
---
At long last tickets... I still slip sometimes and refer to ticketing systems as "bug trackers", but they're much more than that. If version control is a project's memory of where it has been, ticketing is the to-do list telling it where it's going.  New feature ideas, open questions, requirements---I haven't found a limit yet to what a ticketing system can be used to remember.

The simplest possible ticketing system is a flat ASCII list of things that need to be done.  Store this under version control, so that everyone in the project can edit it concurrently without information being lost, and you're already better off than you were. I ran several projects in the late 1980s and early 1990s this way, and still sometimes miss the simplicity.

But people want more: they want to know who's responsible for each ticket, how important it is, when it was created, and so on.  They also want to slice the data in other ways to find out which tickets particular people (usually themselves) are responsible for, or which tickets have to be closed before Version 3.2 can go out the door.

Historically, the only sensible way to build systems that needed to perform complex queries on structured data has been to use a relational database.  It's easy to create text files with email-style headers like this:
<pre>Author: Alan Turing
Owner: Alan Turing
Date-Created: 1950-07-03 13:29:00
Summary: Write a chess-playing program  As the rules of the game are algorithmic in
nature, surely it must be possible to create a stored program capable of emulating
or surpassing human play?</pre>
but sooner or later, you have to write a little Boolean query engine so that you can find tickets created by Alan Turing, but owned by someone else, that aren't about "chess".  If we were inventing issue tracking for the first time today, open source text search engines like <a href="http://www.lucene.org">Lucene</a> might make text files under version control viable; as it is, every issue tracker I know of has a database in it somewhere (even <a href="http://roundup.sourceforge.net/">Roundup</a>, which breaks with tradition in many other ways).

All right: what does our database need to store?  Text fields for the creator and owner, another text field for the one-line summary, another for the body of the ticket...  Oh, and date fields for when it was created and last updated, and---am I forgetting anything here?  Oh yeah, how important it is, and whether it's a bug, a feature request, a question, um, better throw "miscellaneous" in there as well...  And another date field for when it's due, and---

At this point, alarm bells ought to be ringing in your head. Jumping straight to implementation is a classic engineering mistake; instead of designing a database schema, I ought to be asking who the intended users are, and what they need to do and know.  In one word, I should be thinking about <em>workflow</em>.

I wish I could tell you we did it that way.  I wish I could say we wrote out <a href="http://en.wikipedia.org/wiki/Use_case">use cases</a>, or at least <a href="http://en.wikipedia.org/wiki/User_story">user stories</a>, and derived requirements from them.  What we actually did was look at <a href="http://trac.edgewall.org">Trac</a>, <a href="http://cvstrac.org/">CVSTrac</a>, <a href="http://www.bugzilla.org">Bugzilla</a>, and a couple of other systems, then ask, "Which of the features in these systems will our students actually use?"  When I have to, I justify that methodology by saying that <a href="http://www.drproject.org">DrProject</a> is supposed to teach students how to use grown-up project management tools, so it makes sense for its features to imitate those of real-world systems.  Still kind of wish we'd done more thinking up front, though...

So: our typical user is an undergraduate student familiar with version control, IDEs, and automated builds who has never used web-based project management tools.  She's working in a group of six; they have one term (12 or 13 weeks) to design, build, test, and document a moderately complicated extension to an existing piece of software.  Here's a sample of what she and her team need to keep themselves on track:
<ol>
	<li>The team will create roughly a hundred tickets during the term. That's few enough that we can display one-line summaries of all of them on a single web page.</li>
	<li>Team members will want to see all tickets (so they can judge where the project is as a whole) and the tickets currently assigned to particular people (especially themselves).  They may also want to sort by age (to find things they may have forgotten about), due date, and priority [1].</li>
	<li>They need to change ticket ownership (i.e., assign tickets to one another).  We don't need to wrap permissions around this: if Jiao mistakenly or maliciously assigns all his tickets to Petra, the team will be able to sort it out.</li>
	<li>The whole point of integrating the ticketing system into <a href="http://www.drproject.org">DrProject</a> is to hook it up to the wiki and other systems.  To simplify this, ticket descriptions should support wiki syntax, and it should be as easy to link to tickets from wiki pages (and other tickets) as it is to link to wiki pages.</li>
</ol>
There are lots of other issues as well, but these are enough to highlight two key design points.  The first is, once again, versioning: as with source files or wiki pages, we want to keep track of who made what changes to a ticket, and when.  Partly, this is to protect users against accidents: if someone erases the body of a ticket, we want them to be able to revert it to its previous state.  Keeping history also helps people get answers to questions: if you don't understand the two paragraphs that were just added to a ticket you're responsible for, you'll want to be able to find out who added them, so you can request a clarification.

Versioning tickets brings up all the issues discussed <a href="http://pyre.third-bit.com/blog/archives/688.html">previous</a> in the context of wiki pages.  How do we handle conflicts if two people are updating the same ticket at once?  We don't: whoever submits their change first wins, and whoever submits second is told that they are/were editing an out-of-date version of the ticket. The problem hardly ever arises in practice, so we're not going to rewrite <a href="http://www.drproject.org">DrProject</a> with everything in verison control, but it still irks.

The second key design point that our abbreviated requirements list brings out is that there are three types of fields in tickets:
<ul>
	<li>free-form text fields, like the summary and body;</li>
	<li>those with other "obvious" types, like the creation and modification dates; and</li>
	<li>enumerated fields, like priority and owner.</li>
</ul>
Fields of the first kind are obviously stored as text.  Fields of the second kind are easy too: dates are stored as dates [2], integers as integers, and so on.  But what about enumerated values?  Suppose we want to be able to mark tickets as high, medium, and low priority---should we use strings?  If we did, we'd have to tell users what strings were allowed, and check that they only typed in values we were willing to accept.  Or we could put a table of strings in our CGI program, so that the UI could display them in a dropdown...but then anyone who wanted to add new priority values would have to edit the code.

The best answer is to store a table of acceptable values that the CGI can read, display, and validate against.  Our options are:
<ul>
	<li>A <em>configuration file</em>: easy for the administrator to edit, but yet another thing that has to be in the right place, and formatted the right way, for the system to work.  We'd also have to write yet another function to read and validate the values.</li>
	<li>A <em>database table</em>: not as easy to edit (although a command-line database prompt isn't much different from a simple editor), but we can grab the values with the same SQL queries we're using to fetch everything else we need to know about tickets.</li>
</ul>
<a href="http://www.drproject.org">DrProject</a> uses a database table with two columns, both text.  The first stores the type of the enumeration, such as "TICKET_PRIORITY"; the second stores the actual values, such as "high", "medium", and "low".  This means that we can put other enumerations (such as ticket states) in the same table, rather than needing a separate table per enumeration.

But there's a catch here, one we didn't spot until relatively late in the day.  The sets of enumerations are add-only: once a value has been put into an enumeration, it can never be taken out, since doing so could make the database inconsistent.  If you decide you only need "high" and "low" for tickets, for example, and remove the pair ("TICKET_PRIORIY", "medium") from the enumeration table, all those tickets currently marked "medium" suddenly have illegal priorities.

No problem: we'll just write a little script that promotes all "medium" tickets to "high" priority, or check that nothing is using an enumeration value before removing it.  But what about the historical record?  If a ticket was created with "medium" priority a week ago, should we retroactively change it to "high" as well?  Or leave it with a now-invalid priority?  Or version our enumerations, so that as we go back in time, our sets of values automatically adjust to what they were in the past?  Add-only enumerations are a much simpler solution [3].

One final note: I don't know how anyone else does design, but I do it by creating and exploring a decision tree.  Each time I have a problem to solve, I list my options, along with their pros and cons. I then develop the most promising one until I hit a snag, at which point I either do a little research, write some experimental code, backtrack, or ask someone for help.  "Tree" isn't quite the right word, though; in many cases, it's more like a partially-filled table, in which some choices can be combined with some others.  Each time I explore one cell in the tree, I potentially learn more about the pros and cons of others.

Next up: all the other hard bits of tickets.

<hr />[1] <a href="http://trac.edgewall.org">Trac</a>'s tickets have, among other fields, enumerations for priority, severity, component, and version.  In practice, everyone seems to fold "priority" and "severity" together in their heads: issues are either urgent, important, or ignorable.  "Component" is also problematic---many issues tie into many components, while others (such as questions) don't have anything to do with components at all---so we dropped it entirely.  (Users can tag tickets with keywords to identify components if they want to.)  Finally, student projects aren't big enough, or long-lived enough, to need version labels; once again, if a project does, it can use tags.

[2] Saying that "dates are stored as dates" glosses over a medium-sized annoyance.  As <a href="http://www.crankycoder.com">Victor Ng</a> pointed out, Python's database interface libraries will return any of several different data types to represent a moment in time, ranging from a <code>datetime.datetime</code> from the standard library to something as exotic as <a href="http://www.egenix.com">eGenix</a>'s <code>mxDateTime</code>, depending on which database and database interface you're using.

[3] The same thing applies to user IDs.  Once a user is in the system, her ID can never safely be deleted, since that would result in dangling references. Instead, <a href="http://www.drproject.org">DrProject</a> stores a Boolean "enabled" flag in each account record; disabled accounts cannot be logged into, mail is not forwarded to them, etc.
