---
title: "DrProject Internals: Setting the Stage"
date: 2006-10-23 16:02:23
year: 2006
---
Over the past 18 months, students here at the <a href="http://www.cs.toronto.edu">University of Toronto</a> have modified and enhanced an open source system called <a href="http://trac.edgewall.com">Trac</a> to create DrProject, a classroom-friendly software project management portal that addresses the unique needs of undergraduate programming teams.  With Version 1.2 of DrProject just a few days away, I thought it would be a good time to describe its current architecture, and how it got to be the way it is.

Let's start with a simple wiki that consists of nothing more than a bunch of pages that can be edited over the web.  Each page is stored as a file on disk, and is written using a simplified syntax in which (for example) <code>''this''</code> becomes an emphasized  <em>this</em> and <code>``that``</code> becomes a code-style <code>that</code> (Figure 1).  When the user wants to view a page, the web server runs a CGI program that translates the simplified wiki markup into HTML; when the user wants to edit a page, the CGI program puts the file's contents into an editable text box, writing it back to the file when the user presses the submit button.

<img alt="Figure 1" src="{{'/files/2006/10/fig0101.png' | relative_url}}" class="centered">

Now suppose we want to keep track of who edited each page, when, and why—in short, we want to keep some <em>meta-data</em> about each page.  One option would be to store a header in each file of the form:
<blockquote>
<pre>Author: Grace Hopper
Timestamp: 2014-07-03 15:43:06
Comment: Updated boot page for IDIAC to describe new quantum array.

= The IDIAC 900 = The IDIAC 900 uses a 1.4 petabit quantum array for…</pre>
</blockquote>
This would be easy to implement: we just teach our CGI program to insert the header when the page is edited, and strip it off before formatting the page for output, and we're done.

But what if we also want to record old versions of pages, so that users can undo changes, or view a page's history?  We could put everything in one file, and separate successive versions with some kind of textual marker, but then we'd have to worry about users putting that marker in their pages.  For example, if the separator was a line of 70 dashes, the CGI would think that any page containing such a line was actually two separate pages.  Another option would be to name successive files <code>PageName.1</code>, <code>PageName.2</code>, and so on, and keep a link called <code>PageName</code> pointing at the most recent version.

Most wikis don't actually do this, though.  Instead, they store pages in a database instead (Figure 2).  At its simplest, the database contains one table with five columns: the page's name, a version number, a timestamp, the author's name, and the text of the page.  When the user asks for a page, the CGI program finds the record with the page's name and the maximum (integer) version number.  To create a new version of a page, it simply adds a new record with the appropriate information.

<img alt="Figure 2" src="{{'/files/2006/10/fig0102.png' | relative_url}}" class="centered">

Storing pages in a database turns out to be simpler and faster than storing them as files.  If you want to find all the pages authored by Grace Hopper, for example, a database can do it with a single query; if your pages are stored as files, your CGI program will have to open them one by one to read their headers.  Similarly, if you want to get the names of all the pages the wiki currently contains, so that you can tell which CamelCaseWords to format as links, the database can give them to you in one operation; if you use the filesystem, you'll have to open the directory, read its contents, throw away everything that contains a version number, and so on.

What kind of database should the wiki use?  Our choices are a database that is managed by its own long-lived server, or an <em>embedded</em> database, which is really just a library of functions that manipulate a chunk of disk reserved to store data (Figure 3).  <a href="http://www.mysql.org">MySQL</a>  and <a href="http://www.postgresql.org">PostgreSQL</a> are well-known examples of the former; <a href="http://www.sqlite.org">SQLite</a> is perhaps the most widely instance of the latter.

<img alt="Figure 3" src="{{'/files/2006/10/fig0103.png' | relative_url}}" class="centered">

The right answer is not to choose.  Instead, we should design our CGI program so that it can use either, since the best solution for a particular deployment will depend on a lot of other factors, and may in fact change over time.  Luckily, every modern language comes with tools that help insulate programs from the idiosyncracies of different databases.  If we use Java's JDBC, for example, the only bits of our code that are specific to a particular database are the bits that load that database's <em>driver</em>, and establish a connection to the database.  Everything after that is written in abstract terms: fetch this value, create that record, and so on.

Life's not actually that simple, though.  SQL is supposed to be a standard, but every relational database implements the standard differently.  SQL commands that work with one database won't work with another, or will behave differently.  Industrial-strength systems therefore have to create (or use) another layer of insulation on top of that provided by SQL and their database connection libraries. These tools are called <em>object-relational mappers</em>, or ORMs, and we'll look at them a few posts from now.  Before then, though, we need to think about how we're going to make our system secure: that will be the topic of the next article in this series.

<hr>

Alan Grosskurth and others have asked, "Why not use a version control repository as a backing store instead of a database?"  It's a good question, and I wondered about this issue myself when I first looked into how wikis are implemented.  Good version control systems, like <a href="http://subversion.tigris.org">Subversion</a> and <a href="http://www.perforce.com">Perforce</a>, can keep track of meta-data, as well as files' histories.  Why not keep each page in a repository?  It would certainly help solve the problem of several people trying to update a page at once.

I think there are two reasons why most wikis haven't gone that route.  The first is performance: in order to format a wiki page, the CGI needs to know the names of every other page in the system (so that it can tell which CamelCaseWords to turn into links, and which to mark as "not yet written").  If you've already established a connection to a database, <code>SELECT PageName FROM Wiki</code> is probably cheaper than calling <code>opendir</code>, reading a list of directory contents, and filtering out things that aren't pages.  I don't actually have any data on this, though; if anyone has pointers to any, please let me know.

The second, and more important, reason that most wikis use a database is inertia.  The four horsemen of the web applicationalypse are browser, server, CGI, and database.  If you're used to building e-commerce and social networking sites in <a href="http://www.php.net">PHP</a>, <a href="http://asp.net">ASP.NET</a>, or <a href="http://www.rubyonrails.org">RubyOnRails</a>, storing text in a database comes naturally; using a version control system feels like adding complexity.  Of course, as soon as you decide you need to reconcile conflicts between concurrent edits, the cost of re-implementing what version control does best quickly outweighs anything you saved by not integrating SVN or P4 into your system…
