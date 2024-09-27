---
title: "Database Schema to Support Customizable/Extensible Application"
date: 2007-02-20
---
We want to redesign the ticketing system of DrProject so that different sites can customize it to meet their needs.  Students in undergrad courses just need an ordered to-do list; companies need all the fields we currently have (with a few more values for some of the enumerations), and one or two more as well.

Coincidentally, Jeremy Miller had a post earlier this week asking the same question I've been mulling over: <a href="http://codebetter.com/blogs/jeremy.miller/archive/2007/02/19/How-do-you-extend-and-customize-a-database_3F00_.aspx">what should the database schema look like to support extensibility</a>? His options are:
<ol>
  <li>Allow sites to add customs fields to the database—madness lies in this direction.</li>
  <li>Use "wildcard" fields (which for my money is just option #1 with poor column names).</li>
  <li>Use name/value extension tables.</li>
  <li>Structure the fields (e.g., store XML). I <em>think</em> this is #1 with angle brackets, but I'm not sure…</li>
</ol>
Have you been there?  Done that?  If so, what would you recommend?  Keep in mind that testability is as important to us as extensibility…
