---
title: "The Inspector's Paradox"
date: 2026-06-04
category: software
katex: true
---
Why is the bus always late? Buses arrive at a stop with some average headway (gap between buses) of $\mu$ minutes. A passenger arrives at a uniformly random time and waits for the next bus. How long do they wait? The naive answer is $\mu / 2$: on average you land in the middle of a gap. The correct answer is almost always longer—sometimes much longer. The expected wait is not $\mu/2$ but:

$$E[\text{wait}] = \frac{\mu}{2} + \frac{\sigma^2}{2\mu}$$

where $\sigma^2 = \text{Var}[\text{headway}]$. The second term is always non-negative, so higher variance always means longer expected waits, even when the mean headway is unchanged.

### Three Bus Schedules with Mean Headway $\mu = 10$

| Schedule    | $\sigma^2$ | Predicted wait | Naive wait |
|-------------|-----------|----------------|-----------|
| Regular     | 0         | 5.0            | 5.0       |
| Exponential | 100       | 10.0           | 5.0       |
| Clustered   | 64        | 8.2            | 5.0       |

For exponentially distributed headways, $\sigma^2 = \mu^2$, so:

$$E[\text{wait}] = \frac{\mu}{2} + \frac{\mu^2}{2\mu} = \mu$$

A passenger waits on average for an *entire* mean headway — twice the naive expectation.

## Why This Happens: Length-Biased Sampling

A passenger arriving at a random time is more likely to land inside a *long* gap than a short one, because long gaps occupy more time on the clock. This is called *length-biased sampling*. The interval containing your arrival is not a random headway: it is drawn from the length-biased distribution with density:

$$f^*(h) = \frac{h \cdot f(h)}{\mu}$$

The mean of this biased distribution is $\mu + \sigma^2/\mu$, and you arrive uniformly within it, giving expected wait $(\mu + \sigma^2/\mu)/2$.

The same phenomenon explains why the average class size experienced by a student exceeds the average class size reported by the university (large classes have more students to report them).

## Why "Inspector's Paradox"?

The name comes from quality control, where an inspector arrives at a random time to sample a production process and systematically encounters longer-than-average intervals. The paradox is that a random observer is more likely to land inside a long gap than a short one, so their experienced mean interval exceeds the true mean interval. It feels paradoxical because you'd expect a random arrival to see the average gap, but length-biased sampling guarantees they see worse-than-average gaps whenever there's any variance at all.

## Understanding the Math

### Length-biased sampling

Suppose buses run on an irregular schedule where gaps between buses are either 2 minutes or 18 minutes, each with probability 1/2. The mean gap is $\mu = (2 + 18)/2 = 10$ minutes. Now ask: if you arrive at a completely random moment, which gap are you most likely to land inside?

A 2-minute gap occupies only 2 minutes on the clock, but an 18-minute gap occupies 18. Out of every 20 minutes of clock time on average, 2 minutes belong to a short gap and 18 to a long one. So a random arrival lands in a short gap with probability $2/(2+18) = 1/10$ and in a long gap with probability $18/20 = 9/10$. The expected gap length you experience is:

$$E[\text{gap experienced}] = \frac{1}{10} \cdot 2 + \frac{9}{10} \cdot 18 = 0.2 + 16.2 = 16.4 \text{ minutes}$$

That is far above the mean gap of 10 minutes. You are disproportionately likely to land inside a long gap simply because it takes up more time.

### The wait formula

Once you are inside a gap, you arrive uniformly within it, so on average you land in the middle. Your expected wait is half the gap length you experience. The full formula is:

$$E[\text{wait}] = \frac{\mu}{2} + \frac{\sigma^2}{2\mu}$$

Here $\mu$ is the mean gap and $\sigma^2 = \text{Var}[\text{gap}]$ is the variance of gap lengths. The first term, $\mu/2$, is what you would get if every gap were exactly $\mu$ (deterministic buses — arrive in the middle every time). The second term, $\sigma^2/(2\mu)$, is the extra waiting from length-biased sampling. It is always non-negative, so irregular buses always make you wait longer than regular buses with the same mean headway.

### Why variance matters

The variance $\sigma^2$ measures how spread out the gap sizes are. A perfectly regular bus schedule has $\sigma^2 = 0$ and gives the naive answer $\mu/2$. An exponentially distributed schedule has $\sigma^2 = \mu^2$, which doubles the expected wait to $\mu$. More irregular buses, higher penalty.

### Connecting to expected values

The formula arises from a standard result: the expected length of the gap containing a random arrival is $\mu + \sigma^2/\mu$. You can think of this as the mean gap plus a correction term proportional to the variance divided by the mean. Dividing by 2 (uniform arrival within the gap) gives the wait formula above.

*This article was originally written for [marimo.io][original].*

[original]: https://marimo.io/for-learners
