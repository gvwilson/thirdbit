---
title: "Web Workflows and Public Embarrassment"
date: 2010-01-05 13:51:01
year: 2010
---
As I've mentioned before, I'm one of the organizers of a set of <a href="http://ucosp.wordpress.com/">undergraduate cross-country open source capstone projects</a>, in which students from <a href="http://ucosp.wordpress.com/2009-fall/">several</a> <a href="http://ucosp.wordpress.com/winter-2010/">universities</a> work together in distributed teams for a term for course credit. Here's what I presently have to do for each student:
<ol>
	<li>Ask her to create a WordPress ID and send it to me (along with the email address it's registered to).</li>
	<li>Add her as an author on the <a href="http://ucosp.wordpress.com">UCOSP blog</a>. (This has to be done by email address, rather than by user ID.)</li>
	<li>Invite her to join our <a href="http://groups.google.com/group/ucosp">Google Group</a>. About 10-15% of invitations are eaten by spam filters and/or trip over a registration problem that seems to be related to GMail cookies.</li>
	<li>Update the <a href="http://maps.google.com/maps/ms?ie=UTF8&amp;hl=en&amp;msa=0&amp;msid=100156001803519969567.00047bf69ca81288680da&amp;z=3">Google Map</a> showing where everyone's from.</li>
	<li>Update the spreadsheet I use to keep track of her personal information. (Before you ask, no, this can't be a Google Doc because of privacy concerns.)</li>
	<li>Update the <a href="http://ucosp.wordpress.com/winter-2010/">HTML table</a> showing the cross-product of schools and projects.</li>
	<li>Once she post a short bio to the UCOSP blog, link her name to that.</li>
	<li>Introduce her to her project's mentor by email.</li>
</ol>
Time per student: 5-10 minutes, if nothing goes wrong, and if I don't forget any steps and have to backtrack. (The worst case is if I update the spreadsheet on one machine, forget to check it in, update it with another students' info on another, <em>do</em> check it in, and then have to merge. Bleah.)

Of course, I do have options here. I could probably, with some work, write a Python script that would use web APIs, COM integration, and screen scraping to do all or most of this for me. Or I could build my own mini-<a href="http://code.google.com/p/soc/">Melange</a> on top of some content management system. Or I could try one of the current generation of browser-friendly record-and-playback tools. However, my gut instinct is that all of those will actually eat more time than continuing to do things by hand.

What I <em>really</em> want, of course, is something that makes this kind of thing as easy to set up and run as "record macro" and "run macro" in [name of text editor goes here]. It would have to understand AJAX (at least as much AJAX as Google Maps uses, which is a fair bit), and also be able to talk to other desktop apps (not just drive a browser). I'm sure that one day it'll exist as an Elisp package; until then, I'll just keep switching tabs in my browser.
