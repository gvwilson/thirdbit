---
title: "A Language for Teaching"
date: 2022-05-08
---

I'm hoping to send *[Software Design by Example][sdxjs]* to the publisher
by the end of this month,
and it has me thinking once again about
what a programming language designed for teaching ought to look like.
Here's one request:

> Built-in support for incremental exposition of code.

Most good books on programming interleave exposition and code
in ways that most languages don't directly support.
For example,
authors commonly want to write something like this
to give readers a roadmap for what's coming next:

```python
class Grid:
    …constants…

    def __init__(self, size):
        …set up…

    def fill(self, value):
        …fill entire grid with value…

    def adjacent(self, x, y):
        …return neighbors of (x, y)…
```

They then want to fill in those markers one at a time
further down the page or a few pages later:

```python
    def fill(self, value):
        for i in range(self.size):
	    for j in range(self.size):
	        self.cells[i, j] = EMPTY
```

I don't know any programming language that allows me to write this as shown.
Some "simple" text processing will allow me to write something like this in my source file:

```python
class Grid:

    ## [+fill]
    def fill(self, value):
        ## [-fill "fill entire grid with value"]
        for i in range(self.size):
	    for j in range(self.size):
	        self.cells[i, j] = EMPTY
        ## [-fill]
    ## [+fill]
```

and then slice the marked regions to produce the two versions shown above,
but having used (and built) several such systems,
I keep wondering why we don't just add this to the language itself.
[Literate programming][lp] promised this,
and while I was a zealous user for a couple of years in the late 1980s,
bolting LP onto pre-existing languages proved too clunky to catch on.
And yes,
there are tricks like [the Blank Maneuver][blank]
and tools like [jdc][jdc] for the Jupyter notebook,
but the former confuses novices ("Wait, you're deriving a class from itself?")
and the latter doesn't support forward markers in the original definition
to show where the later code is going to go.

This issue may seem pretty esoteric—after all,
most programmers don't write books—but it highlights two larger points.
The first is that most programmers *do* have to explain the work at some point,
and there's precious little in-language support for doing that.
The second point is that languages don't have any other support for incremental exposition either.
For example,
every textbook has diagrams,
but you can't put those in your source code:
Jupyter notebooks and R Markdown files can show you the plots produced by your code *in situ*,
but they won't let you draw things by hand.

So here's my suggestion for an enterprising graduate student who wants to change the world:
pick half a dozen books on programming
and go through them to create a catalog of explanatory techniques.
Once you have that,
extend your catalog by looking at slide decks and videos of whiteboard talks,
and then design a little language and editor with built-in support for the top N techniques:
really built-in,
not wedged into specially-formatted comments or requiring extra compilation steps
to see what readers are going to see.
The language itself could be as small as [Quorum][quorum], [Hedy][hedy], or [Lox][lox]:
it's just there to give users something to explain.

I often ask people what they would work on if they could work on anything.
Variations of this idea have been on my list for two decades;
I don't think I have enough years left to see it through myself,
but I'd be happy to chat with anyone who wants to take it on.

[blank]: https://github.com/jupyter/notebook/issues/1243#issuecomment-369753964
[hedy]: https://www.hedycode.com/
[jdc]: https://alexhagen.github.io/jdc/
[lox]: https://craftinginterpreters.com/the-lox-language.html
[lp]: https://en.wikipedia.org/wiki/Literate_programming
[quorum]: https://quorumlanguage.com/
[sdxjs]: https://third-bit.com/sdxjs/index.html
