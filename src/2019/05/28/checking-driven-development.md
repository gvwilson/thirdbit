---
date: 2019-05-28
title: "Checking-Driven Development"
---

I spent some time talking to a colleague this week about software testing and data science,
and I think I'm a little less confused about a few things than I used to be:

1.  I know how to test "normal" software (like e-commerce websites or database drivers):
    set up some input values, run the code, and then check that it produces the expected result.

2.  This methodology is irrelevant to many data scientists because they don't know what result to expect—if they did,
    they would already have published and moved on.

3.  I say "many" rather than "all"
    because some data scientists—those who work as [research software engineers](https://researchsoftware.org/)—write
    libraries for general use and should have lots of tests.
    I think the difference is building products for repeated use
    versus combining those products and their own code to get one specific result.

4.  So how do scientists figure out if their software is doing the right thing?
    The answer is spot checks:
    each time they produce an intermediate or final result,
    they scan a table, create a chart, or inspect some summary statistics
    to see if everything looks OK.
    Their heuristics are usually easy to state,
    like "there shouldn't be NAs at this point" or "the age range should be reasonable",
    but applying those heuristics to a particular analysis always depends on
    the data scientist's evolving insight into the data in question.

I therefore agree that
there are more important things to teach to novice data scientists than unit testing.
(I can already hear my software engineering friends muttering, "Unclean! Unclean!")
What I think we *should* teach is defensive programming:
the checks that data scientists do while they're doing analyses
should be recorded in their code as assertions.
This will help reusability—it's amazing how often a one-off analysis
winds up being used many times—but the real goal is comprehensibility.
If I can get your code and data,
run the former on the latter,
and get the same result that you did,
then your computation is reproducible,
but that doesn't mean I can understand it.
Prose explanations help,
which is part of why knuths<sup><a href="#footnote-knuth">1</a></sup> are so popular,
but comments and paragraphs won't check that assumptions and invariants still hold
when the person trying to reproduce the analysis starts fiddling around with it.
And unlike comments,
runnable assertions can't fall out of step with what the code is actually doing…

By analogy with [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development),
we could call this process "checking-driven development".
Just like writing tests forces you to be explicit about what "done" looks like,
adding checks to analyses forces you to be explicit about what "right" looks like.
I believe this approach is pedagogically defensible:

1.  Knowing how to write useful assertions
    is necessary (but not sufficient) for writing unit tests.
2.  It's the-same-as-but-better-than what good practitioners currently do.

## An Example

Several good libraries for validating data pipelines in R already exist,
including [assertr](https://cran.r-project.org/web/packages/assertr/index.html),
[checkr](https://cran.r-project.org/web/packages/checkr/index.html),
and [validate](https://cran.r-project.org/web/packages/validate/index.html).
What we're missing are:

1.  Lessons to teach budding data scientists what tests they should actually write.
    I strongly suspect that these will have to be (sub)domain-specific;
    as the joke goes,
    physicists worry about decimal places,
    astronomers worry about exponents,
    and economists are happy if they get the sign right.
2.  Hooks to help people recycle their tests in production.
    One-off scripts have a nasty habit of finding their way into pipelines;
    [Taschuk's Rules](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005412)
    tell people how to prepare for that,
    but libraries with hooks so that data engineers can turn them on and off
    and control where their output goes
    *without* editing the source can help a lot.

So what might this look like in practice?
Imagine we have this simple dplyr pipeline
to find the mean age of people who aren't "alpha":

```
data <- tribble(
  ~record_id, ~person_id, ~age,
  100,         "alpha",    17,
  200,         "alpha",    34,
  300,         "beta",     21,
  400,         "gamma",    NA,
  500,         "gamma",    26
)

data %>%
  filter(person_id != "alpha") %>%
  group_by(person_id) %>%
  summarize(midpoint = mean(age))
```

Now imagine a trio of functions `grumble_row`, `grumble_col`, and `grumble_group`
that check conditions on rows, columns, and groups without modifying the data.
The data scientist delivers this:

```
config <- list(MAX_AGE = 120, IN_PRODUCTION = FALSE, LOGGER = warning)

data %>%

  grumble_col(age >= 18) %>%
  grumble_col(age <= config$MAX_AGE, active = !config$IN_PRODUCTION) %>%

  filter(person_id != "alpha") %>%

  grumble_row(is.na(age), logger = config$LOGGER) %>%

  group_by(person_id) %>%

  grumble_group(n() == 2, msg = "Expected two records per person.") %>%

  summarize(midpoint = mean(age))
```

The data engineer pulls those configuration settings out into a YAML file,
then changes `IN_PRODUCTION` to `TRUE`
and replaces `warning` with a function from `futile.logger` or a similar package.
Here's the fully-annotated version to explain the purposes of the checks
and the extra parameters that these functions understand:

```
data %>%

  # Always check that age is greater than or equal to 18.
  # (Would raise error in this example because of record 100.)
  grumble_col(age >= 18) %>%

  # Only check that age lies below maximum when not in production.
  # (Would not raise an error in this example because 'active' would be FALSE.)
  grumble_col(age <= config$MAX_AGE, active = !config$IN_PRODUCTION) %>%

  # Real calculation.
  filter(person_id != "alpha") %>%

  # Generate a warning if there are any surviving NAs in age.
  # (Would generate a warning in this example because of record 400.)
  grumble_row(is.na(age), logger = config$LOGGER) %>%

  # Real calculation.
  group_by(person_id) %>%

  # Check that there are exactly two records for each person.
  # (Would raise an error in this example because there is only one record for "beta".)
  grumble_group(n() == 2, msg = "Expected two records per person.") %>%

  # Real calculation.
  summarize(midpoint = mean(age))
```

## Feedback Please

I think it's reasonable to teach novice data scientists to do ad hoc checking.
I think it's equally reasonable to ask data scientists of all kinds
to move their ad hoc checks from the interactive console into their scripts.
I'd be grateful for your opinions,
and for your thoughts on the checking functions I've proposed above.

<span id="footnote-knuth">1.</span> More commonly called "computational notebooks",
but I figure we should give credit where credit is due.
