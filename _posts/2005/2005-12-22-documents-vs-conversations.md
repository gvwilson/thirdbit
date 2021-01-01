---
title: "Documents vs. Conversations"
date: 2005-12-22 12:11:58
year: 2005
---
Amateurs playing chess think in terms of positions; sharks care more about combinations of moves.  Amateurs think, "I'm going to build a pawn wall, get my bishops onto good squares, and castle so that my kind is somewhere safe."  Sharks think, "I'm going to advance this pawn so my rook can get to that square to cover an advance by my queen."  Since the board is constantly in motion, one piece per turn, the latter style of thinking almost always wins.

I'm starting to think that we've been thinking like amateurs when it comes to software requirements.  We've been trying to create requirements <em>documents</em>, and then connect them to designs, code, tests, and so on.  But real requirements are rarely static; they're never all present and accounted for at one point in spacetime [<a href="#1">1</a>].

What happens if we think about requirements <em>conversations</em> instead?  What if we stop trying to say "X must Y" and start saying "Having read P and Q, R believed at time T that X must Y"?  This shifts the focus from absolute facts (which implicitly assume that omniscience is possible) to relative beliefs (which is all we really have anyway).  It also makes the temporal and causal aspects of "requirements" explicit: you believe something at a particular time because of something you read, heard, or thought of at some earlier time.

Many successful open source groups already work this way.  Their "specs" are mailing list threads, and the comment streams attached to feature requests and bug reports.  It ought to be chaotic, but as <a href="http://producingoss.com">Karl Fogel</a> describes in his recent excellent book <a href="http://www.amazon.com/gp/product/0596007590">Producing Open Source Software</a> (reviewed <a href="http://pyre.third-bit.com/blog/archives/000305.html">here</a>), in practice it is often very efficient.

So, what would a conversation-centric requirements management tool look like?  My first guess would be a search engine that paid close attention to chronological order, reply-to headers, and the like.  I'd want it to detect, highlight, and stitch together relevant subsections of composite items---e.g., to notice that only the middle third of the message Alan sent last march was about authentication.  The goal would be to allow a developer to put her cursor over a method or test case, right click, and bring up a list of links to the things she needed to read to understand what the code was (supposed to be) doing [<a href="#2">2</a>].  I'd also want to be able to drive the tool in the other direction, and ask, "Which bits of this project depend on what was said on this topic before last week's mailstorm?"

Automating this completely, with no extra human input, is a non-starter, as it would require software that understood natural language.  A more realistic tool could combine AI techniques [<a href="#3">3</a>], human tagging, sheep entrails, or anything else. The key requirements are:
<ol>
	<li>The extra effort required from stakeholders must be small.</li>
	<li>The payoff must be immediately obvious.</li>
	<li>It must mine conversations in the form they actually take, including email, bug reports, wiki pages, code comments, test case names, and so on.</li>
</ol>
Any takers?

<hr />Coincidentally, Jon Udell just posted <a href="http://weblog.infoworld.com/udell/2005/12/22.html">this piece</a> on scannable conversation summaries, which includes links back to his earlier discussion of heads, decks, and leads.

<hr /><a name="1"></a>[1] This is true in those rare cases when requirements actually have been fixed and finalized.  Since our short-term memories is limited, we can only ever hold part of even a medium-sized spec in our minds at once.  Wandering around a fixed spec is, I believe, no different from standing still and watching one part of it evolve.

<a name="1"></a><a name="2"></a>[2] Note that conversation-centric development is orthogonal to the question of agile vs. design-first development.  In my experience, for example, it's equally hard to trace cause-and-effect after the fact in programs developed using XP and RUP.  What both lack is a methodical way to connect tests and methods back to pronouncements: neither user stories on 3x5 cards, nor use cases hyperlinked to sequence and class diagrams, come with (for example) a canned query that will pull up the relevant antecedent conversation.

<a name="2"></a><a name="3"></a>[3] <a href="http://selab.netlab.uky.edu/Homepage/HayesNew.htm">Prof. Jane Hayes</a> has been using Information Retrieval (IR) algorithms to match requirements to code, and Bin Liang (an undergraduate student at the University of Toronto) investigated IR's effectiveness with test cases in the Fall of 2005.  Both, however, assumes a static requirements document, rather than a dynamic conversation.
