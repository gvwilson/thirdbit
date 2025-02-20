---
title: "Blaise Pascal's Shorter Letter"
date: 2005-02-05
---
<p>The French mathematician Blaise Pascal once wrote, "I have made this letter longer than usual, only because I have not had the time to make it shorter."  The 'letter' in question was a mathematical proof—Pascal was apologizing for not having taken the time to clean it up and make it more elegant.</p>

<p>Programmers often feel the same way about their programs.  It's not enough to make something work: we want it to be elegantly architected, and lightning fast.  We rarely get a chance to make it either, though; there's always something else that needs our attention.</p>

<p>I think that Extreme Programming's emphasis on continuous refactoring is partly a reaction to this.  There are lots of practical arguments in favor of <a href="http://blogs.pragprog.com/cgi-bin/pragdave.cgi/Practices/DebugWeeding.rdoc">pulling up weeds</a> every time you touch a piece of code (see Michael Feathers' <a href="http://www.amazon.com/exec/obidos/tg/detail/-/0131177052">Working Effectively with Legacy Code</a> for an excellent guide to how best to go about doing this), but I think that's all just <em>post hoc</em> rationalization.  The real reason XPers to refactor is that they're tired of shipping things that they're not proud of.</p>

<p>I'm almost as tired of shipping (and marking) things that are slower than they ought to be.  Tony Hoare might have been right when he said that, "Premature optimization is the root of all evil," but never optimizing—never thinking about performance, never refactoring in order to get your program's run-time from nineteen minutes to six seconds—is evil too.</p>

<p>The problem I face is that modern languages like Java and Python are harder to optimize than lower-level predecessors like Pascal and C.  You're further from the machine, which means you have to think harder to figure out what to change in order to achieve a particular effect.  I'm therefore very interested in work being done in the Python community (and elsewhere) on speeding up these languages.  Two particularly interesting approaches are specialization, as in <a href="http://www-128.ibm.com/developerworks/linux/library/l-psyco.html">Psyco</a>, and mixed-language programming, as in <a href="http://www-128.ibm.com/developerworks/linux/library/l-cppyrex.html">Pyrex</a>.  I haven't tried either on a real program yet, but once my students are finished their first round of changes to <a href="http://projects.edgewall.com/trac">Trac</a>, I'm going to see how much headway I can make with both.</p>
