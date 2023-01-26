---
title: "Software Engineering Revisited"
date: 2019-05-30 14:30:00
year: 2019
---

I am at the [International Conference on Software Engineering](https://conf.researchr.org/home/icse-2019)
for the first time in a decade.
It's been good to catch up with friends,
but this fly-by has confirmed several things for me:

1.  I did the right thing leaving academia—I don't have the patience or diligence
    to be a good researcher.

2.  Most software engineering research has the same effect on programmers
    that astronomy has on stars.
    Some of this is because most of the problems that most working programmers face
    are hard for researchers to tackle,
    not considered "interesting",
    or both.
    However,
    some of it is also
    [the gulf between researchers and practitioners]({{'/2012/12/06/two-solitudes-illustrated/' | relative_url}}),
    which hasn't narrowed noticeably since Vancouver in 2009.
    [Our effort to foster dialog](http://neverworkintheory.org/) failed,
    but...

3.  ...I am more convinced than ever that the standard third-year introduction to software engineering
    based on [textbooks](https://www.mheducation.com/highered/product/software-engineering-practitioner-s-approach-pressman-maxim/M9780078022128.html)
    [like these](https://www.pearson.com/us/higher-education/product/Sommerville-Software-Engineering-9th-Edition/9780137035151.html)
    should be replaced by one that teaches undergraduates how to get, clean, analyze, and understand
    software engineering data.

I've made the case for #3 [before]({{'/2014/10/02/a-better-software-engineering-course/' | relative_url}}),
and if anything,
the case is stronger now than it was [then]({{'/2015/11/29/exaptation/' | relative_url}}).
If we call it "Data Science for Software Engineering" the dean will think it's a good idea;
if we tell faculty in other disciplines that we're (finally) requiring some math
in the core software engineering course,
they will nod approvingly,
and if we teach students how to use the scientific method to separate fact from fiction,
a lot of the fads, half-truths, and outright bullshit floating around the murky pond of industry
might finally settle to the bottom.

A course like this would have to include some statistics—say,
up to the level of the [AP Stats exam](https://apcentral.collegeboard.org/courses/ap-statistics/course)
in the US.
It would also include a bit of programming to implement analyses,
but I think that students in the second half of a Computer Science degree
can pick up enough [tidyverse](https://www.tidyverse.org/) or [Pandas](https://pandas.pydata.org/)
in a three-hour lab session to do what they'd need to do.
(They could even write their analyses in [JavaScript](http://www.data-forge-js.com/) if they wanted to.)
The heart of the course,
though,
would be how to translate imprecise questions into runnable statistical models
and how the choices made while doing so affect the answers produced.
By the end of the course,
I would want students to be able to answer questions like these:

-   How many active repositories are there on GitHub?
    -   This can be answered with some API calls or via [GHTorrent](http://ghtorrent.org/),
        but right away we have to decide whether we mean "original repositories"
        or "all repositories including forks",
        and whether we're including repositories that haven't been touched in—hm, how long?
-   How many people contribute to the average project?
    -   It isn't feasible to examine every project,
        and they're constantly changing,
        so we need to talk about sampling and estimation.
-   How long does the average project last?
    -   And is there a correlation between how long a project has been going on
        and how many people have contributed to it?
        To answer that,
        we'll have to talk about what correlation means and how to measure it.
-   Are there differences between projects that use different languages?
    -   What do we mean by "use different languages"?
        Do we rely on self-identification through repository tagging?
        Do we look at the files in the project?
        Do those classifications correlate?
    -   And once we have a way to classify projects,
        what kinds of statistical tests will tell us if two populations are the same or different?
    -   Beyond *what* tests,
        how do we interpet the results correctly,
        especially without making errors about what the results are actually saying?
-   Are long functions or methods buggier than short ones?
    -   It would be surprising if they weren't—what we're probably actually asking is,
        "Are longer pieces of code buggier *per line* (or per statement) than short ones?"
    -   To answer that,
        we need to figure out how to attribute bugs to lines of source,
        and any three researchers will probably do this four different ways.
-   Are some programmers more productive than others?
    -   What do actually we mean by "productivity"?
    -   Do we think that shows up in the digital artefacts we can collect?
    -   How will answers to this question be mis-used?
        (Begel and Zimmermann found that
        [developers believe there's a high risk they would be](https://www.microsoft.com/en-us/research/publication/analyze-this-145-questions-for-data-scientists-in-software-engineering/).

But I want to prepare students to go further.
Peggy Storey's outstanding keynote at ICSE this morning described
three schools of thought in software engineering research:

1.  Formal sciences (philosophical and mathematical foundations)
    use the scientific method,
    focus on evidence-based reality,
    and value the quantitative over the qualitative.
2.  Explanatory sciences (descriptive and predictive theories)
    acknowledge that reality is subjective and experiential,
    expect biases and make them explicit,
    focus on theory generation,
    and value the qualitative over the quantitative.
3.  Design sciences (exemplified by medical treatments and engineering solutions)
    are collaborative and change-oriented,
    and use a mix of methods.
    They are shaped by researchers' political and social lenses;
    to paraphrase Marx,
    their goal isn't to understand the world, but to change it.

The course I've outlined above is firmly in category #1,
but a lot of the work I value most (like [Marian Petre](http://mcs.open.ac.uk/mp8/)'s)
falls into the second category,
and I'm personally in the third.
I don't know if it's possible to give equal weight to all three in a single course;
I suspect that if we try to do so,
the kind of people who regarded Software Carpentry as "merely useful"
will think that we are watering down the course.

It's worth trying, though.
Putting this course together would be a big project,
but no bigger than creating a practical introduction to statistics for psychologists or economists.
It would be fun,
and if anyone needs a little self-interest to spur them on,
I strongly suspect that people who'd gone through this as undergrads
would pay more attention to software engineering research
and be more willing to collaborate with software engineering researchers
once they were in industry.
