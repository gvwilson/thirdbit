---
title: "Twelve Ways to Be Wrong About AI-Assisted Coding"
date: 2026-05-20
category: programming cs-education
---

Suppose your manager asks you next week to demonstrate that
the AI coding tools your company signed up for
are worth the subscription cost.
Would you measure lines of code generated, or tickets closed?
Or would you send out a survey asking whether developers feel more productive?
Each of those approaches is flawed in a different way;
the sections below explain why.

> Note: this post is about how people are assessing AI,
> not at LLM-assisted coding itself;
> with a little rewording,
> these criticisms could be applied to a lot of the claims that have been made
> about agile development, test-driven development, and other practices.
> If I've learned anything in the last twenty years,
> it's that software engineering would be a lot further ahead today
> if we had been willing to let our peers in the human sciences
> teach us how to study these kinds of things properly.
>
> Also, if you'd like a one-day introduction to the research methods you should use
> to avoid making these errors, please [reach out](mailto:gvwilson@third-bit.com).
> I'm not qualified to teach it, but I know people who are,
> and I could probably talk them into doing it…

## Counting Lines of Code Generated

Proxy metrics stand in for concepts that are hard to measure directly,
and lines of code is one of the oldest.
LLMs generate more code, but not necessarily better outcomes:
a team that sees a 40% increase in lines of code per developer
after adopting LLM tools has measured verbosity, not productivity.
Deleting 2000 lines of tangled logic and replacing it with 200 clean ones
is an improvement that looks like a loss on this metric [Sadowski2019].
More code also means more to read, maintain, and debug,
and AI's contribution to that future burden does not appear in the line count.

## Timing Artificial Tasks

A widely cited study found that
developers who used GitHub Copilot completed a task 55% faster than those who did not [Peng2023].
The task was implementing an HTTP server in JavaScript from scratch, in ninety minutes;
the developers had no other obligations that day.
Real software development involves navigating a large codebase you did not write,
understanding a requirement described ambiguously in a ticket,
coordinating with colleagues,
and attending meetings.
Speed on a greenfield toy task does not predict speed on any of that.
A randomized controlled trial with experienced open-source developers
found the opposite of what participants themselves predicted:
giving them access to AI tools increased task completion time by 19% [Becker2025].

## Before/After With No Control Group

You start using LLMs in January;
by June, pull requests are shipping faster, so the tools must be working, right?
But between January and June you hired twelve engineers,
refactored the CI pipeline,
and switched your cloud provider.
Without a group that did not adopt the tools,
you cannot separate the effect of LLMs
from any of the other changes that happened at the same time.
Internal validity requires a credible counterfactual,
i.e., some way of knowing what would have happened otherwise.

## Asking Developers If They Feel More Productive

Survey results like
"87% of developers report feeling more productive with AI tools"
are regularly cited as evidence that the tools work [Liang2024],
but three things make self-report systematically misleading:

-   The Hawthorne effect means people work differently
    when they know they are being observed and evaluated;

-   The novelty effect means new tools feel faster because they are novel,
    and that feeling typically fades within weeks; and

-   Social desirability bias means respondents tend to say
    what they believe the survey wants to hear,
    especially when management chose the tool.

## Counting Commits, Pull Requests, and Tickets

In 2023,
McKinsey proposed measuring individual developer productivity
using counts of commits, pull requests, code reviews, and similar activities [McKinsey2023].
Goodhart's Law states that when a measure becomes a target,
it ceases to be a good measure [Goodhart1984].
When developers know their commit count is tracked, they make more, smaller commits;
when ticket counts are tracked, tickets get split.
The numbers improve while the underlying work does not [Beck2023].
Activity is not output; output is not value.

## Measuring Only the Easy Half

LLMs make code generation faster, and that half is easy to measure.
The other half is harder:
time spent reviewing LLM-generated code for correctness,
time lost debugging confidently wrong suggestions,
security vulnerabilities introduced by plausible-looking but insecure code,
and technical debt from suggestions that solved the immediate problem
while ignoring the surrounding design.
A study of GitHub Copilot's code found
that a substantial fraction of generated code contained security vulnerabilities,
and that developers under time pressure accepted insecure suggestions at higher rates [Pearce2022].
A 2025 evaluation of five major LLMs found that
none produced web application code meeting industry security standards [Dora2025].
A large-scale analysis of over 300,000 AI-authored commits found that
more than 15% introduce at least one quality issue,
and nearly a quarter of those issues persist in the codebase long-term [Liu2026].
Measuring only the inputs that go up while ignoring the costs that also rise is not measurement;
it is marketing.

## Treating Adoption Rate as a Success Metric

"We have achieved 90% AI tool adoption across engineering"
is a procurement outcome,
not a productivity outcome.
Adoption measures whether the tool is installed and opened;
it says nothing about whether suggestions are useful,
whether developers accept them thoughtlessly,
or whether the accepted suggestions are correct.
High adoption combined with low suggestion quality
produces a workforce spending time managing a tool rather than benefiting from one.
A study of IBM's enterprise AI coding assistant found that
while the tool often provided net productivity increases,
those gains were not experienced uniformly across its user base [Weisz2025].
But adoption is easier to measure than benefit,
which is exactly why it gets reported instead.

## Comparing Volunteers to Non-Volunteers

Studies that compare developers who chose to use LLMs against those who did not
are comparing two different populations,
not two conditions.
Early adopters differ from late adopters and non-adopters
in ways that directly predict productivity:
they are more motivated to experiment,
more comfortable with new tooling,
and more likely to already be high performers.
Selection bias means any observed difference between the groups
may be a property of the person rather than the tool.
This is the most common design flaw in industry AI productivity reports,
because it is the cheapest study to run.
A two-year longitudinal study of Copilot use at a large IT organization found that
developers who used the tool were consistently more active than non-users
even before it was introduced [Stray2026].

## Measuring the Individual Instead of the System

Individual coding speed is the easiest thing to measure, so it gets measured.
But if AI tools help developers write code 30% faster
and the team's time from ticket to production does not change,
the bottleneck was not writing code.
More code generated also means more code to review:
if AI increases code volume without increasing review capacity,
cycle time may worsen [Forsgren2021].
An empirical study of professional developers found that while AI tools boosted output for
less-experienced contributors, senior developers experienced a 19% decline in their own
productivity as they absorbed a 6.5% increase in code review load from AI-generated code [Xu2025].
Optimizing one stage of a pipeline while ignoring the others is a systems-thinking failure
dressed as a productivity study.

## Measuring During the Novelty Period

A four-week study that finds a productivity boost has found a four-week productivity boost.
The novelty effect is real:
developers are more engaged with new tools during the initial period,
which inflates observed performance relative to the long-run baseline.
Effects that actually matter emerge over months, not weeks,
including skill atrophy for tasks now delegated to the AI,
accumulation of technical debt from wrong suggestions,
or changes in how teams collaborate.
A study designed to detect a short-term benefit,
has not told you anything about what happens after the study ends.
An analysis of 807 open-source repositories adopting Cursor found exactly this pattern:
adoption produced a large but transient increase in development velocity alongside
a substantial and persistent increase in code complexity and static analysis warnings [He2026].

## Treating Suggestion Acceptance Rate as a Quality Signal

LLM coding assistants commonly report what fraction of their suggestions developers accept,
and higher acceptance rates are presented as evidence that the tool is useful.
Acceptance measures whether the generated code looked plausible enough
for a developer to press Tab;
it does not measure whether the code was correct, secure, or maintainable.
Developers under time pressure accept more suggestions, including insecure ones [Pearce2022],
so a tight deadline makes acceptance rate rise for exactly the wrong reasons.
An enterprise study of 400 developers found a 33% average acceptance rate
alongside high developer satisfaction,
but tracked no measure of the correctness or security of accepted code [Bakal2025].
A metric that rewards looking good enough is not a metric that rewards being good.

## Comparing AI to Nothing

Studies that compare AI-assisted developers to a control group using nothing
have chosen a baseline that does not exist in practice.
Developers without LLM assistants use documentation, colleagues,
and the time they would otherwise spend thinking through the problem themselves.
The relevant question is whether LLM tools outperform the alternatives developers already have,
and that comparison is rarely made [Peng2023].
Choosing a weak baseline makes any tool look good; it does not make the tool useful.

> I am profoundly grateful to everyone who has taken the time over the years
> to explain this stuff to me.
> Any errors or over-simplifications in what I've written are entirely my fault.

## Bibliography

Bakal2025
:   Gal Bakal, Ali Dasdan, Yaniv Katz, Michael Kaufman, and Guy Levin:
    "Experience with GitHub Copilot for Developer Productivity at Zoominfo."
    arXiv:2501.13282,
    2025.

Becker2025
:   Joel Becker, Nate Rush, Elizabeth Barnes, and David Rein:
    "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity."
    arXiv:2507.09089,
    2025.

Beck2023
:   Kent Beck:
    "Measuring Developer Productivity: Real-World Examples."
    Medium,
    2023.
    <https://tidyfirst.substack.com/p/measuring-developer-productivity>

Dora2025
:   Swaroop Dora, Deven Lunkad, Naziya Aslam, S. Venkatesan, and Sandeep Kumar Shukla:
    "The Hidden Risks of LLM-Generated Web Application Code:
    A Security-Centric Evaluation of Code Generation Capabilities in Large Language Models."
    arXiv:2504.20612,
    2025.

Flournoy2025
:   John C. Flournoy, Carol S. Lee, Maggie Wu, and Catherine M. Hicks:
    "No Silver Bullets: Why Understanding Software Cycle Time is Messy, Not Magic."
    arXiv:2503.05040,
    2025.

Forsgren2021
:   Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, Thomas Zimmermann, Brian Houck, and Jenna Butler:
    "The SPACE of Developer Productivity."
    *ACM Queue*,
    19(1), 2021.

Goodhart1984
:   Charles Goodhart:
    "Problems of Monetary Management: The U.K. Experience."
    In Anthony Courakis (ed.),
    *Inflation, Depression, and Economic Policy in the West*,
    Rowman and Littlefield,
    1984.

He2026
:   Hao He, Courtney Miller, Shyam Agarwal, Christian Kästner, and Bogdan Vasilescu:
    "Speed at the Cost of Quality: How Cursor AI Increases Short-Term Velocity and Long-Term Complexity in Open-Source Projects."
    *Proc. MSR '26*,
    2026.

Hicks2025
:   Catherine M. Hicks, Carol Lee, and Kristen Foster-Marks:
    "The New Developer: AI Skill Threat, Identity Change & Developer Thriving in the Transition to AI-Assisted Software Development."
    <https://osf.io/preprints/psyarxiv/2gej5_v2>,
    2025,
    https://doi.org/10.31234/osf.io/2gej5_v2.

Liang2024
:   Jenny T. Liang, Chenyang Yang, and Brad A. Myers:
    "A Large-Scale Survey on the Usability of AI Programming Assistants: Successes and Challenges."
    *Proc. ICSE 2024*,
    2024.

Liu2026
:   Yue Liu, Ratnadira Widyasari, Yanjie Zhao, Ivana Clairine Irsan, Junkai Chen,
    and David Lo:
    "Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated Code in the Wild."
    arXiv:2603.28592,
    2026.

McKinsey2023
:   Nora Elsayed, Tarek Elhounsri, and Sven Blumberg:
    "Yes, You Can Measure Software Developer Productivity."
    McKinsey & Company,
    2023.
    <https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/yes-you-can-measure-software-developer-productivity>

Pearce2022
:   Hammond Pearce, Baleegh Ahmad, Benjamin Tan, Brendan Dolan-Gavitt, and Ramesh Karri:
    "Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions."
    *Proc. IEEE S&P 2022*,
    2022,
    doi:10.1109/SP46214.2022.9833571.

Peng2023
:   Sida Peng, Eirini Kalliamvakou, Peter Cihon, and Mert Demirer:
    "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot."
    arXiv:2302.06590,
    2023.

Sadowski2019
:   Caitlin Sadowski and Thomas Zimmermann (eds.):
    *Rethinking Productivity in Software Engineering*.
    Apress,
    2019,
    978-1484242209.

Stray2026
:   Viktoria Stray, Elias Goldmann Brandtzæg, Viggo Tellefsen Wivestad, Astri Barbala, and Nils Brede Moe:
    "Developer Productivity With and Without GitHub Copilot: A Longitudinal Mixed-Methods Case Study."
    *Proc. HICSS-59*,
    2026.

Weisz2025
:   Justin D. Weisz, Shraddha Kumar, Michael Muller, Karen-Ellen Browne, Arielle Goldberg, Ellice Heintze, and Shagun Bajpai:
    "Examining the Use and Impact of an AI Code Assistant on Developer Productivity and Experience in the Enterprise."
    *Proc. CHI'25*,
    2025.

Xu2025
:   Feiyang Xu, Poonacha K. Medappa, Murat M. Tunc, Martijn Vroegindeweij, and Jan C. Fransoo:
    "AI-Assisted Programming Decreases the Productivity of Experienced Developers
    by Increasing the Technical Debt and Maintenance Burden."
    arXiv:2510.10165,
    2025.
