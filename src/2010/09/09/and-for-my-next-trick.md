---
date: 2010-09-09
original: swc
title: And For My Next Trick…
---
<p>One of the things people have voted right up to the top of our poll is reproducible research. The phrase means different things to different people, but part of it <em>must</em> be accurately tracking the provenance of every bit of data a scientist touches: where it came from, what was done to it, what was done to the results, and so on.  Once I've done the next episode of the Make lecture (on macros), I'd like to spend 10 minutes showing people how to do some of this by:</p>
<ul>
<li>embedding <a href="http://svnbook.red-bean.com/en/1.4/svn.advanced.props.special.keywords.html">Subversion keywords</a> like $Id:$ in original files, and</li>
<li>having tools copy those IDs, plus their own version numbers and settings, into the files they generate.</li>
</ul>
<p>For example, if the command line to generate summary-1.dat is:</p>
<p><code>stats.py --alpha 3.5 data-1-1.dat data-1-2.dat &gt; summary-1.dat</code></p>
<p>then data-1-1.dat should contain the line:</p>
<p><code> $Id: data-1-1.dat 138 2010-09-08 21:30:43Z cdarwin $</code></p>
<p>which Subversion will update each time the file is checked in. data-1-2.dat should have a similar line, as should stats.py; its should be embedded in a string so that it can be printed:</p>
<p><code># inside stats.py<br />
version = "$Id: stats.py 71 2010-08-17 08:13:17Z aturing $"</code></p>
<p>When stats.py runs, it copies its own ID string, its parameters (–alpha 3.5), and the ID strings of data-1-1.dat and data-1-2.dat into summary-1.dat. If some other program then processes summary-1.dat to create something else, it copies all of that information again, so that each file has a header with its complete ancestry. Yes, a proper <a href="http://openprovenance.org/">provenance tool</a> would be more robust and more flexible, but this technique will convey the idea, and implementing it is a good medium-sized exercise in Python.</p>
<p>Thoughts?</p>
<p>(And if you're interested in reproducible research, you'll probably enjoy a recently-published <a href="http://www.stanford.edu/~vcs/papers/RoundtableDeclaration2010.pdf">declaration of principles</a> drawn up by <a href="http://www.law.yale.edu/faculty/VStodden.htm">Victoria Stodden</a> and others.)</p>
