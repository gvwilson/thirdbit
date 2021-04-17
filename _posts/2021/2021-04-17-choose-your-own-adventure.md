---
title: "Choose Your Own Adventure"
date: 2021-04-17
year: 2021
---

[Julia Evans](https://jvns.ca/) recently posted a description of the
["choose your own adventure" network debugging tutorials](https://jvns.ca/blog/2021/04/16/notes-on-debugging-puzzles/)
that she has been creating with [Twine](https://twinery.org/).
It's a very cool idea,
and a very welcome innovation:
I think we're all getting a bit tired of "read these paragraphs/watch this video and now do this auto-graded drill exercise".
If you're a CS education grad student in search of a cool project,
you could do worse than building a plugin for Scratch or VS Code
that enabled people to choose their own debugging adventure
*within their actual programming environment*.
(This is not the same as building [a tool for authoring Twine](https://marketplace.visualstudio.com/items?itemName=cyrusfirheir.twee3-language-tools),
though I imagine the former could use the latter.)

For example,
one [passage](http://ww.twinery.org/cookbook/terms/terms_passages.html) could give the learner the option
"set a breakpoint on line 26".
Instead of clicking on a link directly to take that action,
the learner would actually set a breakpoint;
the IDE plugin would detect and verify that action and move to the next passage,
or put up an [I'm sorry Dave](https://www.youtube.com/watch?v=ARJ8cAGm6JE) message
if the user tried to do something unanticipated.

I can imagine a boatload of studies someone could do with a tool like this.
I can also imagine something similar for teaching people how to build sophisticated SQL queries
or tidyverse pipelines step by step.
If you know of something like this, or are working on it,
I'd [enjoy hearing from you](mailto:gvwilson@third-bit.com).
