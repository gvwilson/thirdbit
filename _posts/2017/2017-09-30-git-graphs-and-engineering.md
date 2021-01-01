---
title: "Git, Graphs, and Software Engineering"
date: 2017-09-30 05:00:00
year: 2017
---

A couple of years ago,
I complained that distributed version control still hadn't had its
<a href="{{site.github.url}}/2015/07/20/git-as-goto.html">structured revolution</a>.
After yet another discussion about how useful it is versus how hard it is to learn,
I have a proposal:

1. Download data from several thousand large projects on <a href="http://github.com">GitHub</a>.

2. Use your favorite statistical techniques to identify patterns in those repositories' branch-and-merge graphs.
   (To increase the likelihood of your proposal being funded,
   say that you're using machine learning rather than statistics.)

3. Select a small set of common subgraphs that account for a large fraction of everyday use.

4. Build a tool that provides those, *and only those*, to users.
   (For bonus marks, do a field study to see if it's actually easier for newcomers to learn
   using the methods that <a href="http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7999115">Stefik, Hannenberg, and others</a> have pioneered.)

5. Profit.  Well, fame.  OK, will you settle for having made the world a better place?

Step 3 is speculative:
I have no evidence that usage patterns fit a long tail distribution,
but I think most of us would be surprised if that was not true.
Step 4 is the one that will lead to shouting:
as happened when structured languages eliminated `goto` statements,
a minority of very vocal programmers will quote fringe cases
that can't be handled by your chosen set of simple constructs.
Everyone else
(the people Hanselman dubbed "<a href="https://www.hanselman.com/blog/DarkMatterDevelopersTheUnseen99.aspx">dark matter developers</a>")
will thank you for applying the scientific method to the design of something useful.
That was how one of my first professors defined "engineering",
and I think we'd all be better off if we did it.

*See also Perez De Rosso and Jackson's thought-provoking papers
"<a href="https://spderosso.github.io/onward13.pdf">What's Wrong With Git? A Conceptual Design Analysis</a>"
and
"<a href="https://spderosso.github.io/oopsla16.pdf">Purposes, Concepts, Misfits, and a Redesign of Git</a>".
If anyone reading this has time, interest, and graph analysis expertise,
please get in touch...*

*After reading some online discussion of this post,
I'd like to clarify that:*

1. *I'm not suggesting yet another set of aliases for Git: Pascal wasn't macros on top of Fortran, and I don't think a structured distributed VCS will be a layer on top of Git.  (I also believe that any such abstraction will leak early and leak often...)*

2. *I agree that a lot of how people use Git isn't captured in commit logs, but that's what we have easiest access to.*

3. *Yes, it would make a lot of sense to mine the histories of other distributed version control systems like Mercurial as well.*
