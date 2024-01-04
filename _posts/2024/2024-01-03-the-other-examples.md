---
title: "The Other Examples"
date: 2024-01-03
year: 2024
---

I'm not going to write another book in the *Software Design by Example* series,
but if I did,
it would have one of three flavors:

1.  [*Research Software Design by Example*][rsdx]
    would be for budding research software engineers
    who have (mostly) taught themselves how to program
    and want to move from one-off data analysis scripts
    to reusable libraries and applications.
    I outlined a series of examples for this book late last year;
    if you'd like to see it through,
    please [reach out][email].

2.  *Pure Functional Software Design by Example*
    would implement the same kinds of examples as [*SDXJS*][sdxjs] and [*SDXPY*][sdxpy]
    but (as the name suggests) in a pure functional language like [Haskell][haskell] or [Roc][roc].
    I've been thinking about doing this since a conversation with Simon Peyton-Jones over two decades ago,
    and it would force me to finally come to grips with PF languages.
    It would also take at least a year of full-time work,
    since I'd have to learn how to think in a purely functional style before I could tackle it.

3.  *Concurrent Software Design by Example*.
    [Solastalgia][solastalgia] is a form of homesickness
    one gets when one is still at home but the environment has changed.
    I increasingly suffer from computational solastalgia:
    while I was focused on teaching basic skills,
    applications became networked and moved into the cloud.
    Examples of timeouts, authentication, data replication, stream processing,
    and everything else that has taken the place of manual memory management in programmers' hurt list
    would be useful and (I believe) fun.

    However,
    the chapters of the existing *Software Design* books averaged 25 hours of work each,
    not including end-to-end proofreading and discussions with the publisher.
    I believe concurrent and distributed equivalents would be 3X harder to design, build, debug, and explain,
    so this book would require approximately 1800 hours total.
    On top of that,
    I haven't built anything more complex than straightforward client/server applications since I finished my PhD 30 years ago,
    and the concurrency tools in the languages I speak well (Python, JavaScript, C) are wearying to wrestle with.
    [Pony][pony] and [Gleam][gleam] look interesting—the former would scratch my "very strongly typed" itch like most pure functional languages
    while the latter would give me a chance to learn a bit about [Erlang][erlang] as well—but again,
    I'd have to spend a year getting comfortable with the language and paradigm
    before I could start designing things.

So like I said,
I'm not going to tackle these books.
If you want to,
though,
I think they would help a lot of people.
I'm always [happy to chat][email].

*Later: see [the next post in this series][fourth-example].*

[email]: mailto:{{site.author.email}}
[fourth-example]:  {{'/2024/01/04/the-fourth-example/' | relative_url}}
[erlang]: https://www.erlang.org/
[gleam]: https://gleam.run/
[haskell]: https://www.haskell.org/
[pony]: https://www.ponylang.io/
[roc]: https://www.roc-lang.org/
[rsdx]: https://gvwilson.github.io/rsdx/
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxpy]: {{'/sdxpy/' | relative_url}}
[solastalgia]: https://en.wikipedia.org/wiki/Solastalgia
