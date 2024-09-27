---
title: "External Programming Interfaces"
date: 2005-12-29
---
<a href="http://www.artima.com/forums/flat.jsp?forum=106&thread=142428">This article</a>, by Eamonn McManus, is a nice little summary of API design principles.  It contains a bit of motherhood and apple pie—nobody would ever set out to make an API difficult to learn or hard to use, for example—but the specifics are good (particularly the discussion of why interfaces are often the wrong thing to use).  The article contains a link to <a href="http://openide.netbeans.org/tutorial/api-design.html">this essay</a> at the NetBeans site, which talks about some of the same ideas in more detail.

Together, the articles got me thinking: why don't we ever talk about or document a module's <em>external</em> programming interface (which I hereby dub "XPI")?  This is the classes, methods, and system calls that the module depends on; more particularly, it is their semantics.  <a href="http://en.wikipedia.org/wiki/Design_by_contract">Design by contract</a> allows a piece of code to specify what it provides; allowing that code to specify what it requires using similar pre- and post-conditions would be a big help in managing the asynchronous evolution of libraries that makes <a href="http://www.postmodernprogramming.org/">postmodern programming</a> so hard.
