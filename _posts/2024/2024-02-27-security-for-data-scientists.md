---
title: "Security for Data Scientists"
date: 2024-02-27
year: 2024
---

As a follow-on to [the SQL tutorial I've been writing][sql-tutorial],
I'd like to create a one-day tutorial on security for data scientists.
(My initial plan was [systems administration for data scientists][blog-sysadmin],
and I still hope to tackle that,
but "how to be safe" seems more important.)
The tutorial's goal isn't to turn data scientists into security professionals,
but to help them understand why they are asked to use certain tools
and/or do things in certain ways,
and how those tools and methods actually work.
Working on the first few episodes
motivated my need for [a clean way to run concurrent examples][blog-concurrent]
and my recent [adventures with certificates][blog-certificates];
here are a few other thoughts,
and [I'd be grateful for feedback](mailto:{{site.author.email}}).

## Audience

1.  Ning did a bachelor's degree in economics
    and now works as a data analyst for the Ministry of Health.
2.  They learned Python in an undergrad CS-1 course
    and used it in several stats courses,
    and are also comfortable working with Unix command-line tools,
    loading data from the web to use in those programs,
    and using Git and GitHub with one or two colleagues.
3.  Ning wants to automate some reporting for people in the Ministry,
    but is afraid of exposing confidential data or opening the Ministry up to attack.
4.  They need to learn enough about risks and security measures
    to have productive conversations with their IT team.

## Overview

1.  The focus is pulling, pushing, and storing data (e.g., pipelines)
    rather than building interactive applications (e.g., dashboards).
2.  Learners must be able to do all exercises in Python:
    in particular,
    it can't assume they know JavaScript.
3.  Examples and exercises (E&E) must run on Windows, macOS, and Linux
    (we assume they'll can use [WSL][wsl] on Windows).
4.  Strongly prefer E&E that run locally,
    i.e.,
    learners shouldn't have to set up cloud computing accounts.
    This restriction is primarily for portability:
    no matter what provider we pick,
    many learners won't have access to it or won't be able to afford it
    or their institution will be using something else or…
5.  Strongly prefer challenge-and-response,
    i.e.,
    show people how to do something the wrong way,
    explain what the problem is,
    and then show them the fix.

## The First Dozen Topics

I'm (re-)learning this material myself,
so this outline is more tentative and exploratory than usual;
again,
[I'd be grateful for feedback](mailto:{{site.author.email}}).

-   How the web works without any security considerations
    (so we know what we're improving on)
    -   How do I download a file programmatically rather than interactively?
        (Python's `requests` module)
    -   How does an HTTP GET actually work?
    -   How can I check the response?
        (HTTP status codes and response headers)
    -   How can I get data rather than a page?
        (Getting JSON with `requests`)
    -   How does a web server handle requests?
        (Python's `http.server` module with a static response)
-   Living in an imperfect world
    -   How to serve files
    -   What if those files don't exist?
    -   How an evildoer might use `..` to escape the server's sandbox
        (use `netcat` to bypass safeties in `requests`)
    -   Using query parameters to customize requests (e.g., slicing data)
    -   Malformed or malicious query parameters and poorly-formed URLs
-   Authentication
    -   Basic password auth and why not
    -   Giving the server a certificate that a browser will accept
    -   Creating a certificate that `requests` will accept (CA + signing)

[blog-certificates]: {{'/2024/02/26/my-adventures-with-certificates/' | relative_url}}
[blog-concurrent]: {{'/2024/02/17/concurrent-examples/' | relative_url}}
[blog-sysadmin]: {{'/2024/02/05/sys-admin-for-data-scientists-challenges/' | relative_url}}
[sql-tutorial]: https://gvwilson.github.io/sql-tutorial/
[wsl]: https://learn.microsoft.com/en-us/windows/wsl/
