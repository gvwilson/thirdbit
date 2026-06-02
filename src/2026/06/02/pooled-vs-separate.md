---
title: "Pooled vs. Separate Queues"
date: 2026-06-02
category: software
katex: true
---
A facility has two identical servers. Customers arrive as a Poisson process and each needs one server for an exponentially distributed service time. Which queueing discipline should the facility use?

-   Separate queues: each server has its own dedicated line; customers randomly pick a line on arrival and cannot switch.
-   Pooled queue: a single shared line feeds whichever server becomes free first.

It turns out that pooling the queues is always better, even though both systems have identical total arrival rate, identical per-server service rate, and identical utilization $\rho$. The pooled system consistently produces shorter mean wait times, often by a factor of two or more at moderate utilization. The reason is that separate queues waste servers' idle time. In separate queues, one server may be idle while customers wait in the other line. Pooling eliminates this mismatch: a free server always serves the next waiting customer.

> Despite being provably worse, separate queues feel fairer because customers can see their progress. Single lines eliminate the anxiety of watching the other queue move faster, but historically customers resisted them until airlines and banks demonstrated the improvement empirically in the 1960s–70s.

## Understanding the Math

### Why pooling always wins

Two separate M/M/1 queues each running at utilization $\rho$ have mean sojourn time $W_{\text{sep}} = 1/(\mu(1-\rho))$. A pooled M/M/2 queue with the same total arrival rate has strictly lower mean sojourn time for every value of $0 < \rho < 1$. The proof uses the [Erlang-C formula](https://en.wikipedia.org/wiki/Erlang_(unit)#Erlang_C_formula), but the intuition is simpler: pooling converts two independent random processes into one, and the combined queue can exploit any idle capacity instantly. At $\rho = 0.8$, separate queues give roughly twice the mean wait of a pooled queue.

### Connection to variance reduction

Think of the service delivered in a time window by two separate servers as two independent random variables $X_1$ and $X_2$. Their average $(X_1 + X_2)/2$ has variance $\sigma^2/2$, which is half the variance of either component alone. Pooling achieves something similar: by combining demand into one stream served by both servers, the system smooths out random fluctuations. The pooled queue is, in effect, averaging over both servers' idle periods instead of locking each idle period to a single lane.

### Rule of thumb

At $\rho = 0.8$, separate queues produce roughly double the mean wait of a pooled queue. This factor grows as $\rho$ increases, because the $(1-\rho)$ term in the denominator amplifies any wasted capacity. The lesson: whenever you can route demand flexibly to a shared resource, do it.

*This article was originally written for [marimo.io][original].*

[original]: https://marimo.io/for-learners
