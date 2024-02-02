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
-   Responsible: Scrum Master
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

-   Summary: Exploration and validation of potential solutions to address prioritized problems
-   Key Questions:
    -   Should we build it or buy it?
    -   How could we solve this problem for our users?
    -   Which of these solutions seems most promising and are worth further exploration?
    -   What risks and assumptions are inherent to these solutions?
    -   What is the fastest, cheapest way to validate these solutions?
-   Frequency: ongoing
-   Responsible: Product Manager and technical leads
-   Contributors: users and engineering team members

### Engineering Needs

-   Summary: Ongoing assessment of engineering's needs
-   Key Questions:
    -   What parts of our tools, systems, architecture are slowing us down?
    -   What new technical advancements should we be aware of?
    -   What do we *need* vs. what do we *want*?
-   Frequency: ongoing
-   Responsible: technical leads
-   Contributors: entire engineering team

## Delivery

### Project Planning

-   Summary: Documentation and organization of prioritized projects
-   Key Questions:
    -   What problem is this project focused on solving for whom?
    -   What will be the impact of solving this problem?
    -   What are the goals or desired outcomes of this project?
    -   How will we measure success?
    -   What is in scope and out of scope?
    -   What are our milestones, timelines, and expected deliverables?
    -   What are the smallest slices of value we can deliver to our customers?
-   Frequency: project dependent
-   Responsible: Product Manager and technical leads
-   Contributors: engineering team members

### Technical Design

-   Summary: Deep dive into the technical design/architecture of a given solution
-   Key Questions:
    -   What problem is the design solving for whom?
    -   How are they solving the problem today?
    -   What pain points with the existing solution led to the need for a better one?
    -   What is out of scope?
    -   What is the prototype of the technical solution?
-   Frequency: project dependent
-   Responsible: technical leads
-   Contributors: engineering team members

### Biweekly Sprint Goals/Backlog Grooming

-   Summary: Biweekly prioritization to determine team focus for the sprint
-   Key Questions:
    -   What is the next slice of work we want to deliver?
    -   What small improvements should we prioritize?
    -   What key bugs should we prioritize?
    -   What tech debt needs to be addressed?
-   Frequency: biweekly
-   Responsible: Product Manager and technical leads
-  Contributors: engineering team members

### Daily Standups

-   Summary: Daily team sync to discuss progress and identify blockers as relates to the sprint goals
-   Key Questions:
    -   What did you work on yesterday?
    -   What are you working on today?
    -   What is blocking you?
    -   Any key questions, decisions, or concerns to raise with the team?
-   Frequency: daily
-   Responsible: technical leads
-   Contributors: engineering team members

### Sprint Retros

-   Summary: Bi-weekly sync to reflect on the past sprint and identify possible improvements
-   Key Questions:
    -   What went well?
    -   What didn't go well?
    -   What should we improve/change/adopt to make things better?
-   Frequency: biweekly
-   Responsible: Scrum master
-   Contributors: engineering team members

### Feature/Slice Deployment

-   Summary: Testing, deployment, documentation, and communication of fixes and features
-   Key Questions:
    -   Is the feature/fix/change working as expected?
    -   Is it well documented both from a technical and user-facing perspective?
    -   Who needs to be aware of this change once pushed to production?
    -   Is there any training needed to enable use of this change?
-   Frequency: ongoing
-   Responsible: technical leads
-   Contributors: entire engineering team

### Customer Feedback and Metrics

-   Summary: Measuring and assessing impact and identifying gaps or areas for improvement
-   Frequency: ongoing
-   Responsible: VP Engineering and Product Manager
-   Contributors: entire engineering team

[dottie]: https://www.linkedin.com/in/dottie-omino/
[linear]: https://linear.app/
[mitigation]: {{'/2022/06/06/mitigation/' | relative_url}}
[reflection]: https://www.taylorfrancis.com/books/mono/10.4324/9781315237473/reflective-practitioner-donald-sch%C3%B6n
