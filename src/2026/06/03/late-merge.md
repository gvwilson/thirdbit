---
title: "Late Merge"
date: 2026-06-03
category: programming research-methods
katex: true
---
A two-lane road narrows to one lane at a construction zone. Drivers face a choice:

-   Early (courtesy) merge: upon seeing the "Lane Ends Ahead" sign, drivers immediately move from the closing lane into the open lane.
-   Late (zipper) merge: drivers use both lanes all the way to the merge point, then alternate — one car from each lane in turn, like a zipper.

It turns out that late merging produces higher throughput and shorter queues than early merging, even though it feels less polite. Early merging creates a single long queue that wastes the closing lane's capacity. Late merging fully utilises both lanes up to the bottleneck, then processes cars at the same rate with a zipper pattern. This result is not merely theoretical: the Minnesota Department of Transportation, the German ADAC, and the UK Highway Code all recommend late merging in slow-moving traffic precisely because it is provably more efficient.

The primary benefit of late merging is higher throughput: more cars complete the merge per unit time. Mean sojourn time for individual cars may actually be slightly longer under late merge, because the larger total buffer admits more cars into the system, increasing average queue occupancy. By Little's Law $L = \lambda W$, if $\lambda$ grows faster than $L$ falls, $W$ rises. This is not a disadvantage: it means more drivers successfully pass through rather than being turned away.

## Why Early Merging Hurts

With early merging:

-   All $N$ cars queue in one lane of capacity $K$.
-   When the single queue is full ($K$ cars), arriving cars are turned away (blocking), reducing throughput.
-   The merge point processes at rate $\mu$ regardless, but there are fewer cars available to process (the second lane is empty and wasted).

With late merging:

-   Cars distribute across two lanes, each of capacity $K$ (total $2K$).
-   The merge point receives supply from both lanes, reducing starvation.
-   Blocking occurs only when *both* lanes are simultaneously full, a rarer event.

The key metric is the *blocking probability*: the fraction of arriving cars turned away because the pre-merge buffer is full. Let $\rho = \lambda/\mu$ be the utilisation of the merge bottleneck. For a finite-buffer M/M/1/K queue the blocking probability is:

$$P_{\text{block}} = \frac{(1-\rho)\rho^K}{1 - \rho^{K+1}}$$

Early merge has buffer $K$; late merge effectively has buffer $2K$ (spread across two lanes). Since $P_{\text{block}}$ decreases exponentially in $K$, doubling the available buffer dramatically reduces blocking.

## Understanding the Math

### The finite-buffer formula

For a queue with random arrivals, exponential service, a single server, and a buffer that holds at most $K$ cars (the M/M/1/K model), the blocking probability is:

$$P_{\text{block}} = \frac{(1-\rho)\,\rho^K}{1 - \rho^{K+1}}$$

As usual, $\rho = \lambda/\mu$ is the utilization. Notice that the numerator contains $\rho^K$. Because $\rho < 1$, increasing $K$ by 1 multiplies the numerator by $\rho < 1$, shrinking $P_{\text{block}}$ faster than linearly. Each extra slot in the buffer is more valuable than a simple linear reduction would suggest.

### Early vs. late merge in terms of $K$

Early merging creates a single queue with buffer $K$: one lane's worth of space. Late merging uses both lanes up to the merge point, creating an effective buffer of $2K$ cars total. Plugging $2K$ into the formula instead of $K$ replaces $\rho^K$ with $\rho^{2K} = (\rho^K)^2$. Since $\rho^K < 1$, squaring it makes it much smaller. This is the why doubling the buffer dramatically reduces blocking.

### Intuition about two lanes

Here is another way to see it. Under late merge, both lanes must be simultaneously full for a car to be blocked. Suppose each individual lane is full with probability $p$. If the two lanes are roughly independent, the probability both are full at once is approximately $p^2$. For example, if $p = 0.3$, then $p^2 = 0.09$ — blocking drops from 30% to 9%. Two lanes are dramatically more forgiving than one.

### Connection to throughput

Throughput is the rate at which cars successfully pass through the merge: $\text{throughput} = \lambda \cdot (1 - P_{\text{block}})$. Every blocked car is a car that does not get through. Reducing $P_{\text{block}}$ by doubling $K$ therefore raises throughput nearly proportionally. Late merge does not speed up the bottleneck (the merge point still processes cars at rate $\mu$) but it ensures the bottleneck is never starved of cars to process, maximizing the number of drivers who make it through.

### The broader lesson

The key insight is that the *structure* of a waiting space matters, not just its total size. Two separate lanes of capacity $K$ each are far better than one lane of capacity $2K$ because blocking requires both lanes to fill simultaneously. This logic generalises widely: in computer networks, having multiple independent paths reduces the chance a single congested link stalls all traffic; in hospitals, pooling patients across several triage nurses reduces the chance one idle nurse sits beside an overwhelmed colleague. Wherever there is a finite buffer feeding a shared bottleneck, the late-merge principle applies: spread the waiting space across parallel channels and blocking probability falls dramatically.

*This article was originally written for [marimo.io][original].*

[original]: https://marimo.io/for-learners
