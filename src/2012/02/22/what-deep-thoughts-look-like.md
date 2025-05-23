---
date: 2012-02-22
original: swc
title: What Deep Thoughts Look Like
---
<p>Before writing yesterday's post about assessment, I should have explained what I mean by"fundamental concepts".  I'll start with Lewis Epstein's wonderful book <a href="http://www.amazon.com/Thinking-Physics-Lewis-C-Epstein/dp/0935218017"><em>Thinking Physics</em></a>:</p>
<p><img src="@root/files/2012/02/thinking-physics.jpg" class="centered"></p>
<p>Here's a typical problem from the book. Put a block of ice in a bathtub, then fill the bathtub to the brim with water, so that the block is floating freely. When the ice melts, will the water level go up (causing a spill), go down, or stay the same? Hm… well, the ice displaces its own weight of water, so when it melts, it exactly fills the "hole" it made, so the water level stays the same.</p>
<p>Now let's try something a bit more complicated. Put the same block of ice in the bathtub, but put an iron weight on top of it, and <em>then</em> fill the tub to the brim. Now what happens when the ice melts? Does the water level go up, go down, or stay the same? Epstein would say that if you can answer questions like that, then you can think physically. It isn't about calculation–as with Dan Meyer's "<a href="http://blog.mrmeyer.com/?p=12962">Joulies</a>", it's about understanding principles and following them through to conclusions.</p>
<p>The real aim of Software Carpentry is to teach scientists to think like that about computing. We want people to understand the principles:</p>
<ul>
<li>model-view separation</li>
<li>human-readable vs. machine-readable data</li>
<li>copying vs. aliasing</li>
<li>state machines</li>
<li>different models of computation (imperative, functional, reactive, declarative)</li>
<li>interface vs. implementation</li>
<li>the complementarity of algorithms and data structures</li>
<li>code as data (and data as code)</li>
</ul>
<p>The Unix shell, Python, SQL, regular expressions, and what not are how we hook people ("Hey look, something useful") and how we get these principles across (as with most big ideas, any direct description is either incomprehensible or banal). However, these principles aren't natural laws in the way as F=ma and the Second Law of Thermodynamics–if you compare them to the principles I listed a month ago, there's overlap, but the lists aren't the same. So:</p>
<ol>
<li>What <em>is</em> the best way (or a good, stable way) to carve up this intellectual space?</li>
<li>How do we tell what a particular person actually understands?</li>
</ol>
<p>"Write this program" is <em>not</em> an answer to the second problem–as many studies have shown, people can solve routine problems by rote without really understanding what they're doing. (This is the starting point for Eric Mazur's work on peer instruction, and the reason so many of us are so skeptical about things like the Khan Academy.)</p>
<p>Can we just teach the tools (for some value of "just") and let the big ideas sort themselves out? The answer is clearly "yes", because that's what I did from 1998 to 2007. Does it work? I think the answer is "only partially":  some people generalize from specifics to principles correctly on their own, but many either don't do it at all, do it incompletely, or do it incorrectly. And does it matter? I think so: I think that if we want scientists (or anyone else) to use computing on their own, for their own ends, they need to be able to step past what we've shown them with good odds of success, and that certainly requires understanding "why" as well as "what".</p>
