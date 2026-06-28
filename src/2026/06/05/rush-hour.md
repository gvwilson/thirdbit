---
title: "Rush Hour Displacement"
date: 2026-06-05
category: programming
katex: true
---
$N$ commuters all want to leave for work at the same preferred time. The road has a fixed capacity: up to $C$ commuters per time slot travel quickly, but when more than $C$ try to leave in the same slot, everyone in that slot experiences extra delay proportional to the overload.

Each day, commuters observe yesterday's travel times and shift their departure by one slot toward a less congested option with some probability. Much to their disappointment, the rush hour never disappears. Instead it:

1.  flattens slightly (spreading across more slots), but
2.  shifts its peak position over successive days, and
3.  reaches a new quasi-equilibrium that may be no less congested than the original, just at a different time.

The intuition is that any slot that becomes less congested immediately attracts new commuters from adjacent overloaded slots, refilling it. Individual optimization is self-defeating in aggregate.

The simulation in this tutorial shows emergent dynamics:

-   The arrival distribution begins concentrated at the preferred slot.
-   Commuters shift away from congested slots, spreading the peak.
-   The spreading creates new local peaks at adjacent slots, which then attract their own shifters.
-   Over many days the distribution oscillates or drifts without converging to zero congestion.

## The Vickrey Bottleneck Model

The classic model (Vickrey 1969) treats the road as a bottleneck with flow rate $s$ vehicles per unit time. At equilibrium, every commuter faces the same *generalized cost*:

$$c = \alpha \cdot d + \beta \cdot \max(0,\, t^* - t_{\text{arr}}) + \gamma \cdot \max(0,\, t_{\text{arr}} - t^*)$$

where $d$ is queuing delay, $t^*$ is the desired arrival time, and $\beta, \gamma$ are schedule-delay costs for early and late arrival respectively. Vickrey showed that at [Nash equilibrium](https://en.wikipedia.org/wiki/Nash_equilibrium) a departure queue forms with length that rises and then falls as commuters spread across time to equalize cost, but total system delay is unchanged.

This model underlies modern road-pricing schemes: a time-varying toll that exactly offsets the schedule-delay cost eliminates queuing entirely while preserving the total commuting burden. In essence, the toll revenue replaces the wasted queuing time.

## Understanding the Math

### What is a congestion game?

Each commuter (the "player") independently chooses a departure time slot. The delay experienced in any given slot depends on how many other commuters choose the same slot: if the slot is over capacity $C$, delay grows with the number of extra commuters. No central authority coordinates choices. This structure, where each player's cost depends on the collective choices of all players, is called a *congestion game*.

### Nash equilibrium in this context

A Nash equilibrium is a distribution of departure times such that no individual commuter can reduce their own delay by unilaterally switching to a different slot. At equilibrium, every occupied slot has the same congestion-adjusted cost. If slot 15 were cheaper than slot 14, commuters from slot 14 would shift to slot 15 until the costs equalized. The equilibrium is therefore defined by: all slots with commuters in them have equal cost, and all empty slots have cost no lower than the occupied ones.

### Why Nash equilibrium is not the social optimum

The social optimum minimizes total delay summed over all commuters. The Nash equilibrium minimizes each person's individual delay given everyone else's choices. These are generally different objectives. At Nash equilibrium, a commuter choosing a crowded slot ignores the extra delay they impose on every other commuter already in that slot. They feel only their own delay; the cost they impose on others is a negative externality that they do not internalize.

### Why the peak shifts but does not vanish

Suppose slot 15 is heavily congested. Some commuters shift to slot 14, relieving slot 15. But now slot 14 is more congested, so its commuters shift to slot 13. The congestion wave ripples outward in both directions. Meanwhile, commuters who shifted away from slot 15 now observe it as less congested and some drift back. The system never reaches zero congestion: it perpetually redistributes congestion across nearby slots in a slow drift. The Nash equilibrium exists in theory, but the day-by-day best-response dynamics cycle around it rather than converging to it, particularly when commuters respond noisily to yesterday's conditions.

*This article was originally written for [marimo.io][original].*

[original]: https://marimo.io/for-learners
