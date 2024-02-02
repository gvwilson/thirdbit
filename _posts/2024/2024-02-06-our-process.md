Back in 2022 I wrote that there are two ways of looking at roles in a small-to-medium tech company:
what people do, and [what risks they address][mitigation].
Coincidentally,
I had just started working with someone who has turned out to be
[the best product manager I've ever met][dottie].
In the two years since she joined the company
she has overseen lots of improvements in our software engineering processes
(partly, I suspect, to make it easier for her to do her job properly).
She recently summarized the state of play to orient a new hire;
what follows is a summary of her summary with a few explanatory notes
that I hope will be useful to other software developers
working in research-intensive organizations.

I believe the most important part of what follows
is how she has organized her thinking.
Each process exists *to answer key questions*,
has its own *frequency*,
is *someone's responsibility*,
and generates *specific products*.
If you have a description like this of how your team operates,
please [get in touch](mailto:{{site.author.email}}):
I think we could learn a lot from comparisons.

## Company Goals and Priority Projects

This activity happens up in the stratosphere.
As an engineering manager I may occasionally be called on for input,
but for the most part this is the ground for everything else described below.

-   Summary: Prioritized company objectives and initiatives for the year
-   Key Questions:
    -   What should we invest in/focus on?
-   Frequency: 6-24 months
-   Responsible: executive team 
-   Contributors: company leadership and technical experts at all levels
-   Products:
    -   Monthly business review
    -   Annual all-hands meeting

## Engineering Team

Our team includes about a dozen people
and is responsible for half that number of applications,
ranging from complex C++ libraries wrapped up in Python
to three-tier web applications for managing experimental data
and command-line tools to support routine tasks.
The activities below are done by the whole team.

### Engineering OKRs

The VP of Engineering defines objectives and key results at the start of each quarter
based on discussions with senior management,
the leaders of other teams,
and members of our team.
Goals are prioritized as P0 (not doing this will block something critical to the company),
P1 (we need this, but we can scale it back or it can slip if a P0 overruns),
and P2 (it would be nice to have).

-   Summary: Engineering-specific objectives and projects based on:
    1.  company goals
    2.  users' needs
    3.  technical opportunities
-   Key Questions:
    -   What should each engineering team focus on and why?
-   Frequency: quarterly
-   Responsible: VP Engineering
-   Contributors: entire engineering team
-   Products:
    -   Prioritized list of objectives and key results

> Note: we used to define more of these each quarter than we do now.
> The theory was that if we're meeting all of our targets,
> our targets weren't ambitious enough.
> We now realize that setting ourselves up for continual failure like that isn't actually helpful.

### Engineering OKR Reviews

Improvement in anything requires [reflective practice][reflection].
Our end-of-quarter OKR reviews therefore have two purposes:
to make sure everyone understands where we actually are,
and to summarize what we've learned so that we can do better next time.

-   Summary: End of quarter sync on OKR progress
-   Key Questions:
    -   What is the status of each OKR?
    -   What progress did each team make towards overall goals?
    -   What losses, challenges, and obstacles did we encounter?
    -   What did we learn?
-   Frequency: quarterly
-   Responsible: VP Engineering
-   Contributors: project leads and other team members
-   Products:
    -   Ranked list of things that worked well and things that didn't
    -   Ranked list of ideas for things to try to adopt, improve, or drop

### Engineering Quarterly Retrospective

Similarly,
we have a general retrospective at the end of each quarter
to ask ourselves wider-ranging questions
that may not be specific to a particular project's goals.
Practices like having an on-call user support rotation
have grown out of these self-reviews.

-   Summary: End of quarter team sync to reflect on the quarter and identify ways to improve how we work and our ability to deliver
-   Key Questions:
    -   What went well?
    -   What didn't?
    -   What changes would we like to implement to improve the way we work?
-   Frequency: quarterly
-   Responsible: Scrum master
-   Contributors: entire engineering team
-   Products:
    -   Ranked list of things that worked well and things that didn't
    -   Ranked list of ideas for things to try to adopt, improve, or drop

> Note: our product manager has been doubling as our scrum master for the last couple of years.
> Those jobs are usually done by different people in larger organizations,
> so the description above lists the role rather than the person who happens to be doing it right now.

### Engineering All Hands

Our company includes biologists working in a wet lab,
data scientists,
and machine learning specialists staring into the void and hoping it blinks first.
And while most of us are in Toronto,
a substantial minority live and/or work remotely.
This meeting is where the VP of Engineering updates us all
on things we might otherwise miss
(both organizationally and technically).

-   Summary: Biweekly team sync to discuss company and/or engineering news
-   Key Questions:
    -   What's going on elsewhere in the company that might affect us?
    -   What's coming up that we ought to know about?
-   Frequency: biweekly
-   Responsible: VP Engineering
-   Contributors: entire engineering team plus invited guests
-   Products:
    -   Heightened awareness of recent and upcoming changes

### Engineering Design Reviews

One of the things that has come out of our end-of-quarter reviews
is a greater emphasis on presenting designs for new features or applications to the whole team
before diving into implementation.
The goal here is *not* to create a pile of UML diagrams that no one will ever look at again,
but rather to explain what the problem actually is,
what factors a solution must take into account,
what alternatives there are,
and what we're *not* going to do.
Some designs go through two or three overhauls before work starts;
in almost every case,
checking our thinking like this has saved us pain downstream.

-   Summary: Weekly sync to present and discuss technical proposals
-   Key Questions:
    -   What problem is the design solving?
    -   For who?
    -   How are they solving the problem today?
    -   Why isn't that good enough?
    -   What is out of scope?
-   Frequency: weekly
-   Responsible: VP Engineering
-   Contributors: entire engineering team
-   Products:
    -   Designs for new features or applications
    -   Lateral awareness of who's doing what and why
    -   Buy-in from the team (or at least a chance to air our differences)

> A recent change is to update the design doc a few weeks after work starts
> to explain where and why reality has diverged from the plan.
> Doing this extends the useful life of that document,
> but more importantly,
> it's a chance to reflect on what the code is teaching us
> and share that with other people
> so that our next design(s) can be better.

### Weekly Friday Engineering Demos

One of our more experienced team members instituted Friday afternoon demo sessions last year,
and we have all become believers.
Some demos show off a new feature;
others walk the audience through a bug that has been fixed
or introduce the team to useful third-party tools.
Demos runs anywhere from a few minutes to half an hour,
with most being near the low end of that range.
It's a fun way to wrap up the week and remind ourselves that we're actually making progress.

-   Summary: Weekly sync for team to share ongoing work and discoveries
-   Key Questions:
    -   It does *what*??
-   Frequency: weekly
-   Responsible: volunteer engineer
-   Contributors: entire engineering team
-   Products:
    -   Team spirit
    -   Lateral knowledge transfer

### User Support

As mentioned earlier,
we now take week-long turns monitoring the `#eng-support` channel
and responding to users' problems.
In some cases (e.g., when it's my turn to do support)
the response usually takes the form of,
"OK, let me pull in someone who actually understands what's going on here,"
but whether the on-call engineer handles the problem themself or hands it off,
it gives us all regular reminders of how our software is being used
and what state it is actually in.

-   Summary: Ongoing support of issues and requests
-   Frequency: ongoing
-   Responsible: designated engineer (rotation)
-   Contributors: team members as needed
-   Products:
    -   Happier users
    -   Issues in the issue tracker

> The "issues" product deserves a bit more explanation.
> The on-call engineer creates a new issue in our issue tracker (we use [Linear][linear])
> for *every* incident
> so that there is a single point of reference for the conversation.
> Doing this saves people from having to hunt through GitHub, a wiki,
> and various Slack channels and/or Google docs
> when there's a hand-off
> or the issue occurs again.

### Fixit Sprints

We work in two-weeks sprints,
and for the last year and a half,
we've dedicated one sprint each quarter to paying down technical debt.
If we need to clean up the data access layer in an application
or migrate to a backward-incompatible version of a key library,
we put that work in "our" sprint
so that it won't disrupt work on user-facing changes.
The benefits are hard to quantify but very real,
and making this a regular activity makes the time easier to defend.

-   Summary: 1-2 week dedicated period to address technical debt
-   Frequency: quarterly
-   Responsible: VP Engineering
-   Contributors: entire engineering team
-   Products:
    -   Less technical debt

## Team Activities

Everyone on the engineering team is involved in the activities described above.
In contrast,
the activities below are undertaken by specific people or groups of people.

### Problem Discovery

If you've never had the pleasure of working with a good product manager,
you may not realize how much better your life could be.
This activity and the one that follows are the core of what they do:
question, observe, and listen to users,
figure out what their *actual* needs are,
and translate those needs into things for engineers to fix or build.

-   Summary: Ongoing investigation of users' needs
-   Key Questions:
    -   Who are our primary stakeholders?
    -   What projects and iniatives are they working on?
    -   What would accelerate their work?
    -   Which of these needs is most pressing to solve?
-   Frequency: ongoing
-   Responsible: Product Manager
-   Contributors: technical leads and selected users
-   Products:
    -   Prioritized lists of problems
    -   Prioritized lists of features or fixes that would solve them

### Solution Discovery

This activity is where product management and engineering design overlap.
Its output is the starting point for the design docs mentioned earlier:
in particular,
this is where needs, constraints, and big-picture alternatives are formulated.

-   Summary: Exploration and validation of potential solutions to prioritized problems
-   Key Questions:
    -   Should we build it or buy it?
    -   How could we solve this problem for our users?
    -   Which of these solutions seems most promising and are worth further exploration?
    -   What risks and assumptions are inherent to these solutions?
    -   What is the fastest, cheapest way to validate these solutions?
-   Frequency: ongoing
-   Responsible: Product Manager and technical leads
-   Contributors: users and engineering team members
-   Products:
    -   Designs for new features or applications

### Engineering Needs

Software engineers are people too,
and have their own specialized needs.
Our product manager occasionally treats us as users
and uses discovery techniques to (help us) figure out
what would make *our* lives better.

-   Summary: Ongoing assessment of engineering's needs
-   Key Questions:
    -   What parts of our tools, systems, architecture are slowing us down?
    -   What new technical advancements should we be aware of?
    -   What do we *need* vs. what do we *want*?
-   Frequency: ongoing
-   Responsible: technical leads
-   Contributors: entire engineering team
-   Products:
    -   Designs for new features or applications

### Biweekly Sprint Goals/Backlog Grooming

OK,
we've agreed on what we're going to build—now we actually have to build it.
Every two weeks,
the Scrum master and the project's technical lead
create issues for new work
and (if necessary) relabel old issues
to define what we're going to try to accomplish in this sprint.
Most of the new issues come from the design docs,
or are elaborations or breakdowns of things discussed in those docs;
depending on the size of the work,
we may create several sub-issues under a single high-level issue
so that progress reports aren't "I'm working on it" several days in a row.

-   Summary: Biweekly prioritization to determine team focus for the sprint
-   Key Questions:
    -   What is the next slice of work we want to deliver?
    -   What small improvements should we prioritize?
    -   What key bugs should we prioritize?
    -   What tech debt needs to be addressed?
-   Frequency: biweekly
-   Responsible: Scrum master and technical leads
-   Contributors: engineering team members
-   Products:
    -   Labeled issues

> I've worked on teams where issues had a "percent complete" field
> that the people responsible for it were supposed to update daily.
> It wasn't helpful:
> it's easy to see how much ditch you have left to dig,
> but much harder to know how much code you have left to write and debug.
> Breaking milestones down into inch-pebbles
> and marking the latter as "finished" or "not finished"
> has proven much more useful.

### Daily Standups

We don't actually stand up,
but this is still the most important meeting each team has.
The tech lead of the project does a quick lap around the team to find out
what each person has done,
what they're planning to do,
and what's holding them back.
We try to enforce a three-sentence rule:
if a discussion during individual updates goes on longer than that
we defer it until after everyone has finished their initial report.

The "output" from standups is course corrections.
Should we try another approach to a problem?
Did someone discover an issue that ought to go in the backlog for the next sprint,
or something that's important enough to replace something planned for this sprint?

-   Summary: Daily team sync
-   Key Questions:
    -   What did you work on yesterday?
    -   What are you working on today?
    -   What is blocking you?
-   Frequency: daily
-   Responsible: technical leads
-   Contributors: engineering team members
-   Products:
    -   Updated issues

### Sprint Retros

Just as the whole of engineering does a retrospective each quarter,
each team does a short retrospective at the end of each sprint.
Sometimes the output is "let's try doing something differently"
(for a smaller value of "something" than would be discussed by the whole team in a quarterly retro);
other times,
the output is just,
"Well done!"
because it's as important to celebrate victories as it is to learn from defeats.

-   Summary: Bi-weekly sync to reflect on the past sprint and identify possible improvements
-   Key Questions:
    -   What went well?
    -   What didn't go well?
    -   What should we improve/change/adopt to make things better?
-   Frequency: biweekly
-   Responsible: Scrum master
-   Contributors: engineering team members
-   Products:
    -   Updated issues and processes

### Feature Deployment

We figured out what our users needed,
we designed it,
we built it,
we tested it (more on that below),
we did a few trial deployments:
time to put it into production.
As the list of key questions below shows,
that's never as simple as restarting a server
or pushing a new version of a package to our company's conda repository.
We have to tell people the things they've been asking for are now available,
and we have to check that they actually work in production.

-   Summary: Testing, deployment, documentation, and communication of fixes and features
-   Key Questions:
    -   Is the feature/fix/change working as expected?
    -   Is it well documented both from a technical and user-facing perspective?
    -   Who needs to be aware of this change?
    -   Is any training needed to enable use of this change?
-   Frequency: ongoing
-   Responsible: technical leads
-   Contributors: entire engineering team
-   Products:
    -   (Hopefully) happy users

## Reflection

We didn't adopt all these processes at once.
It's taken two years to put them in place,
and there are a few other things we tried that didn't survive.
*This* is the real heart of any software development process:
the willingness to experiment,
to learn,
and to adapt.
As a previous boss once said to me,
"If you're doing everything by the book, you're doing something wrong."

We're not done,
and I hope we never will be.
Right now,
for example,
everyone is responsible for testing the features they develop.
We do catch some of each other's mistakes in code review,
but we're not testing service interoperability nearly as well as we should.
Fixing that will require more than just setting up some more continuous integration tasks;
we will almost certainly have to extend or amend our processes as well.
We'll keep you posted...

[dottie]: https://www.linkedin.com/in/dottie-omino/
[linear]: https://linear.app/
[mitigation]: {{'/2022/06/06/mitigation/' | relative_url}}
[reflection]: https://www.taylorfrancis.com/books/mono/10.4324/9781315237473/reflective-practitioner-donald-sch%C3%B6n
