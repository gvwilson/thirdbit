---
layout: teaching
permalink: /teaching/design.html
title: "How to Teach Programming (and Other Things): Course Design"
---

# Course Design

Designing a good course is as hard as designing good software.
To help you,
this document describes a process based on evidence-based teaching practices:

- It lays out a step-by-step progression to help you figure out what
  to think about in what order.
- It provides spaced check-in points so you can re-scope or redirect
  effort.
- The end product specifies deliverables clearly so you can finish
  development without major surprises.
- Everything from Step 2 onward goes into your final course, so there
  is no wasted effort.
- Writing sample exercises early lets you check that everything you
  want your students to do actually works.

We use the design of an introduction to the Unix shell for data scientists as a running example.

Note: the steps are described in order of increasing detail,
but the process itself is always iterative.
You will frequently go back to revise earlier work
as you learn something from your answer to a later question
or realize that your initial plan isn't going to play out the way you first thought.

## Terminology and Structure

- A **course** is a self-contained module.
- A **chapter** is a major section of a course.
- Chapters are made up of **lessons**,
  each of which has a short video and a handful of **exercises**.

## Step 1: Brainstorming

The first step is to throw together some rough ideas
so that you and your colleagues can make sure your thoughts about the course are aligned.
To do this,
write some point-form answers to three or four of the questions listed below.
You aren't expected to answer all of them,
and you may pose and answer others if you think it's helpful,
but you should always include a couple of answers to the first.

1. What problem(s) will student learn how to solve?
2. What concepts and techniques will students learn?
3. What technologies, packages, or functions will students use?
4. What terms or jargon will you define?
5. What analogies will you use to explain concepts?
6. What heuristics will help students understand things?
7. What mistakes or misconceptions do you expect?
8. What datasets will you use?

You may not need to answer every question for every course,
and you will often have questions or issues we haven't suggested,
but couple of hours of thinking at this stage can save days of rework later on.

Checkin: a rough scope for the course that you have agreed with your colleagues.

### Running Example

The questions and answers for the Unix shell course are:

1. *What problem(s) will student learn how to solve?*
   How to combine existing/legacy tools;
   how to make analyses reproducible.
2. *What techniques or concepts will students learn?*
   History; pipes; shell scripts.
3. *What technologies, packages, or functions will students use?*
   Bash shell; basic Unix commands (`cd`, `ls`);
   basic data manipulation commands (`head`, `cut`, `grep`).
4. *What terms or jargon will you define?*
   Filesystem; redirection; pipe; wildcard.
5. *What analogies will you use to explain concepts?*
   Command-line pipeline is like chemistry pipeline;
   shell scripts are like snippets of command history.
6. *What heuristics will help students understand things?*
   Use filenames that are easy to match with tab completion and wildcards;
   build pipelines step by step.
7. *What mistakes or misconceptions do you expect?*
   That the shell shows the same files and folders as the GUI interface they're used to;
   definition vs. use of variables (especially loop variables).
8. *What datasets will you use?*
   dental records.

## Step 2: Who is this course for?

"Beginner" and "expert" mean different things to different people,
and many factors besides pre-existing knowledge influence who a course is suitable for.
The second step in designing a course is therefore to agree on an audience with your CL.
To help you do this,
we have created [learner personas](personas.md) for typical DataCamp students.
Each persona describes the person's general background,
what they already know,
and what they think they want to do.

After you are done brainstorming,
you should go through these personas
and decide which of them your course is intended for,
and how it will help them.
While doing this,
you should make some notes about what specific prerequisite skills or knowledge you expect students to have
above and beyond what's in the persona.
If none of our personas capture your intended audience,
talk to your CL to make sure you agree on who you're aiming for.

Checkin: brief summaries of who your course will help and how.

### Running Example

This is one of the profiles provided:

> Sindhu is 28 and lives in Bangalore.  She has a BSc in Biochemistry
> and an MSc in Pharmacy, and is now a vaccine researcher at a
> pharmaceutical company.  Sindhu did two courses in statistics and
> experimental design while at university using Excel and SPSS, and
> now wants better data science skills to help her advance in her
> current career.  She isn't sure which languages or skills to start
> with, but knows that she's going to need to use her company's
> compute cluster, and has been told that it runs Unix.  Sindhu
> commutes an hour each way every day by bus, and likes things she can
> do during that time.

And this is the description of how this course will help:

> This course will introduce Sindhu to basic shell commands, to the
> pipe and filter model she can use to combine those commands, and
> show her how to capture her workflows in simple shell scripts.  It
> will *not* show her how to connect to remote machines using SSH, but
> is a prerequisite for the course that does.

## Step 3: What will learners do along the way?

The best way to make the goals in Step 1 firmer is
to write full descriptions of a couple of exercises
that students will be able to do toward the end of the course.
Writing exercises early is directly analogous to [test-driven development][tdd]:
rather than working forward from a (probably ambiguous) set of learning objectives,
designers work backward from concrete examples of where their students are going.
Doing this also helps uncover technical requirements
that might otherwise not be found until uncomfortably late in the lesson development process.

To complement the full exercise descriptions,
you should also write brief point-form descriptions of one or two exercises per chapter
to show how quickly you expect learners to progress.
(Again,
these serve as a good reality check on how much you're assuming,
and help uncover technical requirements.)
One way to create these "extra" exercises
is to make a point-form list of the skills needed to solve the major exercises
and create an exercise that targets each.

Checkin: 1-2 fully explained exercises that use the skills the student is to learn,
plus half a dozen point-form exercise outlines.

Note: be sure to include solutions with example code
so that you can check that your software can do everything you need.

### Running Example

**Complete Exercise: Building a Tool to Find Unique Values in Columns**

As the final exercise in the Unix shell course,
you are given several dozen data files, each of which is formatted like this:

```
2013-11-05,deer,5
2013-11-05,rabbit,22
2013-11-05,raccoon,7
2013-11-06,rabbit,19
```

1. Write a shell script called `unique.sh`
   that takes any number of filenames as command-line parameters
   and prints the names of the species found in each file
   in alphabetical order.
   Each file is processed separately.

> **Solution**
>
> ```
> #!/usr/bin/env bash
>
> # Find unique species in CSV files where species is the second data
> # field.  This script accepts any number of filenames as arguments
> # and processes each separately.
>
> for file in $@
> do
>   echo $file
>   cut -d , -f 2 $file | sort | uniq
> done
> ```

**Complete Exercise: Using Wildcards**

2. With one command,
   use `unique.sh` to find the unique species
   in all of the `.csv` files in the `~/archive` and `~/new` directories.
   Use wildcards to specify the names of the files to be processed;
   do *not* include the `.txt` or `.bak` files in those directories.

> **Solution**
>
> ```
> unique.sh ~/archive/*.csv ~/new/*.csv
> ```

**Exercise Outline: Manipulating Files and Directories**

What is the output of the final `ls` command in the sequence shown below?

```
$ pwd
/Users/jasmine/data

$ ls
mortality.dat

$ mkdir old
$ mv mortality.dat old
$ cp old/mortality.dat ../mortality-saved.dat
$ ls
```

1. `mortality-saved.dat old`
2. `old`
3. `mortality.dat old`
4. `mortality-saved.dat`

Uses:
- `pwd`, `ls`, `cp`, `mv`, `mkdir`
- paths
- the special path `..`

**Exercise Outline: Tracing Pipes and Redirection**

`dental.csv` contains:

```
2017-05-05,incisor
2017-05-05,bicuspid
2017-05-05,molar
2017-05-06,bicuspid
2017-05-06,incisor
2017-05-06,premolar
2017-05-07,bicuspid
2017-05-07,crown
```

What text passes through each of the pipes and the final redirect in this pipeline?

```
$ cat dental.csv | head -n 5 | tail -n 3 | sort -t , -k 2 > final.txt
```

Uses:
- `cat`, `head`, `tail`, `sort`
- pipes
- redirection
- command flags

**Exercise Outline: Selecting Data by Value**

Write a command that selects *only* data in `dental.csv` from the years 2000, 2005, and 2010.

Uses:
- `grep` (with fixed text, not regualr expressions)

**Exercise Outline: Shell Scripts**

Fill in the blanks in `dates.sh`
to select unique dates from the files
whose names are given as the script's command-line arguments.

Uses:
- command-line arguments
- pipes
- wildcards
- `cut`, `sort`, `uniq`
- `#!`

## Step 4: How are concepts connected?

In this stage,
you put the exercises in a logical order
then derive a point-form course outline for the entire course from them.
This is also when you will consolidate the datasets your formative assessments have used.

Checkin: a course outline.

Note:

- The final outline should be at the chapter and lesson level,
  e.g.,
  one major bullet point for each hour of work
  with 4-5 minor bullet points for the episodes in that hour.
- It's common to change assessments in this stage
  so that they can build on each other.
- You are likely to discover things you forgot to list earlier during this stage,
  so don't be surprised if you have to double back a few times.

### Running Example

The chapter and lesson outline for the Unix shell course is:

1. Manipulating Files and Directories
   1. What a shell is; how it compares to a graphical interface.
   2. Basic commands (`whoami`; `pwd`; `ls`).
   3. Moving around (cd; the special paths `.` and `..`).
   4. Creating, deleting, and renaming (`cp`; `mv`; `rm`; `mkdir`; `rmdir`).
2. Manipulating Data
   1. Getting rows (`head`; `tail`).
   2. Getting columns (`cut`)
   3. Repeating steps (`history`; `!number` and `!command`)
   4. Selecting by value (`grep`; quoting arguments to protect special characters)
3. Combining Tools
   1. Redirection with `>`
   2. Piping with `|`
   4. Using the `*` and `?` wildcards
   3. Using `uniq` and `sort` (useful, and further examples of pipelines).
4. Batch Processing
   1. Storing commands in shell scripts.
   2. Permissions; using `!#`.
   3. Using arguments in shell scripts.
   4. Shell variables.
   5. Loops.

## Step 5: Course overview

You can now summarize everything you have created
by writing a high-level course overview that consists of:

- a one-paragraph description (i.e., a sales pitch to students)
- half a dozen learning objectives
- a summary of prerequisites

Doing this earlier often wastes effort,
since material is usually added, cut, or moved around in earlier steps.

Checkin: course description, learning objectives, and prerequisites.

Note: see the appendix for a discussion of how to write good learning objectives.

### Running Example

Here are the final deliverables for the design of the Unix shell course.

**Course Description**

The Unix command line has survived and thrived for almost fifty years
because it lets people to do complex things with just a few keystrokes.
Sometimes called "the duct tape of programming",
it helps users combine existing programs in new ways,
automate repetitive tasks,
and run programs on clusters and clouds
that may be halfway around the world.
This course will introduce its key elements
and show you how to use them efficiently.

**Learning Objectives**

- Explain the similarities and differences between the Unix shell and graphical user interfaces.
- Use core Unix commands to create, rename, and remove files and directories.
- Explain what files and directories are.
- Match files and directories to relative and absolute paths.
- Use core data manipulation commands to filter and sort textual data by position and value.
- Find and interpret help.
- Predict the paths matched by wildcards and specify wildcards to match sets of paths.
- Combine programs using pipes to process large data sets.
- Write shell scripts to re-run command pipes with a varying number of command-line arguments.

**Prerequisites**

None.

## Conclusion

This process is described in sequence,
but in practice you will loop back repeatedly
as each stage informs you of something you overlooked.
When you and your CL agree that your outline is done,
you can copy what you wrote for Steps 3-5 from your course repository's `README.md`
into `course.yml` and your chapters and carry on from there.
When your course is finished,
please take half an hour to update your outline
so that whoever has to maintain your course will understand
what it is trying to achieve and why it is organized the way it is.

[tdd]: https://en.wikipedia.org/wiki/Test-driven_development
