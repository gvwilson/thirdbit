---
title: "Tandem Queue Blocking"
date: 2026-06-05
category: programming
katex: true
---
Two processing stages are arranged in series: Stage 1 feeds work into a bounded buffer, which feeds Stage 2. Both stages have the same mean service rate $\mu$, and the arrival rate $\lambda < \mu$ so neither stage is overloaded on average. However, Stage 1 has high variance (hyperexponential service); Stage 2 has zero variance (deterministic service).

Even though both stages have identical mean throughput and the system is underloaded, Stage 2 sits idle for a substantial fraction of time when the buffer between them is small. The idle fraction only vanishes as the buffer size $K \to \infty$.

High service-time variance at Stage 1 produces bursts of output—many jobs finish close together—followed by droughts. With a small buffer, the burst overflows (blocking Stage 1) and the drought starves Stage 2. Both effects reduce system throughput below what we would intuitively expect.

## Analysis

For a two-stage tandem queue with a finite buffer of capacity $K$, the blocking probability at Stage 1 and the starvation probability at Stage 2 depend on the full service-time distributions, not just their means. The Kingman approximation gives the mean wait in a single G/G/1 queue as:

$$W_q \approx \frac{\rho}{1-\rho} \cdot \frac{c_a^2 + c_s^2}{2} \cdot \frac{1}{\mu}$$

where $c_a^2$ and $c_s^2$ are the squared coefficients of variation of inter-arrival and service times respectively. For a hyperexponential service distribution with $c_s^2 \gg 1$, waiting times are far higher than the M/M/1 formula predicts.

In a tandem network, this extra variability propagates: the departure process of Stage 1 (which is the arrival process for Stage 2) has higher variance than Poisson when Stage 1 has high service variance. This is *Departure Process Variability Propagation* and is a key driver of manufacturing and supply-chain [bullwhip effects](https://en.wikipedia.org/wiki/Bullwhip_effect).

## Buffer as a Variability Absorber

The buffer acts as a shock absorber. Each unit of additional buffer capacity $K$ reduces the starvation probability at Stage 2 by absorbing burst output from Stage 1. The marginal benefit decreases as $K$ grows, leading to a classic diminishing-returns relationship. Practitioners use this to size work-in-progress inventory (WIP) buffers in manufacturing cells.

## Understanding the Math

### Coefficient of variation

The coefficient of variation (CV) of a random variable $X$ with mean $\mu$ and standard deviation $\sigma$ is defined as $c = \sigma / \mu$. It measures spread relative to the mean. A CV of 0 means the variable is deterministic: every value equals $\mu$. A CV of 1 means the spread equals the mean (the exponential distribution has CV exactly 1). A CV greater than 1 means the distribution is bursty: occasional very large values dominate, even if most values are small. The squared CV $c^2 = \sigma^2/\mu^2$ appears frequently in queueing formulas.

### Why high CV at Stage 1 creates bursts and droughts

With a hyperexponential service distribution ($c_s^2 \gg 1$), Stage 1 sometimes completes several jobs in rapid succession (a burst) and sometimes spends a very long time on a single job (a drought). During a burst, jobs pile up in the buffer between stages. During a drought, Stage 2 exhausts the buffer and has to wait for Stage 1 to finish. This wastes capacity even though the system is underloaded on average.

### The buffer as a shock absorber

A buffer of capacity $K$ can hold at most $K$ jobs between the two stages. It absorbs burst output from Stage 1 and releases it steadily to Stage 2. With a small buffer, a burst overflows (blocking Stage 1) or a drought empties the buffer (starving Stage 2). As $K$ grows, both effects weaken and Stage 2 idle time falls. However, the marginal benefit of each extra unit of buffer decreases. Real factories choose $K$ to balance the cost of holding inventory against the cost of machine starvation.

### Kingman's approximation

For a single-stage queue with general service and arrival distributions, the approximate mean waiting time is:

$$W_q \approx \frac{\rho}{1-\rho} \cdot \frac{c_a^2 + c_s^2}{2} \cdot \frac{1}{\mu}$$

Here $c_a^2$ is the squared CV of inter-arrival times and $c_s^2$ is the squared CV of service times. Notice that the formula separates the utilization effect (the $\rho/(1-\rho)$ term) from the variability effect (the $(c_a^2 + c_s^2)/2$ term). When Stage 1 has $c_s^2 \gg 1$, wait time is far higher than the basic M/M/1 formula predicts, even at the same mean throughput. The mean alone does not tell you enough.

### Supply-chain connection

In manufacturing, Stage 1 corresponds to a supplier and Stage 2 to a production line. High variability at the supplier forces the factory to hold large work-in-progress (WIP) buffers, tying up capital and floor space. The [Toyota Production System](https://en.wikipedia.org/wiki/Toyota_Production_System) explicitly targets CV reduction as the primary tool for shrinking necessary WIP by making every process more deterministic through standardized work and small batch sizes. The math here explains exactly why: lower $c_s^2$ directly reduces $W_q$ and the required buffer size $K$.

*This article was originally written for [marimo.io][original].*

[original]: https://marimo.io/for-learners
