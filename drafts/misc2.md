
## The Wider World

Between 1985 and 1987, a programming bug in the [Therac-25][therac-25] resulted
in six patients being given massive overdoses of radiation, leading to death or
serious injury.  This incident has been used as a cautionary tale in software
engineering courses ever since, but since very few of us write control software
for medical radiation machines, this example and others like it seem very
abstract.

In the last few years, though, we have all seen first-hand just how much harm
software can do to everyone.  A decade ago, Facebook discovered that angry
people are more likely to engage with the platform, resulting in higher ad
revenue for the company [%b Hao2021 %].  Since disinformation and
radicalization were profitable, the company did everything it could to deflect
criticism and avoid responsibility, even as they fueled the rise of violent
nationalism and a campaign of mass murder [%b Rajagopalan2018 %].  By the
time COVID-19 began to spread, it and other tech companies had trained people
all over the world believe in conspiracy theories rather than medicine, with
fatal consequences.

<div class="callout" markdown="1">
### We just sell the poison; we don't administer it

In March 2019, a right-wing terrorist killed 51 people at prayer in
Christchurch, New Zealand. Every one of the sources he cited in his manifesto
was making money through a store hosted by a company called
Shopify;
the company didn't end its relationship with any of them.
</div>

Ethical failures by programmers now hurt us all.  For example, your school might
use a piece of software called
Proctorio,
which records video and audio of you and your
screen while you write an exam, then uses algorithms to determine if you're
cheating.  Nobody outside the company can check those algorithms to see if
they're biased against people with nervous tics, and nobody who has ever been
the victim of online harassment or stalking should have to agree to invasive
surveillance in order to pass a course.

Many of these failures have their roots in a lack of compassion—i.e., in an
inability to imagine the world through others' eyes.  As [Mike Hoye][hoye-mike] has pointed out, some wayfinding apps for
phones have an option to avoid checkpoints; it's unlikely that the people who
added that feature ever lost a loved one to a drunk driver.

As a programmer you are able to shape the world in ways that most mad scientists
can only dream of, but with great power comes great responsibility
[%b Lee1962 %].  If you'd like to understand what we're getting wrong now
so that you can avoid making the same mistakes, ask your instructor to accept a
report on one of these books for part of your project grade:

-   *Automating Inequality* [%b Eubanks2019 %] shows how the algorithms used
    to allocate health care, target people for tax audits, and decide where
    police will patrol all punish the poor for being poor.  (And if your
    reaction is, "I'm not poor so I don't care," talk to someone whose credit
    rating has never recovered from someone else with the same name missing a
    few student loan payments.)

-   *Algorithms of Oppression* [%b Noble2018 %] looks at how those
    algorithms, and the ones used by search engines, amplify and perpetuate
    racism and sexism.

-   *Weapons of Math Destruction* [%b ONeil2017 %] delves more deeply into
    the math being used and abused by these systems.  For example, software that
    predicts how likely someone is to commit a crime may use the age of their
    first interaction with the police in its score.  Thanks to racially biased
    policing practices, Black men are likely to have that encounter earlier than
    white men.  The Black man is therefore more likely to receive a prison
    sentence, which increases the chance of a future offense, which is then used
    as evidence that the algorithm works.

-   *Technically Wrong* [%b WachterBoettcher2017 %] and *Invisible Women*
    [%b CriadoPerez2019 %] look at how the lack of diversity among
    engineers and managers leads to products that either don't address
    everyone's needs or actually do harm: seatbelts and airbags that injure
    women because they were only tested on male models, facial recognition
    systems that don't recognize Black faces, and "where's my phone?" apps that
    help abusive domestic partners keep tabs on their victims.

The first and biggest mistake many programmers make is building the wrong thing;
I hope this book and the ones listed above will help you avoid that trap.
[%x reading %] lists other books that aren't as specific to tech but which helped
me understand the world our programs are used in.  Since you probably differ
from me in age, geography, and other significant respects, you may find others
that help you more.  No matter what, the most compassionate thing you can do is
ask yourself at every turn, "What will this be like for people who aren't like
me?"

<div class="callout" markdown="1">
### Why I write

It's time for a confession.  This chapter is the reason I wrote this book.
After the 2016 election in the United States, I organized a group of people to
write a guide for programmers to stuff that actually matters—the stuff that's
in this chapter.  That project fizzled out, in part because someone like Brad
([%x intro %]) wouldn't read something that said, "Programmers are
doing harm and maybe you're part of the problem."
[%b Bullock2021 Cohen2021 Ferreira2021 Gordon2021 Prioleau2021 Rankin2021 %]
are a sign that these bigger issues might finally be added to the curriculum,
but will take a long time to bear fruit. Meanwhile, I hope that starting with
time management and version control, then talking about teams and conflict, will
give people like Brad (and my younger self) a ramp to walk up instead of a cliff
to climb, because if we don't find a way to fix the tech industry our lives are
going to keep getting worse.
</div>
