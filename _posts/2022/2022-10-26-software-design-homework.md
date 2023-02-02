---
title: "Software Design Homework"
date: 2022-10-26
year: 2022
---

I'm a big fan of [DVC][dvc] for managing large files in Git,
but it doesn't handle one of our most important use cases,
and I think that working through that would be a great homework exercise
for a class on software design.
If you use this,
please let me know how it went.

---

Many people want to manage large files like videos or machine learning datasets
in the same way that they manage their code,
but Git doesn't handle multi-gigabyte files well.
To work around this,
tools like [Git LFS][git-lfs] and [DVC][dvc] allow users to
store the actual file somewhere else (like a NAS or the cloud)
and put a placeholder in the Git repository that points at the actual file.

<img src="{{'/files/2022/dvc.svg' | relative_url}}" alt="Structure of DVC class="centered">

1.  The placeholder file is just a bit of JSON or YAML that contains
    the original file's name
    and its remote identifier (typically a file hash).

2.  When the user needs the actual file,
    they run a command that localizes it but does *not* add it to Git.
    (These tools typically add the file to the directory's `.gitignore`
    to prevent it accidentally being added or committed.)

3.  The user can safely delete the actual file whenever they need the space
    and re-localize it later.

4.  If the user wants to update the file (e.g., replace the dataset with a newer version)
    they can use the tool to modify the metadata in the placeholder and re-commit it.

Systems like this don't just save disk space:
they also allow large files to be shared between Git projects without unnecessary duplication:
any particular file is only ever stored once in the cloud,
but any number of placeholders referring to it can be added to any number of projects.

So here's our use case:
we want users to be able to add notes about large files.
These notes should be versioned along with the data,
so the obvious way to do this is to add another field to the placeholder metadata called `notes`.
The problem is that placeholder files aren't shared between projects:
if I add a note to `large.xyz.dvc` in Project A and commit it,
that note is visible to everyone else who has a copy of Project A
but is *not* visible to anyone working in the Git repo for Project B.
What should we do about this?

1.  "Notes aren't shared between projects."
    This option is the easiest to implement but the least satisfying to users,
    who want a global view of what anyone else using the dataset has said about it.

2.  "Store the notes in a second file in the cloud beside the main copy of the large file."
    Cool: how are you going to manage merge conflicts in the notes?

3.  "Store the notes in a database or another Git repository or…"
    See above, plus now you have an extra thing to manage (access permissions, backups, etc.).

For X% of your course grade:

1.  Come up with at least one other solution and explain its pros and cons.

2.  Implement at least one solution (other than the "don't share" solution).

[dvc]: https://dvc.org/
[git-lfs]: https://git-lfs.github.io/
