---
title: "Tables"
date: 2018-03-09
---

An imagined dialog:

A: I'm building a brand-new kind of relational database.

B: Cool. What's new about it?

A: It stores everything in tables.

B: That doesn't sound very new.

A: No, I mean it actually stores everything in tables. You use a text editor to type a table like this in a text file:

```
| CommonName   | ScientificName            |
| Anchorwhip   | Flagellanguis viridis     |
| Flooer       | Florifacies mirabila      |
| Hiri-hiri    | Carnophilius ophicaudatus |
| Oakleaf toad | Grima frondiforme         |
| Shalloth     | Arboverspertilio apteryx  |
```

B: That's…interesting. How do you enforce data types and uniqueness constraints?

A: Oh, you can't.

B: Ah. And what happens if people forget to type the right number of bar characters?

A: Well, obviously they shouldn't do that. But if they do, the database prints an error message as it's loading the table.

B: Ah. Wouldn't it be more efficient to use B+ trees or [some other machine-friendly format](https://en.wikipedia.org/wiki/Database_storage_structures) for storage and then *present* the database as a table?

A: Maybe, but then people couldn't edit it with Vim or Emacs, could they?

B: No, but—

A: And they couldn't use `wc` and `grep` and other command-line tools on their data.

B: Not directly, but—

A: So you see, my way is clearly better.

I could have written this using CAD drawings instead,
or made the case that everyone should type in hexadecimal color codes pixel by pixel to create image files,
but I think you get the picture.
Fourteen years after [I confidently predicted](https://queue.acm.org/detail.cfm?id=1039534)
that we would soon separate models from views for programming,
just like we do for every other sophisticated highly-structured kind of data we work with,
I still can't embed a diagram directly in my source files,
or insert an actual table in my code,
or do any of a dozen other things that I have been able to do with desktop office software for more than 20 years.
Even [the most innovative work in this field](https://cacm.acm.org/magazines/2018/3/225475-a-programmable-programming-language/fulltext)
still seems to treat character-by-character ASCII as an immutable law of nature
rather than as the technological tonsil that it actually is.

Maybe we'll go around it.
Maybe the people working on blocks-based languages and structure editors
will provide ways for people to express their ideas they way *they* want to,
regardless of whether those expressions have a simple, directly-editable character representation.
Maybe programming tools will allow art as well as prose before I write my last program.
Maybe,
but I'm no longer as hopeful as I was [seven years ago](@root/2011/09/16/extensible-programming-a-new-hope/).

(Species names from Dougal Dixon's marvelous *[After Man](https://www.amazon.com/After-Man-Zoology-Published-Hardcover/dp/B00HQ0Y31O/)*.)
