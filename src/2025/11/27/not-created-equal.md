---
title: Not Created Equal
date: 2025-11-27
---

[Yesterday's post][malice] pointed out that
it can be hard to distinguish cause and effect from random variation.
One way to tell them apart is to vary the simulation parameters systematically
to see when various phenomena appear and disappear.
For example,
suppose we modify the simulation to account for the fact that
not all tasks are created equal.
Some bugs and features have higher priority than others,
and our team will generally work on more important items before they work on less important ones.

Alongside the `Store` we have been using to model our work queue,
[SimPy][simpy] offers a `PriorityStore` that keeps items sorted in priority order.
(The lower the item's score, the higher its priority.)
Let's modify the `Simulation` class to make the development and testing queues priority stores:

```python
class Simulation:

    def __init__(self, params):
        self.params = params
        self.env = simpy.Environment()
        self.dev_queue = simpy.PriorityStore(self.env)
        self.test_queue = simpy.PriorityStore(self.env)
        self.queue_log = []
```

and then add a new parameter `task_priorities`
whose value is a list of probabilities:

```python
PARAMS = {
    …previous code…
    "task_priorities": [0.1, 0.3, 0.6],
}
```

The list shown above tells us that there's a 10% chance of a new task having priority 0,
a 30% chance of it having priority 1,
and a 60% chance of it having priority 2.
When we create a task,
we assign it a priority at random with these weights:

```python
    def task_priority(self):
        return random.choices(
            list(range(len(self.params["task_priorities"]))),
            weights=self.params["task_priorities"],
            k=1
        )[0]
```

(We need the `[0]` at the end because `random.choices` always returns a list of choices,
even when we tell it we only want one value.)
Finally,
when we're adding a new task to the development queue
we wrap it in a `PriorityItem`
to pair the task with its priority:

```python
    def generate(sim):

        while True:
            yield sim.timeout(sim.task_arrival())
            task = Task(sim)
            yield sim.dev_queue.put(simpy.PriorityItem(task["priority"], task))
```

<div class="row">
  <div class="col-6 center">
    <img src="@root/files/2025/11/27/queues-136.svg" alt="10/30/60" width="90%">
    <br>
    Queue lengths: 10/30/60
  </div>
  <div class="col-6 center">
    <img src="@root/files/2025/11/27/queues-334.svg" alt="30/30/40" width="90%">
    <br>
    Queue lengths: 30/30/40
  </div>
</div>
<div class="row">
  <div class="col-6 center">
    <img src="@root/files/2025/11/27/queues-433.svg" alt="40/30/30" width="90%">
    <br>
    Queue lengths: 40/30/30
  </div>
  <div class="col-6 center">
    <img src="@root/files/2025/11/27/queues-442.svg" alt="40/40/20" width="90%">
    <br>
    Queue lengths: 40/40/20
  </div>
</div>

The top (green) line in these four charts is the number of priority-2 tasks
waiting in the development queue.
It grows steadily because developers are basically busy at all times with higher-priority tasks;
it's only when 80% or more of tasks are higher priority that
we start to see a backlog of priority-1 tasks build up.
I don't know if I expected this or not,
but I certainly *didn't* expect that the testers would always be able to keep up
with tasks of all priorities.

These curves look familiar to me.
In my previous role at [Plotly][plotly],
I was responsible for managing the backlog of bug reports and feature requests
for the open source libraries.
When I started in April 2025,
nobody had gone through them for several years;
over that summer,
I cleared out enough stale and duplicated items
to get the three main repositories from about 7000 issues down to about 1700.
I then watched as the number grew slowly but steadily over the next twelve months.
Everyone on the team was working hard,
but if your library, tool, or application is useful,
there will *always* be more work to do than people to do it.
The only "solution" is to be ruthless about labeling
so that you don't get demoralized.

[malice]: @root/2025/11/26/malice-and-randomness/
[plotly]: https://plot.ly/
[simpy]: https://simpy.readthedocs.io/
