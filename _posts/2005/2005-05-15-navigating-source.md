---
title: "Navigating Source"
date: 2005-05-15 12:32:57
year: 2005
---
One of the minor items on my to-do list is to replace the <a href="http://projects.edgewall.com/trac">default Trac graphics</a> on the <a href="http://www.third-bit.com/trac/Argon">Argon</a> web site with ones that include some reference to the <a href="http://www.utoronto.ca">University of Toronto</a> and our hippo mascot.  Having spent half an hour on Friday talking to a colleague about how we teach students how to write code, but not how to read it, I thought I'd describe how I figured out what files I'd need to change, and where to find them.

Step 1: what am I looking for?  If you take a look at the <a href="http://www.third-bit.com/trac/Argon">Argon</a> site, you'll see two logos: a large banner at the top of the page, and a smaller "Trac Powered" logo at the bottom.  "View Source" shows me that the top one is produced by the following HTML:
<blockquote>
<pre>&lt;div id="header"&gt; &lt;a id="logo" xhref="http://trac.edgewall.com/" mce_href="http://trac.edgewall.com/" &gt;&lt;img xsrc="/trac-static/trac_banner.png" mce_src="/trac-static/trac_banner.png"  width="236" height="73" alt="Trac" /&gt;&lt;/a&gt; &lt;hr /&gt; &lt;/div&gt;</pre>
</blockquote>
The footer is similar.

Step 2: That <code>&lt;div id="header"&gt;</code> tag looks like a good landmark.  I find it like this:
<blockquote>
<pre>$ cd ~/argon/trunk/trac $ fgrep -e 'id="header"' templates/*.cs templates/header.cs:
<div></div>
</pre>
</blockquote>
Notice that I'm relying here on what I've already learned about Trac: I know that the Python code generates pages based on ClearSilver templates, which live in the <code>templates</code> directory, and have a <code>.cs</code> extension.  If I didn't know that, I'd have run this command instead:
<blockquote>
<pre>$ cd ~/argon/trunk/trac $ fgrep -e 'id="header"' `find . -type f -print | fgrep -v -e '.svn'`</pre>
</blockquote>
(I pipe the results of <code>find</code> through <code>fgrep</code> to filter out everything in the <code>.svn</code> directories that Subversion uses to manage metadata.)

Step 3: take a closer look at the contents of <code>header.cs</code>:
<blockquote>
<pre>&lt;div id="header"&gt; &lt;a id="logo" xhref="&lt;?cs var:header_logo.link ?&gt;"&gt;&lt;img xsrc="&lt;?cs var:header_logo.src ?&gt;" width="&lt;?cs var:header_logo.width ?&gt;" height="&lt;?cs var:header_logo.height ?&gt;" alt="&lt;?cs var:header_logo.alt ?&gt;" /&gt;&lt;/a&gt; &lt;hr /&gt; &lt;/div&gt;</pre>
</blockquote>
The notation <code>var:header_logo.link</code> tells ClearSilver to look in the HDF (Hierarchical Data Format) structure that the Python CGI builds up for it, find the <code>header_logo</code> key, and use the value associated with its <code>link</code> subkey.  Do another search:
<blockquote>
<pre>$ fgrep header_logo `find . -name '*.py' -print` ./trac/db_default.py:  ('header_logo', 'link', 'http://trac.edgewall.com/'), ./trac/db_default.py:  ('header_logo', 'src', 'trac_banner.png'), ./trac/db_default.py:  ('header_logo', 'alt', 'Trac'), ./trac/db_default.py:  ('header_logo', 'width', '236'), ./trac/db_default.py:  ('header_logo', 'height', '73'), ./trac/web/chrome.py:        logo_src = self.config.get('header_logo', 'src') ./trac/web/chrome.py:        req.hdf['header_logo'] = { ./trac/web/chrome.py:            'link': self.config.get('header_logo', 'link'), ./trac/web/chrome.py:            'alt': escape(self.config.get('header_logo', 'alt')), ./trac/web/chrome.py:            'width': self.config.get('header_logo', 'width'), ./trac/web/chrome.py:            'height': self.config.get('header_logo', 'height')</pre>
</blockquote>
The first set of hits, from <code>db_default.py</code>, are from the code that builds up a tuple of tuples called <code>default_config</code>:
<blockquote>
<pre>default_config = (('trac', 'htdocs_location', '/trac/'), ... ('header_logo', 'link', 'http://trac.edgewall.com/'), ('header_logo', 'src', 'trac_banner.png'), ('header_logo', 'alt', 'Trac'), ('header_logo', 'width', '236'), ('header_logo', 'height', '73'), ... )</pre>
</blockquote>
Make a note of that, then look in <code>chrome.py</code> at the second set of hits, which come from the following block of code:
<blockquote>
<pre>logo_src = self.config.get('header_logo', 'src') logo_src_abs = logo_src.startswith('http://') or logo_src.startswith('https://') if not logo_src[0] == '/' and not logo_src_abs: logo_src = htdocs_location + logo_src req.hdf['header_logo'] = { 'link': self.config.get('header_logo', 'link'), 'alt': escape(self.config.get('header_logo', 'alt')), 'src': logo_src, 'src_abs': logo_src_abs, 'width': self.config.get('header_logo', 'width'), 'height': self.config.get('header_logo', 'height') }</pre>
</blockquote>
OK, <code>chrome.py</code> is looking in the configuration object that Trac creates each time it services a request, pulling out the values that describe the header logo, and sticking them into the HDF for ClearSilver to use.  That leaves two questions: how do values get from <code>db_default.default_config</code> into the configuration object, and where do files like <code>trac_banner.png</code> actually live on disk?

Step 4: grepping for <code>default_config</code> gets two hits in <code>env.py</code>:
<blockquote>
<pre>def insert_default_data(self): ... for section,name,value in db_default.default_config: self.config.set(section, name, value) self.config.save()</pre>
</blockquote>
and:
<blockquote>
<pre>def load_config(self): self.config = Configuration(os.path.join(self.path, 'conf', 'trac.ini')) for section,name,value in db_default.default_config: self.config.setdefault(section, name, value)</pre>
</blockquote>
Ah ha!  The configuration object initializes itself by reading from <code>trac.ini</code>.  All we have to do now is find that...

Step 5: Our Trac is run by Apache 2 on Debian Linux, which keeps configuration information under the <code>/etc/apache2/conf.d</code> directory.  Sure enough, there's a <code>trac</code> file in <code>conf.d</code>, which contains the following lines:
<blockquote>
<pre>Alias /trac-static/ "/usr/share/trac/htdocs/" &lt;Directory "/usr/share/trac/htdocs/"&gt; Options Indexes MultiViews AllowOverride None Order allow,deny Allow from all &lt;/Directory&gt;  &lt;Directory "/usr/share/trac/cgi-bin"&gt; AllowOverride None Options ExecCGI -MultiViews +SymLinksIfOwnerMatch AddHandler cgi-script .cgi  Order allow,deny Allow from all &lt;/Directory&gt;  &lt;LocationMatch "/trac/[[:alnum:]]+/login"&gt; AuthPAM_Enabled on AuthName "Pyre Trac" AuthType Basic require valid-user &lt;/LocationMatch&gt;</pre>
</blockquote>
Remember looking at the HTML source in Step 1?  The image path specified there was <code>/trac-static/trac_banner.png</code>, so only the first stanza matters right now.  It specifies that <code>/trac-static</code> is translated into <code>/usr/share/trac/htdocs</code>, and sure enough, that directory contains the PNG images for the two logos.  It also contains a <code>trac.ico</code> file, which produces the little pawprint logo next to Trac URLs in the browser and in Favorites links.

And that's that---the artwork still needs to be done, but at least I know where to put files for testing.

Now, you'll probably never need to find Trac logo files on your computer, but every time you start work with a new code base, you'll need to find your way around.  If there isn't a comprehensive, up-to-date map of the code (and there never is), the first thing to do is to find a landmark, like the <code>div</code> element I picked in Step 1.  Work backward from that: who touches it?  Where does <em>that</em> code get its inputs?  Keep notes---I had half a page of them by the time I was done---so that when you hit a roadblock, you can back up and try another path.  Anything you already know about the application's architecture will help steer you in the right direction, so make sure you understand its processing cycle.  And above all, don't panic, and don't be afraid to ask for help.
