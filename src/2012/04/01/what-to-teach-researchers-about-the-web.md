---
date: 2012-04-01
original: swc
title: What to Teach Researchers About the Web
---
<p>One reason I'm reflecting on what I've learned in the last two years is a question that is back on the top of my work pile: what should we teach researchers about the web? Partly, it's a priority because I'm currently embedded in Mozilla; their mandate is to defend and extend the open web, and their educational efforts are all aimed at that, so I ought to be doing something too. The real reason, though, is that a lot of things have brought this into sharper focus recently:</p>
<ol>
<li>Audrey Watters' investigation of what and how to teach people about webmaking (summarized in <a href="http://openmatt.org/2012/03/28/audrey-watters/">this short talk</a> and <a href="http://hackeducation.com/2012/03/17/what-every-techie-should-know-about-education/">the Audrey Test</a>).</li>
<li>Mark Guzdial's commentary on <a href="http://computinged.wordpress.com/2012/03/30/getting-the-level-right-in-learning-to-be-computationally-literate/">getting the level right</a> (and everything else he's been writing for the last year).</li>
<li>Jon Udell's "<a href="http://blog.jonudell.net/2011/05/17/awakened-grains-of-sand/">Awakened Grains of Sand</a>" and "<a href="http://blog.jonudell.net/2012/03/30/tags-for-democracy/">Tags for Democracy</a>" posts (and everything else <em>he</em> has been writing for the last year too).</li>
<li>Michelle Levesque's thoughts on <a href="http://rwxweb.wordpress.com/2012/03/08/which-web-skills-come-first/">what Mozilla</a> <a href="http://rwxweb.wordpress.com/2012/01/30/web-literacy-skills-now-in-diagram-form/">should teach</a>.</li>
</ol>
<p>Here's what (I think) I've figured out so far:</p>
<ol>
<li>People want to solve real problems with real tools.</li>
<li>Styling HTML5 pages with CSS and making them interactive with Javascript aren't core needs for researchers.</li>
<li>All we can teach people about server-side programming in a few hours is how to create security holes, even if we use modern frameworks.</li>
<li>People <em>must</em> be able to debug what they build. If they can't, they won't be able to apply their knowledge to similar problems on their own.</li>
</ol>
<p>Jon Udell has summed up the <a href="http://blog.jonudell.net/2011/01/24/seven-ways-to-think-like-the-web/">big ideas</a> they ought to know. In concrete terms, we want them to understand</p>
<ol>
<li>how to construct (and deconstruct) URLs;</li>
<li>how an HTTP request/response is processed;</li>
<li>pass by value vs pass by reference, push vs. pull, structured vs. unstructured data; and</li>
<li>how a few common security problems arise.</li>
</ol>
<p>So what can we teach people that meets these goals, and respects our constraints?</p>
<ol>
<li><em>Visualize this</em>: plug an interactive Javascript visualization engine into a web page, show them how to put their data somewhere accessible, and voila: interactive data exploration on the web. This would be fun, but it would fail our debuggability/reproducibility requirement.</li>
<li><em><a href="http://opendap.org/">OpenDAP</a></em> is a framework for sharing the kind of grid-based data that's common in the earth sciences. Setting up a server would be out of reach, but formatting query URLs to pull data from public servers would be within reach, and we could easily run such a server on our site to provide a stable target. My concerns are (a) it's only showing learners half of the equation, and (b) it's not directly relevant to people in genomics and other fields.</li>
<li><em><a href="http://www.kynetx.com/">Kynetx</a></em> (as described in Phil Windley's book <a href="http://www.amazon.com/The-Live-Web-Event-Based-Connections/dp/1133686680/"><cite>The Live Web</cite></a>) is a framework for handling event streams. It's very cool, but it's still very young, and I don't know any scientists who are using it.</li>
<li><em>Read dynamic, write static</em>: download data from several sites, merge it, and produce some static HTML pages that other people can then download and merge. This is a common pattern in real life (especially when run periodically by <code>cron</code>), and with a little bit more work, we can show people that they only need to download things that have changed. On the downside, it's not really dynamic or interactive, and I want people to see that the web is more than just a bunch of pipes that deliver documents.</li>
</ol>
