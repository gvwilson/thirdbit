---
title: "Numerical JavaScript"
date: 2017-05-22 05:00:00
---

I have a terrible record when it comes to making predictions,
but there is one notable exception.
In 2002,
I told a room full of Python programmers in Toronto
that they would all be writing JavaScript in ten years' time.
My argument was that since it was the only choice for front-end web programming,
it was the one language everyone *had* to learn,
and was therefore going to be the safest bet for back-end projects as well.

I spent the next fifteen years
cracking jokes about JavaScript's many failings as a language.
Since changing jobs a few months ago,
though,
I've had to come to grips with its most modern version (ES6),
and have been pleasantly surprised.
Yes,
there are plenty of unpleasant surprises left over from its initial hasty design:

    [] + [] → ""              // Concatenating two empty arrays produces a string
    [] + {} → [object object] // Empty array plus empty object creates an object…
    {} + [] → 0               // …but empty object plus empty array is 0…
    {} + {} → NaN             // …and adding two objects is Not A Number

but there are many pleasant surprises too,
and derivatives like [TypeScript](https://www.typescriptlang.org/)
are as comfortable and robust as anything I've ever used.

I am therefore going to make another prediction.
Ten years from now,
I believe that JavaScript (or a derivative with optional strong typing)
will have supplanted Python and R
as the language of choice for people doing leading-edge open scientific computing.
My reasoning is the same as it was in 2002:
no matter what else programmers use,
they eventually have to learn JavaScript.
What's more,
projects like [Apache Arrow](https://arrow.apache.org/)
are going to make it easier to add a high-performance numerical substrate.

The most important qualifier in the preceding paragraph is probably "leading-edge".
Most people crunching numbers today are still using things like MATLAB and Excel,
and I don't expect that to change.
What I expect instead is that the 5-15% of scientists who are early adopters of new technology
will bypass single-purpose languages like Julia
in favor of the one they're already mastering
in order to take advantage of [D3](https://d3js.org/) and its ilk.
And with major players like Microsoft, Google, and Facebook all working hard
to make general-purpose JavaScript faster,
it will be harder and harder for niche players to keep up.
I've been wrong far more often than I've been right,
but everything I know about how and why computing evolves points this way.
