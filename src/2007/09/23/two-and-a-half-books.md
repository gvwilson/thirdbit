---
title: "Two and a Half Books"
date: 2007-09-23
---
Part way through Tracy Kidder's classic look at the computing industry, <cite>The Soul of a New Machine</cite>, one of the hardware team burns out and quits.  After months of worrying about clock ticks and microseconds, his intent is to think about nothing shorter than a season.  When I first read the book, in the summer of my twentieth year, I pitied him; now, at forty-four, with the leaves turning orange and my daughter turning six months, I feel rather envious.

That's one of the reasons I read as much as I do: it gives me an excuse to slow down a little, and to think about something more interesting than the grant application deadline that's about to whoosh by.  Nygard's <cite>Release It!</cite> is a perfect example.  It is full of useful information and practical advice, interspersed with war stories that help ground the general in the specific.  As the blurb on the back cover says, <cite>Release It!</cite> is about designing applications to deal with the things that don't happen in the classroom or the lab: load fluctuations, power outages, upgrades, tangled configurations, and the fact that Firefox sometimes sends two HTTP requests when you click on a link once.  (OK, that's not in this book, but it's the problem the DrProject team is wrestling with right now, and this book has given me a couple of ideas for dealing with.)

Nygard's focus is on how to make enterprise-scale applications work in the real world.  He assumes his readers are familiar with something like J2EE, and with server farms, web caches, and industrial-strength databases; what he explains is how to use them more effectively.  As an example, the chapter on capacity patterns talks about connection pooling, the importance of building a flush mechanism into every cache, when precomputing content will pay off, why you should tune garbage collection, and why object pooling no longer makes sense (if in fact it ever did).  The rest of the book is equally practical, and just as well written.  It would make a great text for a second course in web programming, and ought to be read by everyone tasked with building an e-commerce site capable of handling a customer's rush season.

Segaran's <cite>Programming Collective Intelligence</cite> is equally practical, though its subject is very different.  The book is an introduction to the machine learning techniques that have helped make Google and Amazon household names.  In Chapter 2, for example, Segaran explains how recommendation engines work by building a simple one in Python.  In Chapter 3, he implements some simple clustering algorithms; in Chapter 4, he covers page ranking, and so on.  Later topics include optimization, spam filtering, decision trees, and many other goodies.

Segaran's examples are all interesting, and both his explanations and his code are exceptionally clear.  Some readers will find there's more math in the book than they'd like, but given the subject matter, that can't be helped.  With a few more exercises at the end of each chapter, it'd be a great textbook; as it is, it's an excellent introduction to a topic that grows more important every day.

Last up this month is Berkun's <cite>The Myths of Innovation</cite>, which, I'm sorry to say, left me cold.  It's partly my fault: I didn't subscribe to the myths Berkun set out to debunk, so there weren't any "ah ha!" moments as I read it.  I'm also instinctively sceptical of "big picture" overviews: whenever someone makes a sweeping general claim (and Berkun makes a lot of them), my first reaction is to say, "Yes, but…"  As an undergraduate, I would have considered this book a life-changing experience.  As a middle-aged first-time father with two and a half startups behind me and grant proposals to write, I didn't feel bad about setting aside to finish another day.

<hr />Scott Berkun: <cite>The Myths of Innovation</cite>.  O'Reilly Media, 2007, 0596527055, 192 pages.

Michael Nygard: <cite>Release It!</cite>  Pragmatic Bookshelf, 2007, 0978739213, 326 pages.

Toby Segaran: <cite>Programming Collective Intelligence</cite>. O'Reilly Media, 2007, 0596529325, 360 pages.
