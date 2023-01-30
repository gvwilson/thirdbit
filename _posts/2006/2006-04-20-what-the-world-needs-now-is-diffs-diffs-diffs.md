---
title: "What the World Needs Now Is Diffs, Diffs, Diffs"
date: 2006-04-20 22:17:01
year: 2006
---
I first heard the term "grand challenge" used in the 1980s to describe the kinds of big projects that would give an entire generation of scientists a focus for their work—something on the scale of putting a person on the moon, or sequencing the human genome.  The phrase has since been applied to many other things, most recently DARPA's <a href="http://www.darpa.mil/grandchallenge/">autonomous vehicle</a> program.

So, here's a grand challenge for the open source community: build a comprehensive library of file differencing tools, so that I can usefully put things other than flat text under version control. If someone modifies an image, a PDF, or a Word document, I ought to be able to pull up a view of the changes, just as I would for source code or a README file.  And if someone adds a couple of attributes to a &lt;table&gt; element in an HTML page, show me that, not the hundred and one places where your editor rearranged the order of pre-existing attributes in ways that aren't semantically meaningful.  If I could see what you've added to our project's use cases or class diagrams, I might just use UML more often; if I could visually merge Gnumeric spreadsheets, I might use them to store grades, rather than tab-separated text files.

There's lots of research to be done here, lots to be invented.  I have a hazy notion of how a diff tool for images might work, but what about sound? Or video? Is there some "deep structure" that unites AutoCAD and VHDL, or some unified algorithm capable of handling all vector graphics formats?  Even if there isn't—even if we only wind up able to handle the hundred most common file formats—we'll have made our lives much, much better.
