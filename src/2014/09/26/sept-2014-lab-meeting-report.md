---
title: "September 2014 Lab Meeting Report"
date: 2014-09-26
original: swc
---

After a two-month break for a sprint and some holidays,
we held another monthly lab meeting this week.
About 50 people showed up to talk about issues large and small;
the key points are below.

-   As mentioned last week,
    we are asking specific people to take charge of particular topics in our core material.
    They will *not* be responsible for developing lessons themselves
    (though they may of course do so).
    Instead,
    their job will be to keep issues and pull requests moving by reviewing,
    managing discussion,
    merging into the master branch,
    and so on.
    Our initial maintainers are:
    -   Bash: Gabriel Devenyi and Christina Koch
    -   Git: Matt Davis and Jessica Hamrick
    -   Python: Azalee Bostroem and Trevor Bekolay
    -   SQL: Abigail Cabunoc and Sheldon McKay
    -   R: John Blischak and Denis Haine
    -   Mercurial: Doug Latornell
    -   MATLAB: Ashwin Srinath and Isabell Kiral-Kornek
    -   Build system: Raniere Silva and Rémi Emonet
    -   Windows installer: W. Trevor King and Ethan White

-   Related to this,
    we are going to break up the `bc` repository.
    It currently holds both our lessons and the templates for creating workshop sites,
    and has become too large and too complicated to manage.
    Our plan is to have a one-to-one match between repositories and lessons
    (e.g., the `novice/python` lesson will be in a small repository of its own);
    we're working out a detailed proposal,
    and hope to have it up early next week.
    Trevor King, Trevor Bekolay, Ré Emonet, and Erik Bray have volunteered to help
    with the Git magic that will be needed to do this without losing history–more help
    will be very welcome when the time comes,
    particularly from people who *aren't* Git experts,
    and can therefore tell us whether what we're doing is usable.

-   Greg Wilson's post on *Building a Better Teacher*
    and companion posts by Azalee Bostroem and Justin Kitzes
    have generated a lot of suggestions over the past three weeks
    about how we could share good teaching practices among our instructors.
    The specific suggestions made at this week's meeting were:
    -   *Match each new instructor with an experienced instructor as a mentor.*
        Azalee Bostroem,
        Erik Bray,
        Abigail Cabunoc,
        Matt Davis,
        Gabriel Devenyi,
        Ivan Gonzalez,
        Adina Howe
        Karin Lagesen,
        Bill Mills,
        Tracy Teal,
        and Naupaka Zimmerman
        all volunteered to be mentors;
        we'll match them with people who finished instructor training this summer.
    -   We'll set up a weekly or bi-weekly meeting in which
        people who have taught in the past couple of weeks
        can "hand off" what they've learned about the lessons
        to people who are going to teach in the coming couple of weeks.
        This will also be an opportunity for Greg Wilson to debrief recent instructors.
    -   We will ask instructors to send us their checklists after each workshop
        so that we can see what they actually did
        (and trim the things they didn't).
    -   We'll have "in-service days" a couple of times a year
        in which people who have been teaching for a while
        can find out what changes have been made to our lessons recently.

-   Before we break up the `bc` repository,
    we're going to simplify things by using `gh-pages` as the main branch
    (i.e., the starting point for new features)
    instead of the `master` branch.
    We have been using `master` as a staging area
    (i.e., as a development branch, with `gh-pages` as the release branch),
    but this has been causing confusion.
    We won't delete `master` until outstanding pull requests are merged,
    but we'll set up our new lesson repositories with `gh-pages` as their default.

-   Naupaka Zimmerman, Chris Kees, and Karin Lagesen volunteered to help us revamp
    our pre-assessment survey
    based on feedback we've received in the last few months.
    In particular,
    they'll make it easier to customize for particular workshops,
    and try to come up with questions that will help us discriminate more accurately
    between different levels of novice learner.

-   Daniel Chen has received about 15 descriptions of what was actually taught in various workshops
    from those workshops' instructors.
    He, Fan Yang, and Marios Isaakidis will use these descriptions
    to revamp our post-workshop instructor survey
    to help us learn more about how our lessons are actually being used,
    and how well they're working.

-   We're going to start using the term "workshop" instead of the term "bootcamp",
    since the latter is harder to translate in some languages,
    and has paramilitary connotations to some people.

Many thanks to everyone who took part in these meetings–we have a lot of work in front of us,
but a good crew to do it.

**Round 1 Attendees (18:30-19:30 Eastern on Thursday, Sept 25)**

-   Greg Wilson (Software Carpentry / Toronto)
-   Bennet Fauber (University of Michigan)
-   Matt Davis
-   Damien Irving (University of Melbourne)
-   Isabell Kiral-Kornek (University of Melbourne)
-   Ashwin Srinath (Clemson University, SC)
-   Trevor Bekolay (University of Waterloo)
-   Balamurugan Desinghu (University of Chicago)
-   Sarah Supp (Univ Wisconsin - Madison)
-   Azalee Bostroem (UC Davis)
-   Kirill Palamartchouk (Newcastle University, UK) Sorry, unable to type today
-   Raniere Silva (University of Campinas, Brazil)
-   Gabriel Devenyi (McGill University)
-   Rémi Emonet (University of Saint Étienne, FR)
-   Bill Mills (Mozilla Science Lab / Vancouver)
-   Trevor (Olympia)
-   Pauline Barmby (Western U, London Canada)
-   Jason Williams (Cold Spring Harbor Laboratory)

**Round 2 Attendees (11:00-12:00 Eastern time on Friday, Sept 26)**

-   Greg Wilson (Software Carpentry / Toronto)
-   Kristjan Onu (Gagest / Montreal)
-   John Blischak (University of Chicago)
-   Denis Haine (Université de Montréal)
-   Nichole Bennett (University of Texas/Okinawa Institute of Science and Technology)
-   Abigail Cabunoc (Mozilla Science Lab / Toronto)
-   Ethan White (Utah State Univ/Univ of Florida)
-   François Michonneau (University of Florida)
-   Naupaka Zimmerman (U of Arizona)
-   Lynne Williams (Child and Family Research Imaging Facility/Vancouver)
-   Jose Beltran (Stockholm University)
-   Adina Howe (Argonne National Lab)
-   Fan Yang (Iowa State University)
-   Arliss Collins (Mozilla Science Lab)
-   Karin Lagesen (University of Oslo)
-   Marios Isaakidis (Cyprus University of Technology)
-   Janet Riley (Cantina Consulting, Boston)
-   Tracy Teal (Michigan State)
-   Sheldon McKay (New York)
-   Robert Till (CUNY - John Jay)
-   Amy Brown (no fixed address/Toronto)
-   Ivan Gonzalez
-   Olav Vahtras (KTH Stockholm)
-   JC Leyder
-   Tom (Sickkids)
-   Stephen Turner (University of Virginia)
-   Erik Bray (STScI)
-   Daniel Chen (CUMC)
-   Chris Kees (ERDC/Coastal and Hydraulics Lab)
