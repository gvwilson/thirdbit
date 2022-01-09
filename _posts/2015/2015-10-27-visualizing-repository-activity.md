---
title: "Visualizing Repository Activity"
date: 2015-10-27 12:00:00
year: 2015
original: swc
---
<p>
  I am updating the
  lessons learned paper,
  and would like to include histograms showing how many people have contributed how often to our lessons.
  More specifically,
  I have 9 data sets (one for each lesson),
  ranging in size from 5 to 16 records,
  in which each record shows a number of commits and how many people have committed that often.
  For example,
  the data for our SQL lesson is:
</p>
<pre>num_contributions,num_contributors
1,8
2,8
3,2
4,3
6,3
8,2
10,1
25,1
28,1
30,1
106,1</pre>
<p>
  meaning eight people contributed once,
  eight contributed twice,
  and one contributed 106 times.
  What's the best way to visualize this,
  given the spread of values on the X axis?
  And what's the easiest way to generate that visualization in Python?
</p>
