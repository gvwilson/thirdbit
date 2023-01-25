---
title: "How Long Is This MP4?"
date: 2010-10-05 01:31:11
year: 2010
---
We have made over 50 videos for <a href="https://software-carpentry.org/">Software Carpentry</a> so far, and as part of reorganizing the site, we want to list their lengths beside their names. If they were text files, I'd use <code>wc(1)</code> to find their size–but what do I do for MP4 files?  After a few false starts [1] I found <a href="http://ffmpeg.org/">ffmpeg</a>'s ffplay, and the following command:
<pre>ffplay -an -vn -stats ${filename} 2&gt;&amp;amp1 | grep Duration | sed -e 's/,.*//' -e 's/ *Duration: *//'</pre>
It isn't pretty–my screen flickers uncomfortably as ffplay launches and closes down for each file–but it works.

[1] My first stop was <a href="http://www.pyglet.org/">Pyglet</a>, but after installing from their DMG download on Mac OS X 10.6, every attempt to do anything more than <code>import pyglet</code> results in a QuickTime error.
