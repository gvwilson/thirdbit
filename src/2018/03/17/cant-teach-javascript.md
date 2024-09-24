---
title: "I Can't (Quite) Teach JavaScript"
date: 2018-03-17
---

I've been thinking about what tools I would use to teach librarians how to crunch data
if I was starting today with a blank slate,
and I have reluctantly concluded that I can't (quite) use JavaScript.
I hope my reasons for considering it,
and my reasons for saying "no",
may both interest people.

First, why consider it at all?
The answer is simple:
if you want to build anything interactive on the web,
it's the only viable choice.
Yes,
there are cross-compilers for other languages,
but when it comes to tooling, community, and everything else,
JavaScript is to the web what Latin was to the Medieval church
or the twelve-bar blues is to jazz.

But that's not the whole answer any more.
I was surprised last year to discover that modern JavaScript
is a very solid language for server-side programming.
Yes,
it has retained some awkward features from its younger days,
but no more so than (for example) C++ or R,
and Node has a wealth of libraries to do pretty much anything you might want to do
(except high-performance number crunching,
but [that would be easy to fix](@root/2017/05/22/numerical-javascript/)).
While I haven't finished my introduction to JavaScript for scientists,
what I have so far has convinced me that it's a good choice for everyday tasks.

However,
JavaScript is *not* suitable for teaching novices how to write 30-line programs
to clean up legacy accession records with regular expressions and stuff them into a relational database.
The reason is the ubiquity of asynchronous execution via callbacks, promises, and async/await.
Sequential control flow is hard enough for people to wrap their heads around;
"set this up now to run later" is much, much harder,
and while a few of the core Node file I/O libraries do support synchronous operations,
there's simply no way to avoid having to deal with it in the first few lessons of a JavaScript-based course.

"Oh come on," I hear you say, "It's not that bad, is it?"
Well yeah, it is.
Bobby Brennan's blog post about [upgrading to asynch/await](https://medium.com/datafire-io/upgrading-to-async-await-with-javascript-es7-3c67602ea7f8)
is well-written, as gentle as it can be,
and completely out of reach for people who are still struggling to understand what loops actually do.
As just one example,
think about how many things someone needs to understand
in order to understand when they can use `Array.forEach`
and when they have to use `Promise.all`.
A course can't just start with `for` loops,
then introduce `Array.forEach`,
and then go on to promises and async/await
because the Node library functions we want to call repeatedly are asynchronous.

I don't know where this leaves me.
I really want people to be able to build interactive browser applications by the end of the semester,
but I don't want them to have to learn two languages to get there.
What I *do* know is that the world would be a better place
if language designers adopted tutorial-driven design:
write the lessons that introduce newcomers to the language,
then implement the features those tutorials require.
