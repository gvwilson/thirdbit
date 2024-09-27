---
date: 2012-04-18
original: swc
title: Behind the Scenes (or, the Ethics of Cultivating Discontent)
---
<p>A lot goes on behind the scenes here at software-carpentry.org:</p>
<ol>
<li><em>The site itself</em> is WordPress with a partly-customized theme. We use the blog for topics like this and pages (over a hundred of them) for lecture topics. We used to use Trac to manage work items, but nobody kept it up-to-date; these days, we use a WordPress to-do list plugin for the same purpose, and with as little result.</li>
<li><em>Our videos</em> are hosted on YouTube–we used to store them locally, but performance improved a lot when we offloaded.</li>
<li>We manage our <em>mailing lists</em> and <em>version control repositories</em> through the Dreamhost control panel, which actually delegates mailing list management to Mailman.</li>
<li>The <em>calendar</em> and <em>map</em> are hosted by Google.</li>
<li>We do <em>event registration</em> through EventBrite.</li>
<li>We currently use BlueJeans and Skype for <em>web conferencing</em>, but it's been plagued with both technical and social difficulties: people need to have the right Skype client for their OS, and there are the usual problems with unmuted microphones, unintelligible audio, feedback loops, and so on. Forget flying cars: I'll believe the future has arrived when we can make <em>this</em> work…</li>
</ol>
<p>This analysis leaves me feeling a bit conflicted. When I think about what we should teach researchers about the web, I have three requirements:</p>
<ol>
<li>They should be able to build solutions to problems they actually have.</li>
<li>They <em>shouldn't</em> create egregious security holes.</li>
<li>They should be able to debug things on their own when they go wrong.</li>
</ol>
<p>Since people can only debug things they understand [1], #3 depends on them understanding how the web works. One test of that is whether they recognize that they shouldn't have to log in and out of different sites in order to move information around manually. But if we don't have a solution to that problem (yet), are we really doing them a favor by pointing out that it actually doesn't have to hurt this much?</p>
<p>[1] Tweaking code more or less randomly until it appears to work doesn't count as "debugging" in my book.</p>
