---
title: "How to Write a Technical Book"
date: 2022-06-19
year: 2022
---

I have written three technical books
(with [one more][sdxjs] in the works),
co-written three more,
and edited six.
Here's what I've learned along the way:

1.  **Don't write a book**, at least not at first.
    It's a big undertaking, and it's easy to be discouraged.
    Instead,
    start blogging regularly:
    one article a week, each about a thousand words long.
    You don't have to write them in the order you think they'll eventually go into the book—in
    fact, one of the reasons to blog is to get a better idea of what you want to say—but
    you should try to stitch them together in multi-part sequences
    that can each eventually become a chapter.

2.  **Don't expect to make a profit.***
    Your publisher will give you anything from 12% to 50% of revenue in royalties;
    assuming a US$50 price tag and sales of a thousand copies,
    the most you can reasonably expect is US$25,000.
    It's going to take at least a few hundred hours to write the book,
    so in almost every case you'd be better off doing some contract coding.

    So why both writing?
    1.  *To build your reputation.*
        Several famous technical publishers lose money on the books,
        but make it back because they can charge more for the classes and workshops you teach
        because you're famous.
    2.  *To give back to the community.*
        None of us got here without help,
        and I think we have a moral obligation to repay that by helping others.
    3.  *Because you enjoy writing.*
        Some people like working with wood or wool;
        you might like working with words.

3.  **Start with one or two closely-aligned learner personas.**
    A [learner persona](https://teachtogether.tech/en/index.html#s:process-personas)
    is a short description of who you're trying to teach,
    what they already know,
    and what *they* want to learn.
    Create one or two that are fairly similar and write for them,
    because a book that's meant for everyone is actually useful to no-one.
    And keep in mind the difference between a novice (who is trying to build a mental model),
    a competent practitioner (who has one and wants to fill in gaps in their knowledge),
    and an expert (who wants higher-level discussion of tradeoffs and alternatives):
    no single book can serve all three well.

4.  **Don't write just to cover your ass.**
    I've read or reviewed dozens of books that start with a short introduction to XYZ;
    I cannot remember a single one that was actually useful.
    (If your audience knows Python, they don't need a chapter-length intro to the language.
    If they don't, a one-chapter intro isn't going to help them.)
    I eventually realized that authors included those short introductions
    so that they could claim the book was suitable for novices
    when they knew in their hearts it wasn't.
    Please don't do this.

5.  **Try it out in pieces.**
    I was once part of a team that spent a year and a half building a product
    before showing it to any potential users.
    To no-one's surprise except ours,
    it turned out that most of what we had written was irrelevant to their actual needs.
    Similarly,
    if I had run a workshop or course based on the material for my first book
    *while I was writing it*,
    I would have realized that one of my core assumptions was completely wrong
    while there was still time to correct it.
    Conferences are always looking for tutorials,
    your colleagues will probably welcome some lunch & learn sessions,
    and if all else fails you can create a YouTube channel
    to find out how your material sounds.

6.  **Plan to iterate.**
    There's no point trying material out if you don't incorporate what you've learned,
    and no matter how carefully you plan,
    you'll realize something about the content of Chapter 3 while writing Chapter 4 or 5.
    At a guess,
    every line of *[SDXJS][sdxjs]* has been rewritten at least twice,
    and a quick glance in the version control log tells me that
    some parts have been revisited over a dozen times.

7.  **Drywall, then paint.**
    In other words, get the words and code down,
    *then* worry about diagrams, bibliography citations, glossary entries, and so on.
    The word `FIXME` appeared over a hundred times in first draft of *[T3][t3]*;
    there's no easy way to count,
    but I bet that I changed or discarded more than half of those
    by the time the text settled down.

8.  **Accept that all available authoring tools suck.**
    I've used LaTeX, Microsoft Word, Markdown, and two flavors of computational notebook,
    and they're all more frustrating than they could be.
    I've written and spoken about this many times,
    so I won't belabor the point here,
    but please don't blame yourself.

9.  **Remember Wilkie's Law,**
    which states that an author's job is to produce the manure
    in which an editor grows something worth reading.
    You sweated over that paragraph, but your audience doesn't see your effort, they see your results.
    And yes, the explanation seems clear, concise, and elegant to you,
    but you are not your readers.
    By definition,
    your editor and reviewers are right when they say, "This doesn't make sense."
    Please accept that and revise accordingly.

10. **Don't be afraid to set it aside.**
    I wrote an introduction to R for Python programmers that will probably never see the light of day,
    and have stopped work yet again on an undergraduate guide to being a compassionate programmer.
    In both cases I lost faith in the project:
    the more I wrote,
    the less I believed the book would actually help its intended audience.
    I hope I'll get back to the second book eventually,
    but I won't feel ashamed if I don't:
    scientists don't expect every hypothesis to turn out to be true,
    and authors shouldn't either.

One last word of advice:
You'll spot a typo within seconds of receiving the first printed copy,
someone you've never met will say something uncomplimentary in a review online,
and Chapter 9 will *never* be as good as you wanted it to be.
To hell with all of that:
be proud of what you built and of who you helped by building it.

[sdxjs]: {{'/sdxjs/' | relative_url}}
[t3]: https://teachtogether.tech/
