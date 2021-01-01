---
title: "I'm Probably Wrong Again"
date: 2017-11-01 13:00:00
year: 2017
---

A couple of years ago,
I helped run a [Software Carpentry][swc] instructor training class in Florida.
Part-way through the second day,
one of the participants asked me if their team should use Python or R for a project.
Condensed,
my reply was that Python was a general-purpose language that had some good numerical libraries,
while R was "just" a statistical tool that people had started using for other things.

The workshop's host called me out for saying this,
and was right to do so.
Programmers sneer at one another's languages---Python at R,
Ruby at Perl,
Lisp at everyone and everyone at Visual Basic---and they're all wrong to do so.
[Some languages are easier for novices to learn than others][stefik],
but once you have reflection and garbage collection,
there's precious little evidence that the other differences matter.

Except.

Except I don't ever want to have to write a parser again.
Except I don't ever want to have to create quadtrees from scratch,
or decode PNGs,
or any of a hundred thousand other things.
I want *libraries*.
I want to be able to build on the work of a million other programmers
and know that if I make something useful I'll be able to give it back to them in turn.
I want debuggers and linters and a package manager
(though I'm resigned to the fact that I'll probably have several)
and I don't want to have to write any of them.

Which brings us to Javascript,
and more specifically, to [this tweet][original-tweet]:

> Has anyone built a replacement for Jekyll in JS that provides React-like syntax and semantics?

If you haven't run into [Jekyll][jekyll] yet,
it's the tool that [GitHub Pages][ghp] uses to transform templated Markdown and HTML
into pure HTML for display.
It's written in Ruby,
but is showing its age,
and it was only ever three quarters of a good idea.
While playing around with [React][react] earlier this year,
I came to enjoy its mostly-functional model.

A couple of people kindly pointed me at [Gatsby][gatsby],
but other reactions
ranged from "Oh my goodness" to "I feel like I don't know you any more"
and what I believe was an offer to open negotiations with my kidnappers.
They were all meant in fun,
but what I think they reveal is that everyone who isn't using Javascript is still underestimating it.
Yes,
its initial design left a lot to be desired
(like consistency, predictability, and comprehensibility),
but [ES6][es6] and [TypeScript][typescript] are a genuine pleasure to use,
and OMG have you seen the libraries?
Javascript has libraries for practically everything!
Or have you looked at how many really smart people are building support tools
and working really, really hard to make Javascript go fast?

I have a long history of being wrong.
(I actually [keep a list][mistakes].)
I'm probably wrong about this too,
but I'll bet you ten dollars that
[the most popular numerical programming language in 2027 will be a descendent of Javascript][numjs],
because like it or not,
Javascript is the one language every commercial developer needs to learn.
That means it is to programming what the Intel architecture has proven to be to microprocessors:
inevitable.

[es6]: http://es6-features.org/
[gatsby]: https://www.gatsbyjs.org/
[ghp]: https://pages.github.com/
[jekyll]: https://jekyllrb.com/
[mistakes]: http://third-bit.com/2015/12/06/just-keep-swimming.html
[numjs]: http://third-bit.com/2017/05/22/numerical-javascript.html
[original-tweet]: https://twitter.com/gvwilson/status/925714333392289793
[react]: https://reactjs.org/
[stefik]: http://neverworkintheory.org/2014/01/29/stefik-siebert-syntax.html
[swc]: https://software-carpentry.org
[typescript]: https://www.typescriptlang.org/
