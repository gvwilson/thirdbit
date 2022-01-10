---
title: "Entry-Level Requirements Engineering Revisited"
date: 2006-02-15 13:50:09
year: 2006
---
Try googling for <a href="http://www.google.ca/search?q=%22open+source%22+%22requirements+engineering%22">"open source" "requirements engineering"</a> or <a href="http://www.google.ca/search?q=%22open+source%22+%22requirements+management">"open source" "requirements management"</a>.  Lots of links, but nothing that leads to a mature (or even adolescent) open source requirements engineering tool that would help me keep track of:
<ol>
	<li>what I'm supposed to be building;</li>
	<li>where that requirement came from (i.e., who I have to talk to if I want to change it, or to get more information);</li>
	<li>whether the requirement has actually been implemented; and</li>
	<li>whether that implementation has actually been tested.</li>
</ol>
There are lots of commercial tools in this space, including:
<ul>
	<li><a href="http://www.speedev.com/online-demos.asp">SpeeDEV</a></li>
	<li><a href="http://www.telelogic.com/corp/products/doors/">DOORS</a></li>
	<li><a href="http://www.gatherspace.com/">GatherSpace</a></li>
	<li><a href="http://www.objectiver.com/">Objectiver</a></li>
	<li><a href="http://www.igatech.com/rdt/">Igatech's RDT</a></li>
	<li><a href="http://www.serena.com/Products/rtm/home.asp">Serena RTM</a></li>
	<li><a href="http://users.reqtify.tni-software.com/">Reqtify</a></li>
</ul>
but most of them are just glorified to-do list managers.  Some integrate with Microsoft Office tools, so that users can edit requirements documents in Word or Excel, while others integrate with CASE tools, but for the most part, they all assume that someone, somewhere, is going to type in a whole bunch of itemized, organized, point-form requirements, and then update them regularly as the project progresses.

Which, in my experience, just doesn't happen---at least, not in the domains I'm most interested in:
<div align="center">
<table>
<tr>
<td></td>
<td><strong>School</strong></td>
<td><strong>Open Source</strong></td>
</tr>
<tr>
<td><strong>Customer</strong></td>
<td>prof</td>
<td>nerd</td>
</tr>
<tr>
<td><strong>Developer</strong></td>
<td>student</td>
<td>nerd</td>
</tr>
</table>
</div>
XP's response is to abandon long-range requirements management in favor of short-range user stories.  If your customer's marketing department doesn't need to know what they're going to have to sell next year, and if they're willing to pay for a lot of duplicated effort (sorry, refactoring), that's great, but I've never worked under those conditions.

On the other hand, I <em>have</em> seen projects hum along for several years, hitting deadline after deadline, once sensible requirements management practices were put in place.  However, that only happened after the group in question had been through a couple of death marches.  This leaves me with a conundrum: how to convince people (particularly students) that RE will pay of, without making them jog a few laps of Hell?

The option I'm most interested in is to lower the entry cost of RE. All of the tools described above (with the exception of GatherSpace) have a hefty cover charge: you have to invest a lot in them before you get anything out.  Students working on three-week (or even term-long) assignments won't ever reach those tools' the payoff points; if we say, "You have to use this to get a grade," they'll probably come away thinking even <em>less</em> highly of RE.

So, what does an entry-level RE tool look like?  Something you can learn in a one-hour tutorial (or less), that will make your life easier the second time you use it?  Last summer, Bin Liang explored the possibility of adding a two-pane display to DrProject that would let students connect requirements (created by the prof, in the usual point-form way) to <a href="http://www.junit.org">JUnit</a> unit tests, so that they could see which parts of the assignment they'd actually completed.

It was a nice idea, but in the end, we decided it wouldn't be compelling: profs would have to put a lot more time into creating their assignments, while students wouldn't see much benefit (anyone can keep track of half a dozen requirements in their head).

Bin then went on to explore something more promising, something that wouldn't require any extra work from either profs or students.  Take an assignment, and throw away the stop words (like "the" and "or") to create a set of keywords with locations.  Now take a bunch of <a href="http://www.junit.org">JUnit</a> tests, and break the names of the classes, methods, and variables they contain into words (by splitting on underscores, or on CamelCaseBoundaries) to get another set of located keywords.  What happens when you correlate the two?

As <a href="http://selab.netlab.uky.edu/homepage/">Jane Huffman Hayes</a> and her colleagues found out in a slightly different context, the results are actually pretty good: standard information retrieval algorithms will match code to requirements and vice versa. Not as well as a human being would, maybe, but certainly well enough to be worth exploring further.

There are lots of directions we could go with this, and other people are already blazing the trail.  <a href="http://www.requirementsassistant.nl/index.htm">Requirements Assistant</a>, for example, looks for ambiguous or contradictory phrases in an requirements document; I could see combining the two approaches to try to find places where the code <em>doesn't</em> implement the requirements.  But in the near term, here's a proposal:

On the left, we have the assignment handed out by the prof (format to be determined).

On the right, we have the student's code.

In the middle, we have a tool which matches assignment (requirements) to code, and which highlights bits of code that no part of the assignment maps to.  TAs use this when marking: they click on Part A, B, or C of the assignment spec, and it shows them what (if anything) they should be marking.  They *only* mark the things that the tool finds: if they click on Part C, and the tool says, "I can't find corresponding code," they give the student 0 for that part of the assignment.

When they start the assignment (or course), students are shown the tool, and told, "TAs will use this when grading.  You can run it too, before you submit your work, in order to see what the TA will see. Please note that if the TA clicks on a bit of the assignment spec, and the tool can't find any matching code, they'll give you zero for that part of the assignment, since clearly it's unfair to ask them to waste time hunting around in your code for something that you could have made plain and clear."

Students now have an incentive (a) to learn how to drive the tool, and (b) to add whatever extra information the tool requires (and/or to structure their code the way the tool wants).  The carrot is that they have more insight into the grading process: as with submitting code to run against the prof's test suite, and getting a preliminary score back, they can *see* which bits of their code the TAs are going to be marking to satisfy each bit of the assignment spec.

So, what do you think?  Would you have felt put upon as a student if someone deployed this in a class?  Do you think you would have learned something from it?  Are there other entry-level requirements engineering tools that might have fit your needs better?  I'd be very interested in hearing your ideas.
