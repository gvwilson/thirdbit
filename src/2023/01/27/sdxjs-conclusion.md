---
title: "Software Design by Example: Conclusion"
date: 2023-01-27
---

We've come a long way since the start of this series of posts.
I hope that understanding how
[version control systems][sdxjs_version_control],
[unit testing frameworks][sdxjs_unit_test],
[style checkers][sdxjs_style_checker],
[module bundlers][sdxjs_module_bundler],
and [debuggers][sdxjs_debugger] work
will help you use them better.
And as [I wrote four weeks ago][sdxjs_introduction_post],
I hope that understanding their designs
will help you make things that are elegant as well as useful.

But I want this post to be a beginning, not an ending.
My examples are almost all command-line applications;
I would love to see a second volume that took apart front-end tools and distributed applications,
but don't know enough to write it.
I do,
however,
have a lot of experience [editing][bib],
so if you'd like to contribute a chapter to a collection that described
working models of editors, message queues, databases, and the like,
please get in touch.

I would also enjoy hearing from anyone who is using this material in class.
What *didn't* make sense?
Are the exercises comprehensible and at the right level?
Where are more diagrams needed?
I'm always happy to do a guest lecture in exchange for feedback…

Finally,
I've spent 40 years building things out of bits.
None of my code was ever widely used,
but I'm quite proud of how well some of it was made.
I hope that one day we'll have a vocabulary for talking about that—about
[what it means for software to be "beautiful"][bicycle].
Until then:

<div align="center">
  <p>
    Start where you are
    <br>
    Use what you have
    <br>
    Help who you can
  </p>
</div>

<a href="@root/sdxjs/"><img src="@root/sdxjs/sdxjs-cover.png" alt="Cover of 'Software Design by Example'" width="40%" class="centered"></a>

[bicycle]: @root/2017/12/17/consider-the-bicycle/
[bib]: @root/bib/
[sdxjs_introduction_post]: @root/2023/01/01/sdxjs-introduction/
[sdxjs_version_control]: @root/sdxjs/file-backup/
[sdxjs_unit_test]: @root/sdxjs/unit-test/
[sdxjs_style_checker]: @root/sdxjs/style-checker/
[sdxjs_module_bundler]: @root/sdxjs/module-bundler/
[sdxjs_debugger]: @root/sdxjs/debugger/
