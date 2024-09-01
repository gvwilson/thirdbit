---
title: "Labels for Writing Projects Revisited"
date: 2024-09-02
year: 2024
---

A few months ago I wrote about [the GitHub issue labels I use for writing projects][labels-1].
In retrospect,
that set is more complicated than the problem requires,
but the problem itself is also more complicated than it first seems.

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
| add              | request for new feature               |
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

[cc]: https://creativecommons.org/
[labels-1]: {{'/2024/03/07/labels/' | relative_url}}
[sql-tutorial-license]: https://github.com/gvwilson/sql-tutorial/blob/main/LICENSE.md
