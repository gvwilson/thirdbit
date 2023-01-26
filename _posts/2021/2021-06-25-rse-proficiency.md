---
title: "A Proficiency Test for Research Software Engineers"
date: 2021-06-25
year: 2021
---

Back in 2014,
I worked with Mike Jackson, James Hetherington, and Andrew Turner
to develop a skills assessment for people who wanted to use the DiRAC supercomputing facility.
It never really caught on—it's politically impossible to tell professors
who have already paid for machine time
that their grad students don't know enough about software development to use it efficiently—but
I'm publishing it here in the hope that it will spur others to share
what people ought to know and how we can tell if they know it.

## 1. Introduction 

1.  You have 90 minutes to complete the following tasks.

1.  You may use the web, man pages, and any other resources you would usually use when programming.

1.  If you are completing the assessment with colleagues,
    you are free to discuss hints, tips and the usage of commands,
    but do not share the answers to tasks.

1.  If at any point you would like clarification,
    please do not hesitate to ask.

1.  If at any point you are unable to complete a task,
    feel free to move on to the next task.
    The major tasks (shell, shell scripts, testing, code review) are all independent.
    You may ask for help before moving on,
    but doing so will be considered equivalent to not completing that task.

Clone the exam repository at [URL provided].
This serves as both a repository and your working copy.
You will do all of your work in this local repository
and use version control to commit your solutions as you go.

## 2. Shell

Use the `cd` command to go into the `python/` directory,
which contains two subdirectories.
Within that directory,
use a _single_ shell command to create a list of all files
with names ending in `.dat`
in or below this directory
in a file called `all-dat-files.txt`.

Create a file called `shell-command.txt`
containing the command you ran to get the list of files,
add this to the version control repository,
and commit it.

Add `all-dat-files.txt` to the version control repository and commit it.

## 3. Shell Scripts

Write a script called `do-many.XX` (scripting language of choice)
that runs `power2.py` for the inputs listed in the file `input.d`
and saves the output in a file calld `output.d`.
The output file must contain the following when you are done:

```
16
8
2
1
8
1
32
2
1
```

You do not need to do error-checking on the command-line parameters,
i.e.,
you may assume that they are all non-negative integers.

Add `do-many.sh` to the version control repository and commit it.

## 4. Testing

`analyze.py` contains a function called `running_total`
that is supposed to calculate the total of each strictly increasing sequence of integers in a list:

```
running_total([1, 2, 1, 8, 9, 2])       == [3, 18, 2]
running_total([1, 3, 4, 2, 5, 4, 6, 9]) == [8, 7, 19]
```

`test_analyze.py` contains a unit test implementing the first example above.
Write four more unit tests that you think are most important to run to test this function.
Do not test for cases of invalid input
(e.g., inputs that are strings,
lists of lists,
or an
input that isn't a flat list of numbers).
You can run your tests using the command:

```
py.test test_analyze.py
```

Add `test_analyse.py` to the version control repository.

## 5. Scale Testing

What is the approach you would use to check the scaling of a program called `long_run.py`?
Explain your method in 50 words.

Create a file called `scale-test.txt` with the commands you would use
and add this to the version control repository.

## 6. Code Review

The programs `power2.py`, `power2.c`, and `power2.f`
each take a single non-negative integer as a command line argument
and produce the powers of two that total to that number.
For example:

```
./power2.py 27
```

produces:

```
16
8
2
1
```

Choose the language you are most comfortable with
and change this program in at least 3 ways to improve its readability, understandability, and modularity
*without* changing its behaviour.

Commit your changes to the version control repository.

## 7. SSH keypairs

Assume you have an account with the username `me` on a remote host called `server.dirac.org`.
You want to use a SSH public/private keypair and associated passphrase to access the remote host.
What commands would you use to create your SSH keypair
and to update the remote host with your public key?

Create a file called `ssh-keypair.txt` with the commands you would use
and add this to the version control repository.

## 8. Secure copy

Assume that in your `me` account on server.dirac.org you have 100 files
called `detector001.dat`, …, `detector099.dat`
in a directory called `data` immediately below your home directory.
What commands would you use to securely copy the directory that contains all these files
from `server.dirac.org` to your local computer?

If a few files have been changed within this directory on your `server.dirac.org` account,
what command would you use to copy over only the changed files?

Create a file called `secure-copy.txt` with the commands you would use
and add this to the version control repository.

## 9. Archiving

Create a file called `save-work.txt` containing a single command
to create an archive called either `exam.tar.gz` or `exam.zip` in your home directory
with the files you have created.
This archive must _not_ contain the `.git` directory.

Run `save-work.txt` and email `exam.tar.gz` or `exam.zip` to your examiner.
