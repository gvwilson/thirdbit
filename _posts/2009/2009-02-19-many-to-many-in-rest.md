---
title: "Many-to-Many in REST?"
date: 2009-02-19 10:00:51
year: 2009
---
Still trying to wrap my head around REST, and have a question for the lazyweb.  Suppose my app contains users and groups, with a many-to-many relationship between them (i.e., a user can belong to any number of groups, and a group can contain any number of users.  I can identify users as /app/user/fred, /app/user/jane, etc., and use GET/POST/PUT/DELETE to fetch, create, update, and delete.  (Yeah, I know, GPPD != CRUD, but you get the idea.)  I can similarly use /app/project/red and /app/project/green to identify projects, but what should I use to identify memberships?  /app/project/green/user/fred?  Nope: it mixes category identifiers ('project', 'user') and item identifiers ('green', 'fred'), and more importantly, implies that users are sub-categories of projects—it would be just as logical to use /app/user/fred/project/green, which means that both are probably wrong.

In the relational database world, of course, many-to-many relationships are almost always represented by introducing new entities, such as a tuple &lt;&lt;17238917, 'fred', 'green'&gt;&gt; (where 17238917 is a magic number created by the system for its own use, and not exposed to the outside world).  Is that the right way to do many-to-many in REST?  I.e., should /app/membership/17238917 return the pair &lt;&lt;'fred', 'green'&gt;&gt;, while /app/project/green/members returns a list of magic membership tuple IDs, and /app/user/fred/groups returns ditto?  What's the right (or at least most common) way to do this?
