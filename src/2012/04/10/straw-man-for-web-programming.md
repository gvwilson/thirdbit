---
date: 2012-04-10
original: swc
title: Straw Man for Web Programming
---
<p>Last week, I asked what we should teach researchers about the web. I think that I have an answer, and that the easiest way to describe it is by describing what we want learners to be able to build when we're done. So, imagine you are studying changes in rainfall due to climate change in North America. As part of that work, you're comparing results from your simulation with historical data from Environment Canada. Since your calculations may be useful to other scientists, you want to share them on the web. You are therefore going to build a command-line tool so that:</p>
<pre>rainy path-to-index.html start-date end-date location</pre>
<p>adds a new entry to your online results page by:</p>
<ol>
<li>reading data from the Environment Canada database,</li>
<li>comparing those historical values to your predictions, and</li>
<li>adding an entry to <code>index.html</code> showing the results.</li>
</ol>
<p>In order to do this, you will need to understand:</p>
<ul>
<li>how HTTP GET with query parameters works;</li>
<li>how to pull things out of XML data (I believe that's what Environment Canada will give us–no sign of JSON on their site); and</li>
<li>how to create HTML programmatically.</li>
</ul>
<p>More fundamentally, they'll see the fetch-remix-publish cycle that underpins so much of the web. Their tool won't be interactive–we won't try to turn it into a CGI script, because doing so would open up too many cans of worms–but I think we can actually do the above in half a day if people are already familiar with something like Python.</p>
<p>Thoughts?</p>
