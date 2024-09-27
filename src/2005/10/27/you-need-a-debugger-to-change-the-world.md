---
title: "You Need a Debugger to Change the World"
date: 2005-10-27
---
Following links from the latest <a href="http://www.subtextual.org/">Subtext</a> demo, I came to Martin Fowler's article <a href="http://www.martinfowler.com/articles/languageWorkbench.html">"Language Workbenches: The Killer-App for Domain Specific Languages?"</a>.  It's well written and thought provoking, like everything else Martin writes, but I think there's one glaring oversight. Two thirds of the way through, he says:

<blockquote>…there are three main parts to defining a new DSL [Domain Specific Language]:
<ul>
  <li>Define the abstract syntax, that is the <strong>schema</strong> of the abstract representation.</li>
  <li>Define an <strong>editor</strong> to let people manipulate the abstract representation through a project.</li>
  <li>Define a <strong>generator</strong>.  This describes how to translate the abstract representation into an executable representation.  In practice the generator defines the semantics of the DSL.</li>
</ul>
</blockquote>

That's great—but #4 should have been:

<blockquote>
<ul>
  <li>Create an <strong>inspector</strong> that allows people to debug their DSL's behavior in its own terms.</li>
</ul>
</blockquote>

Now, you could claim that the debugger was implied by #2 (the editor), but i practice, it never works that way.  Time and again, I see people struggling with systems that don't provide tools for debugging: Makefiles, Antfiles, config.xml files for servlet containers, and on and on and on.  When something goes wrong, the only options are (a) tweak it until it converges on what you wanted, or (b) debug the <em>implementation</em> of the nice abstraction you were just thinking in.

I think that the inability of today's C++ debuggers to display something useful when confronted with templated code is the singlest biggest obstacle to their wider use.  I think that Java made a horrible mistake in deciding to erase type information when compiling generics, so that what's actually executing can only say, "Yup, it's another Object."  Extensible languages could revolutionize software development, but it'll only happen if we focus on closing the debugging gap.

So, anyone looking for a Ph.D. topic? ;-)
