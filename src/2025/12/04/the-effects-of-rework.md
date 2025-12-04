---
title: The Effects of Rework
date: 2025-12-04
---

Having [solved yesterday's bug][cancel],
we can get back to looking at the effect of re-work on throughput.
As a reminder,
our workflow looks like this:

```
+----------------+    +-----------+    +------------+    +------------+    +---------+
| task generator | -> | dev queue | -> | developers | -> | test queue | -> | testers |
+----------------+    +-----------+    +------------+    +------------+    +---------+
                            ^                                                   |
                            |                                                   |
                            +---------------------------------------------------+
```

The two parameters that affect re-work are `p_rework_needed`,
which is the probability that a tester is going to send a task back for more work,
and `p_rework_chosen`,
which is the probability that a developer will choose something from her re-work queue
rather than starting fresh work
when both are available.
The extreme cases are:

-   `p_rework_needed` = 0.0, meaning no tasks are ever sent back.
-   `p_rework_needed` = 1.0, meaning every task is always sent back.
    (Note that this means no task will ever be finished:
    instead,
    tasks will circulate endlesslesly between development and testing,
    and yes,
    sometimes it does feel like that happens in real life.)
-   `p_rework_chosen` = 0.0, in which case
    developers only re-do tasks when there is no new work queued up.
    (We know from previous simulations that there are almost always
    new tasks waiting to be started.)
-   `p_rework_chosen` = 1.0, in which case
    developers only start new tasks when nothing needs to be re-done.

Finally,
this version of the simulation always sends tasks back to
the developers who originally worked on them
rather than allowing the first available developer
to re-do someone else's work.

## Final States

The figure below shows the number of tasks in each of the five possible states
at the end of the simulation
as a function of `p_rework_needed` and `p_rework_chosen`:

<div class="center">
  <img src="@root/files/2025/12/04/states.svg" alt="final task states" width="90%">
</div>

As expected,
lots of tasks are in the `complete` state when there is never any need for re-work,
while none are when re-work is always needed.
This finding may seem obvious,
but this simple check uncovered a couple of bugs in the simulation.

A more interesting finding is that
how developers choose tasks doesn't seem to have much effect
on how many they get done:
while there is some variation,
the bars stay more or less the same height when we look at each row.

We can reach the same conclusion by looking at
the number of times tasks were developed and re-worked.
The sizes of the circles in the plots below reflect these counts:

<div class="row">
  <div class="col-6 center">
    <img src="@root/files/2025/12/04/n_dev.svg" alt="development count" width="90%">
  </div>
  <div class="col-6 center">
    <img src="@root/files/2025/12/04/n_rework.svg" alt="re-work count" width="90%">
  </div>
</div>

Again,
the probability of needing re-work has an obvious impact,
while the probability of choosing new work vs. re-work doesn't seem to.

[cancel]: @root/2025/12/03/you-have-to-cancel/
