---
date: 2019-05-02 02:49
year: 2019
title: "Sexing Data Science Chickens"
---

The biggest problem in data science is its bias against people who aren't straight, affluent, white or Asian males.
Its second biggest problem, in my opinion, is that nobody talks about how they sex chickens.
After a long period of trial and error,
people can learn [how to tell at a glance whether a newborn chick is male or female][sexing].
The problem is, most of them don't know how they know:
they've trained the neural network between their ears,
but they don't have conscious access to their decision criteria.

Data scientists do something similar every day:
they decide that a result seems right enough for them to move on to the next problem.
In my experience,
only a handful make this decision consciously
or have explicit criteria (e.g., unit tests that pass).
Most just look at a result and think, "Good---now what's next?"

I really want to know what their heuristics are.
I really want to know how consistent they are from one data scientist to the next,
because I suspect that there's much more variation than we realize.
(As the joke goes,
physicists worry about decimal points,
astronomers worry about exponents,
and economists are happy if they've got the sign right.)
Mostly,
though,
I want to know so that I know what to teach.
It's easy to show people how to use a unit test framework,
but I predict that there's an inverse correlation between how easy tests are to write with the tools we have today
and the things that influence human judgment about whether answers are right enough.

One way to elicit understanding would be to have a couple of dozen data scientists think aloud
while working through a series of problems and trying to decide if there's a bug or not.
I'm sure there are other ways as well;
I'd be grateful for suggestions.

*Note: in response to a question on an early draft of this post,
I'm not necessarily talking about statistical significance when I talk about correctness.
Years ago I helped analyze a study of the spread of drug-resistant tuberculosis in Ontario hospitals.
Thanks to a bit of sloppy SQL,
I accidentally dropped all the records for everyone who didn't have a home address.
It turns out that if you don't include homeless people in a study like this it affects the answer...
Someone else caught the mistake less than an hour before we were going to submit the paper,
but I still wonder how many other non-obvious mistakes I've published.
The code didn't crash,
the graphs weren't flat---nothing smelled off to me.
I'm now a bit obsessive about checking for NULLs,
but I still managed to create a histogram recently in which all zero scores had silently been dropped.
Would a real data scientist have spotted that before sharing it with others?
If so, what would have run their alarm bells?*

[sexing]: https://psmag.com/magazine/the-lucrative-art-of-chicken-sexing
