---
title: "What (a subset of) Done Looks Like"
date: 2021-11-07
year: 2021
---

I recently ran [a workshop on managing research software projects]({{'/mrsp/' | relative_url}}),
and one of the questions that came up was,
"What does 'done' look like?"
There are lots of answers elsewhere for the technical side
[[1](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745),
[2](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510),
[3](https://merely-useful.tech/py-rse/)],
but what about project management and governance?
Here's a first cut of the artifacts used to support those activities
for a project with up to a couple of dozen contributors;
additions, deletions, and corrections would be very welcome.
(As always, please [email me](mailto:{{site.author.email}}):
the last time I opened up comments on this site
it took all of two days for the trolls to show up.)

<div class="tightlist" markdown=1>

1.  A shared Google Drive with a doc called "Roles and Responsibilities"
    -   Google Doc because some collaborators aren't comfortable with Git
        -   And to make it easier to paste in figures and screenshots
    -   Defines roles and explains what each is responsible for in one page
    -   Each role has a doc of its own with its checklists
1.  The same shared Google Drive has one doc per year called (e.g.) "Progress 2022"
    -   Section headings are weekly meeting dates
        -   Table for each week with columns `Name`, `Progress`, `Plans`, and `Problems` (bullet points)
        -   Anything too long to fit comfortably in the table is linked to an issue in the project's GitHub repository
    -   Project has a little script that lists issues and PRs touched by each person (reminder)
1.  Weekly hour-long status meeting (which often finishes early)
    -   On Wednesday so that people aren't scrambling on Friday or a weekend (or holiday Monday) to write status updates
    -   Rotating moderator: last week's moderator is this week's note-taker
    -   Before meeting, members star points in the status doc they want to discuss
    -   Moderator draws up agenda based on starred items
1.  Proposals can be done as either Google Docs (in shared folder) or GitHub issues
    -   Must be flagged to moderator the day before the meeting for inclusion
    -   Added to agenda
1.  Project has a single repo with code, website, tutorials, etc.
    -   So that releases are in sync
1.  Uses Google Docs (again) for publicity materials (because non-programmers)
    -   All materials are owned by project account, not personal accounts
    -   Every change larger than a typo produces a new doc
    -   Every doc has date in title, e.g., "University Press Release 2022-05-13"
1.  Budgets for grant proposals, job contracts, etc., are stored in university system
    -   Legal requirement
1.  `GOVERNANCE.md` in root directory of project explains [Martha's Rules]({{'/2019/06/13/marthas-rules/' | relative_url}})
    -   And membership rule:
        anyone who has had a PR merged in the last year or made some other significant contribution (as determined by the PI)
    -   List of active members and alumni is in the foot of `GOVERNANCE.md`
1.  Another small script checks that the tags in each project repository are consistent
    and that each issue has at least one tag
1.  Project website has a "skills ladder" on the "Positions" page (even when positions aren't open)
    -   "What we mean by each of these terms for the research and coding tracks"
1.  Project website has a value statement and a contact address that *isn't* anyone's personal address
    -   Plus a page for publications
    -   Plus a page pointing at all repositories
    -   Plus a "Getting Started" page
    -   And a "Who's Using Us How" page
    -   And a "People" page
1.  The "help" option for the software includes the URL to the project page

</div>

## A Note on Consensus

As Jo Freeman pointed out in "The Tyranny of Structurelessness", every group has a power structure;
the only question is whether it is explicit and accountable, or implicit and unaccountable.
Unfortunately,
GitHub's [Minimum Viable Governance](https://github.com/github/MVG) guidelines duck this issue:

> **2.1. Consensus-Based Decision Making**
>
> Projects make decisions through consensus of the Maintainers.
> While explicit agreement of all Maintainers is preferred, it is not required for consensus.
> Rather, the Maintainers will determine consensus based on their good faith consideration of a number of factors,
> including the dominant view of the Contributors and nature of support and objections.
> The Maintainers will document evidence of consensus in accordance with these requirements.

In practice,
since people's idea of what constitutes "good faith" varies widely,
"consensus-based" means governance by the self-confident, stubborn, and well-connected,
which marginalizes a lot of people.
[Martha's Rules]({{'/2019/06/13/marthas-rules/' | relative_url}}) and other procedures
for putting proposals forward and voting on them aren't perfect—democracy never is—but
they're better.
