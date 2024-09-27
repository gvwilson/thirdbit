---
title: "Monad and Greasemonkey"
date: 2006-03-05
---
You don't often get to glimpse the future, and when you do, you usually don't realize what you've seen until it's too late to take advantage of it.  Take the World Wide Web, for example: I saw a demo of an early version of the Mosaic browser in 1993, and thought, "Eh." A few years later, Jon Udell explained blogs to me, and I had the same reaction.  And Java?  I still have a copy of an email in which I patiently explained to a friend why it would never make any headway against C++.

That's why I read these two books cover to cover: they both show what part of the future of practical computing is going to look like. Oakley's Monad describes the eponymous tool from Microsoft (also known as MSH).  At first glance, it looks like just another command-line shell, but then you see scripts like this:
<pre>D:Scripts&gt; filter ExtractUrl {$parts = $_.split(" "); if ($parts[10] -eq 200){$parts[4]}} D:Scripts&gt; get-content ex010101.log | ExtractUrl | select-object -Unique</pre>
and you realize that something very different is going on.  Where classic Unix utilities communicate via streams of strings, their Monad equivalents pass objects back and forth.  Those objects can be as simple as lists, or as complex as trees and tables.  Whatever they are, Monad offers simple, uniform ways to dissect, transform, and reassemble them.  The result is something that's as convenient as Awk, but as powerful as a full-blown programming language.

If anything, Oakley's book underplays just how powerful Monad might turn out to be.  Instead, he concentrates on the nuts and bolts of installing it, combining built-in filters, creating your own, and so on.  The writing is classic O'Reilly: clear, concise, and technical without being intimidating.  The examples are right where they should be, and the index pointed me right at the answer to every question I had.  Its only weaknesses are a near-total lack of diagrams, and the fact that Monad itself uses Perlish syntax (which isn't Oakley's fault, but is still both a sin and a shame).

Greasemonkey Hacks is just as important, though it's a rougher read, both because it's a compilation, and because its authors are so fascinated with their cool new toy that they make few concessions to non-cognoscenti.  Greasemonkey is a Firefox extension that processes HTML pages after the browser has received them from the server, but before they're displayed.  You describe what you want to do by writing a snippet of Javascript (where "snippet" sometimes means "ten pages or more").

So, do you want to resize text entry fields?  Highlight search terms?  Create a keyboard shortcut to will zoom images?  Strip out ads?  This book describes user scripts to do all of these things, and dozens more.  "Describes" is the operative word, though—not "explains".  I'm all for showing people code, but to take the most egregious example, do the five pages of hex codes in "Hack 89: Syndicate Encrypted Content" really add to anyone's understanding of anything?

While Greasemonkey may seem like nerd candy, it's actually an important step toward a user-centric web.  Prior to Greasemonkey, the only control non-programmers had over how they consumed content was whether they got it by email, in their blog reader, or by jumping to something in their favorites list every once in a while.  Greasemonkey changes that: most people will never write scripts, but they will share and tweak them like music and photos.  By the time today's twenty-year-olds are thirty, they'll be as bewildered by a younger generation's casual remixing of content as I am by my niece's text messaging shorthand.  You heard it here first, friends; you heard it here first.

<hr />Andy Oakley: Monad.  O'Reilly, 2005, 0596100094, 206 pages, $34.95.

Mark Pilgrim: Greasemonkey Hacks.  O'Reilly, 2005, 0596101651, 495 pages, $24.95.
