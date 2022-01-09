---
title: "Allocating Responsibilities"
date: 2019-11-19 02:59
year: 2019
---

*I wrote this guide ten years ago when I was supervising undergraduate
programming projects at the University of Toronto.  I hope it's still
useful.*

You and your friends have just formed a team: now what?  How do you decide who
does what?  And just as importantly, how do you make sure that everyone actually
does what they're supposed to?

There are many ways to divide project work between team members.  In a *modular
decomposition*, each person is responsible for all aspects of one part of the
program.  For example, one person might design and build the GUI, while another
writes the database interface, and a third implements the business rules.  This
is generally a bad strategy for three reasons:

-   Unless the team is very disciplined, it leads to **big bang integration**, in
    which all the components meet each other for the first time right at the end
    of the project.  Big bang almost always fails.

-   Each team member only really understands one aspect of the project as a whole.
    This can hurt a lot if there's a final exam (which is just a pointed way of
    saying "team members will learn less").

-   If someone drops out or fails to complete their module, the project as a whole
    will fail.

*Functional decomposition*, in which each person is responsible for one type of
task, is usually more successful.  With this strategy, one person does the
testing, another handles the documentation, a third does the bulk of the coding,
and the fourth takes care of build and deployment.  This guarantees that
everyone understands most of the project by the end of the term.  The obvious
drawback is that each person only gets to hone one set of skills.

Another, less obvious, drawback stems from the fact that some activities are
viewed as being more prestigious than others.  If the team decomposes work
functionally, the self-appointed "alpha geeks" will usually wind up with the
plum jobs, like architecture and coding, leaving less appealing work to people
who aren't as pushy or self-confident.  This tends to reinforce existing
inequities; it also tends to lower the team's overall grade, since there's often
little relationship between how outspoken people are and how well they work.

*Uniform decomposition* is a scaled-down version of modular decomposition that
is much more effective.  Instead of owning an entire module for the lifetime of
the project, each developer does the design, coding, testing, and documentation
for one small feature after another.  Working this way is central to agile
development, and is a good way to cope with the never-ending timeslicing of
student life.

Finally, there is *rotating decomposition*: everyone does one task for a few
weeks, then a different task for the new few, and so on.  This is initially less
productive in absolute terms than either of the preceding strategies, since the
team has to pay for ramp-up several times over.  In the long term, though, it
outperforms the alternatives: it is more robust (having a team member drop out
is less harmful), and if everyone on the team is familiar with every aspect of
the software, they can all contribute to design and debugging sessions.

> The boss of a product group I worked in rotated developers into testing for a
> few weeks at the end of every release cycle.  I learned more about the product
> I was building in those weeks than I learned in the rest of the year;
> configuring the product to work with databases I'd never even heard of before,
> and exercising features I only vaguely knew existed, paid dividends many times
> over.

Any of these strategies is better than *chaotic decomposition*.  If people have
different ideas about who's supposed to do what, some things won't be done at
all, while others will be done several times over.  (You can tell if your
decomposition is chaotic by counting how many times people says, "I thought
*you* were doing that!"  or "But I've already done that!"  The more often these
phrases are heard, the more trouble you're in.)  All other decompositions tend
toward chaos under pressure, so it's important to establish rules early, and
stick to them when the going is easy, so that the instinct to do the right thing
will be there when you need it.

Your instructor may mandate a particular work decomposition.  If she does, your
first team meeting should be devoted to deciding who will do what.  Do *not*
allocate work on the basis of who's loudest or most willing to interrupt:
remember, there is only a
[weak correlation](https://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect)
between how confident someone is and how competent they are.

No matter what decomposition you use, your team should write, sign, and hand in
a contract outlining what everyone has agreed to do to make the project a
success.  In my experience, this is a lot more effective if students make it up
themselves as their first assignment; that way, they actually have to think
about what they're promising their teammates.  Here's an example:

> We, the members of Team 12, agree the following:
>
> - Work on each assignment will be divided according to role.  Two
>   people will code, one will test, and one will be responsible for
>   documentation.  One of the coders will run the weekly meeting; the
>   other will take minutes, and post them to the project wiki and
>   mailing list on the same day as the meeting.  These roles will
>   rotate for each assignment.  No one will code two assignments in a
>   row.
>
> - The tester will be responsible for actually submitting the
>   assignment.  Someone will only be listed as contributing to that
>   assignment if at least two other members of the team think she
>   completed, or made significant progress on, at least one work
>   item.
>
> - We will aim to get at least 80% on each assignment.
>
> - We will hold a half-hour status meeting every week on
>   Thursdays at 4:00 pm.  Everyone will attend, and be on time.  If
>   someone cannot attend, they will let the rest of the team know by
>   email no later than noon on that day.
>
> - Everyone will email a brief point-form summary of their
>   progress during the week to the team mailing list no later than
>   noon on Thursday.  Everyone will read everyone else's summary
>   before the 4:00 meeting and make a list of their questions and
>   concerns.
>
> - All email about the project will go to the team mailing
>   list, rather than person-to-person.  Everyone will check email at
>   least twice a day during the week, and at least once a day on
>   weekends.
>
> - No one will check code into version control that fails to
>   compile.  No one will check in code that fails to pass existing
>   tests without first getting the permission of that round's tester.
>   No one will change the database schema or add dependencies on
>   third-party or open source libraries without first getting
>   permission from the whole team.

It may sound a little silly, like those "contracts" that some
parents and children make up regarding chores and allowances, but
it's actually very effective.  First, people really do have
different expectations about what being in a team means.  Some
people, for example, may be happy with a bare pass; others may
want the team to shoot for an A+ on everything.  Knowing who wants
what won't make these tensions go away, but it certainly helps
focus the argument.

Drawing up a contract also prevents later disagreements about who actually
promised or agreed to what.  As with
[meetings]({{site.github.url}}/2018/05/11/meetings/), people often remember
things differently; having a signed record is everyone's second-best
defense. (The best, of course, is personal integrity.)

I still don't know if teams should have to give copies of their contracts to
their instructors or not.  On the one hand, it's a great way to let your
instructor know how you're planning to operate, and what you're planning to
achieve.  Given that she probably has a lot more experience than you, it gives
her a chance to tell you if you've forgotten anything, or how well those really
cool ideas your teammate talked you into will actually work.  On the other hand,
as soon as something has to be handed in, some students will write what they
think the instructor wants to read, rather than what they actually think.

Two last notes.  First, most software development teams in industry and open
source don't bother with contracts like these.  There may be corporate
guidelines on good citizenship, or performance metrics written into your job
spec, but in general, people expect that if you're doing this for a living, you
know what others can reasonably expect of you, and you will live up to those
expectations.  (This often turns out not to be the case, which is one of the
reasons so many real-world projects fail.)

> "You can't manage what you don't measure" is a truism in the business world.
> Unfortunately, so is, "You only get what you reward."  If developers are
> rewarded for the number of lines of code they write, they will write
> overly-verbose code; if they are rewarded for the number of bugs they find,
> they won't bother to do any testing up front, since that would actually lower
> their score.  I think metrics are valuable, but it requires a lot of maturity
> (and the ability to reflect on what they actually mean) to realize that value.

Second, if your instructor has you draw up a team contract at the start of the
project, then she can and should base part of your team's grade on how well you
stuck to it.  If she handed you a team contract, she should definitely base part
of the grade on compliance.  If there was no contract at all, then I think it's
unfair to turn around at the end of the project and ask people to rate one
another, since they won't have known while they were working what they were
going to be rated on.
