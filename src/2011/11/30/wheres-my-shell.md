---
title: "Where's My Shell?"
date: 2011-11-30
---
My first programming language was PL/1. (Look it up if you need to, kid.) My second was Pascal, and then in the summer of 1982 I was introduced to two more: C, and the Unix shell. I realized that C was a programming language right away, mostly because that's what people said it was.  It took me longer to realize that the shell was also a programming language; I still remember the first time the sys admin responsible for our VAX 11/780 wrote a 'for' loop on the command line to try my program for each of several input files.

But now I'm programming on the web, which means I'm writing Javascript. OK, that's the equivalent of C: full of traps for the unwary, but able to do quite a bit once you get your head around it.  What I want to know is, where's my shell?  Where's the tool that's not quite as expressive (try manipulating tree-shaped data in the Bourne shell), and not as fast, but lets me do with two or three commands what would take half an hour to code and debug at the base level?

JQuery isn't what I'm looking for (though I'm very, very grateful that it exists). JQuery isn't a watertight layer of abstraction above Javascript: it's <a href="http://en.wikipedia.org/wiki/Leaky_abstraction">leaky</a>, in the sense that users still have to pay attention to Javascript-y things.  ("Wait, I forgot to say 'var'…")  <a href="http://jashkenas.github.com/coffee-script/">CoffeeScript</a> and other compile-to-JS languages are leaky too, but the shell is as close to being leak-free as any abstraction layer I can think of. In almost 30 years of nearly constant use, I've almost never had to think at the C level in order to debug a problem at the shell script level [1].

So what would a shell-like tool for in-browser programming look like? Well, I think it would look something like Microsoft PowerShell. There'd be lots of more-or-less orthogonal tools, each of which did one thing, but instead of communicating via streams of text, they'd send one another streams of objects. Those tools would probably be written in Javascript, and the shell might be as well (just as bash and its ilk are written in C), but users wouldn't see that.  What they <em>would</em> see is that they could package combinations of tools into scripts that could then be used as tools in their own right. The syntax for simple operations would be much simpler than that of Javascript, at the cost of some expressive power, but that's OK: 80/20 splits are a good thing.

And hey, it would give us a chance to choose command names that are more mnemonic than 'ls' and 'mv'… :-)

[1] And the times I did were my own fault, because one of the components in my pipe was a program I'd written myself, which didn't fork properly, and—never mind, it's not important.
