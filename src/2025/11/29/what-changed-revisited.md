---
title: What Changed Revisited
date: 2025-11-29
---

Let's take another look at the log-scaled version of [yesterday's chart][what-changed]:

<div class="center">
  <img src="@root/files/2025/11/28/times-log.svg" alt="log-scale time plot" width="90%">
</div>

There hasn't been any turnover in the team or a major rewrite of the product,
so why has the number of bugs that take more than 100 hours to close
been creeping up slowly but steadily?
Luckily,
we have access to the source code of the simulation,
so we can get a definitive answer.
(Yes, this is cheating…)

The first difference is that
the development and testing queues are priority queues:

```python
class Simulation:

    def __init__(self, params):
        self.params = params
        self.env = simpy.Environment()
        self.dev_queue = simpy.PriorityStore(self.env)
        self.test_queue = simpy.PriorityStore(self.env)
```

We have also added constants to define two priority levels—remember,
a lower number is a higher priority:

```python
PRI_REWORK = 0
PRI_NEW = 1
```

We have also made a small but crucial change to
the class that simulates a tester:

```python
class Tester(Labeled):

    def work(self):
        while True:
            item = yield self.sim.test_queue.get()
            priority, task = item
            yield self.sim.timeout(task["test_time"])
            if self.sim.task_rework():
                self.sim.dev_queue.put(simpy.PriorityItem(PRI_REWORK, task))
```

The last two lines of `work` say,
"If testing reveals that this task needs to be re-done,
put it back in the development queue with high priority."
If you'll excuse a bit more ASCII art,
this change means that our simulation is now:

```
+----------------+    +-----------+    +------------+    +------------+    +---------+
| task generator | -> | dev queue | -> | developers | -> | test queue | -> | testers |
+----------------+    +-----------+    +------------+    +------------+    +---------+
                            ^                                                   |
                            |                                                   |
                            +---------------------------------------------------+
```

From quarter to quarter,
the probability of QA revealing that a task needs to be re-done
has gone from 0% to 50%.
As noted yesterday,
we see a corresponding decrease in the total number of tasks completed each quarter:

| quarter | number |
| ------: | -----: |
|       1 |   2222 |
|       2 |   1912 |
|       3 |   1525 |
|       4 |    993 |

What these numbers don't tell us is *why*.
Are our testers getting better at finding bugs?
Are our developers making more mistakes because they're burning out?
Or has there been some sort of change in how work is being tracked?
(0% rework in the first quarter seems suspicious…)
Once again,
data can draw our attention to things that need to be explained,
but we still have to find the explanation.
