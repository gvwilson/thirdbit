---
title: Analyzing the Simulation
date: 2025-11-24
---

[Yesterday's post][multiple-stages] added a second stage to the simulation,
and made a prediction about where work would pile up.
Today,
we're going to check whether that prediction is correct.
As a reminder,
our system is:

```
+----------------+    +-----------+    +------------+    +------------+    +---------+
| task generator | -> | dev queue | -> | developers | -> | test queue | -> | testers |
+----------------+    +-----------+    +------------+    +------------+    +---------+
```

Tasks arrive every 2.0 timesteps.
It takes each of our two developers an average of 5.5 timesteps to complete a task,
while each of our three testers needs an average of 4.5 timesteps to test the result.
This means that developers should complete one task every 2.75 timesteps,
and testers should be able to complete one every 1.5 timesteps.
We should therefore see work piling up in the development queue,
while the test queue should be more or less empty most of the time.

## Yup

It only takes a few lines of code
to produce time-series line chart using [Polars][polars] and [Plotly Express][plotly-express]:

```python
import sys

import polars as pl
import plotly.express as px


assert len(sys.argv) == 3, "usage: analyze.py csvfile plotfile"
df = pl.read_csv(sys.argv[1]) \
       .filter((pl.col("kind") == "dev_queue") | (pl.col("kind") == "test_queue"))
fig = px.line(df, x="time", y="count", color="kind")
fig.write_image(sys.argv[2])
```

Sure enough,
the queue of tasks waiting for a developer's attention grows and grows,
while tasks only wait occasionally (and briefly) for testing:

<div class="center">
  <img src="@root/files/2025/11/24/queues.svg" alt="time-series chart of queue lengths">
</div>

A little bit more analysis confirms that yes,
our testers are spending a lot of their time waiting for work
while our developers are busy nearly 100% of the time:

<div class="center">
  <img src="@root/files/2025/11/24/times.svg" alt="time-series chart of developer and tester time">
</div>

## Little's Law

One of the most useful results from queueing theory is
a generalization of the quick-and-dirty math we did at the start of this post
that predicted where jobs would pile up.
[Little's Law][littles-law] states that L = λW, where:

-   L is the average number of tasks in the system,
-   λ is the average arrival rate, and
-   W is the average time each task spends in the system.

For example,
if tasks arrive at a rate of λ = 2 per day
and each spends W = 5 days being worked on,
then on average L = 10 tasks are being worked on at any time.
If each worker does one task at a time, we can infer there are 10 workers.
Most software development teams don't track *any* of these three numbers;
I hope this series of posts is convincing you that it's worth doing.

[littles-law]: https://en.wikipedia.org/wiki/Little%27s_law
[multiple-stages]: @root/2025/11/23/simulating-multiple-stages/
[plotly-express]: https://plotly.com/python/plotly-express/
[polars]: https://pola.rs/
