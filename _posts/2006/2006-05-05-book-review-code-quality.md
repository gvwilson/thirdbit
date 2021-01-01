---
title: "Book Review: Code Quality"
date: 2006-05-05 13:32:16
year: 2006
---
When Diomidis Spinellis's first book, Code Reading, came out in 2003, I said that it didn't matter whether you were still in high school, or had been programming for 30 years---it would teach you things you really needed to know.  Well, guess what?  The second one is even better.

Code Quality picks up where Code Reading left off.  Instead of explaining how to find your way around in large projects, it tells you how to judge the quality of what you're looking at.  Spinellis breaks this down into seven categories: reliability, security, time performance, space performance, portability, maintainability, and floating-point arithmetic.  Each gets a chapter of its own; each chapter draws dozens of examples from well-known open source projects, such as NetBSD, Perl, ACE, and Apache; and each example makes its point clearly and irrefutably.

Flip it open at random.  Page 414 dissects the sin of code duplication; the accompanying diagram shows how many hundreds of lines of code have been copied and pasted in the Catalina class loader. Page 279 compares the number of instructions required to call a virtual method with the number required to inline the same operation, then goes on to explain why such simple comparisons can be misleading. Flip back, and page 432 is the start of a 19-page discussion of testability.

Like its predecessor, Code Quality is a bit dry---I've read half a chapter at a time for two weeks---and very Unix-centric. Those are minor---nay, miniscule---complaints, though: the book ought to be required reading in every undergraduate software engineering program, and everything it covers should be on every professional developer's check-list.

<hr />Diomidis Spinellis: Code Quality: The Open Source Perspective.  Addison-Wesley, 2006, 608 pages, 0321166078, $54.99.
