---
title: "Unicode in Action"
date: 2004-12-12 08:54:51
year: 2004
---
<p>From Pat Smith and Jeffrey Jia, who've been working on the Psiphon project:</p>

<p>One of the more challenging parts of getting Psiphon up and running
was the internationalization and localization of the interface. The
problem was Unicode. As we <a href="http://www.joelonsoftware.com/articles/Unicode.html">discovered</a>,
Unicode (or rather, pretending it does not exist) is a big problem in
software. In order to ensure that Psiphon would work with "all"
languages, we needed to get a language such as Chinese or Persian
working. Both Chinese and Persian use the UTF-8 encoding, and they do
not use the ASCII character set we are used to dealing with. Chinese
and Persian were two ideal languages to try because Chinese requires
more bites to be displayed, and Persian is also a "right-to-left"
language.</p>

<p>The first big problem was that of the development tools that we were
using to develop Psiphon, not one was able to properly handle the
Unicode characters. During initial tests on the Persian translation
file we were unable to tell if the problem was with our data file, or
with wxPython and PythonCard. After four to five hours of working
along side Michelle Levesque, comparing how our different tools
handled the Unicode, we determined that it was our development tools
that were causing the problem.</p>

<p>Of Komodo, Cygwin, Windows Command Prompt, and IDLE, it appeared
(at first) that IDLE was the best at handling Unicode. Komodo could
probably display the data file when it was opened, but its Python
shell interpreter would print gibberish when it attempted to handle
the data. We determined it was a codec problem with Komodo's Python
shell, by observing patterns in the gibberish that was returned and
using Google to see if the results were a common occurance when
dealing with Unicode. We had moderate success with IDLE, however,
after further tests with more Unicode, it seemed that IDLE also had
problems dealing with alot of Unicode. We were not able to find any
tool that was capable of handling all Unicode correctly, so we decided
to continue working on the internationalized interface without a
satisfactory tool.</p>

<p>We soon realized that the Unicode was not being displayed properly
because a non-Unicode build of wxPython was installed. After
uninstalling it and installing the correct Unicode build of wxPython,
the problem was still not fixed. wxPython includes a demo application
which includes a Unicode example, with the Unicode build installed,
this demo should run without a problem, this was not the case. After
many uninstalls/reinstalls, it was discovered that there was an old
partial install on the path that was part of an unsuccessful Unix
install under Cygwin. Removing that allowed the wxPython demo to run
smoothly, but Psiphon's Persian translation was still causing the
program to crash.</p>

<p>Reading the error trace we were able to determine that the problem
was now within PythonCard's handling of Unicode. The problem was
traced to PythonCard's multicolumnlist module. A multi-column list is
used in Psiphon to track the connected users, and the headers of each
column require internationalization. By reading through the
multicolumnlist source code, and reading the Python 2.3 documentation
for <code>Types</code>, we found that PythonCard was using
<code>StringType</code>, which according to Python 2.3 does not
include Unicode strings. The PythonCard source would produce an error
if Unicode was given to a multi-column list. By changing all
occurances of <code>StringType</code> with <code>StringTypes</code>
(includes Unicode), we were able to avoid the multi-column list
error. However, it does require users to change their own version of
multicolumnlist.py if they choose to run Psiphon from the source. We
reported the bug to the PythonCard author Kevin Altis, and he posted
on the PythonCard mailing list that the bug will be fixed on the next
release.</p>

<p>Despite all this, we were still getting errors when Psiphon tried
to display Unicode. Since we were sure (well, pretty sure) that the
Unicode wxPython wasn't the problem, we determined that the PythonCard
resource file was the problem. This lead to many hours of considering
the possibility of redoing the interface entirely in wxPython, which
would have resulted in many hours of work to migrate the existing GUI
away from PythonCard and into just wxPython.</p>

<p>Back to Kevin Altis, who informed us of a bug: Unicode was handled
in resource files in the same way it was handled in the multi-column
list component. Unfortunately, the suggested fix only worked if the
resource file was being written in Unicode, and not dynamically
creating a resource file while a program is running. Robin Dunn of
wxPython gave much appreciated help in examining the resource file
generating code, and with his help we were able to get Psiphon working
with Unicode languages. However, we were unable to get the
"right-to-left" working with Persian. Since we needed Psiphon to be
multi-platform we could not simply use the GTK wxPython build. GTK
itself is able to handle "right-to-left" easily, but wxPython does not
have its own related options.</p>

<p>The Unicode problem took a lot of hours to fix, but forced us to
understand Unicode, and why we should never write a program which does
not handle Unicode properly. We also gained experience in sorting out
problems in open source software. Tracking down a new bug in an
existing tool gave more insight into how the tool itself works. It
also taught us how to better debug code, and to realize that sometimes
the bug may not be in the code you are writing, but rather in the code
from a tool that you are using. Overall, the time invested in fixing
the Unicode problem was worth it for the knowledge that was gained.</p>
