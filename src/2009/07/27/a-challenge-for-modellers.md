---
title: "A Challenge for Modellers"
date: 2009-07-27
---
Like many software developers of a certain age, I had a brief love affair with UML in the 1990s. Pictures of programs—what a great way to communicate! In my case, it lasted about four months. I simply didn't find class diagrams helped me understand what was going on in my programs, or anyone else's.

I think I can finally explain why. Over the weekend I started reading Olsen's <a href="http://www.amazon.com/Design-Patterns-Ruby-Addison-Wesley-Professional/dp/0321490452"><em>Design Patterns in Ruby</em></a>, which is possibly the best introduction to design patterns I've ever read [1]. What I suddenly noticed, though, was how hard it would be to know which patterns the author was talking about if you blanked out the class names in the UML diagrams given with each chapter.

This is definitely <em>not</em> the case in other fields that rely on graphical notations. The logic gates making up a one-bit adder, for example, are unmistakable; the text around them speeds up understanding, but the meaning is in the diagram.

So here's an empirical test: draw UML diagrams representing various design patterns, but <em>don't label them</em>, and see how many people can tell which are which. Or analyze the natural language description of the design pattern and see how much of the information needed to understand how the pattern works is <em>not</em> present in the diagram. Yes, you can get some of that by adding a sequence diagram as well, but I'll bet that even the combination still needs to be explained in order to be comprehended.

And while we're on the subject: has anyone ever designed a programming language by starting with a catalog of design patterns and asking, "What do I need in order to make expressing these simple and obvious?"  If so, I'd be grateful for a pointer…

[1] There are several reasons Olsen's book is so good:
<ol>
  <li>He clearly likes the languages he's using (English and Ruby), and knows how to use both well.</li>
  <li>The classic Gang of Four patterns are much simpler to express in dynamic languages like Ruby than in modern Java or C++.</li>
  <li>We've learned a lot since the original Gang of Four book about how to teach patterns and in what order.</li>
</ol>
#1 is the most important, though; I hope he writes a Python version soon.
