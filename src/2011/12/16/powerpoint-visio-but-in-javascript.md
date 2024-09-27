---
title: "PowerPoint + Visio, but in Javascript?"
date: 2011-12-16
---
I've been complaining for a couple of years now about not being able to use HTML + Javascript as a replacement for PowerPoint. Yes, it's easy to put images and text beside one another in <a href="http://meyerweb.com/eric/tools/s5/">S5</a> or one of its many descendents, but I want to be able to draw on top of my text, just like I do on a whiteboard.

I can do put text and figures together in HTML5's <code>canvas</code> element, but (a) laying out the text is more difficult than it is in plain old HTML, and (b) as soon as someone resizes their browser, the textual and diagrammatic parts of my page won't line up any longer. Putting my text and drawing in <a href="http://html5.litten.com/using-multiple-html5-canvases-as-layers/">separate layers</a> seems like a step in the right direction; my question is, is there something out there that'll give me Visio-style anchoring as well? I.e., can I give an element in one layer a reference to something in another, then ask someone's Javascript library to lay out the referring element afresh whenever the referred-to element is redisplayed? It would be a nice complement to <a href="http://worrydream.com/Tangle/">Tangle</a>…
