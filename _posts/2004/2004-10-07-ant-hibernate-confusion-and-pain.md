---
title: "Ant + Hibernate = Confusion and Pain"
date: 2004-10-07 12:07:26
year: 2004
---
<p>Once again, an attempt to get two stable, mature, well-documented open source Java tools to talk to each other has resulted in several hours of frustration, as well as all the bad karma associated with using Those Words (as my Grade 3 teacher called them) out loud.  I finally figured out how to avoid the problem, but I still don't understand why it happens in the first place.  If any Ant and/or Hibernate gurus would care to enlighten me, I would be grateful.</p>

<p>Here's what happened:</p>

<dl>

<dt>Background</dt>
<dd><p>I wanted to create a near-trivial example application to introduce future generations of students to Hibernate (an object/relational mapping framework for Java).  Hibernate gives developers two options: write a JavaBean class, then write a mapping file to describe how that class's members map to database tables, or write the mapping file, and then have Hibernate generate the JavaBean class.  Half of this fall's students did it one way, half did it the other; based on their experiences, I decided to go the code generation route.</p></dd>

<dt>Setup</dt>
<dd><p>I created four files:
    <ul>
        <li><code>hibernate.cfg.xml</code>: the Hibernate configuration file.</li>
        <li><code>build.xml</code>: the Ant build file.  (If you haven't seen Ant, it's a pure-Java replacement for Make, which has become the standard build tool for Java programming).</li>
        <li><code>src/User.hbm.xml</code>: the Hibernate mapping file for my <code>User</code> class.</li>
        <li><code>src/Test.java</code>: a simple test program.  I initially used JUnit, but when things started to go pear-shaped [<a href="#1">1</a>], I yanked it out in an attempt to isolate the problem.</li>
    </ul>
    Note that my source files are in a <code>src</code> directory.  <code>build.xml</code> creates two output directories at the start of the build process: one called <code>gen</code>, for generated code, and another called <code>class</code>, for compiled <code>.class</code> files.</li>

<li><code>build.xml</code> has four targets:
    <ol>
        <li><code>clean</code>: deletes the <code>gen</code> and <code>class</code> directories, and also the <code>data</code> directory (described below).</li>
        <li><code>codegen</code>: invokes Hibernate's <code>Hbm2JavaTask</code> to generate <code>gen/User.java</code> from <code>src/User.hbm.xml</code>.</li>
        <li><code>compile</code>: compiles <code>gen/User.java</code> and <code>src/Test.java</code> to create <code>class/User.class</code> and <code>class/Test.class</code>.</li>
        <li><code>schema</code>: creates a <code>data</code> directory, and invokes Hibernate's <code>SchemaExportTask</code> to generate database schema files in that directory.  <code>SchemaExportTask</code> reads <code>src/User.hbm.xml</code>, checks that it's consistent with <code>class/User.class</code>  (compile-time checking—excellent), and creates <code>data/hippo.log</code> and <code>data/hippo.properties</code>, which between them tell HSQLDB (the database I'm using) what table(s) to create, and how.</li>
    </ol>
</p></dd>

<dt>The first hour and a half</dt>
<dd><p>The examples in Hibernate in Action (the book I'm using) show several examples of <code>hibernate.properties</code> files, which use the older Java properties file syntax, but when it comes to XML configuration files, the book says, "Go see your install documentation."  I didn't find that documentation helpful; in particular, it wasn't clear when the XML configuration file's properties had to have the same names as were used in the plain text configuration file, and when they had to be different.  Hibernate's error messages didn't help at all: all I could do to debug was make more-or-less random changes to the configuration file, and see what effect they had.</p></dd>

<dt>The next hour and a half</dt>
<dd><p>I finally annealed [<a href="#2">2</a>] my configuration file into a working state.  A fresh cup of tea, and I was ready to start making some progress—except now Ant was unhappy.  The four targets in <code>build.xml</code> are linearly dependent: <code>schema</code> depends on <code>compile</code>, while <code>compile</code> depends on <code>codegen</code>.  <code>ant schema</code> should therefore erase the working directories, generate <code>gen/User.java</code>, compile it and <code>src/Test.java</code>, and generate a database schema.</p>
<p>When I tried it, the first three steps worked perfectly, but schema generation failed with an error message saying, "Unable to read User.class".  My first thought was that this was yet another classpath problem, but then I discovered that if I ran <code>ant schema</code> again, <em>without</em> running <code>ant clean</code> in between, Ant and Hibernate would generate my schema for me.</p>
<p>After ninety minutes and a lot of bad language, I convinced myself that this was some sort of timing problem.  If I ran <code>ant compile</code>, then ran the schema-generation target on its own, everything worked.  If I left the dependency between the <code>schema</code> and <code>compile</code> targets in <code>build.xml</code>, and tried to do everything in a single Ant run, it failed.  I went so far as to revive a little Python inventory tool I wrote a while back, which walked through the directory tree, recording timestamps, file sizes, and MD5 checksums.  As far as I could tell, there was no difference in the files generated by running Ant in two steps, versus running it in one.</p>
<p>And no, it isn't Windows-specific: I get exactly the same behavior on Debian Linux...</p>
</dd>

</dl>

<p>At this point, I know how to work around the problem (run Ant twice), and could go back to working on my Hibernate example.  But how am I going to explain this to students?  "Hi, everyone, this term we're going to be using Ant.  It's a replacement for Make, and sometimes, well, sometimes you just have to run it a couple of times to get it to work."  I don't think it's acceptable for software to act like a spoiled six-year-old ("I won't! I won't! I won't I won't I won't and you can't make me!"); I certainly don't feel comfortable telling my students that when it does, they should just put up with it.</p>

<p>If you know something about Ant and Hibernate, and would like to figure out what's going on, I've put the project's four files on the web, and I'm <a href="mailto:gvwilson@cs.utoronto.ca">easy to reach</a>.  I look forward to hearing from you.</p>

<p>[<a name="1">1</a>] "Pear-shaped" is a British expression meaning "gone bad".  No idea how it originated; if anyone knows, I'd like to hear.</p>

<p>[<a name="2">2</a>] "Annealing" is the process of banging on metal to get the kinks out.  "Simulated annealing" is an optimization technique in which you make random changes to your proposed solution, keeping those that make things better, and throwing aways those that don't.  Simulated annealing is a lousy way to debug programs.</p>
