---
date: 2018-08-18
title: Ten Simple Rules for Creating an Effective Lesson
---

I'm preparing a couple of talks based on [*Teaching Tech Together*](http://teachtogether.tech),
and this seems like a useful topic to cover.
Updated notes are below;
I'd be grateful for [feedback by email](mailto:gvwilson@third-bit.com).
(I've disabled comments on this site until the trolls find someone else to pester.)

### Introduction

-   There are many kinds of lessons, formal and informal, from seconds long to lifelong
-   This guide is about prepared instructional plans and content for half an hour to a day

### A Little Bit of Theory

-   Psychology of learning
    -   Load short term memory
    -   Keep it there long enough to transfer to long term memory
    -   Create links so that knowledge is retrievable (bigger obstacle than outright retention)
-   Goal for novices is to build a mental model
    -   Following a path through a concept map helps ensure connectedness
    -   Naming subgoals help
-   Cognitive load theory points out that learners are trying to:
    -   Recall factual knowledge
    -   Choose a solution strategy
    -   Formulate a response
    -   Use tools,
    -   So teach these all separately and synthesize as a lesson in its own right
-   While we're here, a few myths:
    -   Mindset and stereotype threat are probably not as important as initially thought (this is how science progresses)
    -   VAK learning styles
    -   The "Pyramid of Learning"
    -   And teaching evaluations are suspect, as are self-assessments

### 1. Write Learner Personas to Define Your Audience

-   A lesson is a user interface for knowledge, so borrow methods from user interface design
-   *You are not your learners* (expert blind spot)
-   General background
-   What they already know
-   What they think they want to know
-   What they actually need to know in order to achieve their aims (which may be different from what they think)
-   Special considerations (e.g., accessibility, child care)
-   How the lesson will help them achieve their aims
-   First four parts are usually shared across multiple lessons and instructors

### 2. Write Summative Assessments to Set Concrete Goals

-   "Understand linear regression" is vague; a specific exercise makes aim much clearer
-   Also helps communicate value of lesson to learners
-   Derive learning objectives from what learners will do to demonstrate knowledge
-   Remember, "understand X" isn't checkable
-   Draw a concept map!
-   This series should be "7 plus or minus 2 Rules"

### 3. Write Formative Assessments for Pacing, Design, Preparation, and Reinforcement

-   Spend 1-2 minutes checking in with learners via formative assessment every 10-15 minutes
-   Pacing: are they still with you?
-   Design: they act as milestones building toward the summative assessment
-   Preparation: everything in the summative assessment should be exercised by a formative assessment
-   Reinforcement: learners remember more if they use material right away (problem isn't forgetting, but access)
-   Doing this almost always tell you that you're trying to cover too much
-   Makes prerequisites explicit
    -   Enumerating prerequisite knowledge and skills helps you overcome expert blind spot
    -   And helps stitch lessons together
    -   Be careful not to intimidate learners who have impostor syndrome
    -   As with summative assessment, works best when concrete
    -   Not "understand linear regression", but "can do the following"

### 4. Be Inclusive

-   Choice of language or examples will tell people whether or not they're welcome and likely to be taken seriously
-   (If you don't already know this, you're probably a member of a privileged group)
-   Do not use a deficit model ("they" are missing something, "they" need to try harder)
-   For example, Lach2018 explored two strategies:
    -   Community representation: highlights students' social identities,
        histories, and community networks using after-school mentors or role
        models from students' neighborhoods, or activities that use
        community narratives and histories as a foundation for a computing
        project.  Major risk is shallowness, e.g., using computers to build
        slideshows rather than do any real computing.
    -   Computational integration: incorporates ideas from the learner's
        community, e.g., reverse engineering indigenous graphic designs in a
        visual programming environment.  Major risk is cultural appropriation,
        e.g., using practices without acknowledging origins.
    -   When in doubt, ask your learners and members of their community what
        they think you ought to do and give them control over content and
        direction.
-   DiSa2014a demonstrates effectiveness

### 5. Eliminate Incentives for Cheating

-   Cheating is usually not a symptom of moral failing, but a rational response to poorly-designed incentives
    -   Beck2014 found that cheating is no more likely online than in person
-   Motivation and demotivation in adult learners
    -   Motivators: agency, utility, communality
    -   Demotivators: unpredictability, unfairness, indifference
-   Examples from Lang2013:
    -   Set the cost of failure very high
    -   Rely on single assessment mechanisms like multiple-choice tests
    -   Arbitrary grading criteria

### 6. Use Concreteness Fading

-   PETE (Problem, Explanation, Theory, Example) goes from specific and tangible to more abstract
-   What is the authentic problem that the lesson solves next?
-   Explain a concrete solution
-   Fill in the underlying theory
-   Provide a second example so that learners will understand which parts generalize
-   Authentic problem may be an end goal, or in later lessons, may arise out of a previous solution
-   Build a usable mental model so that learners have somewhere to put knowledge, then correct the model as necessary
-   E.g., ball-and-spring model in chemistry, evolution solely by descent, CPU-memory-disk model in computing

### 7. Design for Peer Instruction

-   Scalable approximation of individual tutoring that engages learners
    1.  Students do pre-class reading
    2.  Instructor poses question
    3.  Students vote publicly
    4.  Students discuss reasoning with each other
    5.  Students re-vote
    6.  Instructor reviews
-   Crou2001 and Port2016 are just two examples of studies showing its effectiveness
-   In practice, often do some instruction in class, but always leading to peer discussion as quickly as possible
-   E.g., type and run a few lines of code, then ask "what happens if I add X?" or "what line do I add to achieve Y?"
    -   Thanks to Mark Guzdial for this example
-   *The Discussion Book* has many other methods (e.g., think-pair-share)

### 8. Design Around Worked Examples

-   Learners learn faster from worked examples than they do from solving problems on their own
    -   They eventually need to do the latter, but step-by-step explanation of why and how helps more
-   Live performances (music, programming, theorem proof) are effectively worked examples
    -   The "PEE" in "PETE"

### 9. Show How to Detect, Diagnose, and Correct Common Mistakes

-   One aspect of worked examples that's important enough to deserve its own section
-   Novices spend much of their time making mistakes and trying to fix them, because they're novices
-   Including DD&C in the lesson reduces frustration, which in turn accelerates learning
-   Also helps solidify their mental model

### 10. Foster Collaboration with Other Instructors

-   DiSa2014b shows that lessons are often not findable
-   FAIR Principles for data (findable, accessible, interoperable, reusable) also apply to lessons
    -   But "reusable" is aiming low
-   Instead of one author broadcasting for others to use, foster collaboration in a teaching commons
    -   Open source software and Wikipedia demonstrate the benefits
    -   Increases inclusivity and reduces lesson maintenance burden
    -   And it's more fun
