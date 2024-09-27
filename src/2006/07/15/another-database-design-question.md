---
title: "Another Database Design Question"
date: 2006-07-15
---
Apple Viriyakattiyaporn is adding tagging and <a href="http://en.wikipedia.org/wiki/Tag_clouds">tag clouds</a> to DrProject this summer, and an interesting database design problem has come up. She wants to be able to tag tickets, wiki pages, milestones, and email messages. (For the moment, tags will be added to email messages after the fact, rather than when they're sent.) She also wants to be able to search for items with particular tags as easily as possible, <em>and</em> allow people who are writing new components for DrProject to add tagging to those components with minimal grief.

The problem is that different things inside DrProject are keyed in different ways. The key for a ticket is [project, ticket_number], which is [string, integer].  (It's actually [project, ticket_number, revision_number], since we keep old versions of tickets, but the third field doesn't matter for now.) The keys for wiki pages, on the other hand, are [project, page_name], which is [string, string].

So how should tags be stored? Option #1 is to have a separate tag table for each component table, i.e., a TICKET_TAGS table containing [project, ticket_number, tag], a WIKIPAGE_TAGS table containing [project, page_name, tag], and so on. That's simple to write, but not extensible: every time a new tagged component is added, DrProject needs to be told to search its tag table.

Option #2: put all the tags in a single table [component_name, project, component_key, tag]. Search is now easy—but what's the type of component_key, integer or string? We can stringify integer keys, but that makes it clumsier to look up tags for integer-keyed components, and if we ever have a component with a multi-part primary key, we'll be in a real mess.

Option #3: all tags for integer-keyed items in one table, while those for string-keyed items go in another.  Again, it'll work, but the SQL to find all items with a particular tag isn't pretty.

Option #4: add a unique integer ID to every item that is currently string-keyed, and use [project, component_name, integer_id, tag] for the tags table. It's doable, but saying that the keys for string-keyed tables now have two parts (the string and the integer) messes up the integrity constraints a bit.

For the moment, Apple is going with option #2, i.e., stringifying integer keys and hoping for the best.  I'd be interested to hear what other people think—is there a more elegant way out of this?
