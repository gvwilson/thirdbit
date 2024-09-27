---
date: 2018-07-05
title: "Isaac Ezer's Dragnet"
---

<p>
  I wrote a description last year of
  <a href="@root/2017/10/16/exercise-types/">different kinds of exercises people use when teaching programming</a>.
  In it,
  I talked about the many kinds of things that could be implemented by dragging and dropping labels on diagrams,
  from matching problems to tracing execution and even Parsons Problems.
</p>
<p>
  Well,
  <a href="http://www.isaacezer.com/">Isaac Ezer</a> went ahead and created a prototype.
  A map of Canada is stored as an SVG with the labels in the correct places
  but surrounded by double curly braces like <code>{% raw %}{{Ontario}}{% endraw %}</code>;
  you could create a diagram of your own using any vector drawing tool
  without doing any programming.
  Isaac's <a href="https://github.com/iezer/dragnet">Dragnet</a> library
  searches the SVG for labels of this kind and pulls them over to the site.
  To complete the exercise,
  you click on the labels and drag them onto the <code>--</code> markers
  that the library has placed where they were.
</p>
<p>
  A finished tool would need more bells and whistles,
  like a re-set button to move all the labels back to the menu on the right,
  but this is pretty awesome for 147 lines of JavaScript.
  If you'd like to help improve it,
  please fork <a href="https://github.com/iezer/dragnet">its GitHub repository</a>
  and submit some pull requests.
  And if you're a computing education researcher and you'd like to do some studies
  of whether diagram labelling and execution tracing help people learn to code,
  please get in touch.
</p>
