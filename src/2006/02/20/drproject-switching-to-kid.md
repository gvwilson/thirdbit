---
title: "DrProject: Switching to Kid"
date: 2006-02-20
---
Chris Lenz, Jason Montojo, and I began work on refactoring DrProject in early January.  One of the first decisions we made was to replace the <a href="http://www.clearsilver.net/">Clearsilver</a> templating framework with <a href="http://kid.lesscode.org">Kid</a>, an XML-based alternative. Now that the work is done, we've learned a few things about Kid that others might find useful.

Why did we abandon Clearsilver? First, its templates are not valid XML documents, making maintenance very difficult.  If you have ever had to modify someone elses clearsilver template, you will already know it's difficult at best.  Second, Clearsilver is not Pythonic: when passing data into the template, you first have to preprocess it into a pseudo-dictionary of strings, which means you have to process your data <em>twice</em>: once for the preparation phase, and then again when the template is being rendered.  Finally, since you cannot access Python functions and objects from within the template, you have to
execute many UI-related functions in the controlling layer, rather than in the template, which blurs the separation between controller and view.

After looking at a few alternatives, we settled on <a href="http://kid.lesscode.org">Kid</a> as a replacement.  At first glance, it seemed like a perfect solution: Kid templates are guaranteed to be well-formed XML, and you can pass Python data structures and objects to the template for use in the rendering stage.

Once we eventually finished porting the view layer to Kid (a non-trivial process which I will describe in an upcoming post), the end result was cleaner controlling code and cleaner templates, which will be significantly easier to maintain.

But Kid isn't perfect (what is?).  There are many problems and "gotcha's", which I have been documenting. Most of these issues are minor, and only ever catch the developer once. Rendering speed, however, is turning out to be a very significant problem. Simply put, Kid is slow.  In my tests, the rendering phase of a single web request is approximately 2-3 times longer than the processing phase, which includes many database seeks.  You can see the difference by running this simple test:
<blockquote>
<pre>#!/usr/bin/python
#

import timing

timing.start()
data = ['Number &lt;em&gt;%s&lt;/em&gt;' % x for x in range(100)]
timing.finish()
process_time = timing.milli()

source = """
&lt;html xmlns:py="http://purl.org/kid/ns#"&gt;
&lt;head&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;table&gt;
&lt;tr py:for="x in data"&gt;
&lt;td&gt;${XML(x)}&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;/body&gt;
&lt;/html&gt;
"""

import kid
timing.start()
template = kid.Template(source=source, data=data)
content = template.serialize()
timing.finish()
print "Processing time: %d, Rendering time: %d" % (process_time, timing.milli())</pre>
</blockquote>
which results in: <em>Processing time: 0, Rendering time: 1759</em>

This performance is almost shockingly poor.  The problem appears to be a side-effect of guaranteeing the template is well-formed XML: when you remove the <code>XML(…)</code> fragment from the template, and just display<code> x</code>, the rendering time drops to 129 milliseconds.

There has recently been some talk on the Kid mailing list calling for an option to disable the "well-formed XML" check when embedding XML into a template.  Hopefully for DrProject, this change gets pushed into Kid very soon. In the meantime, if you have experienced similar performance issues with Kid and have found a workaround, please email me.
