---
title: "Governance dot Em Dee"
date: 2020-08-26
---

I had another good conversation with [Mike Hoye](http://exple.tive.org/blarg/) last night
about life, the Internet, and everything.
I always learn a lot talking with him,
and what I realized this time is that *governance should be discoverable*.
Pretty much every open source project has a `LICENSE` file in their root directory these days,
and most now have a `CONDUCT` file as well.
Between them,
these files tell passers-by how they're allowed to use the software
and what social norms they're required to adhere to if they want to contribute to it.

But how can they find out who decides what the project is going to do next,
or who gets a say in deciding that?
Many projects have a `CONTRIBUTING` file,
but those usually describe how to set up a build environment and where to post questions,
not how decisions are made or who makes them.
Non-profit organizations like the [Python Software Foundation](https://www.python.org/psf/)
have bylaws (they're legally required to) but they're exceptional cases.
"[Infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code)" is a powerful idea;
standard licenses,
install scripts,
build files,
and issue labeling conventions like "good first issue" all make projects run more smoothly
*and* make them more inclusive.

That last point is the most important one.
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
you are effectively voiceless.

I therefore think every open project should have a file in its root directory called `GOVERNANCE`
that lays out the answers to five key questions:

1.  Who gets a say in which decisions.
2.  How to get a decision made.
3.  How to find out what decisions have been made.
4.  How to become part of the decision-making process (e.g., how to get a vote).
5.  How to change these rules (i.e., how to amend the constitution).

I don't think projects should write these files themselves.
Instead,
we should assemble a small set of common governance models that organizations can choose from,
just as they pick [an OSI-approved license license](https://opensource.org/)
or adopt [the Contributor Covenants](https://www.contributor-covenant.org/).
One of these models should be "benevolent dictator":

1.  One person (typically the project's founder) has final say on everything.
2.  File an issue tagged "discussion".
    The BD will triage it like any other issue
    and either make an immediate decision or invite commentary from other contributors.
3.  Decisions are recorded in a page called `decisions` in the project's wiki
    in reverse chronological order.
4.  Doesn't apply:
    the BD may grant commit privileges to regular contributors,
    and a good one will listen carefully to their suggestions when making decisions,
    but any votes are purely advisory.
5.  Propose changes to the BD.

This is how most new or small projects are run right now.
It's a good model,
and I suspect it will be as widely used as the [MIT License](https://opensource.org/licenses/MIT)
or the [GPL](https://opensource.org/licenses/gpl-license),
but it's not the only one.
Another is [Martha's Rules]({{site.github.url}}/2019/06/13/marthas-rules.html),
which work well when decision-making is shared equally among a handful to a few dozen people.
I don't think we would need many more,
but agreeing on names and wording and making rules findable
will make life a little bit easier for a lot of people.
