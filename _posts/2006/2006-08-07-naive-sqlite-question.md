---
title: "Naive SQL(ite) Question"
date: 2006-08-07 12:42:38
year: 2006
---
The best thing about writing <cite>Data Crunching</cite> wasn't that it let me work out some ideas for material that's now in the Software Carpentry course (although that was nice).  The best part was that it forced me to finally learn a little SQL.  For reasons I've now forgotten, I developed a dislike for databases when I was an undergrad.  As a result, I was one of the few developers I knew who couldn't do anything more than "select * from table".

But I still don't know very much, which is why I'm asking for help. I've inherited an <a href="http://www.sqlite.org">SQLite</a> database showing who's been involved in projects of various kinds.  One of the tables looks like this:
<table class="centered">
<tr>
<td align="center" colspan="4"><strong>People</strong></td>
</tr>
<tr>
<td><strong>Ident</strong></td>
<td><strong>Surname</strong></td>
<td><strong>Forename</strong></td>
<td><strong>Affiliation</strong></td>
</tr>
<tr>
<td>7701</td>
<td>Turing</td>
<td>Alan</td>
<td>Cambridge University</td>
</tr>
<tr>
<td>6903</td>
<td>Hopper</td>
<td>Grace</td>
<td>US Navy</td>
</tr>
<tr>
<td>0055</td>
<td>Newton</td>
<td>Isaac</td>
<td>Cambridge University</td>
</tr>
<tr>
<td>…</td>
<td>…</td>
<td>…</td>
<td>…</td>
</tr>
</table>
There's a lot of redundancy in the "Affiliation" entries (only about 1200 different values, out of more than 7000 records).  I'd therefore like to split the table in two:
<table class="centered">
<tr>
<td align="center" colspan="4"><strong>People</strong></td>
</tr>
<tr>
<td><strong>Ident</strong></td>
<td><strong>Surname</strong></td>
<td><strong>Forename</strong></td>
<td><strong>AffilId</strong></td>
</tr>
<tr>
<td>7701</td>
<td>Turing</td>
<td>Alan</td>
<td>0</td>
</tr>
<tr>
<td>6903</td>
<td>Hopper</td>
<td>Grace</td>
<td>1</td>
</tr>
<tr>
<td>0055</td>
<td>Newton</td>
<td>Isaac</td>
<td>0</td>
</tr>
<tr>
<td>…</td>
<td>…</td>
<td>…</td>
<td>…</td>
</tr>
</table>
and:
<table class="centered">
<tr>
<td align="center" colspan="2"><strong>Institutions</strong></td>
</tr>
<tr>
<td><strong>Ident</strong></td>
<td><strong>Name</strong></td>
</tr>
<tr>
<td>0</td>
<td>Cambridge University</td>
</tr>
<tr>
<td>1</td>
<td>US Navy</td>
</tr>
<tr>
<td>…</td>
<td>…</td>
</tr>
</table>
Here's what I've done so far:
<ol>
  <li>Used "select distinct" to pull the institution names out of the   "Person" table and stuff them into "Institutions" with an   auto-incremented integer ID.</li>
  <li>Added an integer-valued "AffilId" column to "Person".</li>
</ol>
The next step is to put the right institution ID values into the "AffilId" column (they're currently all zeroes), and then delete the no-longer-needed "Affiliation" column.  I thought the first half of this would look something like:
<pre>update People set AffilId = (</pre>
<pre>select Institutions.Ident</pre>
<pre>from Institutions, People</pre>
<pre>where Institutions.Name = People.Affiliation</pre>
<pre>);</pre>
but SQLite rejects that.  I've tried several variations without success; if anyone knows the answer, I'd welcome advice.

<hr />In response to Shahan's comment, here's what I'm doing:
<pre>-- Create the 'People' table, and show its contents</pre>
<pre>create table People(Ident integer not null, Surname text not null, Affil text not null);</pre>
<pre>insert into People values(123, "Newton", "Cambridge");</pre>
<pre>insert into People values(456, "Darwin", "London");</pre>
<pre>insert into People values(789, "Turing", "Cambridge");</pre>
<pre>select * from People;</pre>
<table class="centered">
<tr>
<td>123</td>
<td>Newton</td>
<td>Cambridge</td>
</tr>
<tr>
<td>456</td>
<td>Darwin</td>
<td>London</td>
</tr>
<tr>
<td>789</td>
<td>Turing</td>
<td>Cambridge</td>
</tr>
</table>
<pre>-- Create the 'Places' table and show its contents</pre>
<pre>create table Places(Ident integer not null, Name text not null);</pre>
<pre>insert into Places values(0, "Cambridge");</pre>
<pre>insert into Places values(1, "London");</pre>
<pre>select * from Places;</pre>
<table class="centered">
<tr>
<td>0</td>
<td>Cambridge</td>
</tr>
<tr>
<td>1</td>
<td>London</td>
</tr>
</table>
<pre>-- Create the table that will hold the refactored data</pre>
<pre>create table Result(Ident integer not null, Surname text not null, AffilId integer not null);</pre>
<pre>insert into Result select Ident, Surname, 999 from People;</pre>
<pre>select * from Result;</pre>
<table class="centered">
<tr>
<td>123</td>
<td>Newton</td>
<td>999</td>
</tr>
<tr>
<td>456</td>
<td>Darwin</td>
<td>999</td>
</tr>
<tr>
<td>789</td>
<td>Turing</td>
<td>999</td>
</tr>
</table>
<pre>-- Test the intended subquery: it seems to do what I want</pre>
<pre>select People.Surname, Places.Ident from Places, People, Result</pre>
<pre>where (People.Ident = Result.Ident)</pre>
<pre>and (People.Affil = Places.Name);</pre>
<table class="centered">
<tr>
<td>Newton</td>
<td>0</td>
</tr>
<tr>
<td>Turing</td>
<td>0</td>
</tr>
<tr>
<td>Darwin</td>
<td>1</td>
</tr>
</table>
<pre>-- Try to update the final table in place</pre>
<pre>update Result set AffilId = (</pre>
<pre>select Places.Ident from Places, People, Result</pre>
<pre>where (People.Ident = Result.Ident)</pre>
<pre>and (People.Affil = Places.Name) );</pre>
<pre>select * from Result;</pre>
<table class="centered">
<tr>
<td>123</td>
<td>Newton</td>
<td>0</td>
</tr>
<tr>
<td>456</td>
<td>Darwin</td>
<td>0</td>
</tr>
<tr>
<td>789</td>
<td>Turing</td>
<td>0</td>
</tr>
</table>
Whoops—'Darwin' should have a location ID of '1', not '0'.  What's going on?
