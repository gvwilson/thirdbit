---
title: "Data Science for Software Development"
date: 2017-11-20
---

<p>Many software developers are learning data science to analyze their
customers' data. What a growing number are realizing is that they can use those
same techniques to answer their own questions, such as:</p>
<ul>
<li>When will this project be ready to ship?</li>
<li>Which components of our application most need to be tested?</li>
<li>Who should fix this bug?</li>
<li>What parts of my API do people find hardest to use?</li>
</ul>
<p>Over the past 15 years, there has been an explosion of empirical 
research in software engineering to explore these questions, fuelled in 
part by the availability of data from sites like <a href="http://github.com/">GitHub</a> and <a href="https://stackoverflow.com/">Stack Overflow</a>. This blog post presents a few representative results, then explores the methods behind three in more detail.</p>
<h2 id="data-science-and-software-engineering-examples">Data Science and Software Engineering: Examples</h2>
<p>Let's start with a finding that affects everyone doing data science at scale: <a href="https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-yuan.pdf">Yuan et al's discovery</a>
 that simple testing can prevent most critical failures in distributed 
data-intensive systems. They examined failures on Cassandra, Hadoop 
MapReduce, and similar systems and found that:</p>
<ol>
<li>Almost all failures required 3 or fewer compute nodes to reproduce. 
That is, you usually don't need a cluster to debug a cluster.</li>
<li>Error logs usually contained enough data to allow reproduction.</li>
<li>The majority of catastrophic failures could easily have been prevented by performing simple testing on error handling code.</li>
</ol>
<p>The last point is the most unexpected. While professionals usually 
test that their analysis code works when things are going well, they 
rarely test that it does the right thing when something goes wrong. 
Adding just a few such tests during development would prevent a lot of 
pain downstream.</p>
<p>Another large-scale result comes from <a href="https://kar.kent.ac.uk/46742/1/fp1187-altadmri.pdf">the work of Altadmri and Brown</a>,
 who looked at 37 million attempts to compile programs by high schoolers
 in the United Kingdom. They then asked teachers what their students' 
most common mistakes were, and discovered that:</p>
<ol>
<li>Teachers didn't agree with each other about what mistakes students were most likely to make.</li>
<li>More importantly, teachers' predictions had only weak correlation with what students actually got wrong.</li>
</ol>
<p>Of course, data mining isn't the only way to generate useful evidence-based insights in programming. In 2013, <a href="http://web.cs.unlv.edu/stefika/">Andreas Stefik</a>'s team published the second in a series of studies of whether some languages are easier to <em>learn</em> than others. As a baseline, they included a made-up language in their study whose keywords were generated at random.</p>
<p>To their surprise, curly-brace languages like Java and Perl were just
 as hard for novices to learn to recognize as a randomly-generated 
language. Python and Ruby were both significantly easier to learn, and 
Quorum, which A/B tests the syntax of every new feature before adding 
it, was easier still. Andreas discusses this result, and the reasons why
 programming language designers pay so little attention to usability, in
 <a href="https://www.functionalgeekery.com/episode-55-andreas-stefik/">this entertaining podcast</a>.</p>
<h2 id="identifying-security-bug-reports">Identifying Security Bug Reports</h2>
<p>As an example of how these studies are done, <a href="http://www.lero.ie/people/fayolapeters">Fayola Peters</a> at <a href="http://www.lero.ie/">LERO</a>
 used text-based prediction models to find reports of security bugs in 
the bug trackers of large systems so that work on them could be 
prioritized. In one study, she used data from the Chromium, Wicket, 
Ambari, Camel, and Derby projects; these contain a total of 45,940 bug 
reports, but only 0.8% are security bug reports.</p>
<p>Some security bugs are manually labelled, and these can be used to 
train classifiers to detect unlabelled ones.  Techniques like Naïve 
Bayes and Random Forests are a starting point, but the efficiency of 
generic models can often be improved via filtering of specific keywords.
 The most important check is how well models built from projects with 
labelled security bugs can find similar bugs in other projects. The 
results were encouraging: Peters found that her classifiers worked well 
enough to be useful in practice.</p>
<h2 id="will-my-patch-be-accepted-">Will My Patch Be Accepted?</h2>
<p>As a second example, companies want their modifications be included 
in projects in order to avoid having to maintain the code themselves, 
and volunteers want an indication whether their patch stands a chance as
 well. Since there is often a long time between patch submission and 
acceptance, <a href="http://mcis.polymtl.ca/bram.html">Bram Adams</a> and his group at the Polytechnique Montréal have been building models to predict which ones will be accepted.</p>
<p>Like many data science projects, this one starts by getting and 
cleaning data from multiple sources, including Git repositories and <a href="https://www.gerritcodereview.com/">Gerrit code reviews</a>.
 However, for projects that use email-based review, like the Linux 
kernel, gathering data means scraping mailing list archives and using 
heuristics like the checksums of patches or set-based intersection of 
changed lines to match patches to conversations. Even with the help of 
tools like <a href="http://grimoirelab.github.io/">GrimoireLab</a>, 
there will always be patches of which multiple versions were reviewed, 
and patches split into multiple parts that were reviewed separately. As 
in all data science, it is up to the analyst to build a model, and the 
assumptions in it will have a powerful impact on the final conclusions.</p>
<p>The second step is to decide what variables to examine and what metric to use for each, such as:</p>
<ul>
<li>patch quality</li>
<li>the experience of the patch developer</li>
<li>the review process (for example, review comments and number of reviewers)</li>
<li>review quality (for example, degree of detail of reviews)</li>
<li>review time</li>
<li>interaction of patch author and reviewers (for example, friendly versus angry)</li>
</ul>
<p>Just this half dozen might use everything from survival statistics to
 sentiment analysis. Once deciding what to measure, you can apply
data science tools. Since your real goal is to predict acceptance of future 
patches, the most straightforward approach is logistic regression, but 
there are many others.</p>
<p>Finally, you can measure variable importance to determine the impact 
of each variable on patch acceptance. This will necessarily be partly 
qualitative, since your goal is to identify what developers can do to 
improve the odds of their work making it into the product. As always, 
you have to be careful about confusing correlation with causation, but 
even a few simple recommendations (like "DON'T USE ALL CAPS IN YOUR 
COMMIT MESSAGES") can make a real difference.</p>
<h2 id="finding-help">Finding Help</h2>
<p>The biggest change in how programmers work over the last 20 years 
hasn't been in the languages they use: it has been the near-universal 
reliance on <a href="https://stackoverflow.com/">Stack Overflow</a> for asking questions and getting answers. <a href="http://ctreude.ca/">Christoph Treude</a> at the University of Adelaide and his collaborators have been developing methods to make sites like this more useful.</p>
<p>Their starting point is the <a href="https://archive.org/details/stackexchange">Stack Overflow data dump</a>.
 After doing some exploratory statistics to look at the number of words 
and sentences, most common words, term frequency–inverse document 
frequency (TF-IDF), and so on, the next step is to see which words in 
the Stack Overflow threads co-occur with higher votes, higher acceptance
 rates, and higher view counts.</p>
<p>Since software documentation contains many incomplete sentences and 
code elements, off-the-shelf natural language processing libraries often
 get things wrong. Software documentation written in languages other 
than English is even more difficult to parse since it still tends to use
 English for technical terminology. That is, it mixes two natural 
languages and code elements. Ad hoc heuristics and more advanced 
modeling techniques have to be used together to handle cases like this.</p>
<p>Putting the pieces together makes it possible to build a tool that 
takes the name of a Python module as input and produces meaningful 
sentences about this module from the Stack Overflow threads. Going 
further, Treude and his collaborators were able to use grammatical 
dependencies between words to automatically find software documentation 
that explains how to perform a task, and then to automatically identify 
code snippets that can accomplish this task.</p>
<h2 id="conclusion">Conclusion</h2>
<p>All too often, widely-held truths about software development are 
based on strong opinions and loud voices rather than evidence. As 
described at the outset, that is changing as hundreds of high-quality 
studies appear every year to support some beliefs, such as "code review 
really is the best way to find bugs", and challenge others, like 
"test-driven development isn't as effective as some people believe, and <code>goto</code> statements aren't really harmful".</p>
<p>"Engineering" has been defined as "the application of the scientific 
method to create useful things". If that's true, then software 
development might finally, thanks to data science, be on its way to 
becoming a real engineering discipline.</p>
<h2 id="further-reading">Further Reading</h2>
<p>Researchers present dozens of new findings in this area every year at conferences like <a href="http://www.msrconf.org/">Mining Software Repositories</a>.
 Some of these proceedings are still locked behind academic paywals, but
 a growing number of researchers make preprints available.</p>
<p>For those in search of an overview, the 2010 book <em><a href="http://www.amazon.com/Making-Software-Really-Works-Believe/dp/0596808321/">Making Software</a></em> was a "greatest hits" collection of the most interesting results of the time.  A new trilogy titled <em><a href="http://www.amazon.com/Perspectives-Data-Science-Software-Engineering/dp/0128042060/">Perspectives on Data Science for Software Engineering</a></em>, <em><a href="http://www.amazon.com/Art-Science-Analyzing-Software-Data/dp/0124115195/">The Art and Science of Analyzing Software Data</a></em>, and <em><a href="http://www.amazon.com/Sharing-Data-Models-Software-Engineering/dp/0124172954/">Sharing Data and Models in Software Engineering</a></em> are a broader and more up-to-date coverage of the same topics, and separately, Derek Jones is working on a new book titled <em><a href="http://www.knosof.co.uk/ESEUR/">Empirical Software Engineering Using R</a></em>.</p>
