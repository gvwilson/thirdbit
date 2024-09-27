---
title: "Tools"
date: 2020-10-21
---

A couple of days ago I tweeted:

> What tools do you use daily to build software that aren't on this list:
> text editor, version control, test runner, build manager, debugger, style checker, doc generator, package manager, issue tracker?

Answers included:

-   An IDE (which combines many of the tools listed above and below)
-   Pen and notebook
-   Stack Overflow and other Q&A sites for indirect collaboration
-   Search engine (see above)
-   Real-time collaboration tools (Slack, Zoom, …)
-   Asynchronous collaboration tools (a wiki, a mailing list, …)
-   Unix command-line tools (`find`, `grep`, home-grown scripts for scraping event logs)
-   Code reviewing system (usually not a separate tool, but built into whatever online software forge the team is using)
-   Continuous integration/continuous deployment
-   UI design/review tools like [Figma](https://www.figma.com/) or [Abstract](https://www.abstract.com/)
-   A [drawing tool](https://www.diagrams.net/)
-   File sync/backup tools (rsync, Dropbox) that *aren't* version control
-   [Linter](https://en.wikipedia.org/wiki/Lint_(software)) and [memory checker](https://valgrind.org/)
-   Code reformatter (often combined with the linter)
-   Compiler (oh yeah, people still used compiled languages…)
-   Coverage analyzer/profiler
-   Issue tracker (for threaded discussions as well as bugs)
-   Visual diff viewer
-   Model checker
-   Terminal multiplexer
-   Docker or other container/virtualization system (particularly for testing installations)
-   Package repository (because a package manager isn't much use without one)
-   Mutation tester
-   Databases (indirectly: the IDE keeps one for symbols and cross-references in programs, for example)

It's quite a list, and I'm willing to make a few bets:

1.  Most developers pick these up on their own rather than being taught explicitly how to use them.
2.  As a result, most developers don't use most of these
    (where by "most" I mean Hanselman's [dark matter developers](https://www.hanselman.com/blog/dark-matter-developers-the-unseen-99),
    not just the minority who blog and tweet and answer questions on forums and go to meetups).
3.  Proficiency with these tools doesn't just correlate with productivity—it predicts it.
    In other words, if you teach people how to use these tools well, they will become more productive.

I further believe that:

1.  These tools aren't in the curriculum because the act of building software isn't considered part of computer science.
    Consider: to the best of my knowledge, no university in the English-speaking world offers a full semester course on debugging,
    and I've only ever seen [one decent textbook](https://www.spinellis.gr/debugging/) on the subject
    (compared to literally hundreds on writing compilers).
2.  They also aren't included in the curriculum because it's hard to create meaningful pen-and-paper exam questions for them.
3.  It *would* be possible to examine proficiency meaningfully by having students record their desktop while solving problems
    and then submitting the video.
    I believe this could be done without violating students' privacy,
    and that instructors could watch those videos at 5X or 10X and give meaningful feedback.

If you're a graduate student in software engineering or computing education and looking for a research topic,
I think this would be a good one—I'd be happy to chat any time if you want to brainstorm.

And following up on a suggestion from a friend,
I guesstimated the genders of the people who responded to my original tweet from their profiles.
This may not be accurate—studies have shown that
women often use neutral or male identities online to avoid harassment—but
the breakdown saddens me:

-   apparently male: 46
-   apparently female: 4
-   indeterminate or non-binary: 3

My estimate of the breakdown by race is undoubtedly no more accurate,
but looks even more one-sided :-(
