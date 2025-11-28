---
title: What Changed?
date: 2025-11-28
---

Your company brought in a new CEO,
and she believes that you can't manage what you don't measure.
One of the first things she does is dig up historical data
on how long developers and testers have spent fixing bugs over the past year.
When she plots the data quarter by quarter,
she gets the following plots:

<div class="row">
  <div class="col-6 center">
    <img src="@root/files/2025/11/28/times-0.0.svg" alt="no rework" width="90%">
    <br>
    First Quarter
  </div>
  <div class="col-6 center">
    <img src="@root/files/2025/11/28/times-0.1.svg" alt="10% rework" width="90%">
    <br>
    Second Quarter
  </div>
</div>
<div class="row">
  <div class="col-6 center">
    <img src="@root/files/2025/11/28/times-0.3.svg" alt="30% rework" width="90%">
    <br>
    Third Quarter
  </div>
  <div class="col-6 center">
    <img src="@root/files/2025/11/28/times-0.5.svg" alt="50% rework" width="90%">
    <br>
    Fourth Quarter
  </div>
</div>

The number of bugs taking more than 20 hours to close is clearly going up over time,
but why?
There hasn't been any turnover in the team,
or a major rewrite of the product.
What has changed?

After a bit of digging,
she discovers that developers were reporting time in 10-hour blocks in Q1,
so that sharp cutoff is an accounting artifact.
However,
that doesn't explain why the number of issues taking more than 10 hours
has slowly but steadily been creeping up from Q2 to the end of the year.
I'll post the reason tomorrow;
for today,
see what theories you can come up with
and what data you would need to confirm or refute them.
