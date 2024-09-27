---
title: "I Want a Memory Diagram Generator"
date: 2022-12-04
---

Following up on last week's grumble about
[what I want for writing code examples in books](@root/2022/11/30/what-i-want-for-code-in-textbooks/),
I'd like to make another request.
I'm a big fan of Guo et al's [online program visualizer](https://pythontutor.com/),
which animates memory diagrams like the one below
as users single-step through code:

<img src="@root/files/2022/pythontutor.png" alt="PythonTutor screenshot" width="80%" class="centered">

I want a tool that will let me specify a program,
its inputs,
and a specific instant in its execution,
and will then run the program to that instant,
generate the memory diagram,
and save it in a scalable file format like SVG.
Specifying the point at which I want the diagram is the hard part:
"stop at line 36" isn't enough,
since I might want to stop at that line on the fourth call
or when the program is five levels deep in recursive calls.

What would specify an instant in a program's execution look like?
I'm a lousy UX designer,
so please don't take this proposal too seriously,
but I imagine something with two parts:

1.  A notation for specifying logical locations in source code
    similar to [DOM selectors](https://www.w3.org/TR/2020/SPSD-selectors-api-20201103/),
    [XPath](https://www.w3.org/TR/2017/REC-xpath-31-20170321/),
    or [JSONPath](https://datatracker.ietf.org/wg/jsonpath/about/).
    For example,
    `pokey.clusp.marther[3:5]`
    would be the third through fifth statements of the `marther` method
    in the `clusp` class
    of the `pokey` package.
    (I did warn you not to take my design too seriously…)

2.  A second notation that would build on the first to specify call chains,
    repetition counts,
    etc.,
    so that users could say, "This point the thirty-third time it's encountered,"
    or, "That point but only when the variable `nobble` is not null."
    (I did warn you…)

That tool would be tremendously valuable,
and would open the door to others:
I could,
for example,
specify a dozen such stopping points in a program
and a comment to display when each was encountered
in order to give readers a guided tour of a program's execution.
And if the whole thing came with a diagram diff tool
that would tell users when one or more diagrams had changed
with respect to earlier versions,
there'd be much less risk of code, diagrams, and descriptions getting out of sync.
I realize these tools would be a lot of work to build,
particularly if they were to be cross-language,
but the benefits would be enormous.
