---
title: "The Psychology of Building Harmful Things"
date: 2026-05-05
category: sdgc ethics
---

In September and October 2021,
the Wall Street Journal published a series of articles
based on tens of thousands of internal Facebook documents provided by a former employee named Frances Haugen.
Among other things,
the documents showed that Facebook's own researchers had found that
Instagram worsened body image issues and increased suicidal ideation in teenage girls,
and that the company had known this for years while publicly denying that its platforms caused harm.
The documents also showed that Facebook's algorithms systematically promoted outrage and divisive content
because it generated more engagement,
and that internal teams had identified this as a serious problem without being able to change it.

None of this is surprising in retrospect.
What *is* surprising is how ordinary the behavior looks when you read the documents:
working groups, slide decks, and recommendations sent to committees.
The harm was not produced by villains.
It was produced by an organization operating in ways
that feel completely familiar.

The psychologist Stanley Milgram ran his obedience experiments at Yale in 1961 and 1962.
In the most famous version, subjects were told they were participating in a study of learning,
and were instructed by an authority figure to administer electric shocks
to another person whenever that person gave a wrong answer.
That "other person" was a confederate;
the shocks were fake,
and the screams were recorded.

Sixty-five percent of them administered
what they had been told was the maximum voltage—labeled "Danger: Severe Shock"—because
a person in a lab coat told them to.
Milgram's explanation was that people in hierarchical situations shift into an agentic state:
they stop regulating their own behavior against their personal moral standards
and start executing instructions from whoever they perceive as legitimate authority,
locating responsibility in the authority rather than in themselves.

The psychologist Albert Bandura identified eight mechanisms
by which people disengage their moral standards
to engage in or tolerate harmful behavior without feeling responsible for it.
Moral disengagement does not require cruelty or indifference.
It operates through cognitive reframing
that is available to people
who consider themselves good.
Moral justification frames the harm as serving a higher purpose,
while euphemistic labeling describes content moderation failures as "trust and safety challenges".
Advantageous comparison measures the harm against something worse
("At least we're not as bad as authoritarian governments"),
and displacement of responsibility points to someone else:
the advertisers demanded this, the users clicked on it.
Diffusion of responsibility distributes it across so many people
that no single one feels it:
the engineers wrote the algorithm, the product managers set the metrics, the executives approved the strategy.
Dehumanization of those harmed is rarely explicit,
but treating teenage users primarily as engagement statistics
accomplishes much of the same work.

<div class="callout" markdown="1">

The sociologist Diane Vaughan's analysis of the Challenger disaster identified a related mechanism
she called normalization of deviance:
the gradual process by which organizations come to accept risk thresholds
that would initially have been unacceptable,
through repeated exposure to near-misses
that did not immediately produce catastrophe.
NASA engineers had known for years that O-rings on solid rocket boosters failed in cold temperatures.
Each launch
that succeeded despite the problem
was treated as evidence that the problem was manageable.
The risk was not hidden:
it was documented, discussed, and progressively normalized.
The night before the Challenger launch,
engineers who understood the risk recommended against launching in cold weather.
Their recommendation was overruled by managers
who reframed the decision as requiring proof of danger rather than proof of safety.
No one decided to kill the seven astronauts who died the next day.
NASA had simply accumulated a set of practices that made the outcome possible.

</div>

The Facebook documents are interesting partly
because they show several mechanisms working together.
Individual researchers and developers knew about specific harms and documented them.
Their documentation traveled upward through an organization
where each level had reasons like competitive pressure,
advertising revenue,
or political sensitivity to treat the problem as manageable
rather than as a reason to change the product.
By the time decisions were made at the level that could change the product,
the people making those decisions were insulated from the specific harms
by many layers of summary and abstraction.
They were also,
not coincidentally,
the people whose personal wealth was most directly tied to the metrics the product optimized.

The phrase "we just build hammers" is the most common form of moral disengagement in technology work.
It frames engineers as neutral suppliers of capability,
placing all responsibility for consequences on whoever chooses to use the tools
and however they choose to use them.
This framing collapses when you look at what the tools actually do.
A recommendation algorithm that is trained to maximize engagement
and deployed on a platform used by teenagers
is not neutral the way that a hammer is.
It is a system specifically designed to capture attention,
running on knowledge about how human psychology responds to certain kinds of content,
at a scale that no individual user can resist or comprehend.
The programmers who built it made choices about what to optimize,
and their bosses approved those choices.

The economist Albert Hirschman distinguished three responses available to people inside failing institutions:
exit (leaving), voice (speaking up), and loyalty (staying and tolerating).
The Facebook documents are a record of people choosing voice—writing memos,
flagging concerns,
recommending changes—and being answered with loyalty:
the problem is noted,
continue executing,
the strategy will not change.
Most of them stayed.
Their alternatives were limited:
mandatory arbitration clauses meant they could not easily sue,
non-disclosure agreements meant they could not easily speak,
and other large platforms were no better than Facebook.
Haugen's choice to leave and bring documents with her was unusual
precisely because the structural incentives pointed the other way.

None of this means that people inside organizations that cause harm are helpless.
It means that the conditions that produce harmful outcomes are predictable,
that they operate through ordinary human psychology rather than through exceptional malice,
and that understanding them is prerequisite to changing them.
Big tech's ethics boards
and principled statements about responsible AI
are no more meaningful than the diversity commitments they have spent the last couple of years ditching.
They are meant to soothe while leaving the incentive structures unchanged.
When the metrics that determine whether a career succeeds
are the same metrics that produce harm,
most people will find ways to make peace with the harm.

*[see the whole series](@root/sdgc/) · [email me](mailto:gvwilson@third-bit.com?subject=SDGC)*

<span id="Arendt2006">Arendt2006</span>
:   Hannah Arendt:
    *Eichmann in Jerusalem: A Report on the Banality of Evil*.
    Penguin,
    2006,
    978-0143039884

<span id="Bandura1999">Bandura1999</span>
:   Albert Bandura:
    "Moral Disengagement in the Perpetration of Inhumanities."
    *Personality and Social Psychology Review*,
    3(3),
    1999,
    doi:10.1207/s15327957pspr0303_3.

<span id="Ehmke2025">Ehmke2025</span>
:   Coraline Ada Ehmke:
    *We Just Build Hammers: Stories from the Past, Present, and Future of Responsible Tech*.
    Apress,
    2025,
    979-8868812484.

<span id="Palazzo2025">Palazzo2025</span>
:   Guido Palazzo and Ulrich Hoffrage:
    *The Dark Pattern: The Hidden Dynamics of Corporate Scandals*.
    PublicAffairs,
    2025,
    978-1541705302.

<span id="Vaughan1996">Vaughan1996</span>
:   Diane Vaughan:
    *The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA*.
    University of Chicago Press,
    1996,
    978-0226851754.
