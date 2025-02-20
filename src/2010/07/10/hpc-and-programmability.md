---
date: 2010-07-10
original: swc
title: HPC and Programmability
---
<p>Via <a href="http://osl.iu.edu/~lums/">Andrew Lumsdaine</a>, a pointer to an interesting article in <a href="http://cacm.acm.org/"><em>Communications of the ACM</em></a> by Eugene Loh titled "<a href="http://cacm.acm.org/magazines/2010/7/95060-the-ideal-hpc-programming-language/fulltext">The Ideal HPC Programming Language</a>". A few key quotes:</p>
<blockquote><p>These programmability studies began with a focus on programming  languages, but the focus quickly shifted to other topics. Existing  languages–notably Fortran…–proved remarkably adequate. Programming challenges stem mostly  from other factors.</p></blockquote>
<blockquote><p>The DARPA HPCS program…sponsored the development of new programming  languages: Chapel from Cray, Fortress from Sun, and X10 from IBM.  Proponents of those languages would show early on how rewriting familiar  HPC benchmarks in the new languages could reduce source-code volume  substantially–tenfold reductions were not surprising–but rewriting these  benchmarks even in Fortran achieved similar source-code reductions and  corresponding improvements in expressivity.</p></blockquote>
<blockquote><p>In HPC, the mind-set is usually to program for performance rather than programmability even before establishing whether a  particular section of code is performance sensitive or not.</p></blockquote>
<blockquote><p>Repeating some of these…studies on larger HPC programs would be interesting. In particular, it would be  nice to move from self-contained programs that are small enough  for one person to have written…to larger pieces of software…</p></blockquote>
<p>The Cowichan Problems were designed to explore that last issue in an affordable way. If you're interested in helping us re-design them so that they better represent the full range of today's HPC applications, please let me know.</p>
