---
title: "The Last of September's Reading"
date: 2006-10-17 09:34:28
year: 2006
---
In the years leading up to the First World War, French military doctrine held that the élan of their troops—their superior fighting spirit—was guaranteed to win the day.  Never mind the machine guns; what mattered most was courage.

We all know what happened next.

I was reminded of this history lesson a few weeks ago when two books landed in my inbox within a few hours of one another.  The first, from the Chicago-based web development firm 37Signals, is called <cite>Getting Real</cite>.  Here's a quote:
<blockquote>Getting Real is about skipping all the stuff that <em>represents</em> real (charts, graphs, boxes, arrows, schematics, wireframes, etc.) and <em>actually building the real thing</em>.</blockquote>
Here's another:
<blockquote>There's nothing more toxic to productivity than a meeting... They usually convey an abysmally small amount of information per minute...often contain at least one moron that inevitably gets his turn to waste everyone's time with nonsense...[and] frequently have agendas so vague nobody is really sure what they are about.</blockquote>
This is what Steve Yegge, in his blog post "<a href="http://steve-yegge.blogspot.com/2006/09/good-agile-bad-agile_27.html">Good Agile, Bad Agile</a>", calls "snake oil".  Do schematics and wireframes actually get in the way of building the real thing?  That depends on how complicated your "real thing" is, and (crucially) how willing your customer is to pay you to rewrite—sorry, refactor—your code a jillion times.  And meetings are no more likely to be toxic than code is to be unreadable: in both cases, what makes the difference is discipline and professionalism.

My real objection to <cite>Getting Real</cite> isn't that it's an infomercial (again borrowing Yegge's terminology).  My real objection is that the authors don't back up their claims with evidence. Anecdotes, yes, but if anecdotes were proof, then eating a raw onion before each playoff game would be enough to guarantee your team the trophy.  A few people are actually doing rigorous, empirical studies of how effective agile practices are; unfortunately, this book's approach is to shout, "Over the top!"

The contrast with Steve McConnell's latest book, <cite>Software Estimation: Demystifying the Black Art</cite> couldn't be clearer. McConnell is one of the most reasonable people in the industry today, and has a wikipedic knowledge of the literature on development practices.  His contention in this book is that estimation isn't as difficult as people think, as long as it's approached like any other engineering problem.  Did you keep track of how long it took to build the last system of this kind?  If so, those numbers can make your next estimate more accurate.  Are you sure that everyone on the team is including the same factors when they give their estimates?  If not, the fanciest spreadsheet in the world is going to churn out garbage.

The best part of this book for me is the way McConnell weighs each piece of evidence.  Take, for example, his discussion of the COCOMO II estimation formula, which includes almost two dozen different factors calculated from mountains of empirical data collected over many years. As McConnell points out, many of the factors require human judgment, which means that COCOMO II's output is too easily skewed to be of real practical use.  However, it's a great way to see what relative effect changes in estimates will have, since it takes into account the nonlinear relationships between those factors.  McConnell caps this discussion off with a pair of diagrams showing the diseconomies of scale introduced by various factors on projects of different sizes. This "appeal to evidence" is what the snake-oil advocates of UML, agility, and other fads don't do, but it is what our profession needs most.

This month's other two books didn't inspire such strong emotion, though they are both well worth reading.  Derby and Larsen's <cite>Agile Retrospectives</cite> explains how to figure out what's going right or wrong in a project, while that project is going on. That last phrase is what makes it special: to paraphrase the authors, incremental process improvement is just as effective as incremental software development.

Much of the book describes particular activities you can use to set the stage, gather data, decide on actions, and so on, which come complete with time estimates and a list of the supplies you'll need (hint: whiteboard pens and sticky notes).  The authors also talk about how to keep such meetings on track, in order to avoid the productivity drain that the authors of <cite>Getting Real</cite> were so worried about.

Finally, there's the <cite>No Fluff Just Stuff 2006 Anthology</cite>, a collection of articles on a wide range of topics from participants in the eponymous developers' conference.  Neal Ford writes about domain-specific languages (DSLs); Stuart Halloway explains the use of aspect-oriented programming (AOP) in the Spring framework; Ian Roughley preaches the gospel of code coverage (amen), and Eitan Suez gives a programmer's perspective on CSS.  As far as I can tell, what ties these articles together is their authors' passion for their subjects, and the high quality of their writing.  I expect every reader will decide for herself which pieces to skim over, and which to dive into, but I'm pretty sure that everyone who picks it up will look forward to the 2007 edition.

<hr />37Signals: <cite>Getting Real</cite>. https://gettingreal.37signals.com (viewed October 17, 2006).Esther Derby and Diana Larsen: <cite>Agile Retrospectives</cite>. Pragmatic Bookshelf, 2006, 0977616649, 170 pages.

Neal Ford: <cite>No Fluff Just Stuff, 2006</cite>.  Pragmatic Bookshelf, 2006, 0977616665, 240 pages.

Steve McConnell: <cite>Software Estimation: Demystifying the Black Art</cite>.  Microsoft Press, 2006, 0735605351, 308 pages.
