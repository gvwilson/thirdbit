---
title: "Managing Student Projects Using Blogging: First Impressions"
date: 2005-01-08
---
If you already know what blogs are, and how they work, you can skip <a href="#1">down</a> in this posting.  If not, read on…

Students who are new to 49X will have heard me say that I'm tracking each project's progress using blogs.  A "blog" (short for "web log") is essentially an on-line journal; typically, one person posts articles to it, which many people can then read.  You can think of it as being like a mailing list or newsgroup, which only one person (or a small number of people) can send information to.

Here's how blogs work: when the blog's author wants to post a new article, she adds information to a file (typically called <code>index.rss</code> or <code>index.rdf</code>) on her web server. Each entry in the file looks something like this:

<pre>&lt;item rdf:about="http://pyre.third-bit.com/blog/archives/000166.html"&gt;
&lt;title&gt;Why Testing Matters&lt;/title&gt;
&lt;link&gt;http://pyre.third-bit.com/blog/archives/000166.html&lt;/link&gt;
&lt;description&gt;This story from the CBC is frightening:
apparently, due to a computer error, abnormal radiology results
for nearly 40 cancer patients weren't sent to their doctors.
If FedEx or Canada Post had lost the results, they'd probably be sued;
since…&lt;/description&gt;
&lt;dc:creator&gt;Greg Wilson&lt;/dc:creator&gt;
&lt;dc:date&gt;2005-01-07T09:31:09-05:00&lt;/dc:date&gt;
&lt;/item&gt;</pre>

The blog's author almost certainly <em>doesn't</em> type in this XML by hand.  Instead, she typically uses a GUI, or a web interface, which has fill-in fields for the title and description, and which generates the rest of the information (such as the permanent link for the item) automatically.  Pyre's blog, for example, is created using a PHP-based system called <a href="http://www.movabletype.org/">Movable Type</a>.

Now, suppose that I want to <em>read</em> some blogs, instead of writing a new entry for this one.  On my machine, I keep a list of the URLs of all the blogs I'm interested in, along with the IDs of the entries from each that I've read.  When I run my blog reader (such as <a href="http://minutillo.com/steve/feedonfeeds/">FeedOnFeeds</a> or <a href="http://www.feedreader.com/">FeedReader</a>—there are literally hundreds out there), it polls each of those URLs to find out which ones have new entries, then downloads those entries and shows them to me.  Once I've read them, my blog reader updates its little database (the one stored on my hard drive).

Blogging (which can mean both "writing a blog" and "reading blogs") is exploding in popularity right now because it addresses one of the biggest problems on the internet: signal-to-noise ratio.  Sooner or later (usually sooner), mailing lists and newsgroups are either swamped by people asking questions that have been answered a hundred times before, consumed by flame wars, inundated with spam, or all three.  The only solutions (so far) are to have human moderators filter the messages, or to restrict who can post; the former is expensive, and the latter stifles the conversation.

Blogs, on the other hand, are subscription-based, and since each feed usually has just one author, you can quickly decide if you want to keep listening or not.  If you don't, you just remove that feed's URL from the list your reader checks, and bingo, it's gone.

<a name="1"></a>Here's the cool bit.  Nothing says a blog's content has to be written by a human being: it can equally well be created by programs like <a href="http://projects.edgewall.com/trac">Trac</a>. Each Trac project generates a blog automatically; every time someone checks something into the project's Subversion repository, Trac makes a blog entry out of their check-in comments.  It does the same thing when someone creates, modifies, or closes a bug report or milestone.

A week ago, I subscribed to the blogs being created by this term's projects.  This means that I can go to one web page, and click the "update" button, and get an up-to-the-minute summary of everything that has happened in each project since the last time I checked. (Assuming, of course, that people write meaningful comments when they make changes: if they write, "Did stuff," I'm not much wiser than I was before.)

It's only been a week, but I already know that this is a much, much better way to track multiple projects than having Subversion and the bug tracker send me email.  Having everything consolidated on one page means that I can see at a glance that Sean updated <code>Important.java</code> three times in quick succession, or that Laurie just opened nine new bugs.  It wouldn't scale to a hundred projects, but then, no one can manage a hundred different projects anyway.

I already have lots of ideas about how to improve Trac's project management blogging.  I'm not posting them here yet because many of them are contradictory, and because I'm sure all of them have already been tried, critiqued, and improved—I need to spend a few hours googling for prior art.  In the meantime, though, I'm hoping to get <a href="http://minutillo.com/steve/feedonfeeds/">FeedOnFeeds</a> installed on Pyre some time in the next few days, so that students can track projects' progress.

Now, if only I could figure out how to integrate instant messaging into all of this…
