---
title: "Many Ways to Break"
date: 2007-01-21 13:14:34
year: 2007
---
One of the driving forces behind DrProject was instructors' need for a scripting API to support batch operations (such as creating one repository for each pair of students in a course, or filing the same ticket against each team).  We have mostly succeeded, but as we discovered last week, that just means that we've introduced another place for bugs to breed.

The problem was this: when I created projects using the web-based administration interface, students could access the associated repositories without any trouble.  When I created the project from the command line, using the drproject-admin tool (which is just a text-based wrapper around the same Python that the web system uses), students couldn't check out their repositories.  The reason?  Out of habit, I'd typed:

sudo drproject-admin /home/courses/csc407/drp project create g0llum

rather than:

sudo -u csc407 drproject-admin /home/courses/csc407/drp project create g0llum

The result?  The files in the repository were owned by root, which meant that Apache couldn't read them.  Once the files were owned by the csc407 dummy user, everything worked fine.

Update: and it appears that after this happens, the .svn_access file that controls who can get at particular repositories isn't updated any longer, and no error message is generated.  I have some patching to do…
