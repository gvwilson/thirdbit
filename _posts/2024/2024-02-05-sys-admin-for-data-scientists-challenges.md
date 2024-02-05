---
date: 2024-02-05
year: 2024
title: "Challenges Designing System Administration for Data Scientists"
---

I've started outlining a lesson on system administration for data scientists,
and it's going to be harder to build than the [SQL tutorial][sql-tutorial] because:

1.  It needs to be horizontal rather than vertical,
    i.e., needs to go wide across many tools instead of deep into one.
    That means each tool will only get shallow coverage,
    but some tools aren't useful or compelling until learners reach a certain depth.

2.  Idempotent hands-on examples
    that learners can immediately re-start if they screw up their first attempt
    are much harder to set up.
    A bunch of Docker images might solve this,
    but (a) that means starting with Docker,
    which is *not* a natural place to start,
    and (b) that makes things less painful rather than painless.

3.  Some important topics are difficult or impossible to teach using only the learner's laptop
    and are tied to commercial services like AWS, Azure, or Google Cloud
    that are very different from each other.

On the bright side,
there seems to be rough consensus on what constitutes "system administration" for data scientists.
I figure it will take another few days to produce a rough concept map that I'm happy with;
after that,
I'll have to do a lot of reading to fill in gaps in my own knowledge
before I start creating examples.

Tangentially,
thinking about this has got me thinking once again
about the things that can be taught as a series of 5-minute examples
and things that can't.
I'd really like to take another run at
[a workshop on managing research software projects][mrsp],
but I don't think it can be taught this way.
Instead,
I think it wants to be
a series of half-hour lectures alternating with 15-minute exercises
like my [teaching workshop][teaching-workshop].
My [previous attempt][mrsp] to do this was a failure,
but if we can teach people how to teach,
I hope that we can teach them how to manage.
(What I should *actually* be doing is finishing the three stories for children that I'm supposedly working on
and revising a fourth,
but I find it harder every year to focus on things
that don't have nearly-immediate feedback.)

[mrsp]: {{'/mrsp/' | relative_url}}
[sql-tutorial]: https://gvwilson.github.io/sql-tutorial/
[teaching-workshop]: {{'/t3/' | relative_url}}
