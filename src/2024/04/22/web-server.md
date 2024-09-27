---
title: "Software Design by Example in Python 22: Serving Web Pages"
date: 2024-04-22
---

Having shown learners how to [transfer files][sdxpy_ftp] over TCP,
the next step is to explain how an HTTP server works,
which is what [Chapter 22: Serving Web Pages][sdxpy_http] does.
The full story would fill several books,
so I focused on the fact that requests and responses are just formatted text
and on how to test a web server.

Looking at the material now,
I regret that I didn't devote a chapter to authentication.
I had [a bruising encounter with certificates][certificates] last month
that left me believing there's a need for a scale-model tutorial of how they work,
but while a bunch of people wanted to *read* a book on [security by example][votes_are_in],
nobody wanted to help *write* it.
I suppose there's always the next life…

<img class="centered" src="@root/sdxpy/http/concept_map.svg" alt="Concept map for a web server"/>

> Terms defined: body (of HTTP request or response), header (of HTTP request or response), HTTP, HTTP method, HTTP protocol version, HTTP request, HTTP response, HTTP status code, path resolution, query parameter, throw low, catch high, Universal Resource Locator.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[certificates]: @root/2024/02/26/my-adventures-with-certificates/
[layout_post]: @root/2024/04/14/page-layout/
[sdxpy_ftp]: @root/sdxpy/ftp/
[sdxpy_http]: @root/sdxpy/http/
[votes_are_in]: @root/2024/01/23/the-votes-are-in/
