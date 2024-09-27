---
title: "How Far We Got"
date: 2008-12-18
---
There's a quote (attributed to various people—I'd welcome a pointer to the original) to the effect that if you show me your code, I don't know what you're doing, but if you show me your data structures, I'll understand.  To figure out just how far our students got rebuilding DrProject on top of <a href="http://www.djangoproject.com">Django</a> this term, I asked one of them to generate a schema diagram for the database tables.  The result, included below, was created by running the following commands in a <a href="http://pypi.python.org/pypi/virtualenv">virtual environment</a>:
<pre>$ svn checkout http://django-command-extensions.googlecode.com/svn/trunk/ django-extensions
$ cd django-extensions
$ python setup.py install
$ django graph_models -ag &gt; schema.dot
$ dot -o schema.png -Tpng schema.dot</pre>
