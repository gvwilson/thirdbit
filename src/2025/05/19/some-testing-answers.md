---
title: Some Testing Answers
date: 2025-05-19
---

A month ago I [asked for advice][testing-question] on testing a little piece of Python
that fills a grid using a random walk.
[Nick Radcliffe][stochastic],
a former colleague who is writing a book on test-driven data analysis,
suggested that one way to test the code is to put move generation in a function of its own,
call that function a few hundred times,
and check that the results are evenly distributed
(e.g., each of the four moves appears 20-30% of the time).
If not,
double the number of moves generated,
check again,
and repeat until either the distribution converges
or you decide that it's not going to.
This approach ensures that tests run quickly most of the time,
and it did indeed catch a bug when I moved from 4-way steps to 8-way (i.e., allowed diagonal moves).

[Nathan Furnal][furnal] suggested a similar approach.
If we generate 30 moves,
the probability of never seeing one of the four possible moves is less than 0.02%.
If we increase the number of moves to 100 (which only takes 61 microseconds on my five-year-old laptop)
the odds of not seeing one of the moves drop to one in 10<sup>13</sup>.
If we're running the tests 1000 times a day,
we can expect one false positive every ten million years or so.

I've added both tests to my test suite,
but would appreciate suggestions for others.
Testing in the face of randomness is more common and more important in (data) science
than in commercial software development;
as more and more applications incorporate small household spirits (i.e., genAI),
we're going to have to figure out how to do this well.

[furnal]: https://nathanfurnal.xyz/
[stochastic]: https://stochasticsolutions.com/
[testing-question]: @root/2025/04/20/a-testing-question/
