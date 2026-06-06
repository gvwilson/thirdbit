---
title: "Sojourn Time"
date: 2026-05-31
category: programming research-methods
katex: true
---

How long does a customer actually spend in the system?
The previous scenario measured $L$, the mean number of customers in the system at any moment. This scenario measures $W$, the mean time a single customer spends from arrival to departure. This is called the *sojourn time*, *residence time*, or *response time*, and has two components:

- $W_q$: time spent waiting in the queue because the server is busy.
- $W_s$: time spent in service while the server is working on this customer.

$$W = W_q + W_s$$

## The Surprising Finding

For an M/M/1 queue, the mean sojourn time is:

$$W = \frac{1}{\mu(1 - \rho)}$$

This blows up as $\rho \to 1$, just like $L$. But the split between waiting and service shifts dramatically as load increases.

| $\rho$ | $W_q$ (wait) | $W_s$ (service) | $W$ (total) |
|:---:|:---:|:---:|:---:|
| 0.1 | 0.11 | 1.00 | 1.11 |
| 0.5 | 1.00 | 1.00 | 2.00 |
| 0.9 | 9.00 | 1.00 | 10.00 |

The mean service time $W_s = 1/\mu = 1.0$ is constant: the server always takes the same average time to serve one customer. All the extra delay at high load is pure waiting: $W_q = \rho/(\mu(1-\rho))$ grows without bound while $W_s$ stays fixed. At $\rho = 0.9$, 90% of a customer's time is spent waiting for the server to become free.

This formula is closely connected to Little's Law:

$$L = \lambda W$$

Plugging in $W = 1/(\mu(1-\rho))$ and $\lambda = \rho\mu$:

$$L = \rho\mu \cdot \frac{1}{\mu(1-\rho)} = \frac{\rho}{1-\rho}$$

## Understanding the Math

### Why $W_s = 1/\mu$ regardless of $\rho$

Service time is drawn from an exponential distribution with rate $\mu$, so its mean is $1/\mu$. This is a property of the distribution, not of the queue. No matter how busy the server is, once it starts serving you it takes on average $1/\mu$ time.

### Deriving $W_q$

Since $W = W_q + W_s$ and $W_s = 1/\mu$:

$$W_q = W - W_s = \frac{1}{\mu(1-\rho)} - \frac{1}{\mu}
      = \frac{1}{\mu}\left(\frac{1}{1-\rho} - 1\right)
      = \frac{1}{\mu} \cdot \frac{\rho}{1-\rho}
      = \frac{\rho}{\mu(1-\rho)}$$

Note that $W_q = \rho \cdot W$: at high load, almost all of $W$ is waiting.

### Units check

$\lambda$ has units of [customers/time]; $W$ has units of [time]; so $L = \lambda W$ has units of [customers/time $\times$ time] $=$ [customers]. This count of people is dimensionless, as it should be. Checking units this way is a quick sanity test whenever you apply Little's Law to a real problem.

*This article was originally written for [marimo.io][original].*

[original]: https://marimo.io/for-learners
