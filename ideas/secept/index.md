---
title: "Software Engineering: Compassion, Evidence, Process, and Tools"
layout: page
---

Are some programming languages easier for novices to pick up than others?
Does test-driven development produce higher-quality code in less time?
Is there any truth behind the "10X programmer" meme?
And if a team has limited resources for testing, what should they focus on?
Empirical research has answers to all of these questions and more,
but most programmers don't know that research exists.
As a result,
many continue to use inefficient or insecure practices when better alternatives exist.

I would like teach programmers (both students and practitioners)
what we actually know about software engineering and why we believe it's true.
I believe the best way to do this is to teach them some basic data science,
then have them use their new knowledge and skills
to understand analyses of what makes software engineers more effective.
This show-don't-tell approach would ensure that they know what we already know,
that what they learn sticks,
and that they have the tools they need to analyze and improve their own work.

But that's not enough.
Many of the hard problems in software engineering stem from the fact that
we have to design programs to fit our limited mental capacity.
Many others are rooted in the social psychology of group interactions,
or in our tendency to believe what people around us believe
rather than examining evidence.
This book would therefore be guided by a modified version of [Dobzhansky's Rule][dobzhansky]:

> Nothing in software engineering makes sense except in the light of psychology.

Our aim is to teach you how to be a *compassionate programmer*:
one who cares about the well-being of their colleagues and users.
This focus is not entirely altruistic—everything you do to help others
also helps your future self—but now that we know how much harm software can do,
we need to learn to build it in better ways.

### FAQ

How long will this take?
:   I believe a minimum viable set of lessons can be ready to test in six months, and the first release can be ready six months after that.

What do you need?
:   Funding for one person for 12 months to build, try out, and proselytize the lessons; funding for a graduate-level researcher for 6 months to study the use and impact of these lessons would help a lot too.

What are your qualifications for doing this?
:   [Software Carpentry][carpentries], a non-profit I founded in 2010 to teach programming skills to researchers, has delivered several thousand workshops worldwide to over 80,000 people; the books I organized and edited on [software architecture][aosa] and [empirical software engineering research][making-software] have been read by tens of thousands of people; I received the ACM SIGSOFT Influential Educator of the Year Award in 2020; and I have extensive contacts in both academia and industry.

Why can't you do this on your own time?
:   I tried: it was going to be next after *[Teaching Tech Together][t3]* and *[Software Design by Example in JavaScript][sdxjs]*. What I found while prototyping is that the material requires so much more unbroken concentration that I don't think I will complete it as an evening-and-weekend project.

Why are you teaching data science rather than just summarizing published results?
:   The average computer science student does a lot less data analysis in college than the average biologist or economist, so most programmers don't have the background needed to understand what's actually being claimed or the evidence for it. If we're going to reach the majority we need to give them a foundation; presenting this as "let's teach you the Python you need to wrangle data" seems most likely to hook them.

Why are you teaching data science when there are so many good free courses already?
:   People learn best if the examples are drawn from their domain: people in finance want finance examples, people in pharma want pharma data, etc., so we should use software engineering data to introduce statistical thinking to programmers. Generic courses will reach the 5-15% of programmers who are just generally interested in learning new things, but I'd like to go wider than that.

What data science will these lessons cover?
:   Data cleaning, reproducible analysis, significance testing, linear regression, clustering, and classic visualization will be enough for people to follow and evaluate the overviews that follow. This material is necessary because many programmers have no statistical training and need to be introduced to the software tools used later.

What research findings will be covered?
:   The questions raised in the opening paragraph will definitely be addressed; other topics will be prioritized by polling an advisory group to find out what's most likely to appeal to the target audience, and based on what datasets researchers are willing to share. A few favorites include showing that the distribution of error messages follow Zipf's Law, Altadmri & Brown's work on the mistakes novices make (and the fact that their teachers mis-predict common errors), Xu et al's work on how infrequently used most configuration options are, Nakshatri et al's demonstration that exceptions are mostly ignored, and Zeller et al's "IROP" study.

What tools will be used for practical examples?
:   We will use the scientific Python stack, primarily because the average programmer is more likely to have encountered Python than R, Julia, or other data science languages.

Will these lessons cover qualitative methods as well as quantitative ones?
:   They should—learners should be aware of the unique insights that qualitative methods can produce—but it will depend on whether compelling exercises can be created.

Do you think people will actually read it?
:   Yes: something that bills itself as "data science for software engineers using software engineering examples" is going to strike a lot of chords, as will "here's what we actually know about building better software faster".

Who else has tried to do this?
:   *[Facts and Fallacies of Software Engineering][facts-fallacies]*, *[Rapid Development][rapid-development]*, *[Making Software][making-software]*, and *[Accelerate][accelerate]* have presented empirical evidence about software development in one form or another (and have all sold pretty well). *[Empirical Software Engineering using R][eseur]* is more recent and more comprehensive, but is too dense for our target audience.

[accelerate]: https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339/
[aosa]: https://aosabook.org/
[bst]: https://buildtogether.tech/
[carpentries]: https://carpentries.org/
[dobzhansky]: https://en.wikipedia.org/wiki/Nothing_in_Biology_Makes_Sense_Except_in_the_Light_of_Evolution
[eseur]: http://www.knosof.co.uk/ESEUR/
[facts-fallacies]: https://www.amazon.com/Facts-Fallacies-Software-Engineering-Robert/dp/0321117425/
[making-software]: https://www.amazon.com/Making-Software-Really-Works-Believe/dp/0596808321/
[rapid-development]: https://www.amazon.com/Rapid-Development-Taming-Software-Schedules/dp/1556159005/
[sdxjs]: {{'/sdxjs/' | relative_url}}
[t3]: http://teachtogether.tech
