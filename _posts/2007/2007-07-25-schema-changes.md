---
title: "Schema Changes"
date: 2007-07-25 15:22:50
year: 2007
---
A while back, I posted a handmade picture of <a href="http://www.drproject.org">DrProject</a>'s database schema. Thanks to <a href="http://www.minq.se/products/dbvis/screens.html">DB Visualizer</a>, we now have pictures of the 1.2 database schema, and the new-and-improved schema that works with <a href="http://www.sqlalchemy.org/">SQLAlchemy</a> and <a href="http://elixir.ematia.de/">Elixir</a>.  Alex and DW are starting work on a migration tool to translate from the latter to the former; those of you who have done this before will want to wish them good luck :-). According to Alex:
<blockquote>What's really cool about this diagram is that it shows a topological
ordering of the graph of foreign keys, so if we migrate the rightmost
tables first, we shouldn't run into any foreign key constraint
violation problems!</blockquote>
