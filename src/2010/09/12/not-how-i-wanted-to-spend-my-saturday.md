---
title: "It Shouldn't Hurt This Much"
date: 2010-09-12
---
<ol>
  <li>One of my students says good things about Spyder, a Python environment with MATLAB-like features. OK, I'd like to give it a try.</li>
  <li>On Mac OS X.</li>
  <li>Ah—it need PyQT.</li>
  <li>And SIP.</li>
  <li>And some optional modules, but I'll ignore those for now.</li>
  <li>So the first step is to install Qt.</li>
  <li>But there aren't binaries—I have to do that from source.</li>
  <li>So I have to get XCode onto this machine (fine, that works, it just takes 30 minutes to download).</li>
  <li>And hey, Qt builds—I'm on a roll.</li>
  <li>So, go into the PyQT directory, do "python configure.py" to, um, configure it, then run "make".</li>
  <li>Good, good, good, then: kaboom. The error message is:</li>
</ol>
<pre>g++ -c -pipe -fPIC -O2 -Wall -W -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_CORE_LIB -I. -I/Users/gregwilson/PyQt-mac-gpl-4.7.6/qpy/QtCore -I/System/Library/Frameworks/Python.framework/Versions/2.6/include/python2.6 -I/mkspecs/macx-g++ -I/Library/Frameworks/QtCore.framework/Headers -I/usr/include -F/Users/gregwilson/PyQt-mac-gpl-4.7.6/qpy/QtCore -F/Library/Frameworks -o sipQtCorecmodule.o sipQtCorecmodule.cpp
In file included from /Library/Frameworks/QtCore.framework/Headers/qmetatype.h:45,
from /Library/Frameworks/QtCore.framework/Headers/QMetaType:1,
from sipAPIQtCore.h:40,
from sipQtCorecmodule.cpp:34:
/Library/Frameworks/QtCore.framework/Headers/qglobal.h:288:2: error: #error "You are building a 64-bit application, but using a 32-bit version of Qt. Check your build configuration."
make[1]: *** [sipQtCorecmodule.o] Error 1
make: *** [all] Error 2</pre>
Er, what? Why does it think I'm trying to build a 64-bit application? Earlier compile lines say:
<pre>g++ -c -pipe -fno-strict-aliasing -O2 <span style="text-decoration: underline;">-arch i386</span> -fPIC -Wall -W -DQT_NO_DEBUG -DQT_GUI_LIB -DQT_CORE_LIB -DQT_SHARED -I/usr/local/Qt4.6/mkspecs/macx-g++ -I. -I/Library/Frameworks/QtCore.framework/Versions/4/Headers -I/usr/include/QtCore -I/Library/Frameworks/QtGui.framework/Versions/4/Headers -I/usr/include/QtGui -I/usr/include -I/System/Library/Frameworks/Python.framework/Versions/2.6/include/python2.6 -I../../QtCore -I. -I. -F/Library/Frameworks -o moc_qpycore_pyqtproxy.o moc_qpycore_pyqtproxy.cpp</pre>
I've highlighted the "-arch i386" line to show that yes, Qt knows I'm on a 32-bit processor—at least, when it's compiling the files in libqpycore.a. Is it a bug in the SIP build and install? Is it—aw, do I really care? Spyder looks nice, but increasingly, my feeling is that if an application doesn't "just install", I'm not interested: I certainly can't ask students doing Software Carpentry to wrestle with issues like this.

*sigh*

<em>Later: <a href="http://old.nabble.com/PyQt4,-Qt-on-osx-SnowLeopard-td26394590.html">this page</a> helped, but not enough: I've got PyQT 4.7.6 installed (at least, "make / make install" in PyQt-mac-gpl-4.7.6 ran to completion), and "python setup.py install" in the spyder-1.1.5 directory worked, but when I try to run spyder from the command line (/usr/local/bin/spyder), it tells me that it can't find PyQT version 4.4. Don't think I'm going to be introducing my students to it any time soon…
</em>
