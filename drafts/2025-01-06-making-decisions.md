---
title: Making Decisions
date: 2025-01-06
---

The first release of GitHub's [Minimum Viable Governance][github-mvg] guidelines
included this:

> **2.1. Consensus-Based Decision Making**
> 
> Projects make decisions through consensus of the Maintainers.
> While explicit agreement of all Maintainers is preferred,
> it is not required for consensus.
> Rather,
> the Maintainers will determine consensus based on their good faith consideration of a number of factors,
> including the dominant view of the Contributors and nature of support and objections.
> The Maintainers will document evidence of consensus in accordance with these requirements.

It sounds reasonable,
but it is harmfully wrong.
Every team has a power structure:
the question is whether it's formal or informal—in other words,
whether it's accountable or unaccountable [[Freeman2013][Freeman2013]].
In the latter case,
decisions will effectively be made by the people
who are the most self-confident or stubborn
rather than by those with the most insight.

To guard against this,
groups need to spell out who has the authority to make which decisions
and how to achieve consensus.
In short,
they need explicit governance.

Martha's Rules [[Minahan1986][Minahan1986]]
are a practical way to do this in groups of up to a few dozen people,
and work very well for smaller teams too:

1.  Before each meeting, anyone who wishes may sponsor a proposal.
    Proposals must be filed at least 24 hours before a meeting in order to be considered,
    and must include:
    -   a one-line summary
    -   the full text of the proposal
    -   any required background information
    -   pros and cons
    -   possible alternatives

2.  A quorum is established in a meeting if half or more of voting members are present.

3.  Once a person has sponsored a proposal,
    the group may not discuss or vote on the issue
    unless the sponsor or their delegate is present.

4.  After the sponsor presents the proposal a *sense vote* is cast:
    -   Thumbs up: who likes the proposal?
    -   Thumbs down: who is uncomfortable with the proposal?
    -   Thumbs sideways: who can live with?

5.  If everyone likes or can live with the proposal,
    it passes with no further discussion.

6.  If the majority is uncomfortable with the proposal,
    it is sent back to its sponsor for further work.
    (The sponsor may decide to drop it if it's clear the majority isn't ever going to support it.)

7.  Otherwise,
    the group has a brief moderated discussion.
    After 10 minutes,
    or when no one has anything further to add,
    the moderator calls for a straight yes-or-no vote on the proposal.
    If a majority votes "yes" it is adopted;
    otherwise,
    it is returned to the sponsor for further work.

Every group that uses Martha's Rules must make two procedural decisions:

How are proposals put forward?
:   The easiest way to do this in a software project
    is to file an issue in the project's issue tracker
    tagged *Proposal*.
    Team members can comment on it there
    so that the sponsor can revise it before bringing it to a vote.

Who gets to vote?
:   In a course project the answer is "whoever is part of the team,"
    but a more explicit rule is needed for larger or longer-lived projects.
    One method is for existing members to nominate new ones,
    and for the team to hold a straight yes-or-no vote on each.
    Another is to automatically include anyone whose changes to the code
    were accepted by existing members,
    though this under-values non-programming contributions
    like doing code reviews
    or testing new releases.

Rules that people don't know about can't help them.
Once your team agrees on a decision-making procedure,
document it for newcomers
(and to prevent disputes among people already in the team).
You can put this in the project's `README` file ([%x starting %])
or in a separate file called `CONTRIBUTING`.
Wherever it goes,
remember that the easier it is for people to figure out how to contribute,
the more likely they are to do so [[Steinmacher2014][Steinmacher2014]].

## Nothing about us without us

The rules laid out above were created
by and for people near the middle of the bell curve with respect to focus and attention span.
People who are neurodivergent
(i.e., whose brains work differently from the average
when it comes to sociability, learning, attention, and mood)
may find that other approaches work better for them.

But while society accepts that
people of different heights need different desks and seating to be comfortable,
there is still a lot of stigma
associated with differences in mental function,
which are often classified according to
[how inconvenient they are to other people][adhd-thread].
One example is how tests for
attention-deficit/hyperactivity disorder (ADHD) are phrased.
"Subject is overly talkative": compared to who?
"Subject does X when it is inappropriate": by whose rules?
"Struggles to pay attention": in fact,
most people with ADHD can pay very close attention,
but not when they are in environments like noisy classrooms
that are full of distractions.

Decisions that affect people should only be made
with the full participation of those who will be affected.
If you are neurodivergent,
you probably have a set of strategies for managing time and attention.
If you are neurotypical and have neurodivergent teammates,
ask them what works well for them rather than ignoring the difference
or guessing what they might want.
Please do the same if you have teammates who have difficulty seeing, hearing, or moving about:
they have expertise you don't.

[Freeman2013]: https://muse.jhu.edu/article/528558
[Minahan1986]: https://doi.org/10.1177/088610998600100206
[Steinmacher2014]: https://dl.acm.org/doi/10.1145/2593702.2593704
[github-mvg]: https://github.com/github/MVG
