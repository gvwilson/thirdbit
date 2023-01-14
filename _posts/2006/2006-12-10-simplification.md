---
title: "Simplification"
date: 2006-12-10 19:19:43
year: 2006
---
We held a <a href="https://www.drproject.org/All/wiki/Fall2006PostMortem">post mortem</a> on this term's projects Friday before going out to dinner. I took away three major points:
<ol>
	<li>We have to simplify the ticketing interface in DrProject, so that people will use it even in very small groups. One suggestion is to make it more like <a href="http://basecamphq.com">Basecamp</a>'s <a href="http://basecamphq.com/tour-todos.php">to-do list</a>. However:</li>
<ul>
	<li>We want to keep AJAX to a minimum (accessibility, stability, etc.).</li>
	<li>Some of the companies who are thinking about adopting DrProject (or who have done so already) want to <em>add</em> complexity; in particular, they want parent-child and precedes-follows relations on tickets, a "ready for test" state, and so on.</li>
</ul>
	<li>Students think that doing demos is a valuable experience, but it takes a lot of time. (Students get to do their demos twice: once for feedback, and one for a grade.) Swapping them around---i.e., having one day's students practice on their peers, then do their real demos for another day's students---is one possibility, but scheduling is going to be difficult. We've also tried having students do their final demos in tutorial sections of sophomore courses, to give second-year students a taste of what they could be doing by final year, but again, scheduling is hard.</li>
	<li>I didn't track students' progress nearly as well as I should have. There's no amalgamated cross-project view in DrProject (yet---David Scannell has built it, but we haven't deployed it on the production server), and while cycling through seven projects to check event logs isn't <em>that</em> tedious, I somehow never quite got around to it. As a result, students didn't structure their work around making the event log look good, which led to a downward spiral.</li>
</ol>
If we upgrade DrProject over the break, #3 will (mostly) take care of itself. I'm open to suggestions for #2, but what I'd really like from readers is ideas for #1.  We do <em>not</em> want a "kitchen sink" interface that relies on configuration files to hide certain features in certain installations; I know from personal experience that these are a nightmare to test and maintain.

Ideas?
