---
title: "Changes to DrProject's Ticketing System"
date: 2006-12-16
---
Here's a draft proposal for modifying DrProject's ticketing system based on feedback from the post-mortem:
<ol>
  <li>State is simply "open" or "closed", and becomes implicit: the buttons to update a ticket are labeled "Preview", "Update", and "Close".</li>
  <li>Tickets can be assigned to roles, as well as to specific users, so that if an organization distinguishes "tester" from "developer", tickets can be marked accordingly.</li>
  <li>Get rid of "type": if people want to distinguish different kinds of tickets, they can evolve a set of tags.  (This is the same argument we used to get rid of the "component" field inherited from Trac.)</li>
</ol>
Still unsure what to do about actual and estimated effort: companies want it, but we know that student teams won't use it (or that if they do, their numbers will be science fiction).  Is a "small/medium/large" pulldown when filing the ticket enough, if people can adjust it again when closing the ticket to show actual effort?
