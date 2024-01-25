---
date: 2024-01-24
year: 2024
title: "Working Backwards"
---

Here's the last exercise in an introductory programming course for biologists:

> This zip file contains 236 CSV files,
> each of which has readings from a 16x16 microplate.
> Some of the plates were calibration runs with no samples in them;
> other plates had samples placed in random locations in a handful of wells.
> We know that the samples have much higher readings on average than the untreated wells,
> but unfortunately we've lost the records that would tell us which plates were calibration and which we treated.
> Write a Python script that:
> 
> 1.   reads the CSV files;
> 2.   calculates the average reading for each plate; and
> 3.   classifies the plates into untreated or treated based on the average.
>
> Include some tests to convince the examiner that your solution is correct.

Let's work backward to define the course's curriculum:

-   Read CSV files
    -   So either `sys.argv` and enough shell to write `python script.py *.csv`
        or introduce the `glob` module
    -   Either way, they're going to have to loop over filenames…
    -   …and read each file into a dataframe
-   Calculate the average reading for each plate
    -   They'll have to combine the dataframes they just read into one big dataframe…
    -   …after pivoting the data to have the four columns (filename, row, col, reading)…
    -   …and then perform a grouped aggregation to calculate the average for each
-   Classify the plates
    -   Either classical statistics (identify the two means of a bimodal distribution)…
    -   …or fancier modern stuff (1-dimensional k-nearest neighbors for k=2)…
-   Testing
    -   Check the values in each dataframe to make sure they didn't mis-read
    -   Generate a bit of synthetic data to test their classifier

The initial four goals have turned into ten or twelve,
depending on how you count.
We can now come up with a short exercise for each of those
and work backward to discover their prerequisites,
and continue until we get to printing "Hello, world."

The technique has several names,
but I first learned it as "reverse instructional design",
and it brings me to something Cat Hicks posted on Mastodon earlier today:

> This morning's chats have got me thinking about
> an initiative at the Developer Success Lab we've been talking about
> that we're calling Be Your Own Scientist—publishing guidance and teaching
> all about helping *you* bring the power of science
> to answer questions about software teams
> (and perhaps using it to protect the good stuff you already know you're doing!)
>
> What kinds of topics would you want our team of social scientists to tackle?

I answered:

> 1.  How are various kinds of decisions actually made in software engineering organizations?
> 2.  Why are some specialties seen as higher-status than others, and (how) has that changed over time?
> 3.  How do developers acquire their understanding of users' needs, and what gets lost or garbled in translation?
> 4.  How do programmers explain things to (a) peers (b) new team members (c) management and (d) users?
>     How and why do these differ?

Cat responded:

> [Those] sound like research questions rather than teaching people how to answer their own questions?
> Good research questions but not quite the same as scientific thinking as a practice.

to which I tooted:

> agreed—what science thinking / techniques would you teach me
> so that I could tackle these (or at least understand others' answers)?
> I think I don't even know what to ask for…

Thinking about it some more,
I've realized that I work backward more often than I'd recognized.
I don't know what I need to know,
but I *do* know what questions I want to (be able to) answer.
Whether it's a lesson on Python,
training on scientific thinking,
or what book to write next,
I often jump ahead to the conclusion I want
and then backtrack to figure out how to get there.
It's not profound or original,
but it works for me.
