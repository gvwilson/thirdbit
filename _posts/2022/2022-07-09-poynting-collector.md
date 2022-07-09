---
title: "Poynting Collector"
date: 2022-07-09
year: 2022
---

Back in 2020 I [asked](https://twitter.com/gvwilson/status/1309927394468392961):

> If you're running a 400KW oscillation overthruster in 5-10 msec bursts,
> how much shielding do you need to reduce harmful effects
> from the intermediate vector bosons it throws off
> to acceptable levels?
> (Beam alignment is phase neutral but non-moiré.)

One person responded:

> The rule of thumb is 2<sup>18</sup> quanta per KW/ms if you are using lead,
> but check your supplier for more modern alternatives.
> We haven't recommended lead on oscillation thrusters for a decade
> due to exactly the problem you're trying to solve.

However, someone else said:

> What if you didn't treat vector bosons as a harmful byproduct to be compensated for
> but a useful part of the closed loop system?
> Get a Poynting collector and feed it back into your spin condenser.

It was an interesting idea that sent me down a couple of rabbit holes.
(For example, it turns out there's a thriving market in Soviet-era industrial supplies in Ecuador…)
By March 2021 I was far enough along to say:

> Beam alignment still isn't phase-neutral
> and I still don't know how I'm going to couple it to the Poynting collector
> but we're getting there…

<div align="center">
  <img src="{{'/files/2022/overthruster.jpg' | relative_url}}" alt="oscillation overthruster" width="40%" />
</div>

But nothing's ever done.
The first reply asked if I'd rotated the starboard beam collimator properly.
After a bit of experimentation I realized that I wouldn't be able to get the required precision
because my diffraction grid is analog rather than digital
(see the comment above about Soviet-era industrial supplies).

I set the project aside for a while (COVID, job changes, etc.),
but finally found time to come back to it in May and June.
Having taken everything apart and put it back together,
I now believe the easiest way forward is going to be to take the photozygometer out of this:

<div align="center">
  <img src="{{'/files/2022/laser.jpg' | relative_url}}" alt="laser" width="40%" />
  <em>(not to scale)</em>
</div>

and use it to spallate a new diffraction grid.
I've never done this before,
though,
so if you have with either a lithium chloride or lithium iodide photozygometer,
I'd be grateful if you could give me a shout.
