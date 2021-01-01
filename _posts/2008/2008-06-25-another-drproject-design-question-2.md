---
title: "Another DrProject Design Question"
date: 2008-06-25 18:56:56
year: 2008
---
We've hit another "what should it do?" question in DrProject, and I'd welcome opinions from readers.  As I've mentioned previously, the new ticketing system for DrProject is going to be extensible.  Each project's tickets will initially contain just four fields: sequence number, date created, creator ID, and one line of text.  The first three will be filled in automatically; the user will only have to type the fourth.  From experience, a simple "to do list" like this is all student teams really want or need.

However, almost everyone wants to add "just one more field" to this design. Sometimes it's a person responsible; other times it's priority, due date, a larger text area for a detailed description of the problem, or attachments. The new ticketing system will therefore allow the developers in a project to change the ticket schema <em>for that project</em> using a drag-and-drop form editor.

(Not that it matters right now, but we're not just building this to support teams' chosen workflows. It will also give us a way to find out what those workflows actually are---if we deploy DrProject, wait a few months, then look at what people have chosen to record, it should give us some insight into how they're thinking about their work.)

Now here's the problem. DrProject currently offers two "personal" views called "All Projects" and "All Tickets". The first shows a merge of the event logs from all the projects the user belongs to; the second shows all the tickets assigned to the user from across all the same projects. The question is, what should we show for "All Tickets" if every project's ticketing schema can be different? To make this more concrete, imagine that project Telepathy's schema has grown to:

(id INTEGER, created DATE, creator USER_ID, title TEXT, duedate DATE, priority ENUM("hi", "med", "low"))

while project Antigravity's schema has grown to:

(id INTEGER, created DATE, creator USER_ID, title TEXT, priority("urgent", "optional"), owner USER_ID)

Options we can see are:
<ol>
	<li>Only show the common fields. (Unlike user-added fields, the four basic fields can never be deleted from a project's ticket schema, so we know they'll always be there.)</li>
	<li>Show the union of all the columns. This is awkward for all the obvious reasons: it'll be very wide, many tickets will have blanks in many columns, enumerations with the same name but different values will be a pain, etc.</li>
	<li>Have one table for each project, but put all the tables on the same HTML page. A basic version is easy to implement, but sorting and filtering would be difficult.</li>
</ol>
Anyone have strong preferences? Can anyone see anything better? The ticket for this problem is <a href="https://www.drproject.org/DrProject/ticket/1506">#1506</a>,  and as I said, input would be welcome.
