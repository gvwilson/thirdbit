---
title: "Playing the Kazoo"
date: 2014-05-05
original: swc
---
<p>
  Yesterday,
  Matt Davis quoted Peter Wang as saying,
  "A violin is to a kazoo as Python is to Excel."
  To which I replied,
  "Exactly: anyone who wants to make music can play a kazoo right away without days of training."
  The difference between these two points of view lies at the heart of Software Carpentry.
  As I said in a post two years ago:
</p>
<blockquote>
  <p>
    Suppose you have a processing pipeline with three stages:
  </p>
  <p>
    <img src="@root/files/2012/03/pipeline.png" class="centered">
  </p>
  <p>
    Each stage takes one second to run; what's its overall performance?
    As Roger Hockney pointed out in the 1980s, that question isn't well formed.
    What we really need to ask is, how does its performance change [with] the size of its input?
    It takes 3 seconds to process one piece of data, 4 to process two…and so on.
    Inverting those numbers, its rate is 1/3 result per second for one piece of data, 1/2 result/sec for two, etc.:
  </p>
  <p>
    <img src="@root/files/2012/03/curve.png" class="centered">
  </p>
  <p>
    Any pipeline's curve can be characterized by <em>r<sub>&infin;</sub></em>,
    which is its performance on an infinitely large data set,
    and <em>n<sub>1/2</sub></em>,
    which is how much data we have to provide to get half of that theoretical peak performance…
  </p>
  <p>
    …twenty (!) years ago,
    I <a href="http://www.amazon.com/Practical-Programming-Scientific-Engineering-Computation/dp/0262231867/">said</a>
    that the more interesting measure…was actually <em>p<sub>1/2</sub></em>,
    which is how many programming hours it takes to reach half of a machine's theoretical peak performance…
    [Software Carpentry]'s goal is to increase researchers' <em>r<sub>&infin;</sub></em>,
    i.e., to help them produce new science faster.
    Our <em>challenge</em> is to minimize <em>p<sub>1/2</sub></em> so that researchers see benefits early.
  </p>
  <p>
    In fact, our real challenge is that learners' performance over time actually looks like this:
  </p>
  <p>
    <img src="@root/files/2012/03/final.png" class="centered">
  </p>
  <p id="glass-law">
    That dip is due to Glass's Law: every innovation initially slows you down.
    If the dip is too deep,
    or if it takes too long to recover from it,
    most people go back to doing things the way they're used to, because that's the safest bet.
  </p>
</blockquote>
<p>
  I've never met Peter Wang,
  but I'll bet that,
  like Matt Davis,
  he chose at some point in his career
  to delay gratification in order to maximize <em>r<sub>&infin;</sub></em>.
  Most researchers make a different choice:
  they would rather get today's work done today
  than bang their heads against a wall for a couple of weeks
  until they understand a new set of tools well enough
  to get back to where they were.
</p>
<p>
  What frustrates me is that
  the dip in the curve above isn't dictated by the laws of nature:
  it's there because programmers like me put it there.
  Spreadsheets don't have to be minefields for the unwary;
  there's no reason version control systems couldn't diff and merge
  the document formats used by WYSIWYG editors
  (see <a href="http://nbdiff.org">NBDiff</a> for proof),
  and the inconsistencies between the hundred and one flavors of Markdown,
  or between the flags taken by common Unix commands,
  are middle fingers raised to the whole world.
</p>
<p>
  Not long after writing the tweet that opened this article,
  Matt described a partial solution to the <em>p<sub>1/2</sub></em> problem:
  "If <a href="http://ipythonblocks.org">ipythonblocks</a> is an onramp for arrays and image processing,
  can an equivalent be made for your favorite computational library/process?"
  His work,
  and Mike Hansen's on
  <a href="http://github.com/synesthesiam/novice">a novice image processing module</a>,
  are proof that we can give learners an early payoff
  to convince them stay the course.
  We need more of them:
  if you're interested in helping to create them,
  please <a href="mailto:gvwilson@third-bit.com">get in touch</a>.
</p>
