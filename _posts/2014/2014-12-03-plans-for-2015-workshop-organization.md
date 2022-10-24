---
title: "Plans for 2015: Workshop Organization"
date: 2014-12-03 09:20:00
year: 2014
original: swc
---
<p>
  As I write this,
  228 people have been certified to teach Software Carpentry workshops,
  of whom 136 have taught in the past twelve months.
  That's amazing,
  but as I said in a previous post,
  growth in one part of a pipeline inevitably turns another into a bottleneck.
  In our case,
  that bottleneck is organizational:
  Arliss Collins
  and Giacomo Peru
  are stretched to the limit handling requests and lining up instructors,
  and we're still not keeping up with demand.
</p>
<p>
  This kind of work can't be done by a volunteers in bits and pieces:
  the startup overheads are significant,
  as is the context required to manage each conversation,
  and there are time when mail really needs to be answered right now,
  not when it's convenient.
  We are therefore asking our Partners
  to organize workshops in their region,
  and hope that others will shoulder some of the burden as well.
</p>
<p>
  We're also trying once again to build a tool to simplify workshop management.
  I have started a simple Django application called Amy
  to keep track of who wants a workshop,
  who can teach what,
  who our learners have been,
  and so on.
  The data model is mostly done,
  and I've included a dump of our existing database
  with personal information redacted
  to aid further development and testing.
</p>
<p>
  All Amy can do now is display information.
  What we want to do is add and edit new data.
  If you'd like to help,
  please fork the project
  and send us pull requests&mdash;we'd be grateful for your help.
</p>
<div align="center">
  <a href="{{'/amy' | relative_url}}"><img src="{{'/files/2014/12/amy-logo.png' | relative_url}}" alt="Amy Logo" /></a>
</div>
