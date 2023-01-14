---
title: "Another Use for Extensible Programming"
date: 2008-09-19 12:51:28
year: 2008
---
I've grumbled before about the fact that mass-market tools like Firefox and Microsoft Word allow people to mix pictures and text, but programmers' editors (including IDEs) do not.  My standard answer when people ask why I'd want that is, "So that I can put before and after pictures of data structures for methods, just like I would in a textbook."  Discussion about the <a href="http://www.djangoproject.com/">Django</a> port of DrProject has brought up another use case, though.  Suppose you need to initialize a set of objects for a test fixture, and their mutual reference graph contains cycles.  Using text, you have to do things like this:
<blockquote>left = Something(null)

right = Something(left)

left.setPartner(right)</blockquote>
It's non-declarative, it's error-prone, and worst of all, you have to relax the error-checking in classes so that they can be initialized in  states that you don't want them to be in the real program.

Now, wouldn't it be great if you could just <em>draw</em> what you want?  Imagine an editor that would let you create two circles (one for left, one for right) and join them up with arrows labeled "partner" to show the final state you wanted.  A combination of clever compilation and reflection could then stitch everything together for you.  What's even nicer, you wouldn't have to worry about how to bootstrap the fixture into a legal state.

Oh, but that's crazy talk, isn't it?  Non-ASCII content in programs?  Why, next you'll be wanting pictures in debuggers, too...
