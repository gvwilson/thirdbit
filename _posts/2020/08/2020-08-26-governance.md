---
title: "Governance dot Em Dee"
date: 2020-08-26
---

I had another good conversation with [Mike Hoye](http://exple.tive.org/blarg/) this week
about life, the Internet, and everything.
I always learn a lot talking with him,
and what I realized this time is that *governance should be discoverable*.
Pretty much every open source project has a `LICENSE.md` file in their root directory these days,
and most now have a `CONDUCT.md` file as well.
Between them,
these files tell passers-by how they're allowed to use the software
and what social norms they're required to adhere to if they want to contribute to it.
But how can they find out who decides what the project is going to do next,
or who gets a say in deciding that?
Non-profit organizations like the [Python Software Foundation](https://www.python.org/psf/)
have bylaws (they're legally required to),
but they're exceptional cases.
Smaller projects often have a `CONTRIBUTING.md` file,
but those usually describe how to set up a build environment and how to file bug reports,
not how decisions are made or by whom.

Spelling this out is an important part of making a project inclusive.
As Jo Freeman pointed out fifty years ago in her influential essay
"[The Tyranny of Structurelessness](https://www.jofreeman.com/joreen/tyranny.htm)",
every organization has a power structure:
the only question is whether it's accountable or not.
If a group says it doesn't have rules,
what it's really saying is that it's run by an old boys' network,
and that getting things done depends on your personal connections with unofficial influencers
and on how self-confident and assertive you are.
If you didn't room with one of the core developers in college,
aren't part of another's anime fan group,
and aren't willing to barge into discussions,
you might effectively be voiceless.

An organiation's governance can be summed up in answers to five key questions:

1.  Who gets a say in which decisions
    (where "gets a say" means "must approve" or "can veto"---being consulted
    is nothing more than a social nicety without guarantees of real influence).
2.  How to get a decision made.
3.  How to find out what decisions have been made.
4.  How to become part of the decision-making process (e.g., how to get a vote).
5.  How to change these rules (i.e., how to amend the constitution).

Most open source projects [don't explain any of this](https://opensource.com/open-organization/18/4/new-governance-model-research),
but I think that doing so would facilitate
[legitimate peripheral participation](https://en.wikipedia.org/wiki/Legitimate_peripheral_participation)
in the same way that "[infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code)" does.

I would therefore like every open project to have a file in its root directory called `GOVERNANCE.md`,
but I don't think projects should write these files themselves.
Instead,
they should be able to choose a model from a small set of tried-and-tested alternatives,
just as they pick [an OSI-approved license license](https://opensource.org/)
or adopt [the Contributor Covenants](https://www.contributor-covenant.org/).
For example,
a brand-new individual project could add the "benevolent dictator" governance file to its repository:

1.  One person (typically the project's founder) has final say on everything.
2.  To get a decision, file an issue tagged "discussion".
    The BD will triage it like any other issue
    and either make an immediate decision or invite commentary from other contributors before deciding.
3.  Decisions are recorded in a page called `decisions` in the project's wiki
    in reverse chronological order.
4.  The BD will listen carefully to suggestions when making decisions,
    but any votes are discretionary and purely advisory.
    (In practice, a BD who doesn't listen quickly finds themselves working alone again.)
5.  The BD can change these rules at any time,
    and will announce changes in the project's blog and by updating this file.

This is how most new or small projects are run right now,
and I suspect it would be adopted as widely as the [MIT License](https://opensource.org/licenses/MIT)
or the [GPL](https://opensource.org/licenses/gpl-license).
Another is [Martha's Rules]({{site.github.url}}/2019/06/13/marthas-rules.html),
which work well when decision-making is shared equally among a handful to a few dozen people.
I don't think we would need many more,
but agreeing on names and wording and making rules findable
would make life a little bit easier for a lot of people.
