---
title: "The Convoy Effect"
date: 2026-06-05
category: programming simulation
katex: true
---
A single server processes jobs that arrive randomly according to a Poisson process. Most jobs are quick (exponential service with small mean), but a rare few are very slow (exponential service with large mean). This *hyperexponential* service distribution has high variance. This post compares the performance of two scheduling disciplines in this situation:

-   FIFO (First In, First Out): jobs are served in the order they arrive.
-   SJF (Shortest Job First): the server always picks the shortest queued job next.

The surprising result is that SJF dramatically outperforms FIFO: not just for the small jobs that directly benefit from skipping ahead, but also for mean sojourn time across *all* jobs. The improvement is most visible at the tail (95th and 99th percentiles) because FIFO creates a *convoy effect*: one long job blocks many short jobs behind it, inflating everyone's wait.

### The Convoy Metaphor

Picture a one-lane road with one slow truck and many fast cars. Every car behind the truck must drive at truck speed; no overtaking allowed. The truck is the long job; the cars are the short jobs stuck behind it in FIFO order. SJF is like a passing lane: fast cars jump ahead of the truck and reach their destination much sooner. The truck itself arrives at the same time either way, but the total delay experienced by all vehicles plummets.

### Why FIFO Hurts with High Variance

In FIFO, the server's current job is chosen at arrival time, not at decision time. When a slow job begins service, every subsequent arrival must join the queue and wait. The expected excess work in service (the remaining time of the current job, seen by an arriving customer) under FIFO is:

$$W_{\text{FIFO}} = \frac{\lambda \overline{s^2}}{2(1-\rho)} + \frac{1}{\mu}$$

where $\overline{s^2}$ is the second moment of service time. High variance inflates $\overline{s^2}$ without changing $\rho$, directly worsening wait time.

### SJF Minimises Mean Sojourn Time

For a single server with non-preemptive SJF and any service-time distribution, the mean sojourn time is given by the formula below (which is discussed in "Understanding the Math" at the end of this lesson):

$$W_{\text{SJF}} = \frac{1}{\mu} + \frac{\lambda \overline{s^2}}{2(1-\rho)}$$

SJF achieves this minimum because short jobs that would otherwise be blocked by a long job are promoted ahead, reducing the total waiting work in the system.

## Practical Relevance

Operating system CPU schedulers use time-quanta and priority aging to approximate SJF without knowing job sizes in advance. Database query planners estimate query cost and reorder execution to minimize blocking. The phenomenon reappears as *head-of-line blocking* in HTTP/1.1 (one slow response stalls a connection), motivating HTTP/2 multiplexing and HTTP/3's QUIC stream independence.

## Understanding the Math

### The second moment

For a random variable $S$ representing service time, the second moment is $E[S^2]$. Recall from your statistics course that variance is $\text{Var}(S) = E[S^2] - (E[S])^2$, which rearranges to:

$$E[S^2] = \text{Var}(S) + (E[S])^2$$

This means high variance inflates $E[S^2]$ even if the mean $E[S]$ stays fixed. Doubling the spread of service times can quadruple $E[S^2]$, even with the same average service time.

### Why variance of service time hurts

Imagine a FIFO server handling jobs that are either 0.1 minutes or 10 minutes long, with 90% being short and 10% being long. The mean service time is $0.9 \times 0.1 + 0.1 \times 10 = 1.09$ minutes, so utilization $\rho = \lambda / \mu$ might be modest. But when a 10-minute job starts, every job arriving during those 10 minutes must join the queue and wait. The longer $E[S^2]$, the more average work sits ahead of each arriving job.

### The Pollaczek–Khinchine formula

The mean time a job spends waiting (not counting its own service time) in a FIFO single-server queue is:

$$W_q = \frac{\lambda \cdot E[S^2]}{2(1 - \rho)}$$

Here $\lambda$ is the arrival rate, $E[S^2]$ is the second moment of service time, and $\rho = \lambda \cdot E[S]$ is the server utilization. Both $\lambda$ and $E[S^2]$ appear in the numerator, so more variance means more waiting even at the same $\rho$. The $(1-\rho)$ denominator is the familiar blow-up term from M/M/1.

*This article was originally written for [marimo.io][original].*

[original]: https://marimo.io/for-learners
