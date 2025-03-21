---
date: 2012-10-04
original: swc
title: "Wanted: An Entry-Level Provenance Library"
---
<p>One of the reason we keep teaching Subversion is that it allows us to show students a simple but useful trick. If you add the following to a text file:</p>
<pre>$Revision: $</pre>
<p>and then tell Subversion to set the "Revision" keyword on that file, the next time you commit it, Subversion will automatically update the text to:</p>
<pre>$Revision: 423$</pre>
<p>or whatever the revision number actually is. This is handy if you're mailing files around, and want people to be able to tell exactly which revision they have, but what makes it <em>really</em> useful is this:</p>
<p>1. Embed the revision number in a string:</p>
<pre>version_string = "$Revision: 423$"</pre>
<p>2. Extract it (I'll show the Python, but the trick works in any language):</p>
<pre>version_number = int(version_string.strip("$").split()[1]) # version_number is now 423</pre>
<p>3. Print this as a comment at the start of any output, along with parameters:</p>
<pre>print '#', sys.argv[0], version_number
print '# …alpha', alpha
print '# …beta', beta
for result in all_results:
    print result</pre>
<p>so that the program's output is:</p>
<pre># analyze.py 423
# …alpha 0.5
# …beta 1.7
22,43,17.5
22,44,18.5
…,…,… # and so on</pre>
<p>This is a quick and easy way to keep track of the provenance of the data: if done systematically, it ensures that every result contains a record of how it was produced.</p>
<p>Of course, a real provenance system needs to do more than this: it needs to track the inputs to the program, so that if <code>analyze.py</code> was run something <code>preprocess.py</code> produced, we can trace backward from <code>analyze.py</code>'s output all the way to <code>preprocess.py</code>. There was <a href="http://openprovenance.org/">an abortive effort</a> a few years ago to standardize provenance information, but it got bogged down in XML schemas and ontologies and all the other details that standards committees love and working scientists find irrelevant.</p>
<p>What the scientists we're trying to help actually need right now is something a lot simpler: a suite of inter-operable libraries for various languages that are no more complicated than the various <a href="http://en.wikipedia.org/wiki/XUnit">xUnit</a> <a href="http://en.wikipedia.org/wiki/List_of_unit_testing_frameworks">libraries</a> for testing, or the <a href="http://docs.python.org/library/argparse.html">argparse</a> and <a href="http://commons.apache.org/cli/">CLI</a> libraries for parsing command-line arguments in Python and Java respectively. It's OK if those libraries don't capture all the information that anyone might conceivably want; what's most important is that they capture enough to be useful, with close to no effort on the scientist's part, so that we can get this ball rolling.</p>
<p>If this sounds like something you'd be interested in helping with, please give us a shout. It would be a good contribution to the scientific programming community, and a good way to meet other believers in better scientific software.</p>

