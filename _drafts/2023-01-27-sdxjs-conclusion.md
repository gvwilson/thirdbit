---
title: "Software Design by Example: Conclusion"
date: 2023-01-27
year: 2023
---

We've come a long way since the start of this series of posts.
[Version control systems][sdxjs-version-control],
[unit testing frameworks][sdxjs-unit-test],
[style checkers][sdxjs-style-checker],
[module bundlers][sdxjs-module-bundler],
[debuggers][sdxjs-debugger]:
I hope that understanding how those tools work will help you use them better.
And as [I wrote four weeks ago][sdxjs-introduction-post],
the best way to learn how to design software is to look at examples,
so I hope that understanding why these tools are built the way they are
will help you make things that are elegant as well as useful.

But I want this post to be a beginning, not an ending.
My examples are almost all command-line applications;
I would love to see a second volume that took apart front-end tools and distributed applications,
but don't know enough to write it.
I do,
however,
have a fair bit of experience editing,
so if you'd like to contribute a chapter to a collection,
please get in touch.

I would also enjoy hearing from anyone who is using this material in class.
What *didn't* make sense?
Are the exercises comprehensible and at the right level?
Where are more diagrams needed?
I'm always happy to do a guest lecture in exchange for feedback…

Finally,
I have spent most of my life building things out of bits.
I don't think any of my code is still in widespread use,
but I'm still quite proud of some of it.
I hope that one day we'll have a vocabulary for talking about that—about
[what it means for software to be "beautiful"][bicycle]—and
if this book helps you see that,
then it was worth writing.

<div align="center">
  <img src="{{'/files/bib/sdxjs-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="40%" />
</div>

<div align="center">
  Start where you are
  <br/>
  Use what you have
  <br/>
  Help who you can
</div>

[bicycle]: {{'/2017/12/17/consider-the-bicycle/' | relative_url}
[sdxjs-introduction-post]: {{'/2023/01/01/sdxjs-introduction/' | relative_url}}
[sdxjs-version-control]: {{'/sdxjs/file-backup/' | relative_url}}
[sdxjs-unit-test]: {{'/sdxjs/unit-test/' | relative_url}}
[sdxjs-style-checker]: {{'/sdxjs/style-checker/' | relative_url}}
[sdxjs-module-bundler]: {{'/sdxjs/module-bundler/' | relative_url}}
[sdxjs-debugger]: {{'/sdxjs/debugger/' | relative_url}}
