---
title: "Review: Why Programs Fail"
date: 2005-12-24
---
2005 was an excellent year for books.  Not only were there a lot of good ones, some covered topics that hadn't been covered before (at least, not well or recently). Fogel's Producing Open Source Software, Doar's Practical Development Environments, Feathers' Working Effectively with Legacy Code, Thompson and Chase's Software Vulnerability Guide…

…and now Zeller's Why Programs Fail.  Zeller is the creator of DDD (http://www.gnu.org/software/ddd/), a graphical front end for the GNU debugger that uses box-and-arrow displays and charts (among other things) to show what programs are doing.  Now a professor at Saarland University in Germany, Zeller is still building and studying new tools to help developers figure out what's going wrong in their programs, where, and why.

This well-written, copiously-illustrated book is, in many ways, a status report from the front lines.  After setting the scene in Chapter 1, Zeller dives straight into the first debugging tool every developer should: a bug tracker.  He explains what good bug reports ought to contain, and how to manage them as their numbers grow.

He then gives us a chapter each on "Making Programs Fail", "Reproducing Problems", and "Simplifying Problems".  These chapters set the tone for the rest of the book: instead of high-level handwaving, we get a detailed look at what particular tools do, how, and (most importantly) why.  He describes, for example, how to decouple a program from external components, and looks at the pro's and con's of replay debugging.  Later, the chapter on simplification presents an automatic divide-and-conquer tool that can strip a test case down to its essentials.

Subsequent chapters are equally technical.  Chapter 7, for example, looks at how dependency analysis and program slicing can be used to isolate faults.  Chapter 8 discusses both interactive debuggers and logging frameworks; Chapter 11 looks at automatic anomaly detectors that compare execution traces from successful and failing tests, and Chapter 14 discusses cause-effect chains and backward reasoning tools like IGOR.

There are a lot of things to like in this book: the clarity, the references, the "How To" markers and end-of-chapters summaries.  What I enjoyed most, though, was the feeling I got of watching over Zeller's shoulder as he sorts through the jumble of parts on his workbench, sorting things into categories and figuring out how they all fit together.  Most of us spend more time trying to figure code out than we do writing new code.  Despite that, debuggers have always been poor cousins to editors, compilers, and other development tools. If, ten years from now, they have caught up with their peers—if the new approaches that Zeller describes have matured enough to be taken for granted—I think much of the credit will go to this book.

<hr />Andreas Zeller: Why Programs Fail: A Guide to Systematic Debugging.  Morgan Kaufmann, 2006, 1558608664, 448 pages.
