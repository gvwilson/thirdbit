---
title: "Labels for Technical Writing Projects"
date: 2024-09-12
year: 2024
---

*(Originally posted in the [rOpenSci blog][ropensci]—my thanks to [Yanina Bellini Saibene][yanina] for editing.)*

Over the past thirty years I have written five technical books,
co-written three others,
and edited a further six.
Since 2007 they have all lived in GitHub repositories,
as did the first versions of the [Software Carpentry][swc] lessons that I helped to write.

A few months ago I wrote about [the GitHub issue labels I use][labels-1]
for writing projects like these.
As I put that post together,
I realized that I wasn't actually using all of the labels I had created,
and that the problem of choosing good labels for a mixture of code and prose
is more complicated than it seems.

1.  GitHub only allows one set of labels per project,
    which means that the labels you would want to apply to issues
    are in the same pile as labels you'd want to apply to pull requests (PRs).
    This overlap quickly leads to confusion:
    "bug" is the right label for an issue reporting a problem,
    but doesn't feel appropriate for the PR that fixes the problem.
    ("Wait, is this PR adding a bug?")
    Most projects use two different labels (e.g., "bug" and "fix"),
    but after going back and forth,
    I've settled on "fix" to mean both "Please fix this" (in an issue)
    and "This contains a fix" (in a PR).

1.  By default,
    GitHub provides nine labels for issues and PRs.
    Fully a third of these—`duplicate`, `invalid`, and `wontfix`—describe reasons to close an issue
    or discard a PR.
    That seems excessive to me,
    and I feel it's polite to add a sentence or two of explanation as a comment.
    (You have to do this anyway when marking an issue or PR as `duplicate` to point at what it's duplicating.)

    *Note: I find it a bit ironic that GitHub provides three ways to say "no" but none for saying "yes".
    If I was going to use labels to mark closed issues,
    I would include "resolved" and/or "merged".*

    *Also note: English doesn't have an antonym for "mistake", i.e., we don't have a single word
    that means, "A thing done well."
    We sometimes say "a score" or "a win" to mean this,
    but those are the outcome, not the act itself.
    I sometimes wonder what this absence says about English speakers' view of the world…*

1.  When you create a new project on GitHub,
    you can select any of several widely-used licenses.
    However,
    all of those licenses apply to code:
    the [Creative Commons][cc] licenses for prose (written work) aren't offered.
    I always wind up writing [a custom `LICENSE.md`][sql-tutorial-license] to say that
    all of the written material is made available under the CC-BY-NC-4.0 license
    while the software is made available under the MIT License.

    I mention this here because I find other things missing as well for writing projects.
    One of GitHub's default issue labels is "documentation",
    but I don't think the prose in a lesson or chapter is documentation of code:
    the code is there to support the writing.

So here's what I'm using in my current writing projects:

| Name             | Purpose                               |
| ---------------- | ------------------------------------- |
| add              | (request for) new feature             |
| change           | exists but could be better            |
| code             | in software                           |
| discussion       | questions and conversations           |
| fix              | something is broken                   |
| good first issue | good for newcomers                    |
| governance       | meta-discussion of project management |
| prose            | in written content                    |
| task             | one-off task                          |
| tooling          | infrastructure                        |

In more detail:

-   `add`, `change`, and `fix` are meant to be mutually exclusive
-   `code` and `prose` can be used together (e.g., a new lesson adds both)
-   `discussion` and `governance` are for project management
-   `tooling` is used for the build system, page templates, etc.
-   `task` is something that needs to be done once (e.g., "publish a release")
-   `good first issue` is there because we want people to feel welcome

I'd enjoy hearing about what you're using—please [email me](mailto:{{site.author.email}})
if you'd like to start a conversation.

> Later: someone mailed to ask why I use the "NC" (non-commercial) clause in my license.
> The answer is that I don't think it's sustainable for companies to take lesson material that people have made public
> and profit from it without compensating the authors of that material.
> If you, as an academic, want to re-use my notes and slides, you are very welcome to do so;
> if Elsevier wants to bundle them up in a book and charge students €60 for it,
> I want to be able to say "no",
> or to say, "yes, but you have to give me some of that so that I can keep producing this material".
> 
> The NC clause is also part of my deal with my publisher (CRC Press):
> they are OK with me putting an HTML version of [*Software Design by Example*][sdxpy] and other books online
> for people to read for free,
> but would _not_ be OK with some other for-profit publisher taking that and republishing it without permission.
> I think that's a fair bargain:
> people who can't afford to buy the book can read it,
> and the publisher can make money from the printed, PDF, and EPUB versions
> as compensation for the effort they put into editing and publicizing the book.

> Later: a collaborator pointed out an interesting inconsistency.
> I follow [Conventional Commits][conventional] style in my Git commit messages,
> so the title line of each commit starts with a single word like "fix",
> "feat" (short for "feature"),
> or "publish" (when all I'm doing is rebuilding the HTML version of the lesson).
> These words don't line up with the labels I use for issues and PRs:
> I don't have a label for "publish",
> and I use "feat" instead of "add" for something new.
> I'm embarrassed that I didn't notice this before,
> and now I need to think about what to do about it…

[cc]: https://creativecommons.org/
[conventional]: https://www.conventionalcommits.org/
[labels-1]: {{'/2024/03/07/labels/' | relative_url}}
[ropensci]: https://ropensci.org/blog/2024/09/12/labels-writing-projects/
[sdxpy]: https://third-bit.com/sdxpy/
[sql-tutorial-license]: https://github.com/gvwilson/sql-tutorial/blob/main/LICENSE.md
[swc]: https://carpentries.org/
[yanina]: https://yabellini.netlify.app/
