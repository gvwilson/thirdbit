---
title: "Code reviews"
date: 2005-03-11 10:47:30
year: 2005
---
<p>We're two weeks away from the coding cutoff, so I've got students doing code reviews.  For most of them, this is the first time in their lives that they've marked someone else's code, and had their own examined line by line.  (They've all had plenty of code marked, of course, but with an average of 70 students in a course, TAs can't give the kind of detailed feedback students we all wish they could.)</p>

<p>Coincidentally, I had to do a little code review of my own this morning.  I decided earlier this week to move my online bookmarks from Bookmark4U to <a href="http://del.icio.us">del.icio.us</a>.  The ever-useful Adam Goucher found <a href="http://delicious-py.berlios.de/">a Python module</a> for working with del.icio.us, so I downloaded all my old bookmarks, and wrote a 10-line script to parse that data and upload the links and tags to del.icio.us.  Simple, right?</p>

<p>Wrong.  For some reason, all of the entries were showing up tagged as <code>"system:unfiled"</code>, and the tags themselves were showing up as the extended description of the link.  A quick check showed that I was calling <code>delicious.add()</code> correctly, so I started tracing the code.  It only took a couple of minutes to discover that <code>delicious.py</code>'s author had reversed the order of a couple of parameters in a nested call. Tweak tweak tweak, rerun my script, and all is now good.  (See <a href="http://del.icio.us/gvwilson">my del.icio.us page</a> for my links.)</p>

<p>This experience reinforces conversations I had earlier this week with two different colleagues at <a href="http://www.cs.utoronto.ca">U of T</a>—conversations that I'm sure thousands of instructors around the world have had over and over again for the last thirty years.  We teach students how to write code, but we never (or hardly ever) teach them how to <em>read</em> it.  With the exception of Spinellis's <a href="http://www.amazon.com/exec/obidos/ASIN/0201799405">Code Reading</a>, I don't even know of any books devoted to the topic.  I'd love to make this part of the standard undergraduate curriculum, so that students could tackle coursework using realistically-sized code bases (such as the OS simulator used in <a href="http://www.cs.utoronto.ca/~csc369h">CSC369</a>), but I honestly don't know what I'd drop to make room for it…</p>
