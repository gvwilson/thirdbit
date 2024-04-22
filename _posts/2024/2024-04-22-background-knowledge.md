---
title: "Background Knowledge"
date: 2024-04-22
year: 2024
---

I would like to teach people how to use Git hooks in [this tutorial][sys-tutorial].
After reading [the official explanation of Git hooks][git-hooks] I do this:

```
# Make a place for this example.
$ mkdir example
$ cd example

# Turn it into a Git repository.
$ git init .
Initialized empty Git repository in /Users/gvwilson/example/.git/

# Create a pre-commit script that always fails (i.e., exits with non-zero status).
$ cat > .git/hooks/pre-commit.sh
#!/bin/sh
echo "hook running"
exit 1

# Make that script executable.
$ chmod 755 .git/hooks/pre-commit.sh

# Run it and check its exit status.
$ .git/hooks/pre-commit.sh
hook running

$ echo $?
1

# Create some content.
$ cat > a.txt
content

# Try committing it.
# The hook should print "hook running" and the commit should be prevented.
$ git add a.txt

$ git commit -m "should not work"
[main (root-commit) 7e5fcba] should not work
 1 file changed, 1 insertion(+)
 create mode 100644 a.txt

# Whoops: the commit seems to have happened.
# Let's check.
$ git log
commit 7e5fcba19343b513a88c3608126535416b67185d (HEAD -> main)
Author: Greg Wilson <gvwilson@third-bit.com>
Date:   Mon Apr 22 18:14:18 2024 -0400

    should not work
```

OK, clearly I'm doing something wrong.
After reading [this Stack Overflow question][stack-overflow] I try this:

```
# See what core.hooksPath is set to: turns out it isn't.
$ git config --local core.hooksPath

# Double-check.
$ cat .git/config
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true

# Set it.
$ git config --local core.hooksPath .git/hooks
$ git config --local core.hooksPath
.git/hooks
$ cat .git/config
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
	hooksPath = .git/hooks

# See if that has fixed things.
$ cat > b.txt
more content
$ git add b.txt
$ git commit -m "should not work"
[main 3c42b28] should not work
 1 file changed, 1 insertion(+)
 create mode 100644 b.txt
```

My questions are:

1.  Why isn't this working? (I'm using Git 2.39.3 on MacOS Sonoma 14.4.1 with Bash 3.2.57.)
2.  What would someone who is new to the world of scripts, actions, and what-not need to know
    in order to understand what I've done so far and then debug it?
    The list includes, but is not limited to, `chmod`, `#!`, zero and non-zero exit statuses (statii?),
    the fact that Git is configurable, and the commands used to configure it.

The second matters more to me than the first.
I'm sure I can figure this out if I go and make tea,
but working backwards from something that someone might reasonably want to do (or debug)
is a good way to design a lesson,
particularly if you want to avoid skipping things that you have known for so long
that you forget they needed to be learned.
As always, [your thoughts are appreciated](mailto:{{site.author.email}}).

[git-hooks]: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
[stack-overflow]: https://stackoverflow.com/questions/49912695/git-pre-and-post-commit-hooks-not-running
[sys-tutorial]: https://gvwilson.github.io/sys-tutorial
