---
title: "Software Engineering Research Topics"
date: 2022-08-30
year: 2022
---

I have been collecting random software engineering research ideas from friends and colleagues
for more than a decade.
I know it's a weird hobby,
but I've always thought that
studying the things practitioners are actually curious about
would lead to more fruitful collaboration between academia and industry.
(There's certainly room for improvement:
if you compare highly-ranked questions from
[[Begel and Zimmermann 2014](https://thomas-zimmermann.com/publications/files/begel-icse-2014.pdf)]
or [[Huijgens et al 2020](https://arxiv.org/abs/2010.03165)]
to a list of topics from recent software engineering conferences,
there isn't much overlap.)

So here,
in no particular order,
are the questions I've been asked since I started taking notes ten years ago.
I apologize for not keeping track of who wanted to know,
but if you're working on any of these,
please get in touch and I'll try to track them down.

1.  Does putting documentation in code (e.g., Python's docstrings) actually work better
    than keeping the documentation in separate files,
    and if so,
    by what measure(s)?

1.  Do [doctest](https://docs.python.org/3/library/doctest.html)-style tests
    (i.e., tests embedded directly in the code being tested)
    have any impact long-term usability or maintainability
    compared to putting tests in separate files?

1.  Which tasks do developers collaborate on most often
    and which do they do solo most often?
    (If I'm reading my handwriting correctly,
    the questioner hypothesized that programmers routinely do bug triage in groups,
    but usually write new code alone,
    with other tasks falling in between.)

1.  Are slideshows written using HTML- or Markdown-based tools more text-intensive
    than those written in PowerPoint?
    In particular,
    are slides written in formats that version control understands (text)
    less likely to use diagrams
    than slides written with GUI tools?

1.  A lot of [code metrics](https://neverworkintheory.org/category/#metrics)
    have been developed over the years;
    are there any for measuring/ranking the difficulty of getting software installed and configured?

1.  How does the percentage of effort devoted to tooling and deployment change
    as a project grows and/or ages?
    And how has it changed as we've moved from desktop applications to cloud-based applications?
    (Note: coming back to full-time coding after a decade away,
    my impression is that we've gone from packaging or building an installer taking 10% of effort
    to cloud deployment infrastructure being 25-30% of effort,
    but that's just one data point.)

1.  Has anyone developed a graphical notation for software development processes
    like [this one for game play](https://lostgarden.home.blog/2006/01/16/creating-a-system-of-game-play-notation/)?

1.  How do open source projects actually track and manage requirements or user needs?
    Do they use issues,
    is it done through discussion threads on email or chat,
    do people write wiki pages or [PEPs](https://peps.python.org/),
    etc.?

1.  Has anyone ever done a quantitative survey of programming books aimed at professionals
    (i.e., not textbooks)
    to find out what people in industry care enough to write about
    or think others care about?

1.  Has anyone ever done a quantitative survey of the data structures used in undergraduate textbooks
    for courses that *aren't* about data structures?
    I.e.,
    do we know what data structures students are shown
    in their "other" courses?

1.  Has anyone ever done a quantitative survey of
    how many claims in the top 100 software development books are backed by citations,
    and of those,
    how many are still considered valid?

1.  Are there any metrics for code fitness that take process and team into account?
    (I actually have [the source](https://twitter.com/sarahmei/status/819256231869214721) for this one.)

1.  Which of the techniques catalogued in
    [*The Discussion Book*](https://www.wiley.com/en-us/The+Discussion+Book%3A+50+Great+Ways+to+Get+People+Talking-p-9781119049715)
    are programmers familiar with?
    Which ones do they use informally (i.e., without explicit tool support),
    and how do they operationalize them?

1.  Is there a graphical notation like UML to show the problems you're designing around
    or the special cases you've had to take into account
    rather than the finished solution to the problem
    (other than complete UML diagrams of the solutions you didn't implement)?

1.  Ditto for architectural evolution over time:
    is there an explicit notation for "here's how the system has changed",
    and if so,
    can it show multiple changes in a single diagram
    or is it just stepwise?

1.  The Turing Test classifies a machine as "intelligent"
    if an independent observer can't distinguish between it and a human being in conversation.
    Has anyone ever implemented a similar test for malicious software
    (which we should call the [Hoye Test](https://exple.tive.org/blarg/) in honor of the person who proposed it,
    or the [Moses Test](https://twitter.com/gvwilson/status/1159605481196937216) in "honor" of the person who inspired it):
    1.	Pick an application (e.g., Twitter).
    1.	Build a work-alike that is deliberately malicious in some way
    	(e.g., designed to radicalize its users).
    1.	Have people selected at random use both and then guess which is which.

summarize ACM distinguished dissertation awards
survey developers to find out what the most boring part of their job is
survey speakers' fees at tech conferences by age/subject/gender/geography
list of things ESE has "proven" (ranked) vs. list of things programmers believe (ranked)
are programmers with gardens in the office (https://twitter.com/gvwilson/status/852869480841662464) happier than programmers with foosball tables?
compare time-to-understand with and without UML or other notations
how much do developers know about cognitive psychology and/or social psychology? what mistruths and urban myths do they believe?
trace genealogy of software engineering lesson decks
apply security analysis techniques to peer review models
compare-and-contrast Markdown-ish tools for building documentation and/or tutorials
follow-up to https://programming-journal.org/2017/1/17/
impact of retrospectives: https://twitter.com/pauldambra/status/882959719370964994
adoption of fixes to git interface (e.g. git switch) over time
correlation between README length and usage stats: https://twitter.com/teabass/status/884708605441843200
does it help to have one operator for defining variables and another for updating them?
how and when do people migrate between open source projects?
how often do devs do performance profiling, how do they do it?
how often are ESE findings mentioned in SE courses (not textbooks)? which ones?
score ICSE papers against "Analyze That!"
how do people physically organize lessons when using Markdown-ish compilers?
things like Sajaniemi's roles of variables for refactoring steps or test cases or...
roles of columns (like roles of variables)
follow-up to https://dl.acm.org/doi/10.1145/3230977.3230986
how does team size affect the proportion of time spent planning and its accuracy?
update of new CSS features over time
correlation between quality of error messages and community quality
analyze data from a dozen projects, then try to guess which ones think they're doing agile and which aren't. Compare it to what team members tell you they're doing. See if there's anything more than weak correlation
what is taught about debugging after first year?
Can we assess students' proficiency with tools by watching screencasts of their work? And can we do it efficiently enough to make it a feasible way to grade how they code (as well as the code they write)?
altruism in software teams: how to detect it, what's the effect?
Embedded code chunks in OpenOffice: https://twitter.com/gvwilson/status/1159857430219644929
when people write essay-length explanations like https://beepb00p.xyz/mypy-error-handling.html and https://fly.io/blog/sqlite-internals-wal/, what do they explain and how?
has anyone done a study that plots when people get funded on a loose timeline of "building a startup"? like if 0 is idea and 100 is fully functioning company, where do most black/brown founders get funded vs. other poc founders vs. white founders?
prevalence of pseudoscience (e.g., Myers-Briggs) in tech hiring
analyze videos of coding clubs: are girls treated differently than boys by instructors?
how does the distribution of language constructs actually used in large programs vary by language? e.g., repeat https://twitter.com/Noahpinion/status/1211039070152880128 for programming languages
calculate a Gini coefficient for how effectively scientists use computing, I think you'd find the inequality is steadily increasing: the most proficient are getting better but the vast majority haven't budged in 25 years.
1. Train a Markov text generator on your software's documentation. 2. Generate some fake man pages. 3. Give users a mix of real & fake pages and see if they can tell them apart.
How does the number of (active) Slack channels in an org grow as a function of time or of the number of employees?
how well do the abstracts of SE research papers summarize actual findings?
what do tech support staff informally teach during tech support calls?
I wish there was a simple, standard, widely-supported notation like CSS selectors for selecting parts of a program to display in tutorials. I've used five (six?) tools based on specially-formatted comments with various publishers, and it's getting tired
how does the order in which people write code for production differ from the order in which they explain code in a tutorial and why?
computational notebook with 2-column display (code on the left, commentary on the right): how does that change things?
extract E-R diagrams from Pandas/tidyverse scripts and see if they help
what percentage of time to developers spend debugging and how does that vary by the kind of code they're working on?
balance between rewriting and fixing
are SQL statements written in execution order easier for novices to understand? Less likely to be buggy? Does syntactic congruence with notional machines have measurable impact?
what error recovery techniques are used in what languages and applications how often?
what labels do people use on GitHub and how do they transfer between projects when people move?
what examples do people use when teaching security? is it still Ariadne crashing or do they talk about intimate partner abuse?
how much do engineering managers know about settled results from organizational behavior, social psychology, etc.? and how much pseudoscience do they know?
evolution of the PEP system
create a set of scenarios, each w/ multiple-choice options; have an ethics expert determine the best available answer; then have students & professionals answer the same questions and see where they do/don't agree w/ the expert on ethics.
tudy students from 1st to final year of college/uni and see what tools they start using when. Particularly interested in when/whether they start to use more advanced features of their IDE (e.g., "rename variable in scope").
how whisper networks in tech adapted to COVID lockdown
Repeat "Different languages, similar encoding efficiency" (Coupé et al 2019) for programming languages
