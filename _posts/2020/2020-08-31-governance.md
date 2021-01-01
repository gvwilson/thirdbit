---
title: "Governance"
date: 2020-08-31
year: 2020
---

I had another good conversation with [Mike Hoye](http://exple.tive.org/blarg/) this week
about life, the Internet, and everything.
I always learn a lot talking with him,
and what I realized this time is that *governance should be discoverable*.
Pretty much every open source project has a `LICENSE.md` file in their root directory these days,
and most now have a `CONDUCT.md` file as well.
These files tell passers-by how they're allowed to use the software
and what social norms they're required to adhere to if they want to contribute to it.

But how can they find out who decides what the project is going to do next,
or who gets a say in deciding that?
Large organizations like the [Python Software Foundation](https://www.python.org/psf/)
[typically have bylaws](https://arxiv.org/abs/2005.10063)---as registered non-profits,
they're legally required to---but
[most smaller organizations don't explain any of this](https://opensource.com/open-organization/18/4/new-governance-model-research).
They may have a `CONTRIBUTING.md` file,
but that usually describes how to set up a build environment and how to file bug reports,
not how decisions are made or by whom.

Spelling this out helps people [make their first contributions](https://en.wikipedia.org/wiki/Legitimate_peripheral_participation),
which [helps projects grow](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1007296).
It's also better ergonomics:
if you don't know who to ask or whose consent you need,
whatever you want probably won't happen.
But most importantly,
it's essential to making a project genuinely inclusive.
Every organization has a power structure;
the only question is [whether it's accountable or not](https://www.jofreeman.com/joreen/tyranny.htm).
If a group says it doesn't have rules,
what it's really saying is that it's an old boys' network,
and that getting things done depends on your personal connections with unofficial influencers
and on how self-confident and assertive you are.
If you didn't get drunk with one of the core developers in college
and you're not willing to barge into discussions,
then no matter how hard you work you might be a second-class citizen of this project forever.

This is why I'm convinced that every open project should have a file in its root directory called `GOVERNANCE.md`
that explains:

1.  Who gets a say in which decisions
    (where "gets a say" means "must approve" or "can veto"---promises of consultation
    are a social nicety without such guarantees).
2.  How to get a decision made.
3.  How to find out what decisions have been made.
4.  How to become part of the decision-making process (e.g., how to get a vote).
5.  How to change these rules (i.e., how to amend the constitution).

To make explicit governance easier and more consistent,
projects should be able to choose a model from a small set of tried-and-tested alternatives,
just as they pick [an OSI-approved license license](https://opensource.org/)
or adopt [the Contributor Covenants](https://www.contributor-covenant.org/).
For example,
a project with a single decision maker (typically the founder) could copy
the [bucks stops here]({{ '/files/2020/08/buck-stops-here.md' | relative_url }}) file into its repository,
while a consensus-based team project could use [Martha's Rules]({{ '/files/2020/08/marthas.md' | relative_url }}).
I don't think we would need many more,
but agreeing on names and wording,
making rules findable,
and providing [a simple guide](https://choosealicense.com/)
would make life a little bit easier for a lot of people.

*Update: <http://lua-users.org/lists/lua-l/2008-06/msg00407.html> explains
how the [Lua](https://www.lua.org/) project runs itself and why.*