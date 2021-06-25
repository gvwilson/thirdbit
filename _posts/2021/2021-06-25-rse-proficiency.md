---
title: "A Proficiency Test for Research Software Engineers"
date: 2021-06-25
year: 2021
---

Formative Assessment for the DiRAC Supercomputing Facility 2014

Mike Jackson (Software Sustainability Institute, University of Edinburgh)
Greg Wilson (Software Carpentry)
James Hetherington (University College London)
Andrew Turner (University of Edinburgh)


1. Introduction 

You have 90 minutes to complete the following tasks.

You may use the web, 'man' pages and any other resources you would
usually use when programming.

If you are completing the assessment with colleagues, you are free to
discuss hints, tips and the usage of commands, but do not share the
answers to tasks.

If at any point you would like clarification, please do not hesitate
to ask.

If at any point you are unable to complete a task, feel free to move
on to the next task.The major tasks (shell, shell scripts, testing,
code review) are all independent.You may ask for help before moving
on, but doing so will be considered equivalent to not completing that
task.

1a.Submit evidence: Version Control

Clone the exam repository https://bitbucket.org/softwaresaved/dirac-test.git

This serves as both a repository and your working copy.You will do all
of your work in this local repository, and use version control to
commit your solutions as you go.

2. Shell

Use the cd command to go into the python/ directory, which contains 2
subdirectories. Use a single shell command to create a list of all
files (within the python directory) with names ending in .dat in or
below this directory in a file called all-dat-files.txt.

2a. Submit evidence: Version Control

Add all-dat-files.txt to the version control repository and commit it.

Create a file, shell-command.txt, containing the command you ran to
get the list of files, add this to the version control repository and
commit it.

3. Shell Scripts

Write a script called do-many.XX (scripting language of choice) that
runs power2.py for the inputs listed in the input.d file and all the
outputs are listed in a file called output.d

The output file must having the following output:

    16
    8
    2
    1
    8
    1
    32
    2
    1

as its output.You do not need to do error-checking on the command-line
parameters, i.e., you may assume that they are all non-negative
integers.

3a. Submit evidence: Version Control

Add do-many.sh to the version control repository and commit it.

4. Testing

The analyze.py program contains a function called running_total, which
is supposed to calculate the total of each strictly increasing
sequence of integers in a list:

    running_total([1, 2, 1, 8, 9, 2])       == [3, 18, 2]
    running_total([1, 3, 4, 2, 5, 4, 6, 9]) == [8, 7, 19]

In the file test_analyze.py, you will find a unit test implementing
the first example above. Write four (4) more unit tests that you think
are most important to run to test this function.Do not test for cases
of invalid input (e.g. inputs that are strings, lists of lists, or an
input that isn't a flat list of numbers).

You can run your tests using the command:

    py.test test_analyze.py

4a. Submit evidence: Version Control

Add test_analyse.py to the version control repository.

5. Scale Testing

What is the approach you would use to check the scaling of your code?
Explain your method in 50 words.

5a. Submit evidence: Version Control

Create a file, scale-test.txt, with the commands you would use, and
add this to the version control repository.

6. Code Review

The program power2.py, power2.c and power2.f takes a single
non-negative integer as a command line argument and produces the
powers of two that total to that number.For example:

    ./power2.py 27

produces:

    16
    8
    2
    1

Choose the language you are most comfortable with and change this
program in at least 3 ways to improve its readability,
understandability and modularity *without* changing its behaviour.

6a. Submit evidence: Version Control

Commit your changes to power2.py/power2.c/power2.f to the version
control repository.

7. SSH keypairs

Assume you have an account, username "me", on a remote host,
server.dirac.org. Password-based authentication to remote hosts are
vulnerable to brute-force attacks. SSH public key authentication can
provide you with additional security.

Supposing you want to use a SSH public/private keypair, and associated
passphrase, to access the remote host, what commands would you use to
create your SSH keypair and to update the remote host with your public
key?

Assume that you are using the default files *name the file* and
therefore when you are prompted to enter the file in which you want to
save the key you would press enter to use the default files.

7a. Submit evidence: Version Control

Create a file, ssh-keypair.txt, with the commands you would use, and
add this to the version control repository.

8. Secure copy

Assume that in your "me" account on server.dirac.org you have 100
files, detector001.dat, ..., detector099.dat, in a directory, data.

What commands would you use to securely copy the directory that
contains all these files from server.dirac.org to your local account?

Assume a few files have been changed within this directory on your
Dirac account, what command would you use to copy over only the
amended files.

8a. Submit evidence: Version Control

Create a file, secure-copy.txt, with the commands you would use, and
add this to the version control repository.

Assesment Complete

Please tar/zip your dirac-test directory and email to your examiner.
