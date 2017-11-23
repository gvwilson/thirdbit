---
layout: plain
permalink: /lesson-design/design.html
title: "The Design of Lesson Design"
---

# The Design of Lesson Design

*This is the original one-page design for "Lesson Design"
using the template laid out in Part 3 of that lecture.*

<!-- -------------------------------------------------------------------------------- -->

## Step 1: Brainstorming

1. What problem(s) will students learn how to solve?
   - How to figure out who a course is for and ensure that it meets their needs.
   - How to decide on a practical scope for a course.
   - How to design good exercises for a course.
   - How to make it easy for a course's intended audience to find it.
2. What concepts and techniques will students learn?
   - What a mental model is (and why it doesn't have to be complete or completely correct to be useful).
   - The differences between novices, competent practitioners, and experts.
   - How those differences affect instructional design.
   - The difference between formative and summative assessment.
   - The difference between short-term and long-term memory.
   - How the limits to short-term memory affect lesson design.
   - How cognitive load impacts learning.
   - That legitimate peripheral participation is the best way to welcome people into a community of practice.
   - How to use reverse instructional design to create a course that meets learners' needs.
3. What technologies, packages, or functions will students use?
   - [Deans for Impact][deans] 10-page summary
     (archived [here](readings/science-of-learning-2016.pdf)).
   - [Learning Scientists][learning-scientists] single-page summaries of effective practices
     (archived [here](readings/learning-scientists-2017.pdf))
4. What terms or jargon will you define?
   - Formative assessment.
   - Summative assessment.
   - Short-term (working) memory.
   - Long-term memory.
   - Cognitive load.
5. What analogies or heuristics will you use?
   - Short-term memory is your cache, long-term memory is your hard drive.
   - Experts have a more densely connected mental graph than competent practitioners.
6. What mistakes or misconceptions do you expect?
   - Your learners don't think the same way you do (and possibly not even the way you did).
   - "Learning styles" (visual, auditory, kinesthetic) aren't a thing.
   - Diving in at the deep end isn't as effective as guided exploration.
   - You can't just ask people how well they understand something.

<!-- -------------------------------------------------------------------------------- -->

## Step 2: Who is this course for?

## Catalina

Catalina, 56, is a professor of statistics in Chile.
She teaches graduate and undergraduate courses in her own department,
and also manages a course for approximately 300 medical students
on experimental design and data analysis.
Catalina has used Excel SAS, and R for years.
She would like to teach them to the medical students,
but given their schedules,
needs to put the training online.
Since she's going to do that,
she has agreed to turn her materials into a DataCamp course.

While she has been teaching for years,
Catalina has no formal training in lesson design.
This course will introduce her to a few basic concepts
and show her how to apply them to build a course that meets her learners' needs
quickly and reliably.

<!-- -------------------------------------------------------------------------------- -->

## Step 3: What will the student do along the way?

- Characterize learner levels.
  - Given some brief descriptions of actions and thought processes,
    classify each person as a novice, competent practitioner, or expert.
- Match distractors with misconceptions.
  - Given an MCQ,
    match each of the wrong answers provided with the misconception it is meant to diagnose.
- Label a concept map.
  - Given a partially-completed concept map,
    assign the labels provided to the unlabelled concepts and connections.
- Estimate cognitive load.
  - Given a three-sentence explanation of a new concept,
    enumerate the ideas and connections.
- Give feedback on live teaching.
  - Watch [this video of bad teaching][bad-live] and rank the following mistakes.
- Give feedback on recorded teaching.
  - Watch [this good screencast][good-screencast] and [this bad screencast][bad-screencast]
    and make notes about the differences.

<!-- -------------------------------------------------------------------------------- -->

## Step 4: How are the concepts connected?

- Chapter 1: From Novice to Competent
  - People go through a more-or-less predictable set of transitions from novice to competent practitioner to expert.
    - A novice does not yet have a usable mental model of the problem domain.
    - A competent practitioner has such a model.
    - Address experts later.
  - The goal when teaching a novice is not to give her information,
    but to help her construct a mental model so that she has somewhere to put information.
  - The key to doing this is to clear up misconceptions.
    - Use formative assessments with diagnostic power to identify and correct misconceptions while learning is taking place (every 5-10 minutes).
    - Which means quality of instruction depends on quality of correction (feedback in SCTs) as much as quality of explanation.
    - Formative assessment also allows learners to practice skills and gauge progress.
- Chapter 2: From Competent to Expert
  - Knowledge isn't stored as a graph, but it's a useful metaphor.
  - Expert's graph isn't just larger: it's also much more densely connected.
    - Where a competent practitioner has to search, an expert can "see" the solution in a single step.
  - Expertise only emerges through *reflective practice*
    - Most people drive for 10,000 hours without becoming expert drivers…
  - Sometimes use *concept maps* to represent and communicate understanding.
- Chapter 3: Cognitive Load
  - Human memory consists of long-term memory (permanent storage) and short-term memory (working set).
    - Instruction loads new information into short-term memory; reinforcement keeps it there long enough for it to be transferred to long-term memory.
    - Short-term memory is very small (7±2 items), so lots of small exercises are more effective for novices than a small number of large exercises.
    - Larger exercises are more effective for more advanced learners because they are trying to master high-level skills.
  - Good teaching loads (but doesn't overload) the learner's short-term memory, then reinforces long enough for knowledge to *transfer* to long-term memory.
  - Effective lessons focus on one aspect of a problem at a time to reduce cognitive load.
    - Making choice of strategy, subgoals, and connections between concepts explicit helps us gauge cognitive load.
- Chapter 4: Exercise Types
  - We offer multiple choice questions and "write and run", but they can be used in many ways.
  - MCQ
    - Tracing execution order: offer choices of order in which lines are run (good for control flow).
    - Tracing values: good for control flow, especially vectorized operations.
    - Fault mapping: given an error message, which line of code triggered it?
      - Requires reflection and exercises a very useful skill.
  - W&R
    - Fill in the blanks: lowers cognitive load, especially when done in sequences.
    - Parsons Problems (rearrange code): also lowers cognitive load.
      - Research finding: requiring people to write/modify code while rearranging is *harder* than either pure alternative.
    - Minimal fixes: exercises debugging skills.
      - Again, requires higher-level thinking and exercises a common skill.
  - Things we don't currently support well
    - One-to-one matching.
    - Diagram labelling.
    - Summarization.
    - Ranking.

<!-- -------------------------------------------------------------------------------- -->

## Step 5: Course overview

**Course Description**

This course is a brief introduction to modern evidence-based teaching
practices, including
*   what actually happens when people learn;
*   how people's thinking changes as they go from being novices to
    competent practitioners and then experts; and
*   how to design effective lessons in a repeatable way.

**Learning Objectives**

- Explain the differences between novices, competent practitioners, and experts.
- Design questions and exercises that diagnose novices' misconceptions.
- Break lessons into pieces that take into account the limits of human cognition.
- Describe and justify the steps in a repeatable lesson design process.

**Prerequisites**

None.
This course is a prerequisite for *How to Make a DataCamp Course*.

[bad-live]: https://www.youtube.com/watch?v=-ApVt04rB4U
[bad-screencast]: https://www.dropbox.com/s/bf3hof8lgmqr1ou/Greg%20Wilson%20-%20bad-teaching.m4v
[deans]: https://deansforimpact.org/resources/the-science-of-learning/
[good-screencast]: https://www.dropbox.com/s/c5tmipi3fhvli3c/Laurent%20Gatto%20-%20laurent_gatto_reading_ms_data.mp4
[learning-scientists]: http://www.learningscientists.org/downloadable-materials/
