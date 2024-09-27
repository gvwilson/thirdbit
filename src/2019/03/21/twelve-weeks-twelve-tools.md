---
date: 2019-03-21
title: "Twelve Weeks, Twelve Tools"
---

Suppose you have a group of junior developers
who have built moderately complicated web applications using [Express](https://expressjs.org/)
and [React](https://reactjs.org/),
but don't really understand how their tools work.
Suppose further that they want to learn,
both because they're curious
and because it would help improve their software design skills.
Finally,
suppose they have six hours a week for twelve weeks
in which to build simplified versions of a set of basic tools.
What would you have them build?
My list would be:

1.  [Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
    to make sure that they really understand callbacks and exception handling.
1.  A documentation generator like [JSDoc](http://usejsdoc.org/)
    so that they learn to think about code as data.
1.  A style checker like [JSLint](https://www.jslint.com/)
    to drive that lesson home.
1.  A function-level profiler that manipulated a program's [AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
    instead of just walking it.
1.  A module loader
    to help them understand how large programs are actually assembled.
1.  A unit testing framework like [Jest](https://jestjs.io/)
    that includes mocking
    (again, to help them understand that code is data).
1.  A text editor so that they'll have a better grasp of what theirs can do.
    (In my experience, most people only use a fraction of their editor's power.)
1.  A smart backup tool that stores compressed files indexed by hashes
    (which is the core of how [Git](https://git-scm.com/) works).
1.  An HTTP server—basically a stripped-down [Express](https://expressjs.org/).
1.  A text-only web browser like [Lynx](https://lynx.invisible-island.net/)
    to help them understand how a DOM tree in memory becomes positioned text on a screen.
    (It wouldn't handle CSS, but it *would* do simple tables.)
1.  An interactive command shell like [Bash](https://www.gnu.org/software/bash/)
    or [PowerShell](https://docs.microsoft.com/en-us/powershell/).
1.  A state management framework like [Redux](https://redux.js.org/)
    to show them how to manage concurrency without going mad.

And speaking of going mad,
you might think that I have at this point.
Building any one of the tools described above would be a big job for an experienced developer;
there's no way a junior could do it in just six hours.
The answer is that we would scale the project down to fit the time available.
A style checker that only checks variable names and the number of parameters per function
illustrates how such tools work
and is only a single page of code
on top of a parser like [Acorn](https://github.com/acornjs/acorn).
Similarly,
Mary Rose Cook's [Gitlet](http://gitlet.maryrosecook.com/docs/gitlet.html)
(which is truly beautiful) can't be rebuilt in just six hours,
but a hashing-based backup tools can be.

This idea is inspired by books like
*[The Unix Programming Environment](https://www.amazon.com/Unix-Programming-Environment-Prentice-Hall-Software/dp/013937681X/)*,
*[The Elements of Programming Style](https://www.amazon.com/Elements-Programming-Style-2nd/dp/0070342075/)*,
and *[Software Tools in Pascal](https://www.amazon.com/Software-Tools-Pascal-Brian-Kernighan/dp/0201103427/)*,
which taught my entire generation to think about programs as tools and code as data.
*[500 Lines or Less](http://aosabook.org/)* convinced me that it's possble and worthwhile;
if you have any pointers to prior art,
or thoughts about the kinds of tools that should be added and which ones could be removed to make room,
I'd enjoy hearing from you.
