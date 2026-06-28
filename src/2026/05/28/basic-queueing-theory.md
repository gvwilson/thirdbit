---
title: "Basic Ideas in Queueing Theory"
date: 2026-05-28
category: programming
katex: true
---

## Arrivals, Servers, and Utilization

Three concepts underpin every queueing model. The first is *Poisson arrivals*: when customers arrive independently at a constant average rate $\lambda$, gaps between consecutive arrivals follow an *exponential* distribution with mean $1/\lambda$, and the count of arrivals in any window of width $t$ follows a Poisson distribution with mean $\lambda t$. These two descriptions are equivalent: if one holds, the other must too.

The second key idea is that the exponential distribution is *memoryless*. Knowing you have already waited $s$ units gives no information about when the next arrival will come. This property makes the math simple, but means that the exponential distribution isn't a good fit for scenarios where events happen in bursts. Some of the later tutorials will explore models that handle this.

The final concept is *server utilization*. A server completing work at rate $\mu$ has utilization $\rho = \lambda/\mu$, which is the long-run fraction of time it is busy. The system is stable only when $\rho < 1$. When $\rho \geq 1$, arrivals outpace service and the queue grows without bound. Even at exact balance ($\rho = 1$), randomness creates bursts that accumulate faster than the server recovers, so the expected queue length is infinite.

The code below uses [asimpy][asimpy] to model a simple job queue. The technical term for this kind of system is an [M/M/1 queue][mm1_queue]: memoryless (Poisson) arrivals, memoryless service times, and one server.

```python
class ArrivalSource(Process):
    """Generates arrivals at a Poisson rate."""
    def init(self, rate, gaps):
        self.rate = rate
        self.gaps = gaps

    async def run(self):
        while True:
            gap = random.expovariate(self.rate)
            await self.timeout(gap)
            self.gaps.append(gap)
```

`random.expovariate(rate)` samples from an exponential distribution with the given rate. The gaps between consecutive arrivals follow $\text{Exp}(\lambda)$, which is precisely the defining property of a Poisson process.

## Understanding the Math

### Why inter-arrival gaps are exponential

Divide $[0, t]$ into $n$ tiny slices of width $\Delta = t/n$. The probability of an arrival in each slice is $\approx \lambda\Delta$; slices are independent. The probability of no arrival across all $n$ slices is $(1 - \lambda t/n)^n \to e^{-\lambda t}$ as $n \to \infty$. This is $P(X > t)$ for the exponential distribution.

### Why mean equals standard deviation for the exponential

If $E[X] = 1/\lambda$, then $E[X^2] = 2/\lambda^2$, so $\text{Var}(X) = 2/\lambda^2 - 1/\lambda^2 = 1/\lambda^2$ and $\text{SD}(X) = 1/\lambda = E[X]$. Equal mean and standard deviation means roughly one-third of gaps are longer than the mean.

### Why the busy fraction equals $\rho$

Over a long run $T$, about $N \approx \lambda T$ customers are served, each occupying the server for mean $1/\mu$. Total service time $\approx N/\mu = \lambda T/\mu = \rho T$. Dividing by $T$ gives busy fraction $= \rho$.

### Why $\rho = 1$ is unstable

At exact balance, the queue length after each service completion performs a symmetric random walk on the non-negative integers. This random walk is *null recurrent*: it returns to zero but with infinite expected return time, so the mean queue length is infinite even when arrivals and service are perfectly matched on average.

*This article was originally written for [marimo.io][original].*

[asimpy]: https://asimpy.readthedocs.io/
[mm1_queue]: https://en.wikipedia.org/wiki/M/M/1_queue
[original]: https://marimo.io/for-learners
