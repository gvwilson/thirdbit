---
title: Malice and Randomness
date: 2025-11-26
---

The main point of [yesterday's post][you-cant-tell] was that
any simple view of a complex system can be interpreted in several ways.
Is work piling up?
That's good to know
(quick, do you have a plot of how much your backlog has grown over the last year?),
but figuring out *why* requires usually close investigation.

Here's another example.
Suppose you're keeping track of the development and testing backlog over time,
and you get a graph like this:

<div class="center">
  <img src="@root/files/2025/11/26/queue-1k.svg" alt="queue lengths over time">
</div>

Your first question is going to be,
"What changed around t=3000 that made the development backlog get five times larger?"
Your second will be,
"And what changed around t=5000 to bring it back down again?"
You might even ask what happened between t=1000 and t=3000 to cause a smaller spike;
was that an early warning that you missed?
Or did the same thing go wrong at t=1000 and t=3000,
but for some reason it was caught and fixed earlier the first time?

[Hanlon's Razor][hanlon] states,
"Never attribute to malice that which is adequately explained by stupidity."
The statistical equivalent is,
"Never attribute to human action that which is adequately explained by random variation."
The truth is that *nothing remarkable happened* to cause the two humps shown in the plot above.
They are just random variations in a random system.
We can see more of this if we run the simulation for 10,000 timesteps instead of 1000:

<div class="center">
  <img src="@root/files/2025/11/26/queue-10k.svg" alt="queue lengths over time">
</div>

It *looks* like the development backlog is slowly increasing,
and that the testing backlog is following that increase with a bit of a lag,
but how confident are you of this?
If we run the simulation even longer,
would you be surprised if the backlogs decreased again?

The data we collect and the dashboards we build
can help us identify things that might need to be explained,
but we have to interpret them in order to create those explanations.
As Elisabeth Hendrickson and Joel Tosi point out in their upcoming book
*[Signals & Levers][signals-levers]*,
something as simple as a [Shewhart chart][shewhart]
can help you distinguish normal variation from things you might need to worry about.

[hanlon]: https://en.wikipedia.org/wiki/Hanlon%27s_razor
[shewhart]: https://en.wikipedia.org/wiki/Shewhart_individuals_control_chart
[signals-levers]: https://signalsandlevers.com/book/
[you-cant-tell]: @root/2025/11/25/you-cant-tell/
