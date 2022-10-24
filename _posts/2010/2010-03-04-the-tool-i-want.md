---
title: "The Tool I Want"
date: 2010-03-04 07:05:15
year: 2010
---
I want to make the next version of the <a href="https://software-carpentry.org">Software Carpentry</a> material more dynamic. I'm planning to use screencasts to show people how to use a debugger and other power tools, but I don't like screencasts for showing programming examples: the text is often hard to read (even when anti-aliased), and they're almost never accessible to the visually impaired.

What I'd like instead is a Javascript widget I can embed in a web page that will step forward and backward through a fixed piece of code and its output. This isn't the same thing as <a href="http://tryhaskell.org/">Try Haskell</a> and other "sandbox in a browser" tools that let people write and run arbitrary snippets of program.  Instead, I want to say, "Here's a piece of Python (or whatever), here are the pop-up comments I want to appear at various points in its execution, and here's the output I want displayed at other points."  In the browser, it would look like this:

<img title="browser-ide" src="{{'/files/2010/03/browser-ide.png' | relative_url}}" alt="browser-ide" width="393" height="173" />

(You can see why I'm not allowed to design user interfaces...) "Step Forward" and "Step Backward" don't actually execute code; instead, they replay a previously-recorded execution sequence and its textual output.  Whoever created that sequence can add explanatory notes (like the bubble shown) that appear and disappear as execution proceeds.

Three things are needed to make this happen:
<ol>
	<li>A desktop tool for recording and annotating the execution of small programs.</li>
	<li>A data format for storing those recordings and annotation.</li>
	<li>A Javascript widget for playing them back in the browser.</li>
</ol>
Ideally, this combination would also handle interactive interpreter sessions, in which the program appears as you go along, and output is interleaved with input.  If you know of something that already does this, I'd welcome a pointer; if you don't, and are looking for a really cool course project, please give me a shout.
