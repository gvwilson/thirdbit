---
title: "Please Tell Me Python Logging Isn't Supposed to Work This Way"
date: 2006-02-02
---
<p>I'm looking at <a href="http://www.python.org/doc/2.4.1/lib/minimal-example.html">http://www.python.org/doc/2.4.1/lib/minimal-example.html</a>;
I try a cut-down version of the example:</p>

<pre>
$ python
&gt;&gt;&gt; import logging
&gt;&gt;&gt; logging.debug('debug')
&gt;&gt;&gt; logging.info('info')
&gt;&gt;&gt; logging.warning('warning')
WARNING:root:warning
</pre>

<p>Cool.  Now I do this:</p>

<pre>
&gt;&gt;&gt; logging.basicConfig(level=logging.DEBUG)
</pre>

<p>I believe I've turned on output for debug-level logging, but no,
it's still working as before:</p>

<pre>
&gt;&gt;&gt; logging.debug('debug')
&gt;&gt;&gt; logging.info('info')
&gt;&gt;&gt; logging.warning('warning')
WARNING:root:warning
</pre>

<p>Hm… OK, try it in a fresh Python session:</p>

<pre>
$ python
&gt;&gt;&gt; logging.basicConfig(level=logging.DEBUG)
&gt;&gt;&gt; logging.debug('debug')
DEBUG:root:debug
</pre>

<p>So is really only possible to configure logging once???  Bah…
Let's try this:</p>

<pre>
$ python
&gt;&gt;&gt; logging.getLogger().setLevel(logging.DEBUG)
&gt;&gt;&gt; logging.debug('debug')
DEBUG:root:debug
</pre>

<p>All right, so I can grab the internal logger object out of the
logging framework, and change its settings, but
<code>basicConfig</code> doesn't change settings that are already in
place…???</p>

<p>Hm: <a href="http://www.python.org/doc/2.4.1/lib/multiple-destinations.html">http://www.python.org/doc/2.4.1/lib/multiple-destinations.html</a>
suggests that what I ought to do is create a new handler object,
configure it, and stick it back into the logging framework.  This
seems clumsy—which might explain why nobody I know ever uses the
logging library.  I hope someone can tell me that there's an easier
way…</p>

<hr />

<p>Later: CrankyCoder says, "log4j was a bad idea in Java, it seems
like a worse idea in Python."  You have to grab the root logger to set
the log level for all child loggers.  Unless of course you have those
child loggers with overridden log levels.</p>

<pre>
$ python
&gt;&gt;&gt; from logging import *
&gt;&gt;&gt; debug('fda')
&gt;&gt;&gt; root

&gt;&gt;&gt; root.level = DEBUG
&gt;&gt;&gt; debug('fda')
DEBUG:root:fda
</pre>

<p>The documentation isn't all that clear but with <code>basicConfig</code> <code>debug()</code>,
<code>warn()</code>, <code>info()</code> or other logging commands,
you're registering a handler.  From <code>basicConfig</code>:</p>

<pre>
1203     if len(root.handlers) == 0:
1204         filename = kwargs.get("filename")
1205         if filename:
1206             mode = kwargs.get("filemode", 'a')
1207             hdlr = FileHandler(filename, mode)
1208         else:
1209             stream = kwargs.get("stream")
1210             hdlr = StreamHandler(stream)
1211         fs = kwargs.get("format", BASIC_FORMAT)
1212         dfs = kwargs.get("datefmt", None)
1213         fmt = Formatter(fs, dfs)
1214         hdlr.setFormatter(fmt)
1215         root.addHandler(hdlr)
</pre>

<p>Basically - you're expected to get loggers by calling
<code>getLogger('your.named.logger')</code>.  You build a hierarchy of
loggers up and the log levels cascade down the dotted namespace:</p>

<pre>
$ python
&gt;&gt;&gt; from logging import *
&gt;&gt;&gt; root

&gt;&gt;&gt; logA = getLogger('a')
&gt;&gt;&gt; logAB = getLogger('a.b')
&gt;&gt;&gt; logA.level = INFO
&gt;&gt;&gt; debug('from root logger')
&gt;&gt;&gt; warn('from root logger')
WARNING:root:from root logger
&gt;&gt;&gt; logA.debug('from a')
&gt;&gt;&gt; logA.info('from a')
INFO:a:from a
&gt;&gt;&gt; logA.warn('from a')
WARNING:a:from a
&gt;&gt;&gt; logAB.debug('from a.b')
&gt;&gt;&gt; logAB.info('from a.b')
INFO:a.b:from a.b
&gt;&gt;&gt; logAB.warn('from a.b')
WARNING:a.b:from a.b
</pre>

<p>Bah—I think that structured logging is essential to good software
development, but I'd be embarrassed putting this in front of students
and saying, "It's supposed to work this way."</p>
