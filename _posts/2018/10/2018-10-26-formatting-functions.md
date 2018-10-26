---
layout: post
date: 2018-10-26 02:15
title: "Formatting Functions"
---

I've written and edited a little over two million words of computer-related material in the last 35 years.
For much of that time I wrote `time()` to mean "the function whose name is `time`".
The empty parentheses aren't part of the name:
they're there to remind readers that this is a function.

I stopped doing this about ten years ago for three reasons:

1. Someone asked me, "Then shouldn't I write `numbers[]` when it's an array
   or `names{}` when it's a dictionary?

2. I discovered that some novice readers had trouble distinguishing between
   "the function called `time`" or "a call to `time` with no arguments",
   since I was writing both as `time()`.

3. I started writing more about functional programming,
   and even I found it confusing to figure out whether "pass `a()` to `b()`"  meant
   "pass the function `a` to the function `b`"
    or "pass the result of calling `a` to `b`"
    or "pass the result of calling `a` to the result of calling `b`"
    (all of which I wanted to do in the same section of one tutorial).

I realize that the `f()` notation is deeply ingrained and unlikely to change,
but I wonder if anyone has ever studied whether it leads to any more confusion
than parenthesis-free notation.
It's the kind of thing that educators refer to as
[pedagogical content knowledge](http://teachtogether.tech/en/pck/),
and I wish we had more of it.
