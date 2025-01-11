---
title: Fairness
date: 2025-01-11
---

This series of posts is about course projects designed to prepare students for real jobs.
How companies get this wrong contributes to how they sometimes build things that harm society
(and embarrass their creators).
It easy to avoid these mistakes if you are willing to look beyond the code you write;
that first step is often the hardest,
but I hope this discussion will help.

## How Tech Companies Get Hiring Wrong

In 1905,
Harvard began selecting students based on their College Entrance Exam Board results.
As a result,
Jewish enrolment began to rise,
and by the early 1920s they made up more than a fifth of the incoming class.
This wasn't an outcome the establishment was willing to accept,
but neither were explicit quotas,
so they moved the goalposts [[Karabel2006][Karabel2006]].
Admissions officers began asking questions about the "character" of prospective students,
and the university began asking for personal essays
that could be graded however the university found most convenient.
By 1933,
the rate of Jewish admission was back down to an "acceptable" 15%.

Harvard's decision to turn away more capable people in favor of less capable ones
seems ridiculous if you think that a university's job is to find and train the smartest people it can.
It makes more sense when you realize that
most institutions' first priority is to perpetuate themselves:
if it wasn't,
they probably wouldn't still be around.

Similarly,
the hiring process at many tech companies isn't designed to find the best programmers.
Instead,
it is designed (or more often has just evolved)
to find people who are like those doing the hiring.
"Cultural fit" almost always means "like me":
consciously or not,
we are all biased toward those who look like us,
talk like us,
and make the same pop culture references as us,
which has nothing to do with on-the-job ability
[[Greenwald1995][Greenwald1995],[Jost2009][Jost2009]].

One way this bias shows up is in whiteboard coding questions about linked lists,
dynamic programming,
and other topics from computer science classes on data structures and algorithms.
As [Hillel Wayne][wayne-hillel] discovered when he looked at [their history][wayne-linked-lists],
they might have indicated how much experience someone had using C or Pascal in the 1980s,
but they have no more to do with on-the-job performance today
than the essay questions used by Ivy League schools have to do with your ability to learn.
When April Christina Curley,
a recruiter at Google,
began coaching Black students how to prepare for interviews with Google that included questions like these,
the company shut her down—even though
schools like Stanford had been running coaching sessions for their students for years [[Tiku2021][Tiku2021]].

[[Behroozi2019][Behroozi2019],[Behroozi2020a][Behroozi2020a],[Behroozi2020b][Behroozi2020b]]
summarize many other things that often go wrong in hiring in tech,
from long delays waiting for feedback
to asking candidates to spend several days working for free on programming assignments.
These aren't just signs of dysfunctional company culture:
they also make hiring harder for some people than others.
For example,
a single parent or someone caring for a relative with chronic illness
may not be able to devote ten hours to an unpaid side project.
If the interview process requires that,
the company is effectively selecting for people who are economically secure and have lots of free time,
which doesn't correlate with how well they can program in a full-time job.

<div class="callout" markdown="1">
**A sign of privilege**

You probably won't be treated with any more respect on the job than you were while interviewing.
However, when suggested in an early draft of this post that,
"If a company does any of these things, go find another one,"
one reviewer replied,
"It must be nice to be able to walk away."
They were right:
most people aren't as financially secure as me,
so they aren't able to be as finicky about who they work for as I am.
In other words,
I made the same mistake as a team lead who assumed that
since their evenings and weekends were theirs to do with as they wished,
everyone else's would be too.
</div>

As a student looking for your first full-time job
you probably won't have any control over the hiring process,
but seeing whether the company does it well or not
gives you valuable information about how well run it is.
Here are a few positive indicators:

Write inclusive, accessible job ads.
:   [[Gaucher2011][Gaucher2011]] is just one of many studies showing
    that gendered wording in job ads reinforces gender inequality in male-dominated occupations.
    [Gender Decoder][gender-decoder] and [GenderMag][gendermag] can help you find bugs like this
    in ads and software [[Hilderbrand2020][Hilderbrand2020]].
    Tools for finding and eliminating racial bias and other problems aren't as common,
    but [[Washington2020][Washington2020]] will tell you what to aim for,
    and if [WebAIM WAVE][wave] doesn't give your online job ads a clean bill of health,
    please fix the accessibility problems it reports.

Post a public description of the hiring process.
:   Does the company share a page with you (or an email)
    that lays out what's going to happen in what order,
    how much time is expected,
    and the principles everything is based on?

Use blinded screening.
:   Everyone has implicit biases,
    and many of the rules scientists follow when running experiments are designed
    to prevent such biases contaminating their results.
    The same is true of hiring;
    for example,
    companies should redact things like a candidate's age, race, and gender
    when circulating resumes for internal review.

Use diverse interview panels.
:   Giving people from under-represented backgrounds a say in who's hired next
    gives other people with similar backgrounds a better chance of being treated fairly.

Have candidates solve realistic problems with their preferred tools.
:   Most programmers have laptops,
    and video calls are now a part of everyday life in industrialized countries,
    so there's no reason *not* to give people an hour to show what they can do using the IDE of their choice.
    There is also no reason to stop them using online search or AI tools while they do this:
    every working programmer relies on our external collective memory,
    so telling a candidate they can't during an interview
    is like telling a chef to make a meal without using saucepans or knives.

These guidelines apply to school and courses as well.
Are course descriptions and course websites inclusive?
Are instructors required to use blinded grading to ensure that personal likes and dislikes don't affect grades?
If the answers are "no", what can you and your classmates do to fix things?

<div class="callout" markdown="1">
**Questions to ask**

I have interviewed people who didn't ask a single question about the company,
what an average day would look like, or how their career might evolve.
[Julia Evans][evans-julia] has a good list of [questions to ask in interviews][evans-interviews],
and [T. Carter Baxter][baxter-t-carter] has [another][baxter-interviews].
There won't be time to get to them all,
but asking two or three will impress your interviewer
as well as giving you valuable information.
</div>

## On the Job

Unfair treatment doesn't end after people are hired.
Study after study has shown that men and women are treated differently on the job:
women have to work twice as hard to be given half as much credit,
they are listened to less often or given less credit for new ideas,
and what is seen as confidence in men is seen as pushiness or stridency in women [[Gavett2017][Gavett2017]].
People of color are undermined and discounted in the same way in majority-white workplaces in Europe and North America,
and discrimination based on race, faith, and caste are endemic in the rest of the world as well.

Many companies have taken steps to remedy this during hiring.
However,
hiring more people from under-represented groups doesn't make a difference
if they have to work twice as hard to be taken half as seriously,
if they are constantly passed over for promotion,
or if discussions about promotion continue to take place in the men's locker room
after the department's Friday afternoon hockey game.
There are no easy fixes to these problems,
but there are things you can ask for even as a junior hire:

Share data on how well the company has been doing recently.
:   It's reasonable to ask what proportion of a company's staff (technical and otherwise)
    come from under-represented backgrounds
    and about the average length of stay at the company.
    If the interviewer doesn't know the answer,
    they should be able to get it;
    if the company doesn't have that data or won't share it,
    you've just learned something.
    (However,
    see the note above about my privilege:
    I can afford to make an interviewer uncomfortable
    in a way that most juniors looking for their first job cannot.)

Have an org chart.
:   As I said when talking about [making decisions][making-decisions],
    every organization has a power structure:
    the only question is whether it's public and accountable
    or whether the organization runs on who you know and how willing people are to barge in on strangers.

Have written criteria for performance reviews.
:   This is a legal requirement in many places,
    and these are something a company can share before hiring you.
    (Asking for them is a good way to impress interviewers.)
    If a company doesn't have criteria,
    or if performance reviews are only done when an employee asks for one,
    the system is once again biased toward extroverts and the well-connected.

Specify how much time employees can take off.
:   Some tech companies have an "unlimited vacation" policy,
    meaning that employees can take as much time off as they want as long as their work gets done.
    This sounds attractive,
    but [people actually take *less* time off][namely-time-off] under these policies
    than the legal minimum in most jurisddictions,
    both because they feel guilty and because they worry about taking too much.
    It also saves companies money:
    the company has to compensate people for unused vacation days if the person is laid off,
    but not if there's no target.

[Behroozi2019]: https://doi.org/10.1109/VLHCC.2019.8818836
[Behroozi2020a]: https://dl.acm.org/doi/10.1145/3377815.3381372
[Behroozi2020b]: https://doi.org/10.1145/3368089.3409712
[Gaucher2011]: https://doi.org/10.1037/a0022530
[Gavett2017]: https://hbr.org/2017/12/what-research-tells-us-about-how-women-are-treated-at-work
[Greenwald1995]: https://doi.org/10.1037/0033-295x.102.1.4
[Hilderbrand2020]: https://doi.org/10.1145/3377811.3380371
[Jost2009]: https://doi.org/10.1016/j.riob.2009.10.001
[Karabel2006]: https://isbnsearch.org/isbn/9780618773558
[Tiku2021]: https://www.washingtonpost.com/technology/2021/03/04/google-hbcu-recruiting/
[Washington2020]: https://doi.org/10.1145/3328778.3366792
[baxter-interviews]: https://github.com/tBaxter/questions-for-employers
[baxter-t-carter]: https://another.rodeo/
[evans-interviews]: https://jvns.ca/blog/2013/12/30/questions-im-asking-in-interviews/
[evans-julia]: https://jvns.ca/
[gender-decoder]: http://gender-decoder.katmatfield.com/
[gendermag]: http://gendermag.org/
[making-decisions]: @root/2025/01/06/making-decisions/
[namely-time-off]: https://library.namely.com/hr-mythbusters-2017
[wave]: https://wave.webaim.org/
[wayne-hillel]: https://hillelwayne.com/
[wayne-linked-lists]: https://www.hillelwayne.com/post/linked-lists/
