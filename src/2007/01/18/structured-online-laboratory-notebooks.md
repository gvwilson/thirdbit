---
title: "Structured Online Laboratory Notebooks"
date: 2007-01-18
---
I spent some time last week with a group of medical imaging researchers who manage their work with Excel.  They explained that it's almost ideal for their needs, since they can use cells to organize their experimental results, diagrams, code snippets, and whatever else they like in whatever free-form manner best suits the problem at hand.  Unlike a web browser, Excel can do simple calculations and re-draw their charts; unlike a database, they can merge cells to create irregular structures if that's what the problem calls for.

The two things they can't do are:
<ol>
  <li>Merge independent edits.  Excel uses a closed-source binary format, so all version control tools can do is say, "These two things are different."  (I've complained about this before.)</li>
  <li>Interact with their data over the web (more particularly, share live documents with colleagues).</li>
</ol>
A few years back, scientists in the US national labs were working on an <a href="http://collaboratory.emsl.pnl.gov">uber-tool</a> that would do all of this and more.  That effort is still going on, but (a) it seems to have slowed down, and (b) it's a big-hammer approach.  I'm wondering if there's a role here for an <a href="http://www.google.com/googlespreadsheets/tour1.html">in-browser spreadsheet</a> whose data format is diffable and mergeable.  It'd be useful for much more than laboratory science: course grades spring to mind, as do address lists and a host of other applications…  Anyone want to be rich, famous, and popular?
