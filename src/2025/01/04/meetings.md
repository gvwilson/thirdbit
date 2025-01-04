---
title: Meetings
date: 2025-01-04
---

The [previous post][time-management] explained how to be productive individually,
but what about being productive with others?
The most important thing is running meetings efficiently,
and the key to doing that is to distinguish between:

-   Status meetings
    for keeping everyone up to date on what everyone else is doing
    and for making simple decisions when the options are well understood.

-   Discussion meetings
    for weighing alternatives and making complex decisions.

-   Co-working sessions like brainstorming sessions and programming sprints
    that are devoted to the content of the project rather than its operation.

## Status Meetings

Every team should have a short weekly status meeting.
One way to organize these is
to create a table in a shared document like the one below.
Everyone adds a few bullet points to their row in the table
at least half an hour before the meeting starts
so that the whole team can mull everything over.
If anyone wants to discuss something,
they highlight it by adding a comment.
The meeting moderator then goes through the highlighted items one by one,
spending no more than a couple of minutes on each;
anything that requires more time is deferred to a discussion meeting

| Person | Progress | Plans | Problems |
| ------ | -------- | ----- | ---------- |
| Ren    | Parsing OCTL records | Tag OCTL records in DVC | Duplicate OCTL tags? |
|        | Deployed progress bar patch | Help onboard Silvia | |
| Mikka  | Refactored PostgreSQL connector | #156: handle records with NULL timestamp | Clarify authorship guidelines |
|        | Patched database tests | #171: auto-archive duplicate records | |
| Sanjay | … | … | … |
| Jess   | … | … | … |

Another way to run a status meeting is to review issues that people have closed in the past week
or are actively working on.
"Actively" is the key word here,
and in my experience,
this method only works if someone is responsible for handling issue triage before each meeting.
The biggest advantage of using issues is that there's no extra work;
the disadvantage is that there's no record later on of what people were doing at any particular time.

## Decision Meetings

Decision meetings are for issues that will have more long-term impact on the project
or that team members disagree about.
Since the stakes are higher,
they need more structure.
(See [this video][video] for a long version of the rules below.)

Decide if there actually needs to be a meeting.
:   If the only purpose is to share information,
    send a brief email instead:
    most people can read faster than they can speak.

Write an agenda.
:   If nobody cares enough about the meeting to prepare
    a point-form list of what's to be discussed,
    the meeting probably doesn't need to happen.
    (Note that "the agenda is all the open issues in our GitHub repo" doesn't count.)

Include timings in the agenda.
:   Doing this helps prevent early items stealing time from later ones.
    The first estimates with any new group are inevitably optimistic,
    so expect to revise them upward for subsequent meetings.
    But don't have second or third
    meeting just because the first one ran over time: instead, try to figure out
    *why* it ran over and fix the underlying problem.

Select a moderator.
:   Put one person in charge of keeping items on time,
    selecting the next person to speak,
    chiding people who are having side conversations or checking email,
    and asking people who are talking too much to get to the point.
    The moderator should *not* do all the talking:
    in fact,
    the moderator will talk less in a well-run meeting than most other participants.

Prioritize.
:   Tackle the most important issues first, even if they're the longest,
    because the little ones always take more time than you expect.

Require politeness.
:   No one gets to be rude,
    no one gets to ramble,
    and if someone goes off topic,
    it's the moderator's job to say, "Let's discuss that elsewhere."

No interruptions.
:   This rule is a special case of the one above,
    since treating other people with respect is the sincerest form of politeness.
    Participants should raise a hand (physically or electronically)
    when they want to speak.
    The moderator should keep track of the queue
    and give each person time in turn.

No distractions.
:   Side conversations make meetings less efficient
    because nobody can actually pay attention to two things at once.
    More importantly,
    if someone is checking their email or texting a friend during a meeting,
    it's a clear signal that they don't think the speaker or their work is important.
    This doesn't mean a complete ban on technology—people may need accessibility aids
    or be waiting for a call about childcare—but by default
    phones should be face down and laptops should be closed
    during in-person meetings.

Take minutes.
:   As discussed below,
    someone other than the moderator should take
    point-form notes
    about the most important information that was shared
    and about every decision that was made or every task that was assigned to someone.

End early.
:   If the meeting is scheduled for 10:00–11:00,
    aim to end at 10:50 to give people a break before whatever they're doing next.

As soon as the meeting is over,
add the minutes to the project's wiki,
version control repository,
or shared cloud drive.
Please don't email minutes to everyone:
our inboxes are full enough,
and the more places new team members need to search in order to find things,
the more likely they are to miss something important.

Sharing the minutes ensures that:

People who weren't at the meeting can follow what's going on.
:   We all have to juggle tasks from several projects or courses,
    which means that sometimes we can't make it to meetings.
    Checking a shared record is more accurate and more efficient than asking a colleague,
    "What did I miss?"

Everyone can check what was actually said or promised.
:   Accidentally or not, people often remember things differently;
    writing them down gives everyone a chance to correct mistakes
    and misinterpretations.

People can be held accountable.
:   Whoever has to draw up the agenda for the next meeting
    can start with the action items from the previous one.

If you would like to become better at sharing information and making decisions,
there is no better place to start than [[Brookfield2016][Brookfield2016]],
which catalogs fifty different techniques for managing discussions
and explains when and how each is useful.

<div class="callout" markdown="1">
### Are you a blowfish or a clam?

[NOAA's guide][noaa-disruptive] to dealing with disruptive behaviors
has useful labels and even more useful advice
for handling people who may send meetings off course.
</div>

[Brookfield2016]: https://isbnsearch.org/isbn/9781119049715
[noaa-disruptive]: https://coast.noaa.gov/ddb/
[time-management]: @root/2025/01/03/time-management/
[video]: https://www.youtube.com/watch?v=PtewOjRy-1U
