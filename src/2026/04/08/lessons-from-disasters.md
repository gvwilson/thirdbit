---
title: "Lessons from Disaster Management"
date: 2026-04-08
---

Last year I started building a workshop on how to shut projects down.
I put it on hold in the fall,
both because I was finding it difficult to figure out what to say
and because working on something like that after being laid off felt a bit unhealthy.
A couple of recent discussions have revived my interest,
though,
so here are some notes that I hope one day will find a home.

## Normalization of Deviance

[Vaughan1996](#Vaughan1996) showed that the engineers involved in the Challenger disaster
did not make a single catastrophic decision
but instead made a long sequence of small decisions in which signals of danger were repeatedly noticed,
reinterpreted as acceptable,
and filed away until deviation from safety standards had become the practical norm.
The parallel for software and research projects is that
teams approaching closure often carry a backlog of things that everyone knows are wrong
but that have never been formally acknowledged.
A deliberate closure process should include an explicit audit of normalized deviations
that the team accepted because stopping to fix them felt too costly,
both to honestly document the project's actual state
and to avoid passing silent assumptions on to anyone who inherits the work.
In practical terms,
a shutdown retrospective is most valuable not when it celebrates successes
but when it names the things the team learned to live with.

## Fantasy Documents and the Rhetoric of Preparedness

[Clarke1999](#Clarke1999) describes how organizations routinely produce disaster response plans
that have no realistic chance of being executed.
Clarke calls these "fantasy documents":
their purpose is to reassure regulators, funders, and the public that someone is in charge,
despite bearing no relationship to what would actually happen under stress.
For software and research projects,
this maps onto the shutdown plan that exists in a drawer but has never been tested,
or to a `HANDOVER.md` written in an afternoon that no one outside the core team has ever read.
A closure plan should be treated as a drill script, not a policy document:
teams should periodically walk through it step by step
and ask whether each action is actually achievable with the people available.

## Tight Coupling and Normal Accidents

*Tight coupling* means that failure in one part of a system propagates rapidly through others
with little time for intervention.
[Perrow1999](#Perrow1999) argues that in complex systems where components are tightly coupled,
accidents are not aberrations but predictable outcomes of the system's design.
Modern software and research infrastructure is often tightly coupled
in ways that only become visible during shutdown:
an account that pays for ten services,
or a single personal login that controls a domain.
These tight couplings mean that an unexpected departure or account closure
cascades into a complete loss of access before anyone has time to respond.
The solution is to treat any single point of control that cannot survive a 48-hour unavailability as a bug.

That said,
[Singer2023](#Singer2023)
contrasts "blame the individual" with "blame the system",
and shows that companies push the latter to absolve themselves of responsibility.

## The Survival Arc

[Ripley2008](#Ripley2008) synthesises research on how people behave when disaster strikes
and puts forward a three-stage survival arc:

1.  Denial: refusal to believe that the situation is as serious as evidence suggests.
2.  Deliberation: a period of paralysed uncertainty about what to do.
3.  Decision: action, which may or may not be correct.

Research on building evacuations, shipwrecks, and plane crashes consistently shows that
the denial phase consumes far more time than people expect,
while thinking through the scenario before it happens dramatically shortens it.
For project closure,
this predicts that the period between a credible signal that a project is in trouble
and the first concrete closure action will be longer than planners assume,
particularly under abrupt conditions.
Rehearsal converts a novel emergency into a recognised pattern.

## Warning Signs

While it is not directly relevant to project closure,
[Palazzo2025](#Palazzo2025) argues that there are patterns in the dynamics of corporate scandals.
Would recognizing them give people early warning that projects were going to fail?

<table>
  <tr>
    <td style="border: none; padding-right: 2rem;">
      rigid ideology
      <br>
      toxic leadership
      <br>
      manipulative language
    </td>
    <td style="border: none; padding-right: 2rem;">
      corrupting goals
      <br>
      destructive incentives
      <br>
      ambiguous rules
    </td>
    <td style="border: none; padding-right: 2rem;">
      perceived unfairness
      <br>
      dangerous groups
      <br>
      slippery slope
    </td>
</table>

## The Collapse of Sensemaking

[Weick2007](#Weick2007) studied organisations that operate reliably in high-stakes, high-complexity environments
and identified five shared practices they call *mindful organizing*.
Two of these are relevant to project closure:
sensitivity to operations
(i.e., maintaining an accurate picture of what is actually happening, not what plans say is happening)
and commitment to resilience (the capacity to improvise when standard procedures fail).
Earlier, [Weick1993](#Weick1993) introduced the idea of a *cosmology episode*:
a moment when the world stops making sense and actors freeze.
These can occur during abrupt project closures
when the governance structures that normally coordinate work suddenly disappear.
One way to deal with this is to make sure that teams have fallbacks
such as personal email addresses or a shared document that doesn't depend on organizational infrastructure.
The twin risks of this are that only insiders will know these unofficial documents exist,
and that they will be out of date by the time they're needed.

## Anticipatory Mourning and the Grief of Planned Endings

[Rando2000](#Rando2000) studied *anticipatory mourning*:
grief that begins before an expected loss, not after it.
She distinguishes this from simple "grief in advance":
it involves simultaneous processing of past losses (what the project once was),
present losses (what it is becoming),
and future losses (what it will never be),
and it is cognitively and emotionally more demanding than grief after the fact
because the person must continue to function while still engaged in the thing they are losing.
For project teams,
planned shutdown triggers this:
team members must continue doing the work of closing down
while processing the loss of their work relationships and the future they had imagined.
A practical recommendation is to name this dynamic explicitly,
because people who understand that their feelings are real are better able to manage them
and to support one another.

## Bibliography

<span id="Clarke1999">Clarke1999</span>
:   Lee Clarke:
    *Mission Improbable: Using Fantasy Documents to Tame Disaster*.
    University of Chicago Press,
    1999,
    978-0226109411.

<span id="Palazzo2025">Palazzo2025</span>
:   Guido Palazzo and Ulrich Hoffrage:
    *The Dark Pattern: The Hidden Dynamics of Corporate Scandals*.
	PublicAffairs,
	2025,
	978-1541705302.

<span id="Perrow1999">Perrow1999</span>
:   Charles Perrow
    *Normal Accidents: Living with High-Risk Technologies*.
    Princeton University Press,
    1999,
    978-0691004129.

<span id="Rando2000">Rando2000</span>
:   Therese A. Rando (ed.):
    *Clinical Dimensions of Anticipatory Mourning: Theory and Practice in Working with the Dying, Their Loved Ones, and Their Caregivers*.
    Research Press,
    2000,
    978-0878223800.

<span id="Ripley2008">Ripley2008</span>
:   Amanda Ripley:
    *The Unthinkable: Who Survives When Disaster Strikes—and Why*.
    Crown Publishers,
    2008,
    978-0307352897.

<span id="Singer2023">Singer2023</span>
:   Jessie Singer:
    *There Are No Accidents: The Deadly Rise of Injury and Disaster—Who Profits and Who Pays the Price*.
	Simon & Schuster,
	2023,
	978-1982129668.

<span id="Vaughan1996">Vaughan1996</span>
:   Diane Vaughan:
    *The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA*.
    University of Chicago Press,
    1996,
    978-0226851754.

<span id="Weick1993">Weick1993</span>
:   Karl E. Weick:
    "The Collapse of Sensemaking in Organizations: The Mann Gulch Disaster."
    *Administrative Science Quarterly*,
    38(4),
    1993,
    10.2307/2393339.

<span id="Weick2007">Weick2007</span>
:   Karl E. Weick and Kathleen M. Sutcliffe
    *Managing the Unexpected: Resilient Performance in an Age of Uncertainty*
    (2nd ed.).
    Jossey-Bass,
    2007,
    978-0787996499.
