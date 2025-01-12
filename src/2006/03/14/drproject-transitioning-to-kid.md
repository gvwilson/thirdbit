---
title: "DrProject: Transitioning to Kid"
date: 2006-03-14
---
<em>Update</em>:  Previously, I discussed some of the issues we encountered by switching to Kid for our templating framework.  While Kid was much nicer to work with, we were surprised at how slow it was.  Chris Lenz, however, corrected me by pointing out that inserting XML fragments into the template (via the <code>XML(…)</code> function) should be avoided whenever possible.  Instead, your controllers should be creating ElementTree objects that can be rendered directly by Kid.

For example, instead of passing the string <code>&lt;em&gt;foobar&lt;/em&gt;</code> to your template, pass an ElementTree:
<blockquote>
<pre>from elementtree import ElementTree element = ElementTree.Element('em') element.text = 'foobar'</pre>
</blockquote>
In addition to the substantial performance boost, using ElementTrees for embedded HTML adds an extra level of security.  Because most templating frameworks just stick HTML strings into a template, the developer must always ensure that those fragments are properly escaped.  Fortunately, this is done automatically when you use ElementTree/Kid.

With this in mind, we set out to replace hard-coded HTML fragments with ElementTree objects.  We soon ran into problems, however, when we realized that nearly all of our embedded HTML was generated by our custom WikiParser engine and third-party syntax highlighting tools.  Refactoring the existing WikiParser engine might qualify as one of Dante's Seven Stages of Hell, and I don't think we could reasonably expect the authors of SilverCity and Enscript to use elementtree ;)

For the time being, we decided to remove syntax highlighting from DrProject. While this is a nice feature to have (see <a href="http://projects.edgewall.com/trac/browser/trunk/setup.py">here</a> for an example), incorporating these tools with Kid was just too difficult.  The HTML returned by enscript is <strong>not</strong> valid XML, so you cannot embed the output into Kid nor can you parse the output to create an ElementTree without a pre-processing stage.  In the future we plan to revisit this issue, as the "ooo" factor for syntax highlighting is a big plus!

Furthermore, we decided to rewrite the WikiParser from scratch, using a proper parsing engine.  Liam Stewart wrote the parser using <a href="http://www.cosc.canterbury.ac.nz/~greg/python/Plex/">Plex</a>.  We have added a custom formatter to build the ElementTree representing the parse tree.  The resulting object can then be passed directly to Kid, without further processing.  The new WikiParser is much cleaner, and much easier to maintain (at least, we think so ;).  The only drawback we have encountered so far is speed; the new parser is quite a bit slower than the old engine.  The performance boost we have gained by not having to perform <code>XML(…)</code> calls in our Kid templates is nearly offset by the time it takes to produce the ElementTree!

While we are currently trying to optimize the parser as much as possible, this performance hit may be unavoidable with a pure Python parsing library.  If you have experience with other Python parsing libraries, let us know.  One caveat: we would prefer to keep the library 100% Python; while using a C-based parsing engine would be much faster, we also have to think about portability and maintainability.  DrProject already has enough dependencies as it is; we don't want to add a whole set of C related libraries.
