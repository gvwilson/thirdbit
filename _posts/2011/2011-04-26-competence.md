---
title: "Competence"
date: 2011-04-26 19:07:29
year: 2011
---
<p>When I first saw Starling Software's <a href="http://www.starling-software.com/employment/programmer-competency-matrix.html">Programmer Competency Matrix</a>, I was struck by the parallels between its four levels and the first four of the five that Dr. Patricia Benner identified in her landmark book <a href="http://www.amazon.com/Novice-Expert-Excellence-Clinical-Commemorative/dp/0130325228/"><cite>From Novice to Expert: Excellence and Power in Clinical Nursing Practice</cite></a>.  Her five levels–which are grounded in a ton of empirical data–are as follows:</p>

<dl>
  <dt><strong>Stage 1: Novice</strong></dt>
  <dd>Novices have had no experience of the situations in which they are expected to perform. Novices are taught rules to help them perform. The rules are context-free and independent of specific cases; hence the rules tend to be applied universally. The rule-governed behavior typical of the novice is extremely limited and inflexible. As such, novices have no "life experience" in the application of rules.</dd>
  <dt><strong>Stage 2: Advanced Beginner</strong></dt>
  <dd>Advanced beginners are those who can demonstrate marginally acceptable performance, those who have coped with enough real situations to note, or to have pointed out to them by a mentor, the recurring meaningful situational components. These components require prior experience in actual situations for recognition. Principles to guide actions begin to be formulated. The principles are based on experience.</dd>
  <dt><strong>Stage 3: Competent</strong></dt>
  <dd>Competence develops when the practitioner begins to see his or her actions in terms of long-range goals or plans of which he or she is consciously aware. A plan establishes a perspective, and the plan is based on considerable conscious, abstract, analytic contemplation of the problem. The conscious, deliberate planning that is characteristic of this skill level helps achieve efficiency and organization. The competent practitioner lacks the speed and flexibility of a proficient one but does have a feeling of mastery and the ability to cope with and manage the many contingencies of the real world. The competent person does not yet have enough experience to recognize a situation in terms of an overall picture or in terms of which aspects are most salient, most important.</dd>
  <dt><strong>Stage 4: Proficient</strong></dt>
  <dd>The proficient practitioner perceives situations as wholes rather than in terms of chopped up parts or aspects, and performance is guided by maxims. Proficient practitioners understand a situation as a whole because they perceive its meaning in terms of long-term goals. The proficient practitioner learns from experience what typical events to expect in a given situation and how plans need to be modified in response to these events. The proficient practitioner can now recognize when the expected normal picture does not materialize. This holistic understanding improves the proficient practitioner's decision making; it becomes less labored because the practitioner now has a perspective on which of the many existing attributes and aspects in the present situation are the important ones. The proficient practitioner uses maxims as guides which reflect what would appear to the competent or novice performer as unintelligible nuances of the situation; they can mean one thing at one time and quite another thing later.</dd>
  <dt><strong>Stage 5: Expert</strong></dt>
  <dd>The expert practitioner no longer relies on rules to connect his or her understanding of the situation to an appropriate action. The expert practitioner, with an enormous background of experience, now has an intuitive grasp of each situation and zeroes in on the accurate region of the problem without wasteful consideration of a large range of unfruitful, alternative diagnoses and solutions. The expert operates from a deep understanding of the total situation.  He or she is no longer aware of features and rules; his/her performance becomes fluid, flexible, and highly proficient. Experts do use analytic tools in situations where they have had no previous experience, or when they make a wrong initial assessment of the situation.</dd>
</dl>

<p>I'd like to find out what knowledge programmers think they acquire at each of these five stages.  My first guess is in the table shown below; what else do you think should be there?  And what shouldn't, or is in the wrong place?  (Note that this table starts at Novice level, which is <em>not</em> the same as an absolute beginner who has seen nothing at all.  For us, a novice is someone who has done a standard first-year university "Computing 101" course, and can hack together code to (more or less) pass an assignment, but in Benner's terms, has no "life experience" of their own on which to base decisions when faced with real-world problems.)</p>

<table border="1">
<tbody>
<tr>
<td width="10%"><strong>Topic</strong></td>
<td width="15%"><strong>Level 1<br>(Novice)</strong></td>
<td width="15%"><strong>Level 2<br>(Advanced Beginner)</strong></td>
<td width="15%"><strong>Level 3<br>(Competent)</strong></td>
<td width="15%"><strong>Level 4<br>(Proficient)</strong></td>
<td width="15%"><strong>Level 5<br>(Expert)</strong></td>
</tr>
<tr>
<td valign="top">Description</td>
<td valign="top">Our assumed starting point</td>
<td valign="top">If they learn just one thing</td>
<td valign="top">If they learn everything in our course</td>
<td valign="top">Beyond the scope of this course (but in the next one)</td>
<td valign="top">Large-scale development for computational science</td>
</tr>
<tr>
<td valign="top">Data Structures</td>
<td valign="top">list</td>
<td valign="top">list of lists</td>
<td valign="top">dictionary, queue</td>
<td valign="top">tree (recursion)</td>
<td valign="top">cyclic graphs (and too many others to mention)</td>
</tr>
<tr>
<td valign="top">Control Flow</td>
<td valign="top">for<br>while<br>if</td>
<td valign="top">raise/except</td>
<td valign="top">overriding methods<br>first-class functions</td>
<td valign="top">recursion</td>
<td valign="top">closures<br>decorators</td>
</tr>
<tr>
<td valign="top">Modularization</td>
<td valign="top">function</td>
<td valign="top">libraries (import)</td>
<td valign="top">first-class functions<br>classes</td>
<td valign="top">dynamic import<br>introspection</td>
<td valign="top">cross-language programming</td>
</tr>
<tr>
<td valign="top">Patterns</td>
<td valign="top">what's a pattern?</td>
<td valign="top">forall<br>case<br>sentinel<br>most valuable<br>flag</td>
<td valign="top">reduce<br>filter</td>
<td valign="top">factory vs. prototype<br>template method<br>visitor</td>
<td valign="top">composite<br>command<br>strategy<br>proxy<br>decorator</td>
</tr>
<tr>
<td valign="top">Text</td>
<td valign="top">readline<br>substring<br>escape characters<br>tokenization using split</td>
<td valign="top">wildcard regular expressions</td>
<td valign="top">character encoding (Unicode)</td>
<td valign="top">–</td>
<td valign="top">recursive descent parsing</td>
</tr>
<tr>
<td valign="top">Relational Databases</td>
<td valign="top">select
where</td>
<td valign="top">aggregation</td>
<td valign="top">join<br>foreign keys<br>one-to-one<br>one-to-many</td>
<td valign="top">many-to-many<br>NULL<br>transactions</td><br>
<td valign="top">triggers<br>stored procedures</td>
</tr>
<tr>
<td valign="top">Data Management</td>
<td valign="top">shared drive</td>
<td valign="top">version control<br>structured vs. unstructured data<br>compression</td>
<td valign="top">dirty/missing data<br>metadata (format specifiers, provenance)<br>discipline-scale databases</td>
<td valign="top">–</td>
<td valign="top">ontologies</td>
</tr>
<tr>
<td valign="top">Design</td>
<td valign="top">functions for code re-use</td>
<td valign="top">entities and relationships<br>encapsulation<br>interface vs. implementation</td>
<td valign="top">polymorphism<br>inheritance<br>Open/Closed Principle</td>
<td valign="top">Liskov Substitution Principle<br>frameworks<br>OO design patterns</td>
<td valign="top">–</td>
</tr>
<tr>
<td valign="top">Version Control</td>
<td valign="top">checkout<br>update<br>commit</td>
<td valign="top">merge</td>
<td valign="top">rollback</td>
<td valign="top">branch management</td>
<td valign="top">–</td>
</tr>
<tr>
<td valign="top">Build</td>
<td valign="top">"javac *.java"</td>
<td valign="top">"make program"</td>
<td valign="top">patterns and rules</td>
<td valign="top">macros<br>conditional builds</td>
<td valign="top">continuous integration</td>
</tr>
<tr>
<td valign="top">Documentation</td>
<td valign="top">README.txt</td>
<td valign="top">Javadoc and equivalents</td>
<td valign="top">–</td>
<td valign="top">–</td>
<td valign="top">–</td>
</tr>
<tr>
<td valign="top">Coordination</td>
<td valign="top">email</td>
<td valign="top">mailing list<br>shared spreadsheet<br>project blog</td>
<td valign="top">bug tracker<br>IRC/chat (archived)</td>
<td valign="top">–</td>
<td valign="top">–</td>
</tr>
<tr>
<td valign="top">Testing</td>
<td valign="top">hand-run tests (interactive or scripted)</td>
<td valign="top">unit tests using a framework<br>"make test"<br>debugger</td>
<td valign="top">boundary case analysis</td>
<td valign="top">static analysis<br>coverage</td>
<td valign="top">stubs/mock objects</td>
</tr>
<tr>
<td valign="top">Packaging and Deployment</td>
<td valign="top">tar and email</td>
<td valign="top">version control labels<br>"make tarball"</td>
<td valign="top">installation scripts</td>
<td valign="top">RPMs, Eggs, autoconf</td>
<td valign="top">–</td>
</tr>
<tr>
<td valign="top">Web Programming</td>
<td valign="top">download files by clicking on them</td>
<td valign="top">wget<br>url.open.read</td>
<td valign="top">the HTTP protocol<br>public/private key pairs</td>
<td valign="top">CGI to serve static content</td>
<td valign="top">partial failure<br>service composition</td>
</tr>
<tr>
<td valign="top">Performance Engineering</td>
<td valign="top">timing</td>
<td valign="top">profiling<br>big-O<br>algorithms vs. tweaks<br>Amdahl's Law</td>
<td valign="top">memory hierarchy<br>task farming</td>
<td valign="top">processor pipeline<br>data parallelism</td>
<td valign="top">threading<br>message passing</td>
</tr>
</tbody>
</table>
