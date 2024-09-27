---
title: "DrProject Internals: I Wasn't Quite Done With Tickets"
date: 2006-11-06
---
OK, we're not quite done with tickets yet—at least, not with the issues that tickets raise.

The first one is email notification.  In Trac and many other systems, you can specify that you want to receive email every time a ticket that you filed is updated.  This is a lot handier than logging in every once in a while and asking the system to display all the tickets you created that have been modified in the last, um, six days? Ten?  When did I last log in, anyway?

We took this out of DrProject because we thought there wouldn't be a need for it.  It's common in industrial-strength systems to open up ticketing to customers and users, so that (a) the number of people who can file tickets is much greater than the number who will be dealing with them, and (b) many of the people filing tickets aren't "members" of the project in any sense.  In contrast, the primary use case for DrProject is lots of little teams, each of which is developing the software primarily for itself.  Since DrProject supports per-project RSS feeds (see below), email notification of changes to tickets seemed redundant.

Well, we [1] were wrong.  Even on a two-person team, people like to be poked when tickets they care about change (or when new tickets are assigned to them).  What we failed to take into account is that students are slicing their time between many different courses; it is very useful for them to have their attention drawn to things as they happen, and email is still the best way to do that.

Turning email notification in specific circumstances back on won't be too hard.  What will be is generalizing it, so that people can (a) specify a rule for when they want notification, and (b) override that rule to be notified (or not) for specific tickets.  For example, as an instructor, I might want to set things up so that I'm only notified about changes to tickets assigned to me, and not to tickets I created, since I'm going to be filing dozens or hundreds of tickets over the course of a term to give students work.  I might also want to add myself as an observer of particular tickets that I didn't create, and that I'm not supposed to be working on.  It isn't rocket science, but it's going to be a grumpy bear to test.

And speaking of RSS: like Trac, DrProject creates an RSS feed (in DrProject's case, one per project) that summarizes the events occurring in a project.  Ticket changes, Subversion check-ins, wiki page edits, and the like are all turned into blog entries.  It's a great way to keep track of what's going on in projects, particularly if you're trying to monitor a dozen at once.

Unfortunately, we've had to disable the RSS feeds for our undergraduates' course projects.  We can't allow one team to see another team's RSS feed, since check-in comments and ticket bodies can contain sensitive information [2].  If we could password-protect the RSS feeds, we would, but there isn't yet a standard way for blog readers to forward credentials.  (And even if there was, we wouldn't be comfortable with students storing the passwords for their lab accounts on web-based feed readers like <a href="http://www.bloglines.com">Bloglines</a>.)  We don't see any way to fix this one…

Another feature of Trac that we've dropped is custom ticket queries.  The idea is seductive: allow users to write arbitrary queries against the ticket database, store them, and create links that trigger them, so that other users can run the same or similar queries. This is a complete non-starter in our context: there is no way we're going to allow students to run their SQL against a shared multi-project database.  That said, it would be nice if there was a way to capture and save the settings someone is using to view the ticket database, so that people could share their favorite views on what it contains…

The last [sic] part of the ticketing system we'd like to revisit is the set of actions users are allowed to perform.  Right now, you have three choices when you update a ticket: leave it open, mark it as complete, or reject it.  No matter what you do, you're supposed to write a short comment explaining your action (just as you're supposed to write comments when you check files into Subversion).

This is working well, but doesn't capture one important use case. The more users a project has, the more likely it is that someone will file a ticket that duplicates one filed earlier.  At present, we rely on users to write something like "Duplicates #456" when the reject redundant tickets; all three of the companies that are thinking about adopting DrProject internally would like something a little more structured, so that they can (for example) search for tickets that were duplicates.

The reason we haven't done this is that it complicates our representation of ticket states.  Right now, states are taken from an enumeration with three values; if we want to add "duplicate" as a fourth state, we have to add another field to keep track of which ticket (or tickets) this one is a duplicate of—fields that wouldn't be meaningful in other states.  Irregularities like this are bad news for maintenance and testing; we won't add "duplicate" until we can think of a way to avoid this one.

Of course, suggestions are always welcome…

<hr />[1] This is a royal "we"…

[2] Yes, the world would be a better place if students could share information and learn from one another.  However, part of our job is to evaluate their work, and we need to be sure that it's <em>their</em> work, which limits how much <del>plagiarism</del> sharing we can allow.
