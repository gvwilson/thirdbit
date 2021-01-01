---
title: "Assessing Competence"
date: 2018-01-26 04:20
year: 2018
---

A friend who is running workshops to teach coding skills to people getting into tech
asked me a question earlier this week:
what's the best way to rate and report someone's skill,
as opposed to their knowledge?
The same question came up at work,
and since I know far less about educational assessment than I should,
I figured I'd share my answer in the hope that someone would correct me.

Our objective is to *rate* someone's skill (i.e., figure out what it is)
and then *report* it (i.e., communicate our rating in a way other people will correctly understand).
A common way to do this is to list the skills and levels:

<table>
  <tr>
    <th></th>
    <th colspan="5" align="center">Understanding</th>
  </tr>
  <tr>
    <th></th>
    <th>None</th>
    <th>Beginner</th>
    <th>Basic</th>
    <th>Good</th>
    <th>Advanced</th>
  </tr>
  <tr>
    <th>Functions</th>
    <td>[&nbsp;]</td>
    <td>[&nbsp;]</td>
    <td>[&nbsp;]</td>
    <td>[&nbsp;]</td>
    <td>[&nbsp;]</td>
  </tr>
  <tr>
    <th>Filter/Map</th>
    <td>[&nbsp;]</td>
    <td>[&nbsp;]</td>
    <td>[&nbsp;]</td>
    <td>[&nbsp;]</td>
    <td>[&nbsp;]</td>
  </tr>
  <tr>
    <th>Immutability</th>
    <td>[&nbsp;]</td>
    <td>[&nbsp;]</td>
    <td>[&nbsp;]</td>
    <td>[&nbsp;]</td>
    <td>[&nbsp;]</td>
  </tr>
</table>

The problem is that terms like "basic understanding" and "good understanding" mean different things to different people.
Unless you operationalize these levels somehow,
different evaluators will use the same term with different meanings.
This isn't a problem with a very small team who've worked together and have a shared (implicit) understanding of goals and levels,
but as soon as you bring on someone who *hasn't* been co-braining with you for ages,
you're in trouble.

Another way to approach this uses the
[four stages of understanding](https://en.wikipedia.org/wiki/Four_stages_of_competence) model.
Given a concrete task like,
"Learner uses filter/map in place of loops or other control strucures,"
the evaluator rates the observed performance as:

1. unconscious incompetence (i.e., doesn't do it and doesn't know that she should)

2. conscious incompetence (knows she should but fumbles execution)

3. conscious competence (does it, but has to check details and makes mistakes)

4. unconscious competence (writes correct code from muscle memory)

Evaluators are more likely to agree with each other on these ratings,
but it does depend on observing process rather than inspection of final result:
you can't distinguish conscious and unconscious competence by looking at a learner's final code.
For small cohorts, though,
observation is feasible:
evaluators can either watch over the learner's shoulder,
or have them record a short screencast of themselves programming
and watch it at 5X.

This approach surfaces another issue that any kind of assessment has to deal with.
The three topics in the table shown earlier were "functions", "filter/map", and "immutability".
The first two are straightforward to operationalize:
does the learner break her code into small, self-contained functions,
and use filter and map instead of loops and conditionals?
The third is a lot harder to fit into this framework.
"Learner uses `const` instead of `let`" is a sign of understanding,
but hardly the whole story.
Requiring assessors to operationalize what they mean–i.e.,
to be specific about what learners are doing to signal what they understand–forces
the assessors to think carefully about what they actually mean.
Sitting here right now,
I honestly don't know how I would tell how well you understood the concept of immutability,
which in turn means that I'm probably shouldn't be trying to put a label on your understanding yet.
