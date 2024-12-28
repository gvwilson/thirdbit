---
title: Crunch Mode
date: 2025-01-02
---

I'm supervising some undergraduate students at the University of Toronto this semester.
It's the first time I've done this in almost 15 years,
and it's giving me a chance to re-think and re-write the advice I used to give
when I was doing this regularly.

<div class="callout" markdown="1">
My starting point is [[Sedano2017][Sedano2017]],
which found that software development projects have nine types of waste:
building the wrong feature or product,
mismanaging the backlog,
rework,
unnecessarily complex solutions,
extraneous cognitive load,
psychological distress,
waiting and multitasking,
knowledge loss,
and ineffective communication.
*None of these are software issues,*
so if you only think about the code in your project and not about the people writing it,
everything will take longer and hurt more than it needs to.
</div>

I used to brag about the hours I was working.
Not in so many words, of course—I had *some* social skills—but
I'd show up for work around noon,
unshaven and yawning,
and casually mention how I'd been up until 6:00 a.m. working on some monster bug.

Looking back,
I can't remember who I was trying to impress.
Instead,
what I remember is how much of the code I wrote in those all-nighters I threw away
once I'd had some sleep.
My mistake was to confuse "long hours" with "getting things done".
You can't produce software (or anything else) without doing some work,
but you can easily do lots of work without producing anything of value.
Scientific study of overwork goes back to at least the 1890s—see
[[Robinson2005][Robinson2005]] for a short, readable summary.
The most important results are:

1.  Working more than eight hours a day for more than a couple of weeks of time
    lowers your total productivity,
    not just your hourly productivity—i.e., you get less done *in total* in crunch mode
    than when you work regular hours.

1.  Working over 21 hours in a stretch
    increases the odds of you making a catastrophic error
    just as much as being legally drunk.

These facts have been verified through hundreds of experiments
over the course of more than a century,
including some on novice software developers [[Fucci2020][Fucci2020]].
The data behind them is as solid as the data linking smoking to lung cancer.
However,
while most smokers will at least acknowledge that their habit is killing them,
people in the software industry still talk and act as if
they were somehow immune to science.
To quote Robinson's article:

<div class="callout" markdown="1">
When Henry Ford famously adopted a 40-hour workweek in 1926,
he was bitterly criticized by members of the National Association of Manufacturers.
But his experiments,
which he'd been conducting for at least 12 years,
showed him clearly that cutting the workday from ten hours to eight hours—and
the workweek from six days to five days—increased
total worker output and reduced production cost…
the core of his argument was that reduced shift length meant more output.

…many studies,
conducted by businesses, universities, industry associations and the military,
…support the basic notion that,
for most people,
eight hours a day,
five days per week,
is the best sustainable long-term balance point between output and exhaustion.
Throughout the 30s, 40s, and 50s, these studies were apparently conducted by the hundreds;
and by the 1960s,
the benefits of the 40-hour week were accepted almost beyond question in corporate America.
In 1962,
the Chamber of Commerce even published a pamphlet extolling the productivity gains of reduced hours.

But, somehow, Silicon Valley didn't get the memo…
</div>

I spent two years at a data visualization startup.
Three months before our first release,
the head of development "asked" us to start coming in on Saturdays.
We were already pulling one late night a week at that point
(without overtime pay—our boss seemed to think that
ten dollars' worth of pizza
was adequate compensation for four hours of work)
and most of us were also working at least a couple of hours at home in the evenings.
To no one's surprise,
we missed our "can't miss" deadline by ten weeks,
and had to follow up our 1.0 release with a 1.1 and then a 1.2
to fix the crash-and-lose-data bugs we'd created.
We were all zombies, and zombies can't code.

Hours like these are sadly still normal in many parts of the software industry,
and may actually be worse now that so many people are working from home.
Designing and building software is a creative act that requires a clear head;
it only takes a couple of minutes to create a bug
that will take hours to track down later.
As Robinson writes:

<div class="callout" markdown="1">
Productivity varies over the course of the workday,
with the greatest productivity occurring in the first four to six hours.
After enough hours,
productivity approaches zero;
eventually it becomes negative.
</div>

It's hard to quantify the productivity of programmers, testers, and UI designers
[[Sadowski2019b][Sadowski2019b], [Forsgren2021][Forsgren2021]],
but five eight-hour days per week has been proven to maximize long-term total output
in every industry that has ever been studied.
There is no reason to believe that ours is any different.

Ah, you say, but that's *long-term* output.
What about short bursts now and then,
like pulling an all-nighter to meet a deadline?
That's been studied too,
and the results aren't pleasant [[Fucci2018][Fucci2018]].
Your ability to think drops by 25 points for each 24 hours you're awake.
Put it another way,
the average person's IQ is only 75 after one all-nighter,
which puts them in the bottom 5% of the population.
Two all nighters in a row and their effective IQ is 50—the level at which
people are considered incapable of independent living.

The catch in all of this is that people usually don't notice their abilities declining.
Just like drunks who think they're still able to drive,
people who are deprived of sleep don't realize that they're not finishing their sentences (or thoughts).
They certainly don't realize that they're calling functions with parameters in the wrong order
or that the reason the tests are failing is that
they've forgotten to redeploy the application—again.

The first and most important lesson is therefore
to think about what's more important—how much you produce
or how much of a martyr you appear to be—and to pace yourself accordingly.

[Forsgren2021]: https://dl.acm.org/doi/10.1145/3454122.3454124
[Fucci2018]: https://arxiv.org/abs/1805.02544
[Fucci2020]: https://ieeexplore.ieee.org/document/8357494
[Robinson2005]: https://igda.org/resources-archive/why-crunch-mode-doesnt-work-six-lessons-2005/
[Sadowski2019b]: https://link.springer.com/book/10.1007/978-1-4842-4221-6
[Sedano17]: http://dx.doi.org/10.1109/icse.2017.20
