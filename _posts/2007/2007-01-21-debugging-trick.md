---
title: "Debugging Trick"
date: 2007-01-21 11:38:26
year: 2007
---
A <a href="http://blogs.msdn.com/greggm/archive/2007/01/17/setting-conditional-breakpoints-using-object-ids.aspx">neat trick</a> when debugging: give the object a unique ID (to avoid confusion if it's relocated by the garbage collector in a way that changes its address), then break on that ID.  I really, really want someone to write a <a href="http://www.third-bit.com/notontheshelves.html#dtp">good book on debuggers</a>.
