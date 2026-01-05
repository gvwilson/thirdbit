---
title: Next Steps for Simulation
date: 2026-01-05
---

I've filed [a few issues][issues]
in the [GitHub repository][repo]
for my [discrete event simulation][sim] of a small software development team
in order to map out future work.
The goal is to move away from what [Cat Hicks][hicks] calls
the "brains in jars" conception of programmers by including things like this:

-   [Rushing work][issue-rush] should increase the chance that re-work will be needed.
-   If programmers don't ever get a break, they [burn out][issue-burnout],
    which increases both their bug rate and the time needed to do the next task.
-   Too many meetings slows things down,
    but [too few meetings][issue-meetings] increases the chance of re-work being needed
    because of faulty or absent communication.

In order to implement these,
though,
I'll need a way to simulate activities that multiple people are working on at the same time.
This would be easy to do if all but the last person to join the activity
sat idle waiting for it to start,
but that's not realistic.
I could instead model it as a multi-person interrupt,
but [interrupts are hard][interrupts].
If you have enough experience with [SimPy][simpy] to offer examples,
I'd be grateful.
And if you're a professor looking for capstone projects for students,
please give me a shout:
I think that a discrete event simulation framework based on `async`/`await` instead of `yield`
would be just about the right size.

[hicks]: https://www.drcathicks.com/
[interrupts]: https://gvwilson.github.io/sim/interrupts/
[issue-burnout]: https://github.com/gvwilson/sim/issues/6
[issue-meetings]: https://github.com/gvwilson/sim/issues/8
[issue-rush]: https://github.com/gvwilson/sim/issues/5
[issues]: https://github.com/gvwilson/sim/issues
[repo]: https://github.com/gvwilson/sim
[sim]: https://gvwilson.github.io/sim/
[simpy]: https://simpy.readthedocs.io/
