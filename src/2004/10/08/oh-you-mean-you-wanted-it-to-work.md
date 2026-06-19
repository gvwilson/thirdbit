---
title: "Oh, You Mean You Wanted It to *Work*…"
date: 2004-10-08
category: education programming
---
Finally back on track building a simple Hibernate example to give future generations of students…or am I?  In case you haven't been following along, I had my project laid out as follows:

-   build.xml
-   hibernate.cfg.xml
-   src/User.hbm.xml
-   src/Test.java

After building, I had all of the above, plus:

-   gen/User.java
-   class/User.hbml.xml
-   class/User.class
-   class/Test.class
-   class/hibernate.cfg.xml

Why copy the .hbm.xml and .cfg.xml files to the class directory?  Because they have to be on the classpath at runtime, and I'm eventually going to deploy only what's in class.

Great—now let's try to run it.  Hm, missing a couple of JAR files… No problem, I can copy them out of hibernate-2.1/lib (I'm doing this on-demand, since I want a minimal set of JARs when I deploy).  But wait—even once all the required JARs are there, I still can't run my test class.

Mutter, mutter… *whack* as my forehead bounces off the wall again… Guess what?  It turns out that Hibernate *doesn't* read settings from hibernate.cfg.xml at startup, even if said file is on the classpath.  It'll read from hibernate.properties, but you can't list your .hbm.xml mapping files in a .properties file.  So, your options are:

1.  Duplicate information (never a good idea).
1.  Separate information (i.e. put some settings in hibernate.properties, and some in your Java code).

*sigh* All right, I'll do the latter, and there's another half hour lost googling, flipping through books, and trying things out.  Go ahead, ask me whether I'm looking forward to adding JUnit to this stew…
