---
title: "Offline Rendering of WordPress Blog Posts?"
date: 2012-10-16 03:12:48
year: 2012
---
I'd like to take a few tens of thousand WordPress blog posts and turn each into a standalone HTML page. I have the text that WordPress stores in its database, but there's a problem: WordPress <em>doesn't</em> (usually) store &lt;p&gt;...&lt;/p&gt; paragraph tags. Instead, it (usually) interprets a blank line as a between-paragraph marker.  I say "usually" because inside a &lt;pre&gt;...&lt;/pre&gt; block, WordPress leaves blank lines alone.  Oh, and it does funky things with tables, and... You get the picture.  So what I want is a command-line tool suitable for batch processing that'll take the text stored in the database and produce exactly the HTML that WordPress actually hands off to browsers. Problem is, I don't speak PHP, and don't have a couple of hours to browse the WP code base. If someone already has what I'm looking for, I'd be grateful for a pointer...
