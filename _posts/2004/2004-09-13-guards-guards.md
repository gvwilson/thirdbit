---
title: "Guards! Guards!"
date: 2004-09-13 21:32:40
year: 2004
---
<p>I'm a big fan of <a href="http://www.terrypratchetbooks.com">Terry Pratchet</a>.  How can you <em>not</em> be a fan of someone who dedicates a book to "the Palace Guard, the City Guard, or the Patrol... Whatever the name, their purpose...is identical: to rush into the room, attack the hero one at a time, and be slaughtered..."</p>

<p><a href="http://www.eclipse.org/">Eclipse</a> and <a href="http://subversion.tigris.org">Subversion</a> made me feel like one of those poor guys today.  Here's what happened:</p>

<p>1. I checked out a copy of Hippo onto my laptop, and created a directory in which to do the training exercise we've assigned to the incoming students.</p>

<p>2. I fired up <a href="http://www.eclipse.org/">Eclipse</a> to create a Java project in that directory.  I put my Java source files in a sub-directory called <code>src</code>, the JAR files my project needed in a sub-directory called <code>lib</code>, and created an empty directory called <code>bin</code> for <a href="http://www.eclipse.org/">Eclipse</a> to put compiled class files in.  I used <code>svn add</code> to add all three directories to the repository.</p>

<p>3. Reading the <a href="http://www.hibernate.org">Hibernate</a> documentation, I thought I had to put the mapping file that described how to store my Java objects in a database in the same directory as the compiled class files.  All right, no problem—I created <code>bin/LoanRecord.hbm.xml</code>, and used <code>svn add</code> to add it to the repository.</p>

<p>At this point, my workspace looked like this:</p>

<pre>
.project                        # Eclipse project file
.classpath                      # Eclipse classpath file
.svn/                           # Subversion metadata
bin/
    .svn/
    LoanRecord.hbm.xml          # Hibernate metadata
lib/
    .svn/
    hibernate2.jar
    hsqldb.jar
src/
    .svn/
    LoanRecord.java             # my one and only source file
</pre>

<p>4.  I started up <a href="http://www.eclipse.org/">Eclipse</a> again, and rebuilt the project, then dropped back to the shell to check the project's status with <a href="http://subversion.tigris.org">Subversion</a>:</p>

<pre>
$ svn status
?      bin/LoanRecord.class
    S  bin
!      bin/LoanRecord.java
</pre>

<p>Uh, what?  I understand that SVN doesn't know about the class files in the <code>bin</code> directory, but what's with the "S"?  And why does it think that there ought to be a file called <code>bin/LoanRecord.java</code>?</p>

<p>An hour and a half later, after chatting with Ben Collins-Sussman and others on the <a href="http://subversion.tigris.org">Subversion</a> IRC channel, we [<a href="#1">1</a>] have an answer.  When <a href="http://www.eclipse.org/">Eclipse</a> builds your code, it copies the <code>.svn</code> sub-directory from the <code>src</code> directory into the output <code>bin</code> directory.  Yup, you heard that right: <em><a href="http://www.eclipse.org">Eclipse</a> overwrites the <code>.svn</code> sub-directory in <code>bin</code> when it compiles</em> [<a href="#2">2</a>].</p>

<p>Now, if I could track down <a href="http://www.eclipse.org">Eclipse</a>'s developers, they would probably either say, "It's not our fault—<a href="http://subversion.tigris.org">Subversion</a> didn't even exist when we started work," or, "Yeah, yeah, we know, our bad, sorry," but I wouldn't accept either.  I <em>might</em> forgive them if <a href="http://www.eclipse.org">Eclipse</a> popped up a dialog saying, "Hey, you have some files here that I don't know anything about, do you mind if I crush them?", but it doesn't even do that.  Trampling on files and directories that aren't yours is just plain rude; anyone who has been programming for more than a few months ought to know better.</p>

<p>The fix is simple: don't add the <code>bin</code> directory to the repository [<a href="#3">3</a>]. But let's do some math.  Assume there are 10,000 <a href="http://subversion.tigris.org">Subversion</a> users out there.  Assume that a quarter of them are using <a href="http://www.eclipse.org">Eclipse</a>, and that one in ten of those make the same mistake I did (adding the compile output directory to the repository).  If each one of them wastes two hours figuring this out (half the time it took us), that's 500 hours, or twelve and a half working weeks.  You can write a <em>lot</em> of software in twelve and a half weeks...</p>

<p>Which is what we have to do, now that <a href="http://www.eclipse.org">Eclipse</a> isn't getting in the way.  Onward!</p>

<p>[<a name="1">1</a>] David James, Michelle Levesque, and Greg Wilson.</p>

<p>[<a name="2">2</a>] <a href="http://www.eclipse.org">Eclipse</a> <em>doesn't</em> do this to <code>CVS</code> sub-directories, presumably because its developers use CVS themselves, and fixed the problem the first time it came up.  Favoritism, that's what that is...</p>

<p>[<a name="3">3</a>] We tried using <a href="http://www.eclipse.org">Eclipse</a>'s inclusin/exclusion filters to prevent it from overwriting the <code>bin/.svn</code> sub-directory, but couldn't get that to work.</p>
