---
title: "Python, JavaScript, and Boost"
date: 2006-02-22 14:28:51
year: 2006
---
<p>A few days ago, Brendan Eich wrote a <a href="http://weblogs.mozillazine.org/roadmap/archives/2006/02/js_and_python_news.html">thoughtful
post</a> on incorporating a few ideas from Python into JS 2.0
(specifically iterators, generators, and comprehensions, but that's
beside the point for the moment).  I replied:</p>

<blockquote><em>
t would be tremendously helpful if JS2 could standardize plugin APIs
in both C and C++ (and do the latter in a template-smart way). Having
simple C APIs accelerated the growth of Python and Ruby tremendously,
and (I believe) is crucial to getting JS accepted as a "traditional"
scripting and glue language. Standardizing "one way to do it" for C++
(esp. templated C++) would avoid a lot of the grief P&amp;R have gone
through.
</em></blockquote>

<p>Brendan's response was:</p>

<blockquote><em>
...for Mozilla, XPIDL and XPCOM (<a href="http://www.mozilla.org/scriptable/">http://www.mozilla.org/scriptable/</a>)
are the way to interface to "plugins" (generally construed)
implemented in other languages, not just C++ but also Python (a C
XPCOM binding could be done, and one was started, but there hasn't
been much interest). A truly painless C or C++ binding should work as
with OCaml -- that is,
<br />
<code>ocamlc foo.c</code>
<br />
This is a fine goal, but not something for ECMA TG1 to standardize
just yet. I would welcome a prototype for SpiderMonkey, if volunteers
capable of pulling it off are motivated.
<br />
Plugins loaded from the net are a different animal, requiring lots of
trust as well as highly compatible, stable APIs on both plugin and
browser sides of the fence.
</em></blockquote>

<p>I've argued <a href="http://www.ddj.com/documents/s=9776/ddj1126538834462/">elsewhere</a>
that Javascript could be the dominant scripting language five years
from now: it's sexy, it's (relatively) simple, and it's one of the two
languages every programmer has to learn (the other being C).  An easy
way to wrap and call legacy C/C++ code---one that handles C++ objects
and templates, rather than requiring programmers to pretend they're
C functions---would be a big step toward this.  <a href="http://www.boost.org/libs/python/doc/index.html">Boost.Python</a>
is the closest thing I've seen yet to a usable solution; if anyone out
there wants to be rich, famous, and popular, Boost.Javascript is just
begging to be created.</p>
