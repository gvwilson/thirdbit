---
date: 2009-08-02
original: swc
title: Next Steps
---
<p>It's clear from Friday's end-of-course review that the course needs shaking up. Before that starts, though, there's a higher-level question to answer: should the course notes be converted to a wiki to encourage contributions from others? It was always my hope that other people would contribute material, but in four years, only five ever have; perhaps wikification would change that.</p>
<p>Right now, the notes are stored as HTML pages in a Subversion repository and compiled by a little Python script to resolve cross-references, insert code samples, and so on. The advantages of this approach are:</p>
<ol>
<li>People can work locally and push coordinated changes when ready.</li>
<li>Slide format can be skinned by changing a flag in the Makefile to select different CSS. (For example, I'm still hoping to get <a href="http://meyerweb.com/eric/tools/s5/">S5</a> or <a href="http://www.netzgesta.de/S5/">S5R</a> working.)</li>
<li>The build step can also insert code fragments, ensure that bibliography references resolve, etc.</li>
</ol>
<p>Advantages of a wiki are:</p>
<ol>
<li>Easier collaboration: people can make small fixes in place without doing an "svn checkout" or running Make.</li>
</ol>
<p>As a programmer, the first three weigh heavier in my mind than the last one, but again, only five people have contributed material in four years, which isn't sustainable. What do you think?  Would switching to a wiki make you more likely to add material or not?</p>
