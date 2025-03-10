---
title: "How to Manage Confidential Data"
date: 2014-11-27
original: swc
---
<p>
  A couple of days ago,
  a member of our community wrote:
</p>
<blockquote>
  <p>
    I am very interested in working on improving research analytics in government
    using the principles developed by Software Carpentry.
    A key stumbling block I run into with my peers is their skepticism
    about these principles being able to protect data
    that is confidential or restricted use.
  </p>
</blockquote>
<p>
  I replied:
</p>
<blockquote>
  <p>
    One option is to put the software and the summary statistics you've extracted from the data out in the open,
    but keep the data itself locked up.
    If you do that,
    you may want to create a handful of files with faked data
    that has the same statistical characteristics as the real thing so that you can test your code,
    and so that other people have a sense of what the real stuff looks like.
    (A colleague here in Toronto spent a year developing a program to synthesize population data
    that had the same distributions of age, gender, income, and half a dozen other factors as the real stuff.
    He said afterward that building it gave him more insight into the real data
    than he could possibly have gotten any other way.)
  </p>
</blockquote>
<p>
  and their response was:
</p>
<blockquote>
  <p>
    I currently work for the Department of Public Instruction in [state].
    Much of the data I use is individually identifiable student records
    such as records of suspensions, expulsions, standardized assessment scores, etc.
    I have been working to switch our Department over to literate programming techniques
    and have had some modest success here.
    However,
    our office is small and often we find it beneficial to share our work and collaborate
    with other offices—but the confidential nature of the data puts it on ice. 
  </p>
  <p>
    I have been slowly building an R module to generate simulated datasets
    that "resemble" the data we use,
    but have to admit that the statistical details of
    how to appropriately approximate but not replicate confidential unit-record data
    are beyond me.
    I think this is a very worthwhile effort,
    and would love to learn from others about how they might be doing it. 
  </p>
</blockquote>
<p>
  So:
  how do <em>you</em> handle confidential data when you want to practice open science?
  What tips can you share,
  what examples can you point to,
  and most importantly,
  what could we add to our curriculum to teach people what they should do?
  Comments on this post would be greatly appreciated.
</p>
