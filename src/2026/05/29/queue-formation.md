---
title: "Queue Formation"
date: 2026-05-29
category: programming research-methods
katex: true
---

*See the [first post in this series][previous] for the basics of queueing theory.*

We can combine arrivals (Poisson at rate $\lambda$) with a server (exponential service at rate $\mu$) into a complete queue.  The system is stable because $\rho = \lambda/\mu < 1$, which means that on average, the server handles more work than arrives.

Our first question is, how long is the queue? The surprising answer is that even when the server has plenty of spare capacity, customers wait.  The mean number of customers in the system (both waiting and being served) is:

$$L = \frac{\rho}{1 - \rho}$$

The table below gives some representative values:

| $\rho$ | $L$ |
|:---:|:---:|
| 0.1 | 0.11 |
| 0.5 | 1.00 |
| 0.8 | 4.00 |
| 0.9 | 9.00 |

When $\rho = 0.5$, half the server's capacity is idle, but there is on average one customer in the system at any moment.  That customer either had to wait for a previous customer, or is currently being served.  The queue is *never* consistently empty, even at moderate load.

The formula also explains why simple queues are so sensitive to utilization: $L$ blows up as $\rho \to 1$. One way to think about this is that the denominator $(1 - \rho)$ is the spare capacity. As spare capacity vanishes, queue length increases.

## Why Queues Form at All

With deterministic arrivals and service (every customer arrives exactly $1/\lambda$ apart and takes exactly $1/\mu$), a server with $\rho < 1$ would never form a queue: each customer would depart before the next arrived. Randomness changes this. Sometimes three customers arrive close together before the server finishes even one, so the server falls briefly behind. While it recovers, customers wait.  These temporary pileups are unavoidable whenever inter-arrival or service times have any variance.

The probability that exactly $n$ customers are in an M/M/1 system at steady state is:

$$P(N = n) = (1 - \rho)\,\rho^n \qquad n = 0, 1, 2, \ldots$$

This is a *geometric distribution* with success probability $1 - \rho$. The formula says the server is idle (i.e., n=0) with probability $1 - \rho$, which is consistent with the utilization result from the previous scenario. Each additional customer in the system is $\rho$ times less likely than the previous count.

This formula $L = \rho/(1-\rho)$ is the foundation of the later M/M/1 nonlinearity scenario, which shows the practical consequences of the $(1-\rho)$ denominator. Every queue-length formula in queueing theory has a similar structure: a traffic factor $\rho$ divided by a spare-capacity factor $(1 - \rho)$, possibly multiplied by a variability correction.

## Implementation

A `Customer` process increments a shared `in_system` counter on arrival and decrements it on departure.  A `Monitor` process samples `in_system[0]` every `SAMPLE_INTERVAL` time units.  The mean of the samples estimates $L$; the simulation sweeps $\rho$ from 0.1 to 0.9 to confirm the formula $L = \rho/(1-\rho)$.

```python
class Customer(Process):
    def init(self, server, in_system):
        self.server = server
        self.in_system = in_system

    async def run(self):
        self.in_system[0] += 1                  # enter the system
        async with self.server:
            await self.timeout(random.expovariate(SERVICE_RATE))
        self.in_system[0] -= 1                  # depart

class Monitor(Process):
    """Samples total customers in system at regular intervals."""
    def init(self, in_system, samples):
        self.in_system = in_system
        self.samples = samples

    async def run(self):
        while True:
            self.samples.append(self.in_system[0])
            await self.timeout(SAMPLE_INTERVAL)
```

The shared list `in_system` lets `Customer` and `Monitor` communicate without explicit message-passing: `Customer` modifies the count, `Monitor` reads it on a timer.

## Understanding the Math

### Why is the queue length geometric?

The M/M/1 queue can be analyzed as a random walk on the non-negative integers.  When the server is busy, the queue grows by 1 with each arrival (with rate $\lambda$) and shrinks by 1 with each service completion (with rate $\mu$).  The ratio $\lambda/\mu = \rho$ is the probability that the queue grows rather than shrinks at the next event. Under steady state, the probability of being at level $n$ is proportional to $\rho^n$ — because reaching level $n$ requires $n$ consecutive "up" steps. Normalizing so the probabilities sum to 1 gives $(1-\rho)\rho^n$.

### Deriving $L = \rho/(1-\rho)$ from the geometric distribution

Given $P(N = n) = (1 - \rho)\rho^n$, the mean is:

$$L = E[N] = \sum_{n=0}^{\infty} n \cdot (1-\rho)\rho^n = (1-\rho) \sum_{n=0}^{\infty} n\rho^n$$

A result from basic calculus is that the geometric series $\sum_{n=0}^{\infty} \rho^n = 1/(1-\rho)$.  Differentiating both sides with respect to $\rho$:

$$\sum_{n=0}^{\infty} n\rho^{n-1} = \frac{1}{(1-\rho)^2}$$

Multiply both sides by $\rho$:

$$\sum_{n=0}^{\infty} n\rho^n = \frac{\rho}{(1-\rho)^2}$$

Substituting back:

$$L = (1-\rho) \cdot \frac{\rho}{(1-\rho)^2} = \frac{\rho}{1-\rho}$$

### Checking the formula at the boundaries

When $\rho \to 0$: there are almost no arrivals, so $L \to 0$, i.e., the server is nearly always idle.

When $\rho \to 1$: the spare capacity is $(1-\rho) \to 0$, so $L \to \infty$, i.e., the queue grows without bound.

Both limits match physical intuition.  Note that the formula is exact (not an approximation) for an M/M/1 queues in steady state.

*This article was originally written for [marimo.io][original].*

[original]: https://marimo.io/for-learners
[previous]: @root/2026/05/28/basic-queueing-theory/
