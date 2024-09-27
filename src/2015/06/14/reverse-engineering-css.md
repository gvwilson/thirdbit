---
title: "Reverse Engineering CSS"
date: 2015-06-14
---
<p>
  Software Carpentry's lessons
  are written in <a href="http://daringfireball.net/projects/markdown/">Markdown</a>,
  then transformed into HTML using <a href="http://pandoc.org/">Pandoc</a>
  which is styled using <a href="http://getbootstrap.com/css/">Bootstrap</a>
  with a bunch of custom styles layered on top.
  For a bunch of historical reasons,
  we translate Markdown that looks like this:
</p>
<pre>
&gt; ## Learning Objectives {.objectives}
&gt;
&gt; *   Learning objective 1
&gt; *   Learning objective 2
</pre>
<p>
  into sections that look like this:
</p>
<pre>
&lt;section class="objectives panel panel-warning"&gt;
  &lt;div class="panel-heading"&gt;
    &lt;h2 id="learning-objectives"&gt;&lt;span class="glyphicon glyphicon-certificate"&gt;&lt;/span&gt;Learning Objectives&lt;/h2&gt;
  &lt;/div&gt;
  &lt;div class="panel-body"&gt;
    &lt;ul&gt;
      &lt;li&gt;Learning objective 1&lt;/li&gt;
      &lt;li&gt;Learning objective 2&lt;/li&gt;
    &lt;/ul&gt;
  &lt;/div&gt;
&lt;/section&gt;
</pre>
<p>
  We'd like to simplify the HTML we generate to be:
</p>
<pre>
&lt;blockquote class="objectives"&gt;
  &lt;h2&gt;Learning Objectives&lt;/h2&gt;
  &lt;ul&gt;
    &lt;li&gt;Learning objective 1&lt;/li&gt;
    &lt;li&gt;Learning objective 2&lt;/li&gt;
  &lt;/ul&gt;
&lt;/blockquote&gt;
</pre>
<p>
  Are there tools that will help extract or reverse engineer
  a minimal set of CSS definitions
  on top of Bootstrap
  so that our pages look the same as they do now?
  If so,
  the source for the existing format is in
  this GitHub repo
  and the new version is coming together in this one.
</p>
