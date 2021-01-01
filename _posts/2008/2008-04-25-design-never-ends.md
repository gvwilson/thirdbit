---
title: "Design Never Ends"
date: 2008-04-25 09:05:29
year: 2008
---
You're never done designing a useful system, because if it is actually useful, people are always coming up with new requirements for it.  For example, I've been using <a href="http://www.drproject.org">DrProject</a> to manage my software engineering course this term: the class notes are all in the wiki (so that students can fix 'em up), I communicate with students through the DrP-managed mailing list, and so on.  But now I want to archive that material in the portal used by the departmental lecturers, so that future instructors can find it after the current portal is shut down. Moving the SVN repository over is trivial, and dumping and restoring the relevant portions of the database needs just a few lines of SQL...

...and might well result in disaster, since keys that are unique in one database might well not be unique in another. The "All" project in one portal is definitely <em>not</em> the same as the "All" project in another; I could replace uses of "All" as a key in appropriate places, but what about the user ID "nick"?  The odds are good that it's the same person in both portals (since they're both hosted by our department, and we use unique Unix IDs wherever possible), but it's not guaranteed.

There are subtler problems too. Suppose there are no conflict in the user IDs I need to import to make ticket ownership and wiki page authorship references resolve.  I go ahead and add the users, import the data, and now the database believes that "nick" created some tickets and sent some email messages before his account existed.

How important is this?  Not very---there's no real cost to leaving the old portal up.  How irritating is it?  Quite---I like to keep things tidy, and having all the old courses in one place just seems like the right thing to do.  (We also had some people from California approach us earlier this week about converting their existing Trac instance to DrProject, during which a similar problem would arise.)  Never done...
