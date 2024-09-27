---
title: "Ant + Hibernate: There's More Than One Way to Fix It"
date: 2004-10-08
---
<p>I don't know who William Lopez is—I've never met the man, and before yesterday at 19:40 EST, I'd never heard of him.  But then a mail message landed in my inbox saying, "I think I've solved your Ant + Hibernate problem."  He included his solution in a ZIP file; it took me all of five minutes to download it, edit a couple of settings for my machine (library files in different places), and convince myself that yes, it did work.  It took another ten minutes to figure out which of his changes was the crucial one, and guess what: it's an Ant bug.</p>

<p>Or maybe not, because three hours later, Eric Burke added a comment to the original posting.  His solution was to rearrange some of the Hibernate-specific stuff in the build file.  So who's fault is it really, Ant's or Hibernate's?  Let's take a look.</p>

<p>I was trying to get Ant to clean my workspace, generate a Java source file from a Hibernate mapping file, compile that file and another one I'd written by hand, and then generate a database schema, all in one invocation. The problem was that when I got to the schema generation step, the Hibernate schema generation task told me that the compiled class file for the generated class didn't exist.  If I ran Ant twice, though, everything worked; it also all worked if I ran Ant as far as "compile the Java", then ran it again to do the schema generation.  But how could there be a timing bug in a strictly sequential chain of operations?</p>

<p>William Lopez's solution was to create all of the temporary directories the build process needed once, at the start of the build process, rather than creating each directory just before it was needed.  Basically, I had:</p>

<blockquote><pre>
&lt;target name="clean"&gt;
    &lt;delete dir="${gen}"/&gt;
    &lt;delete dir="${class}"/&gt;
    &lt;delete dir="${data}"/&gt;
&lt;/target&gt;

&lt;target name="codegen"&gt;
    <b>&lt;mkdir dir="${gen}"/&gt;</b>
    &lt;hbm2java output="${gen}"&gt; /&gt;
&lt;/target&gt;

&lt;target name="compile" depends="codegen"&gt;
    <b>&lt;mkdir dir="${class}"/&gt;</b>
    &lt;javac srcdir="${gen}" destdir="${class}" …&gt; /&gt;
    &lt;javac srcdir="${src}" destdir="${class}" …&gt; /&gt;
&lt;/target&gt;

&lt;target name="schema" depends="compile"&gt;
    <b>&lt;mkdir dir="${data}"/&gt;</b>
    &lt;schemaexport … /&gt;
&lt;/target&gt;
</pre></blockquote>

<p>and William changed it by moving the <code>mkdir</code> actions inside the <code>clean</code> target:</p>

<blockquote><pre>
&lt;target name="clean"&gt;
    &lt;delete dir="${gen}"/&gt;
    &lt;delete dir="${class}"/&gt;
    &lt;delete dir="${data}"/&gt;
    <b>&lt;mkdir dir="${gen}"/&gt;</b>
    <b>&lt;mkdir dir="${class}"/&gt;</b>
    <b>&lt;mkdir dir="${data}"/&gt;</b>
&lt;/target&gt;

&lt;target name="codegen"&gt;
    &lt;hbm2java output="${gen}"&gt; /&gt;
&lt;/target&gt;

&lt;target name="compile" depends="codegen"&gt;
    &lt;javac srcdir="${gen}" destdir="${class}" …&gt; /&gt;
    &lt;javac srcdir="${src}" destdir="${class}" …&gt; /&gt;
&lt;/target&gt;

&lt;target name="schema" depends="compile"&gt;
    &lt;schemaexport … /&gt;
&lt;/target&gt;
</pre></blockquote>

<p>So it has to be an Ant problem—except that Eric Burke <a href="http://www.ericburke.com/blog/2004/10/solution-to-gregs-hibernate-problem.html">fixed the problem</a> by moving the schema export <code>taskdef</code> <em>inside</em> the schema export target, like this:</p>

<blockquote><pre>
&lt;target name="schema" depends="compile"&gt;

    &lt;taskdef name="schemaexport"
             classname="net.sf.hibernate.tool.hbm2ddl.SchemaExportTask"
             classpathref="cpath.compile" /&gt;

    &lt;mkdir dir="${data}"/&gt;

    &lt;schemaexport …/&gt;

&lt;/target&gt;
</pre></blockquote>

<p>and that works too.  <a href="http://www.ericburke.com/blog/2004/10/solution-to-gregs-hibernate-problem.html">His explanation</a> says:</p>

<blockquote>
I suspect the taskdef is resolving the classpath at the instant Ant parses the taskdef tag. Since one of the required .class files has not been generated yet, the SchemaExportTask does not find the necessary files…
While you could blame Ant, I think it's more likely that the SchemaExportTask should probably be modified to accept a classpath of its own. This would make the task more flexible since you wouldn't have to worry about where you define it.
</blockquote>

<p>He then goes on to say:</p>

<blockquote>
I hope someone finds this useful. [Yes, Eric, very; thank you, and thanks to William, too.]  There is still a very steep barrier to entry for tools like Hibernate, various AOP frameworks, etc… The barrier is figuring out all of the initial configuration options and getting your build process to flow. These things are overwhelming when you are first getting started.
</blockquote>

<p>Amen, Eric.  Eleven of <a href="http://www.cs.utoronto.ca">my department</a>'s brightest undergraduates have been banging their heads against Eclipse, Ant, JUnit, Tomcat, Hibernate, Tapestry, and Checkstyle for more than four weeks now.  They're smart, they work very hard, and they really want to master this stuff, but the learning "curve" they face is more like a vertical wall.  If the open source community wants colleges and universities to include modern tools and frameworks in the curriculum, they're going to have to do a better job fixing the "last 10%" of problems that so often gobble up all the hours students are supposed to spend learning…</p>
