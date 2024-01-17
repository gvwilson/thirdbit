---
title: "The First Six Questions"
date: 2024-01-17
year: 2024
---

I've been talking and writing for several years
about teaching programmers the basics of economics, politics, sociology, and related fields
so that they could understand the world they're living in and reshaping.
A few days ago I framed it as [the Scratch of social sciences][like-scratch];
some people interpreted that as, "What software would you use to teach these ideas?"
but when I ask for the "X" in "X is to the social sciences as Scratch is to computer science",
what I want is something that is accessible to people with little or no background knowledge,
immediately useful[^useful],
and serves as a ramp[^ramp] to more advanced ideas[^reflection].

One possibility is something like the [Carpentries][carpentries] workshops,
which typically spend half a day on the Unix shell,
half a day on version control,
and a full day on either Python or R.
Each topic is presented in episodes of 15–30 minutes;
crucially,
there is a practical exercise at the end of each
to build learners' confidence and enable them to check their understanding.

Could that format be used to teach a few key ideas from of the social sciences?
Since I want to teach programmers[^audience],
one approach would be to use problems that come up when working in software development teams
to motivate the episodes.
For example,
rather than presenting some rules for [running meetings][meetings],
a lesson could start by asking,
"Why do have so many meetings?"
or,
"Why do so many meetings feel like a waste of time?"
and then discuss why large social structures tend to become hierarchical
and the way that who's allowed to interrupt whom is tied to perceived social status.

Eight hours minus setup, coffee breaks, lunch, and wrap-up
gives us six useful hours in a day of teaching and learning.
At 45 minutes per episode (including an exercise[^exercise]),
that gives us eight episodes per day
or sixteen episodes in total.
What should the motivating questions for each episode be?
They don't have to lead to the most important topics in each field[^fundamental],
and as footnoted earlier,
they don't have translate immediately into "how to write better OKRs with science!".
What they *do* have to be is engaging:
the prototypical audience member is busy,
a little bit skeptical,
and utterly uninterested in anything that feels pious, faddish, or condescending[^frank].

I've listed six possible questions below,
and hope to set up an hour-long call later this month
for anyone who's interested in expanding on them,
replacing them with better ones,
or suggesting another approach entirely.
If you'd like to take part,
please [email me](mailto:{{site.author.email}}) and I'll send you an invitation.

Why do we have so many meetings?
:   Coordination costs rise as the square of the number of people,
    so large groups must (a)
    make work uniform
    so that sets of people are effectively interchangeable (e.g., assembly lines and typing pools),
    (b) create sub-groups and invest effort in coordinating their work,
    or (c) allow sub-groups to work independently and pay the cost of duplicated or contradictory effort.

Why do so many meetings suck?
:   Most people don't seek to maximize profit, but to maximize social standing within their peer group.
    Some people do this by being helpful, but others try to do it by establishing social dominance.
    Their meetings turn into one-up displays,
    which often take the form of interrupting people they perceive as having lower social status.
    Social norms (such as meeting moderation rules) exist in part to constrain such behavior.

How should software developers be assessed?
:   Exams and performance reviews are facts of life in academia and industry.
    They exist for good reasons—some people truly are more skilled or more productive than others—but
    every quantitative metric for comparing people will inevitably be gamed,
    while every qualitative metric is subject to various biases.
    One response is to allow people to define their own evaluation criteria,
    but that makes it difficult or impossible to compare people,
    and bad actors will always abuse this power.

Who owns the software I write?
:   Depending on your circumstances,
    the software you write may belong to your employer
    even if you wrote it on your own time using your own computer
    (because they provided the training you needed to write it),
    or they may only have an interest in it if you used their physical resources,
    or it may be entirely yours as long as you wrote it on your own time.
    The answer depends on local rules about intellectual property;
    that concept is less than two hundred years old,
    but has expanded steadily over the last century
    via processes such as regulatory capture
    in ways that further the interests of profit-driven corporations.

Why don't programmers need licenses?
:   Depending on locale (mine is Ontario),
    this question could be presented as something like,
    "Even hairdressers need licenses; why don't programmers?"
    The lesson can then point out
    how the question implicitly uses the social status of the two professions:
    "Isn't it ridiculous that *lowly* hairdressers have to get licenses
    but *exalted* programmers don't?"
    The answer is that licensure is tied to professional responsibility,
    which leads to discussion of the fact that
    middle-class professions such as law and medicine are (mostly) allowed to be self-regulating
    while working-class professions like hairdressing mostly have regulations imposed on them.

People of Asian ancestry make up 4–5% of the Canadian population but 50–75% of computer science classes. Does this prove Asians are intrinsically better at programming than everyone else?
:   The corollary is,
    "If you don't believe they are,
    why would you believe arguments about men being better programmers than women?"
    That introduces discussion of how supposedly-objective "science" is often used to prove
    whatever the powerful want proven.

Footnotes:

[^useful]: "Useful" doesn't necessarily mean something like "translates into five tips for running more effective meetings". Instead, this new knowledge should (for example) help people understand why so many people repeatedly vote against their own interests, or why the argument that racism can't exist in a truly free-market society because it's economically inefficient is bullshit.

[^ramp]: Many lessons that are ostensibly aimed at newcomers require them to climb an intellectual cliff. It turns out most people will get to the top faster and more reliably if they're offered a ramp instead.

[^reflection]: One early reviewer wrote that the Scratch of the social sciences is, "…actually critically reflecting on our lives through a scientific approach." I accept that, but I think people have to be taught how to reflect, in the same way that they have to be taught how to analyze character development in a novel.

[^audience]: Ideally, I'd like to reach both professional software engineers with computer science backgrounds *and* research software engineers, data scientists, and others who are mostly self-taught but now find themselves writing large, complex pieces of code.

[^exercise]: Coming up with meaningful, engaging exercises is probably going to be a lot harder than coming up with things to teach.

[^fundamental]: For example, two minutes after I start teaching people how to use the Unix shell, I show them the `history` command and explain how to repeat commands they've recently run. It isn't the most important thing in the shell, but it's something they probably can't do easily with the GUI tools they've used before, and they immediately understand its value. Finding hooks like these is key to learner engagement.

[^frank]: One thing I *don't* want to do is preach to believers, e.g., tell people who already think diversity is important that some people are systematically excluded from power. I often think about Frank, a 25-year-old straight cis white male from a middle-class family who thinks Jordan Peterson is a pompous dick but not necessarily wrong, that Trump voters are idiots but Dave Chappelle is funny, and that the company he's working for shouldn't make "diversity hires".

[carpentries]: https://carpentries.org/
[like-scratch]: {{'/2024/01/13/whats-the-scratch-of-the-social-sciences/' | relative_url}}
[meetings]: https://docs.google.com/presentation/d/1HSdgVQjq0d3UYh-aA4uWHXxYYpySn_xXwfn_M4Ms8Ts/
