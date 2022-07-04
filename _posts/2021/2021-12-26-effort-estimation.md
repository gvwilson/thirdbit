---
title: "Effort Estimation"
date: 2021-12-26
year: 2021
---

A month ago I [wrote]({{site.github.url}}/2021/11/23/not-what-i-set-out-to-do/) about
[*Software Design by Example using JavaScript*]({{'/sdxjs/' | relative_url}})
and how it fell short of what I'd hoped to create.
Part of the problem is that from a teaching point of view,
JavaScript is still crippled by design decisions made in haste in its early days.
Python is an obvious alternative,
and I hope a Python version of the book will exist some day,
but Python is no longer a small language:
I'm now twelve weeks into my first full-time programming job in over a decade,
and I'm a little dumbfounded by how much Python now looks and feels like Enterprise Java.

It's easy to say,
"Just ignore decorators and async I/O and the `:=` operator in class,"
but that's disingenuous.
Newcomers will bump into these things as soon as they search online for help,
because they actually are helpful for people who are programming in the large;
that's just not my use case.

So what about teaching with something that's still small?
[Lua](https://www.lua.org/) is the right size, and well documented,
but I'm unwilling to invest in a language
[whose development is not open](http://lua-users.org/lists/lua-l/2008-06/msg00407.html).
[Wren](https://wren.io/) is about the right size,
but its syntax will be a bit offputting for my target audience;
its derivative [Dictu](https://dictu-lang.com/) will be more approachable,
and it has the beginnings of a decent standard library.

But life is short, and always getting shorter.
I've invested about 50 hours so far working through the second half of
Nystrom's excellent [*Crafting Interpreters*](https://craftinginterpreters.com/)
and enhancing the source of Lox (the little language it builds)
to include array and table primitives and a few other features.
Based on that,
and on a comparison of the size of Dictu's source code with
a need-to-have list based on [*SDXJS*]({{'/sdxjs/' | relative_url}}),
I estimate it would take about 200 hours to turn Dictu into
what I'd want to take a second run at a book on software tools
(which itself would only take about another 200 hours,
since I've already done most of the required thinking).
400 hours is pretty much all of my hobby time for 2022,
and there are other things I want to do more,
so reluctantly---very reluctantly---I'm probably going to have to shelve this one.

Which is a shame,
because (a) I've been enjoying writing low-level code again,
(b) I've been learning stuff, which I always enjoy,
and (c) despite [a long string of failures]({{site.github.url}}/2020/07/09/acm-sigsoft-award/),
I think the final product would help a lot of people.
If I still had access to a pool of senior undergraduates in need of thesis projects
I might reach a different answer;
as it is,
I think this I should mothball the repository and turn my attention elsewhere.

[soundtrack](https://www.youtube.com/watch?v=dpN_kpbVo3U)
