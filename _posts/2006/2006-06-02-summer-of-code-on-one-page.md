---
title: "Summer of Code on One Page"
date: 2006-06-02 09:04:45
year: 2006
---
This year's Summer of Code recipients were announced last week.  I wanted to browse the list off-line, but doing it on the SoC site would have meant clicking through 102 separate pages (one per sponsoring organization).  No problem: Python's urllib lets me download pages as easily as I'd read files, and with minidom, I can parse them, and pull out the information I want.

...except that the HTML on Google's site doesn't escape attributes properly: there are many uses of <em>class=foo</em>, instead of <em>class="foo"</em>, and similar potholes.  OK, my 10-line script turns into 20 lines to transform these so that minidom is happy...

...and then I run into the problem of character encodings and HTML entities.  The polite, professional thing would be to spend 10 minutes remembering how to get the Polish-L-with-a-slash-through-it to display properly in Firefox, <em>and</em> print correctly.  Instead, I add another ten lines to my script to translate the non-ASCII as I go, and bing, there's the page I wanted.

So yes, it probably would have been quicker to click-print-back-down 102 times, but I've saved some trees this way, and can share my results with you.
