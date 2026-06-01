---
title: "Ant + Eclipse = More Pain"
date: 2004-10-08
category: software
---

The biggest problem with classpaths is that there is no standard way of defining them.  Classpaths can be set through environment variables (which have an OS-specific syntax), command-line arguments to the VM, system properties (which can be set through the command-line or a properties file), and even by arbitrary code running within a JVM.

For instance, Eclipse keeps track of classpaths for individual projects through the `.classpath` XML file in the project's root directory.

Ant, on the other hand, builds its classpath from many places.  It looks through environment variables (`CLASSPATH` and `ANT_OPTS`, in particular), the system properties, and the build script that's currently loaded.  On top of that, Ant uses at least two distinct classloaders, which maintain their own individual classpaths: one for loading Ant, the tasks, and their dependencies, and one for for actually executing the tasks.

When you put Eclipse and Ant together, the potential for distaster increases exponentially.

About four-hundred revisions back in time (revision 94, to be exact), I changed the build file around to unify the data model of Hippo with the UI layer, which used to be contained within separate Eclipse projects.  Like all servlet-based web applications, the UI layer stored its class files in `$WEBAPP_ROOT/WEB-INF/classes`.  The test case classes were stored in `build/test`.

In the meantime, Eclipse's `.classpath` file was still set to compile all classes directly into the `build` directory.

This isn't a problem if you use Eclipse's build system exclusively to build and run your code.  It's also not a problem if you use Ant to exclusively build and run your code.

However, if Ant and Eclipse's classpath configurations are not in sync (which has been the case from revision 94 up to just a few days ago) and you use Ant to build and Eclipse to run, you will get many `ClassNotFoundException`s.

Why did that happen?  Eclipse was set to compile classes into the `build` directory.  Therefore, it added the `build` directory to its default runtime classpath.

When you use Ant to build the project, Ant stores the compiled class files in two places.  The test classes are saved in `build/test` while everything else is put into `$WEBAPP_ROOT/WEB-INF/classes`.

Now when you go to run the tests in Eclipse, Eclipse looks for them in `build`, but they're really stored in `build/test` and `$WEBAPP_ROOT/WEB-INF/classes`.

So what's the solution?  Configure Ant so that its build process is in sync with Eclipse.  Right now, this is being done redundantly and manually, but I'm sure with a little extra effort, Ant can be taught to read Eclipse's `.classpath` configuration automatically.

