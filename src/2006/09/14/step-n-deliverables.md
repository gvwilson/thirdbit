---
title: "Step N: Deliverables"
date: 2006-09-14
---
Let's skip ahead to the last step: wrapping up.  For most students, and most assignments, this means handing the work in and getting a grade.  But course projects are different:
<ol>
  <li>They often roll forward from one term to the next, so the end of one team's involvement isn't necessarily the end of the project; and</li>
  <li>Course projects are meant to simulate real life, where delivery of a particular version is just another step in the product lifecycle.</li>
</ol>
In the past, I have asked teams to write a final report, which has been worth either 40% or 50% of their grade.  These reports have ranged from a dozen to 50 pages, depending on the size and enthusiasm of the team.  Typically, they have had the following sections:
<ul>
  <li>A <em>title page</em>, <em>abstract</em>, and <em>table of contents</em>.  The first identifies the document; the second summarizes it in three or four sentences, so that busy browsers can decide whether they ought to read the whole thing; and the third helps people navigate.  (A quick note on abstracts: for some reason, computer scientists often write movie trailers, rather than summaries. "We will contrast frobnication with jambramification" doesn't help browsers who are faced with a hundred candidate links; "We show that frobnication is 28% more likely to spleedle than jamframification under normal circumstances" does.)</li>
  <li>An <em>introduction</em> which sets the stage for the rest of the document.  This explains what problem the team set out to solve, and summarizes any background knowledge needed to understand the team's solution.  It shouldn't state the obvious: there's no need to tell readers what the Internet is, or how a parser works.  Instead, it should cover whatever general knowledge the <em>next</em> team will need in order to continue the project.</li>
  <li>A <em>description of what was done</em>.  This should <em>not</em> simply rehash the A&E (although that's a good place to start). Instead, it should describe the system's architecture, any features of its data formats, class structure, or UI that won't immediately make sense to a knowledgeable observer, and so on.  As with the introduction, the target audience is the next team to work on the project.</li>
  <li>An <em>evaluation</em> of the project.  This should cover both how good the software is, and how well the team functioned.  The first can include high-level criticism ("The persistence layer works fine, but in retrospect, our concurrency control mechanism was a bad choice") and pointers to specifics ("Ticket 213 should be addressed before any further work is done on user preferences").  The second is actually the most important part of the entire course.  What did the team learn about teamwork?  What went well?  What should they never do again? Motherhood-and-apple-pie statements about the importance of version control don't belong here (or anywhere else).  Instead, the team should conduct a proper post mortem, listing the good and bad points of the preceding thirteen weeks as honestly as they can.</li>
  <li><em>References</em>, including books, papers, and links that the team found helpful.</li>
</ul>
As you can see, this report is neither a user's guide nor maintenance documentation.  Instead, it is like the end-of-contract reports I had to prepare when I was a consultant.  What had I done to earn my customers' money?  What should the next person (who might not be me) do?  What could I tell them that would save them time? Internal documentation (like Javadoc) doesn't help with these questions, and anyway, the team should be producing that as they go along, not all in a rush at the end of term.

So, that's what I've done in the past.  This term, I'm going to try something different.  Inspired in part by Karl Fogel's <a href="http://www.producingoss.com"><cite>Producing Open Source Software</cite></a>, I'm going to ask students to prepare some combination of the following:
<ol>
  <li>An attractive home page, with a two-sentence mission statement and a few paragraphs or bullet lists to help newcomers orient themselves.</li>
  <li>An FAQ.</li>
  <li>An architectural overview, including block diagrams of the major components and a walkthrough of the processing cycle.</li>
  <li>An installation guide.</li>
  <li>An evaluation similar to those that have been included in previous terms' reports.</li>
</ol>
All but the last will be written as DrProject wiki pages, so that the next team can pick up right where their predecessors left off.  I hope this will give students a better feeling for what it would be like to work on a real long-lived project.

I'll close with a few quotes from Fogel's book:
<blockquote>…many projects don't bother to standardize their installation procedures until very late int he game, telling themselves they can do it at any time: <em>"We'll sort all that stuff out when the code is closer to being ready."</em>  What they don't realize is that by putting off the boring work of finishing the build and installation procedures, they are actually makingg the code take longer to get ready…  Boring work with a high payoff should always be done early. (pg. 26)</blockquote>
<blockquote>The importance of a bug tracking system lies not only in its usefulness to developers, but in what it signifies for project observers.  For many people, an accessible bug database is one of the strongest signs that a project should be taken seriously. Furthermore, the higher the number of bugs in the database, the better the project looks.  This might seem counterintuitive, but remember that the number of bugs recorded really depends on three things: the absolute number of bugs present in the software, the number of users using the software, and the convenience with which those users can register new bugs.  Of these three factors, the latter two are more significant than the first.  (pg. 26)</blockquote>
<blockquote>The ability to write clearly is perhaps the most important skill one can have in an open source environment.  In the long run it matters more than programming talent.  A great programmer with lousy communication skills can only get one thing done at a time, and even then may have trouble convincing others to pay attention.  But a lousy programmer with good communication skills can coordinate and persuade many people to do many different things, and thereby have a significant effect on a project's direction and momentum. (pg. 121)</blockquote>
