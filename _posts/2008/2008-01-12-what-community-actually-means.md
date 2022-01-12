---
title: "What &quot;Community&quot; Actually Means"
date: 2008-01-12 18:03:32
year: 2008
---
As I was coming out of the library today, I saw a guy in a white van scrape against a car parked on a side street while trying to make a tight corner. The guy in the van didn't stop, but a passer-by went into the library, wrote down the van's license plate number and his own phone number, and taped it to the car that had been scraped.  That got me thinking about the word "community". It's bandied around a fair bit in our field (as in, "open source community"); here's what I think it actually means.
At least week's code sprint, we decided to replace the navigation bar on the left side of DrProject with pull-down menus.  It looks more modern, it'll keep the print view in sync with the web view, and did I mention that it looks more modern? We decided to use <a href="http://dojotoolkit.org/">Dojo</a>, in part because it has better accessibility support than its major competitor, <a href="http://script.aculo.us/">Scriptaculous</a>. Jeff Balogh spent two and a half days ramping up and prototyping; he continued with the conversion after flying back to Florida for school.

At quarter after three on Friday afternoon, David Wolever came into my office and said, "I'm not happy." He'd been playing with Jeff's new interface, and while it was very shiny, it was also very slow: up to four seconds per page load with the browser on the same box as the server. (No, this wasn't the wiki parser bug resurfacing...)

I sent mail to Alex Russell and Kevin Dangoor at 3:25 pm.  At 5:09 pm, Alex sent an 800-word reply that began:
<blockquote><em>Looking at the drproject SVN, I can see some pretty straightforward opportunities to optimize.</em></blockquote>
Yes, that's right: he had checked out our source code and read through enough to realize that we weren't using
<link>tags to load the Javascript, that we hadn't made a layer for the widgets we were requiring, and that we hadn't taken advantage of the Dojo build system's ability to roll up just the widgets we needed into one bundle to reduce the number of requests.
Kevin replied a few hours later as well, but by that time Jeff was able to post the following timings:
<ul>
	<li>Only dojo.js: 35 requests, 1 sec</li>
	<li>dojo.js + dijit.js: 17 requests, 0.62 sec</li>
	<li>dojo.js + dijit-all.js: 35 requests, 1.3 sec</li>
	<li>dojo.js + drproject.js: 4 requests, 0.35 sec</li>
</ul>
Not bad at all.  No idea how long it would have taken to get there without help, but I'm very, very glad that we didn't have to find out---that there was a community out there of people who believed that helping us with no immediate prospect of reward was just the right thing to do.

So thanks, guys---the next beer's on us.
