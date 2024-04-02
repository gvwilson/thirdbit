---
title: "Software Design by Example in Python 22: Serving Web Pages"
date: 2024-04-22
year: 2024
---

Having shown learners how to [transfer files][sdxpy_ftp] over TCP,
the next step is to explain how an HTTP server works
in [Chapter 22: Serving Web Pages][sdxpy_http].
The full story would fill several books,
so I focused on the fact that requests and responses are just formatted text
and on how to test a web server.

Looking at the material now,
I regret that I didn't devote a chapter to authentication.
I had [a bruising encounter with certificates][certificates] last month
while working on [another tutorial][sys_tutorial]
that left me believing there's a need for a scale-model tutorial of how they work,
but while a bunch of people wanted to *read* a book on [security by example][votes_are_in],
nobody wanted to help *write* it.
I suppose there's always the next life…

<img class="centered" src="{{'/sdxpy/http/concept_map.svg' | relative_url}}" alt="Concept map for a web server"/>

> Terms defined: body (of HTTP request or response), header (of HTTP request or response), HTTP, HTTP method, HTTP protocol version, HTTP request, HTTP response, HTTP status code, path resolution, query parameter, throw low, catch high, Universal Resource Locator.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[certificates]: {{'/2024/02/26/my-adventures-with-certificates/' | relative_url}}
[layout_post]: {{'/2024/04/14/page-layout/' | relative_url}}
[sdxpy_ftp]: {{'/sdxpy/ftp/' | relative_url}}
[sdxpy_http]: {{'/sdxpy/http/' | relative_url}}
[sys_tutorial]: https://gvwilson.github.io/sys-tutorial/
[votes_are_in]: {{'/2024/01/23/the-votes-are-in/' | relative_url}}
