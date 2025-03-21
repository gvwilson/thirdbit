---
date: 2012-01-29
original: swc
title: Terminology
---
<p>Before going further with the redesign of the Software Carpentry curriculum, I need to define a few terms and their relationships. These definitions refer to another post on learners and their needs, which you may want to read first.</p>
<ul>
<li>A <em>concept</em> is an atom of learning. It can be a <em>fact</em> (e.g., what a call stack is), a <em>technique</em> (e.g., how to pass parameters to a function), or a <em>rule</em> (e.g., when to copy data).</li>
<li>An <em>association</em> is any connection between two concepts. Obviously, all concepts in a topic should be strongly associated.</li>
<li>A <em>dependency</em> is a prerequisite association between two concepts. Circular dependencies may exist (you can't understand A unless you understand B, which depends on C, which in turn depends on A), but we'll work hard to avoid such cycles, since every particular learner encounters concepts in some sequential order.</li>
<li>A <em>topic</em> is a set of related concepts; for example, the topics "Parameters" includes all of the concepts described above. A concept may be part of several topics, but for learning purposes, we would like its first appearance <em>for an individual learner</em> to be gentler than subsequent appearances for that same learner.</li>
<li>A <em>lesson</em> is an atom of teaching. It will typically comprise a small number (1-4) of closed-related concepts, and be a few minutes long. Where possible, it should be followed immediately by some kind of reinforcement (discussed below). A concept may appear in several lessons (same idea, different contexts).</li>
<li>A <em>tutorial </em>is a specific sequence of lessons on related topics; for example, the tutorial "Functions" would include lessons on parameters, returning values, and so on. Tutorials aren't strictly necessary for free-range learners–they can go through lessons in any order that respects dependencies–but we must define them:
<ul>
<li>to give learners like Zuzel the larger narrative arcs they need (learners like Xanthe only need lessons); and</li>
<li>to give instructors like Tahura, who are working in traditional classroom settings, guidance on how to fill an hour-long lecture.</li>
</ul>
</li>
<li><em>Reinforcement </em>is something done to help people absorb a concept, such as further examples, class discussion, quizzes, or exercises. All four are problematic:
<ul>
<li>Further examples are based on guesses of what learners might not have understood correctly; such guesses are often wrong.</li>
<li>Class discussion is hard to implement for asynchronous, self-directed learners.</li>
<li>Multiple choice quizzes can mislead or frustrate learners (most questions have more than one right answer), or fail to clear up learners' misconceptions ("You're wrong, but I won't tell you why").</li>
<li>Long-answer quizzes and exercises require a human assessor's attention (which is also hard to implement for asynchronous learners).</li>
</ul>
</li>
<li><em>Assessment</em>is anything done to determine how well something else has been done. "How well" is important: assessment will not always (or even usually) be black-and-white. Specific kinds are:
<ul>
<li><em>formative</em> assessment, which provides short-term diagnostic feedback to learners and teachers;</li>
<li><em>summative</em> assessment, which demonstrates attainment of some level; and</li>
<li><em>evaluative</em> assessment, which tell us how well the teaching is working.</li>
</ul>
Formative assessment is a kind of reinforcement; summative and evaluative are (usually) not.</li>
</ul>
<p>The diagram below shows these relationships. I've drawn most relationships as many-to-many, but in practice, we hope that most will actually be one-to-many, i.e., that concepts will fit neatly into topics, and topics into lessons. The one-to-one relationship between summative assessments and topics is also a bit misleading: what it's meant to imply is that any particular learner will eventually demonstrate mastery of some topic (e.g., Yeleina will show that she understands functions). This is the smallest "chunk" for which we'd contemplate awarding a badge, though as discussed earlier, we're going to start with something coarser-grained.</p>
<p><img src="@root/files/2012/01/syllabus.png" class="centered"></p>
