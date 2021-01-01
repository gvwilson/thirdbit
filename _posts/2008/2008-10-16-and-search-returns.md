---
title: "And Search Returns...?"
date: 2008-10-16 11:50:00
year: 2008
---
Here's a design challenge for anyone who wants it: what should search return?  More specifically, suppose you have something like <a href="http://www.drproject.org">DrProject</a>, which stores tickets and wiki pages in a relational database, and revisions to files using a standard Subversion repository. Tickets are identified by ticket number (it's actually the pair [projectId, ticketId], but never mind that for now), while wiki pages are identified by their names (which are strings), and repository entries are identified by a combination of path and version number (e.g., [/trunk/license.txt, 33]). If one ticket, one wiki page, and one file contain the word "Turing", what should 'search("Turing")' return?

Should it be a set of URLs?  I need those eventually if I'm building a web page to display the results, but that feels like mixing two levels---my instinct is that I should be returning "things" that are then converted to URLs.  (For example, if I'm running a command-line admin tool on the desktop, I probably don't want URLs coming out of my search function...)

What about returning a set of pairs, where each pair is [type-of-thing, thing-id], e.g., ["wiki", "Authors"] or ["ticket", 127]?  That feels wrong because it will force all the client code (e.g., the stuff that creates URLs for HTML pages, and the command-line admin tool) to do a type-switch in order to fetch and process the actual items.

OK, so what about defining an abstract base class called 'SearchResult', then require each component of DrProject to subclass it, so that we have 'TicketSearchResult', 'WikiSearchResult', and so on?  These classes could provide 'getItem()' methods to fetch the content that matches, 'toUrl(baseUrl)' methods to create links, and so on.  That feels like a better fit than either of the previous ideas, but I'm still dissatisfied.  Is there a cleaner way to do this that I just don't know about?  If so, I'd welcome a pointer...
