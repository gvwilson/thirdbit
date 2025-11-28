---
title: What Changed?
date: 2025-11-28
---

Your company brought in a new CEO,
and she believes that you can't manage what you don't measure.
One of the first things she does is look at historical data
on how long developers have spent fixing bugs over the past year.
When she plots the data quarter by quarter,
she gets the following:

<div class="center">
  <img src="@root/files/2025/11/28/times-linear.svg" alt="linear-scale time plot" width="90%">
</div>

The change over time is easier to see when we scale the Y axis logarithmically:

<div class="center">
  <img src="@root/files/2025/11/28/times-log.svg" alt="log-scale time plot" width="90%">
</div>

The number of bugs taking more than 100 hours to close is clearly going up over time,
but why?
And why has the number of bugs closed per quarter been dropping:

| quarter | number |
| ------: | -----: |
|       1 |   2222 |
|       2 |   1912 |
|       3 |   1525 |
|       4 |    993 |

There hasn't been any turnover in the team,
or a major rewrite of the product.
What has changed?
I'll post the reason tomorrow;
for today,
see what theories you can come up with
and what data you would need to confirm or refute them.
