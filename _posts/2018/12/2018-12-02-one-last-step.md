---
layout: post
date: 2018-12-02 11:24
title: "One Last Step"
---

I've been [saying for a while]({{site.github.url}}/2017/05/22/numerical-javascript.html)
that within a few years,
most people who are analyzing data will be doing it in JavaScript.
It has an enormous user base,
great tooling,
libraries for doing almost everything else,
much higher performance than most people realize,
and will soon (thanks to [Arrow](https://arrow.apache.org/))
have bindings to a high-performance SIMD calculation engine.

But after reading Ashley Davis's new book
*[Data Wrangling with JavaScript](https://www.manning.com/books/data-wrangling-with-javascript)*
(which I enjoyed a lot, and will write more about soon),
I think one big obstacle remains,
and that is the lack of operator overloading.
Most of the languages people use for crunching data let you add vectors with `a+b` rather than `a.add(b)`,
and R's pipe operator `%>%` is the cornerstone of a thriving menagerie of user-friendly data manipulation tools.
It's easy to label this syntactic sugar,
but it's more like syntactic crack or syntactic bacon sushi:
once you've had a taste,
you won't ever want to go back.

So I did a bit of digging and asked a couple of people,
and if I understand correctly,
the main reason JavaScript doesn't have operator overloading is that
people can't see a way to implement it that won't hit performance,
and it isn't important enough for mainstream programming to justify that.
But that sounds like exactly the kind of problem that an ambitious grad student who's interested in languages
could sink her teeth into.
[This talk](https://www.keithcirkel.co.uk/proposal-operator-overloading/) from Keith Cirkel outlines a few ideas,
and if it can only be done efficiently for TypeScript rather than pure JavaScript,
that would still be pretty honking awesome.
