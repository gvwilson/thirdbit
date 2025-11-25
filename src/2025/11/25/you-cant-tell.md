---
title: You Can't Tell
date: 2025-11-25
---

[Yesterday's post][analyzing] checked our prediction
about where work would pile up.
As a reminder,
here are plots showing the lengths of the development and testing queues
and how much time developers and testers spend working and waiting:

<div class="row">
  <div class="col-6 center">
    <img src="@root/files/2025/11/24/queues.svg" alt="time-series chart of queue lengths" width="90%">
  </div>
  <div class="col-6 center">
    <img src="@root/files/2025/11/24/times.svg" alt="time-series chart of developer and tester time" width="90%">
  </div>
</div>

Let's change a single parameter and re-run the simulation.
We see a few jobs waiting in the testing queue more often,
and more importantly,
that testers are spending most of their time working instead of waiting:

<div class="row">
  <div class="col-6 center">
    <img src="@root/files/2025/11/25/two-testers-queues.svg" alt="time-series chart of queue lengths" width="90%">
  </div>
  <div class="col-6 center">
    <img src="@root/files/2025/11/25/two-testers-times.svg" alt="time-series chart of developer and tester time" width="90%">
  </div>
</div>

Here's the key question,
and the main point of this series of posts:

<div class="center" markdown="1">
*Can you tell from these graphs alone which parameter changed?*
</div>

The answer is "no".
It's clear that *something* has changed,
but our two-plot dashboard doesn't give us enough insight for us to know what.
In this case the answer is that we cut the number of testers on the team from 3 to 2
while leaving both developers in place.
Testing still takes an average of 4.5 timesteps,
while development takes an average of 5.5 timesteps,
so the developers still can't keep the testers busy all the time,
but *you can't tell this from these plots*.

Let's stick to two developers and two testers and make one more change.
The testers are now busy almost all the time,
and the testing queue always seems to have a backlog,
but that backlog doesn't appear to grow over time:

<div class="row">
  <div class="col-6 center">
    <img src="@root/files/2025/11/25/queues.svg" alt="time-series chart of queue lengths" width="90%">
  </div>
  <div class="col-6 center">
    <img src="@root/files/2025/11/25/times.svg" alt="time-series chart of developer and tester time" width="90%">
  </div>
</div>

Again,
you can't tell from these plots alone what changed.
In this case it isn't just a parameter:
instead of the testing time being completely independent of the development time,
we're multiplying the development time by a random number between 0.5 and 1.5
to determine the testing time,
on the theory that things that take longer to develop
usually take longer to test as well.
This is a fundamental change to the model,
but if we didn't have access to the simulation and its parameters
(which we wouldn't in the real world),
we would need to look collect different data and look at it more closely
to figure out what the hell was going on.

[analyzing]: @root/2025/11/24/analyzing-simulation/
