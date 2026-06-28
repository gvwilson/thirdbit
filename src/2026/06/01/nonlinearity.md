---
title: "Queue Nonlinearity"
date: 2026-06-01
category: programming
katex: true
---
A single server handles jobs that arrive randomly and take a random amount of time to process. If both inter-arrival times and service times follow exponential distributions, this is called an *M/M/1 queue*, and is the simplest model in queueing theory.

Managers often treat utilization linearly: "90% busy is only a little worse than 80% busy." The M/M/1 formula shows this intuition is badly wrong. The mean number of jobs in the system (waiting and being served) is:

$$L = \frac{\rho}{1 - \rho}$$

where $\rho = \lambda / \mu$ is the utilization ratio (arrival rate divided by service rate). The mean time a job spends in the system follows from Little's Law $L = \lambda W$:

$$W = \frac{1}{\mu - \lambda} = \frac{1}{\mu(1 - \rho)}$$

The denominator $(1 - \rho)$ causes both $L$ and $W$ to blow up as $\rho \to 1$.

| $\rho$ | $L = \rho/(1-\rho)$ | Marginal $\Delta L$ per 0.1 step |
|-------:|--------------------:|--------------------------------:|
|  0.50  |               1.00  |                            —    |
|  0.60  |               1.50  |                          +0.50  |
|  0.70  |               2.33  |                          +0.83  |
|  0.80  |               4.00  |                          +1.67  |
|  0.90  |               9.00  |                          +5.00  |

Each equal step in $\rho$ produces a larger jump in queue length than the previous step. Going from 80% to 90% utilization adds more queue length than going from 0% to 80% combined. This happens because the queue is stabilized by the gaps in service capacity. When $\rho = 0.9$, only 10% of capacity is slack. Any random burst of arrivals takes far longer to drain than when $\rho = 0.5$ and 50% of capacity is slack. The system spends most of its time recovering from bursts rather than idling.

## Key Takeaway

For any system approximated by an M/M/1 queue, **never target utilization above 80–85%** if low latency matters. The last few percent of throughput come at an enormous cost in queue length and wait time.

*This article was originally written for [marimo.io][original].*

[original]: https://marimo.io/for-learners
