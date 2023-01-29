---
title: "Perforce: For beginners only…"
date: 2006-06-23 15:22:32
year: 2006
---
Perforce certainly has a stellar reputation amongst software
developers; Perforce for real projects, and your choice of open source
version control system if you cannot afford to foot the Perforce bill.
This naturally leads to the idea that Perforce is for power users,
whereas systems like CVS or Subversion are for beginners.  After a few
days using Perforce, however, (I had only ever used Subversion/CVS in the past), I noticed a striking contrast between the two groups that seems to contradict this.

Consider the standard use case for a version control system: editing files, and then committing those changes back to the repository.  If you are using Subversion, you simply edit the files in place.  When you are ready to commit, you issue a 'status' command to get a quick overview of files that have been changed, files that have been added, and files that have been deleted.  You may choose to add some files that are not under version control, revert some files that shouldn't have been edited, and then issue the commit command to finalize your session.

Now consider the same case under Perforce.  You go to edit your first file, only to realize that it is read-only, requiring you to first 'open it for edit'.  After a number of edits, you decide you need to add a new module to your program.  Don't forget to add this file to
Perforce, because as far as I know, there is no way in Perforce to get a list of files that are not under version control.  How many times has someone in your organization broken the build because they forgot to add a new file to Perforce? You then decide that you want to run a script to edit a large number of files.  After you have modified these files to be read-write, you run the script, but then realize Perforce has not picked up the changes in 'Pending Changelists' screen.  Of course not, because you didn't explicitly open these files for edit! After you are ready, you issue the 'submit' command to check in your
changes.

Can you spot the difference?  With Subversion, the version control system is not forcing you to be aware of your changes until you are ready to commit.  With Perforce, you constantly have to be on top of your changes <em>during development</em>.  Perforce is forcing you to think about version control while programming.  While Subversion silently sits
in the background, Perforce is constantly poking you in the back whenever you want to do something.  Could you get any work done if someone was doing that in real life?

The real issue boils down to Power Users vs Beginners.  Perforce holds your hand and puts in restrictive measures to ensure you don't break things.  This is great for beginners, but quickly becomes annoying and frustrating for experienced users.

What about the other features of Perforce?  Surely they must justify the 800$ per head price tag?  Maybe, but as a developer, I'm focused on the edit-resolve-commit cycle for 95% of my time.  Get out of the way and let me work.  Now who broke that build…
