---
title: Mastodon and Webbly
date: 2025-09-05
---

I was going to title this post "Two Great Tastes That Taste Great Together",
but I expect most of my readers are too young to get the reference,
so I'll just dive right in:

1.  Glitch gave literally millions of people a chance to build something on the web
    without having to wrestle with NPM or webpack
    or set up a server
    or deal with any of the other crap that Sumana Harihareswara has dubbed
    [inessential weirdness][iw].
    It was beautiful and useful,
    but it wasn't profitable enough for Fastly to keep it alive.

1.  But the idea of a low-overhead in-the-browser way for the 99% to build things
    didn't start with Glitch
    and hasn't died with it either.
    Projects like [Webbly][webbly] (source [here][webbly-gh])
    are still trying to let people use the web to build the web.
    However,
    someone has to host these things somewhere:
    who's going to do that, and where?
    More specifically,
    can we construct a hosting solution that isn't tied to a particular company
    and therefore doesn't have a singular point of failure?

1.  Well,
    what about [Mastodon][mastodon]?
    Its authors and users are deeply committed to decentralization and federation,
    and more people are running servers for particular communities every day.
    What if (wait, hear me out)
    what if Webbly was bundled with Mastodon
    so that Mastodon site admins could provide an in-the-browser page-building experience to their users
    simply by saying "yes" to one configuration option?

1.  Why would they do that?
    My answer is,
    "Take a look at Mastodon's default browser interface."
    It lets you add a couple of pictures and a few links to your profile,
    but that's less than [MySpace][myspace] offered twenty years ago.
    I am 100% certain that if Mastodon came with an easy in-browser page builder,
    people would use it to create all sorts of wonderful things.
    (Awful ones too, of course, but Mastodon site admins already have to grapple with content admin.)

[Greenspun's Tenth Rule][greenspun] is that every sufficiently complicated program
contains a mediocre implementation of Lisp.
Equally,
I think every useful web-based tool is trying to be
what Visual Basic was in the 1990s
and WordPress was to the early web:
useful, right there, and a gradual ramp for new users rather than a cliff to climb.
I think the sort of people who built useful little things with Glitch
would do amazing things with Webbly
if it was married to their social media.
I also think that allowing people to create custom home pages
or tweak their feeds
would draw a lot of new users away from fragile, centralized systems like X and Bluesky.
I know that I've been wrong far more often than I've been right,
but this really does feel promising.

[greenspun]: https://en.wikipedia.org/wiki/Greenspun%27s_tenth_rule
[iw]: https://www.harihareswara.net/posts/2016/inessential-weirdnesses-in-open-source-software-oscon-2016/
[mastodon]: https://en.wikipedia.org/wiki/Mastodon_(social_network)
[myspace]: https://en.wikipedia.org/wiki/Myspace
[webbly]: https://make.webblythings.com/
[webbly-gh]: https://github.com/pomax/make-webbly-things
