---
date: 2019-03-12 11:05:00
year: 2019
title: "Reviewing Lessons"
---

I had a great discussion yesterday with a colleague about reviewing slides for lessons.
We're teaching a class together next week,
and while I'm happy waving my arms and telling stories,
he likes to put lots of meaningful graphics in front of learners,
just like cognitive science tells us to.

What we realized in discussion is that
it's easy and productive to review someone's papers or code asynchronously,
e.g.,
by commenting on a pull request or a draft document.
Howeer,
asynchronous review isn't nearly as helpful for slides
unless those slides are basically slabs of point-form notes
(which cognitive science tells us is a bad way to teach).
The difference,
we concluded,
is reading a paper or some code is a faithful simulation of how that material is meant to be consumed.
People read papers—that's why they exist—and computers read and execute code,
so reading and (mentally) executing it is an accurate re-creation of how it's meant to be used.

But slides aren't meant to be read:
they're meant to be *performed*.
Good slides take advantage of the fact that
[our brains have separate channels for visual and linguistic input](http://teachtogether.tech/en/load/#s:load-split-attention),
and that presenting correlated information through those channels simultaneously enhances learning.
If I can get everything out of reading your slides that I would get out of your lecture,
then either your slides or your lecture could be improved.
As a corollary,
if I can review your slides effectively without you performing them,
you are probably mis-using or under-using the medium.

Detailed speakers' notes can help, of course:
if the presentation's author writes a slide-by-slide script,
an attentive reader who is familiar with the subject
can probably reconstruct the performance in their head.
But that's asking the author to do a lot of extra work for the benefit of reviewers,
and in my experience,
the more effort that people put into that,
the more resistant they become to making changes
because of their sunk costs.

Versions 3 and 4 of the [Software Carpentry](http://software-carpentry.org) lessons were slides.
A few people contributed to them,
but pull requests didn't really start to arrive until we switched to the explanatory prose
they're made up of today.
At the time I thought it was because the file formats we were using made PRs difficult
(see [yesterday's mini-rant about version control]({{'/2019/03/10/the-tool-i-want/' | relative_url}})),
but now I'm wondering whether the real reason was that
I was asking people to review a song by reading the sheet music
instead of listening to it.
I'd be grateful for your thoughts...
