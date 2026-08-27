---
title: "Outline for an SDGC Workshop"
date: 2026-08-27
category: education
---
This one-day workshop introduces a few ideas that someone with a background in
computer science (or tech more generally) needs to know in order to think
clearly about the harms of social media and AI, and about how they should be
regulated. I would be very grateful for feedback; in particular, I know I'm
trying to cram far too much into one day, and many of my references are probably
out of date.

## At a glance

-   Length: one day (roughly eight hours, including breaks and lunch)
-   Audience: people with programming backgrounds
-   Format: 7 45-minute lessons, each followed by one 10-15 minute exercise
    taken from those listed with the lesson.

*Please see [these pages][sdgc] for background.*

## Stance

1.  Power in society is distributed very unequally, and much of what looks
    "neutral" or "technical" is actually a rule that favors some people over
    others.
1.  Inequality is substantially the product of policy choices and inherited
    advantage, not the natural sorting of individual talent.
1.  Markets are human institutions, not laws of nature. There is no such thing
    as a market without rules; the only question is whose interests the rules
    serve.
1.  What counts as "harm", and therefore what gets regulated, is also the result
    of decisions made by people. Alcohol, cannabis, sex, and guns are not
    regulated in proportion to the damage they do; they are regulated according
    to whose interests and whose anxieties dominate.
1.  Regulation of food, medicine, air, water, cars, and tobacco has repeatedly
    protected the public. Failures of regulation usually come from regulatory
    capture and weak enforcement, not from the impossibility of governing
    markets.
1.  Change is possible.  It is usually won by organized collective action rather
    than by persuasion alone, and technologists have unusual leverage in the
    fights now under way.

## Learning outcomes

By the end of the day, participants should be able to:

-   Distinguish *structural* explanations from *individual* ones, and explain
    why individual explanations are the default in tech culture.
-   Identify *who benefits and who bears the cost* of specific arrangements,
    especially when the benefits are concentrated and the costs are diffuse.
-   Recognize *market failures* (externalities, public goods, information
    asymmetry, market power) and name the regulatory instruments available to
    correct them.
-   Describe how *cognitive biases*, *identity*, and *group belonging* shape
    belief, and how design can amplify or dampen them.
-   Explain how a *society decides what counts as harm*, why regulation is often
    not proportional to harm (e.g., alcohol versus cannabis), and the difference
    between *rare-dramatic-attributable* and *diffuse-pollution* models of harm.
-   Give examples of *regulation that worked*, examples *regulation that
    failed*, and the mechanisms (especially *regulatory capture*) that explain
    the difference.
-   Explain how *media and platforms* frame issues, and shape the range of what
    is treated as debatable.
-   Connect specific harms of social media and AI to each lesson, and sketch
    realistic strategies for responding to them.

## How to run this

Pick one exercise per lesson.
:   Four or more are provided so you can match the room, the time available, and
    the participants' interests. Do not try to run them all.

Exercises are the assessment.
:   Exercises are where participants convert a claim into something they can
    use. Do not skip the debriefs: they are where the learning is consolidated.

Use think-pair-share as the default format.
:   One minute alone, two minutes in pairs, then report back. This gets more
    voices into the room than any other structure in the time available.

Keep it concrete.
:   Every abstract concept in this plan has a named example.  When discussion
    drifts into abstraction, ask, "What does that look like in a product or a
    law?"

Do not manufacture consensus.
:   Like-minded people and disagree about ends and means. "What would change
    your mind?" is usually a better question than "who's right?"

Separate the descriptive from the normative.
:   "This is how X works" and "this is what we should do about X" are different
    claims with different burdens of proof. Keep them distinct.

## Materials

-   A whiteboard or shared document for each group.
-   Sticky notes—lots of sticky notes.
-   Access to the [SDGC materials][sdgc].

## 1) Power and institutions

*Why do some people's preferences become policy and other people's don't?*

### Learning objectives

-   Describe the three "faces" of power (decision, agenda, preference-shaping).
-   Define an institution as "the rules of the game" (formal and informal).
-   Explain why concentrated interests usually defeat diffuse ones.

### Key concepts

-   Three faces of power (Lukes):
    1.  Who wins when there is a visible decision
    1.  Who controls what gets onto the agenda in the first place
    1.  Who shapes what people even *want*, so that some options never occur to anyone
-   Institutions (Douglass North):
    -   The formal rules (laws, contracts) and informal constraints (norms, conventions, taboos)
        that structure interaction
    -   Institutions always allocate advantage; they are never neutral
-   Collective action problem (Mancur Olson):
    -   It's easier to organize a small group with a large stake than a large group with a small stake
    -   This is why producers beat consumers and platforms beat users
-   Path dependence:
    -   Early choices lock in later outcomes, even after the original reasons disappear

### Flow

1.  Opening question (3 min): "Think of a product decision at your company.  Who
    actually decided it, and whose interests won?"
1.  What is power? (10 min): Walk through Lukes' three faces with concrete
    examples. Visible: who wins the vote. Hidden: who writes the agenda, the
    roadmap, the API. Invisible: who shapes what feels "natural", "obvious", or
    "inevitable". Point out that a "neutral" default or a "technical" constraint
    is usually an act of agenda-setting.
1.  Institutions (10 min): North's definition. Formal vs. informal rules.  Show
    that software itself is an institution: default settings, permission models,
    and rate limits are rules that allocate advantage. A design decision is a
    governance decision.
1.  Collective action (7 min): Olson's concentrated-vs-diffuse logic.  Example:
    ad-tech firms (few, organized, rich) versus individual users (many,
    unorganized, each with a small stake). This single asymmetry predicts much
    of tech policy.
1.  Recap (5 min).

### Exercises

Map the decision.
:   Pick a real decision, such as an API change, a layoff, a content-moderation
    rule. On a whiteboard, list (a) the visible decision-makers, (b) who set the
    agenda that made this the decision, and (c) whose preferences shaped what
    seemed "natural". Which face of power is hardest to see, and why?

Three-faces audit.
:   Take a news story about a tech-policy fight. Find one example of each face
    of power, or explain which face is *absent* from the public account and why
    that absence matters.

Concentrated vs. diffuse.
:   List the stakeholders in a policy question (e.g., banning facial recognition
    in public spaces). Classify each as concentrated or diffuse, predict which
    will organize most effectively, and check your prediction against what
    actually happened.

Design the institution.
:   A team is choosing default privacy settings for a product. Write three
    different "rules of the game" (a default, a policy, a norm) that produce
    three different outcomes, and say who wins under each.

Path dependence hunt.
:   Find a feature, protocol, or company practice whose current form is
    explained more by history ("it's always been done this way") than by present
    need. Trace the lock-in and name who benefits from keeping it.

### Takeaway

Power is not only about who wins visible fights; it is about who sets the agenda
and who shapes what people think they want. Institutions are the mechanism, and
they are never neutral.

## 2) Markets are made, not natural

*What are markets, and when do they fail?*

### Learning objectives

-   Explain why "the free market" is a description of a rule-bound institution, not an absence of rules.
-   Name and give examples of four kinds of market failure.
-   Say who bears the cost and who captures the benefit in a negative externality.

### Key concepts

-   Embeddedness (Karl Polanyi): markets are always embedded in a web of legal,
    social, and political rules. Property rights, enforceable contracts,
    currency, and liability all rest on the state. "Deregulation" is not the
    removal of rules; it is the substitution of one set of rules for another.
-   Externalities: costs or benefits imposed on third parties that the price
    does not capture. Pollution is the classic negative externality; attention
    extraction and misinformation are its digital descendants.
-   Public goods: non-excludable and non-rivalrous goods like trust, safety, and
    an informed electorate that markets under-produce because no one can be made
    to pay.
-   Information asymmetry (George Akerlof): when one party knows much more than
    the other, the "market for lemons" result is that bad options drive out good
    ones.
-   Market power: network effects and switching costs produce concentration,
    sometimes "natural monopoly," and the ability to set terms rather than take
    them.
-   Market failure: a situation in which an unadjusted market produces an
    outcome that is neither efficient nor fair.

### Flow

1.  Opening question (3 min): "Which product in this room is *unregulated*?"
    Let the room discover that the answer is "none."
1.  Markets are constructed (10 min): Every marketplace has rules about who may
    sell, what counts as fraud, who is liable, and how disputes are resolved.
    Those rules are choices with distributional consequences. Show that
    "deregulation" is re-regulation.
1.  Market failure (12 min): Four mechanisms, each with a tech example:
    1.  Externalities (misinformation, polarization, teen anxiety as costs
        priced at zero)
    1.  Public goods (an informed public, institutional trust)
    1.  information asymmetry (you do not know what the recommender is doing, or
        why)
    1.  market power (network effects make dominant social networks hard to
        exit)
1.  Who pays, who benefits (5 min): "Efficiency" is not the same as fairness. A
    market can be efficient and still concentrate benefits and diffuse harms.
    (Lesson 5 uses this distinction.)

### Exercises

Externality inventory.
:   Pick one social-media harm (polarization, teen anxiety, election
    misinformation). Identify the negative externality, who bears the cost, who
    captures the benefit, and why the price does not reflect the cost.

Public-good puzzle.
:   Classify "an informed electorate," "trust in institutions," and "online
    safety" as public goods. Explain the free-rider problem and why no single
    company has an incentive to produce them. What follows for who *should*
    produce them?

Information asymmetry.
:   Choose a feature such as a recommender, a "black box" credit or hiring
    model, or an ad auction. Who knows more, the operator or the user? What
    could close the gap: disclosure, audit, a right to explanation, or something
    else?

Natural monopoly.
:   Argue whether a dominant social network is a natural monopoly due to network
    effects, high switching costs, and/or data advantages).  If it is, what
    follows for regulation?

Free market autopsy.
:   Find a product described as "the free market at work." List every government
    rule (and private rule) it depends on related to property, contract, fraud,
    liability, and standards. Discuss: is "deregulation" ever actually the
    *absence* of rules?

### Takeaway

There is no market without rules. The interesting questions are which rules
exist, who wrote them, and who benefits. When markets fail, regulation is the
standard correction, not an alien intrusion.

## 3) How people actually think

*How do real humans make decisions, and how can that be exploited?*

### Learning objectives

-   Distinguish fast/automatic from slow/deliberate processing.
-   Name several biases and give an example of each in an online setting.
-   Explain how identity and group membership shape belief,
    and what that implies for "just show people the facts".

### Key concepts

-   Dual-process theory (Daniel Kahneman): System 1 is fast, automatic, and
    associative; System 2 is slow, effortful, and deliberative. Most online
    behavior is System 1, which is why it is so predictable and so exploitable.
-   Heuristics and biases: availability (what comes easily to mind), anchoring
    (the first number or frame sticks), confirmation (we seek and credit what we
    already believe), representativeness (we judge by resemblance, not base
    rates).
-   Motivated reasoning: when identity is at stake, reasoning becomes a lawyer
    hired to defend a conclusion rather than a judge weighing evidence.
-   Social identity (Henri Tajfel and John Turner): the mere assignment of
    people to groups produces in-group favoritism. People hold beliefs partly to
    *belong*, not only to be right.
-   Conformity and obedience: Asch's line-length studies and Milgram's obedience
    experiments show how powerfully social context shapes behavior.
-   Moral foundations (Jonathan Haidt): different audiences weight values such
    as care/harm, fairness, loyalty, authority, and purity differently.
    Persuasion that ignores this fails.
-   Attention as a scarce resource: variable rewards, infinite scroll, and dark
    patterns are engineered to exploit known psychology.

### Flow

1.  Opening question (3 min): "Why did you click the last thing you clicked?"
1.  Two systems and biases (10 min): System 1/System 2, then four biases with
    everyday online examples. Emphasize: these are *features*, usually adaptive,
    but they are predictable, and predictability is exploitability.
1.  Identity and belonging (10 min): Minimal-group results; identity-protective
    cognition; Asch and Milgram as demonstrations that social context can
    overpower private judgment (including critique of Milgram's findings). Moral
    foundations: why two reasonable people talk past each other about content
    moderation.
1.  The attention economy (7 min): Map the psychological mechanisms to specific
    design choices: variable rewards, manufactured urgency, disguised ads,
    social proof, default nudges. A design choice is a psychological
    intervention, whether the designer acknowledges it or not.

### Exercises

Bias autopsy.
:   Take a recent online argument or viral post. Identify at least two specific
    biases at work (confirmation, availability, in-group signaling, anchoring)
    and say how the platform's design amplified them.

Dark-pattern hunt.
:   In a product you use, find one dark pattern (forced continuity, disguised
    ads, manufactured urgency, infinite scroll, confirshaming).  Name the
    psychological mechanism it exploits.

Identity check.
:   Think of a belief you hold partly because of group membership. Describe,
    honestly, what would happen to your social life if you changed it. Discuss
    what this implies for "if we just showed people the facts."

Moral-foundations translation.
:   Pick a policy debate (e.g., whether to moderate misinformation). Argue it
    once from a care/fairness frame and once from a loyalty/authority/purity
    frame. Which audiences respond to which?

Design a nudge.
:   Choose a desirable online behavior (e.g., reading before sharing). Design
    one System 1 intervention (default, friction, social proof) and one System 2
    intervention (education, disclosure). Predict which works better and why,
    then discuss the ethics of each.

### Takeaway

People are not broken computers: they are social animals with fast, fallible,
identity-driven cognition. Design that respects this is possible; design that
exploits it is the business model of the attention economy.

## 4)Inequality and stratification

*Why are some people consistently better off, and is that "natural"?*

### Learning objectives

-   Contrast structural and individual explanations of social outcomes.
-   Explain cumulative advantage and opportunity hoarding.
-   Describe intersectionality and why single-axis analyses miss the worst harms.

### Key concepts

-   Stratification (Max Weber): three analytically distinct dimensions that
    overlap but do not coincide:
    1.  Class (economic position)
    1.  Status (prestige and honor)
    1.  Power (capacity to realize one's will)
-   Structural vs. individual explanation: attributing outcomes to systems and
    positions versus attributing them to personal traits and effort.
-   Cumulative advantage (the Matthew effect): advantage begets advantage; early
    differences compound over a lifetime.
-   Opportunity hoarding (Charles Tilly): groups use credentials, networks, and
    gatekeeping to keep advantages for themselves while appearing to reward
    merit.
-   Intersectionality (Kimberlé Crenshaw): overlapping systems of disadvantage
    interact; they do not simply add.
-   Social mobility: intergenerational mobility is far lower and stickier than
    the "American Dream" story implies; "meritocracy" often functions as a
    legitimation story for inherited advantage.

### Flow

1.  Opening question (3 min): "When you explain why someone succeeded or failed,
    which verbs do you reach for?"
1.  Three dimensions (10 min): Weber's class/status/power, with tech examples: a
    staff engineer may have high class but limited power; a founder has power; a
    moderator has neither. Mismatches matter.
1.  Structure vs. individual (12 min): The fundamental attribution error applied
    to society: we explain *others'* outcomes by their traits and *our own* by
    circumstance. Cumulative advantage: early advantage compounds.  Opportunity
    hoarding: how "merit" filters are built to reproduce advantage.
    Intersectionality: compounding and interacting disadvantage, and why systems
    (e.g., a facial-recognition model, a hiring algorithm) distribute harm
    unevenly across overlapping identities.
1.  Mobility and measurement (5 min): Mobility is low and sticky across
    generations. Treat "meritocracy" as an empirical claim to test, not an
    assumption.

### Exercises

Explain the gap.
:   Take a real inequality (who gets into a selective program, who receives
    venture funding). Produce two explanations (one individual, one structural)
    then discuss which better fits the evidence and why the individual one is
    the cultural default.

Three-dimension map.
:   For four tech roles (e.g., startup founder, staff engineer, content
    moderator, gig worker), rate class/status/power as high or low. Discuss the
    mismatches (e.g., high status but low power; high income but low security).

Cumulative advantage.
:   Trace how one early advantage like a wealthy school, a first internship,
    seed funding, or an early follower count compounds across a career. Identify
    the points where policy or design could interrupt the compounding.

Opportunity-hoarding audit.
:   Find a credential, interview process, or referral network that functions to
    hoard opportunity. Distinguish its stated purpose from its actual effect.

Intersectional case.
:   Analyze how a policy or product harms people differently across overlapping
    identities (a facial-recognition system, a hiring algorithm, an automated
    welfare screen). Why does a single-axis analysis miss the worst harms?

### Takeaway

Inequality is not a sorting of individuals by merit; it is the accumulated
effect of rules, networks, and compounding advantage. Meritocracy is a claim to
test, and often a story that legitimizes inheritance.

## 5) Deciding what is harmful and how to regulate it

*How does a society decide what counts as harm, and what should it do about the harms it recognizes?*

### Learning objectives

-   Explain why what gets labeled "harmful", and therefore gets regulated,
    does not track a neutral measurement of damage.
-   Contrast the rare-dramatic-attributable model of harm with the diffuse-pollution model,
    and say which one describes social media and AI.
-   Distinguish a moral panic from an evidence-backed harm,
    and say what each implies for regulation.
-   Name the instruments by which harm is regulated and the failure mode of capture.

### Key concepts

-   Harm is not self-evident. What counts as harm, and which harms get
    regulated, is decided through contests of power, moral panic, racial
    hierarchy, and commercial interest, not by first measuring damage and then
    writing a law.
-   Rare, dramatic, and attributable vs. diffuse, cumulative, and statistical.
    Engineers are trained on the first model: the faulty valve that causes a
    boiler explosion. The worst industrial harms (leaded gasoline, tobacco,
    asbestos, opioids, and now social media) are the second: real and massive,
    but spread across millions of small exposures so that no single decision can
    be shown to have caused a single injury.
-   The pollution model. Once a society accepts that harm can be diffuse and
    cumulative, responsibility shifts from proving individual causation to
    holding the emitter accountable for the aggregate. Engineers now study
    pollution not out of conscience but because liability eventually forced them
    to.
-   Moral panic. A disproportionate alarm that often targets the *wrong* harm
    and leaves the real one unaddressed. The violent-video-game panic is the
    canonical case; the real harm was loot boxes, not gunfire.
-   The differential legalization of pleasure. Alcohol kills hundreds of
    thousands a year and sits in supermarkets; cannabis, with a lower harm
    profile, was criminalized for most of a century, with enforcement falling on
    Black and Latino communities. What gets legalized tracks political
    economy and racial hierarchy far more reliably than it tracks
    harm.
-   Precautionary principle and product safety. Where harm is plausible and
    irreversible, the burden of proof may rest on those introducing the risk.
    Pre-market drug approval is the model.
-   Regulation as a toolkit and regulatory capture: recap of standards,
    licensing, disclosure, liability, taxation, and structural remedies, and the
    recurring failure mode in which regulators come to serve the regulated.

### Flow

1.  Opening question (3 min): "Which is more dangerous: alcohol or cannabis? How
    do you know, and does the law match your answer?"
1.  Sex, drugs, and guns (10 min): three cases that show harm is contested, not
    measured.
   -   Sex. What was "private" versus what was "criminal" has been redrawn case
       by case, in someone's interests, with no consistent underlying
       principle. Sexual behavior between consenting adults was legally public
       (in the sense of being criminally regulated) well into the twentieth
       century; the expansion of privacy was won, not discovered.
   -   Drugs. Alcohol kills hundreds of thousands a year and is sold in
       supermarkets; cannabis, with a lower measured harm profile, was a
       criminal offense whose enforcement fell almost entirely on Black and
       Latino communities. Portugal's 2001 decriminalization of personal
       possession, paired with treatment and harm reduction, cut HIV
       transmission and overdose deaths without raising use.
   -   Guns. After Columbine, legislators went after violent video games; the
       evidence never supported the hypothesis, and cross-national comparisons
       point to gun availability, inequality, and the history of racially
       organized violence as the real drivers. Motivated reasoning (Lesson 3)
       means even a trained scientist who owns a gun scrutinizes gun-violence
       studies more skeptically than climate studies.
   -   The point is that we do not first measure harm and then regulate. We
       first decide who and what matters, then find or manufacture the harm that
       justifies the decision.
1.  Two models of harm (7 min): rare/dramatic/attributable versus
    diffuse/cumulative. The engineer's default is the first; the worst damage
    from industry has been the second. Leaded gasoline lowered a generation's
    IQs without any single tank of fuel causing a measurable injury; no
    particular cigarette caused any particular cancer death. Social media's
    harms are this kind (so-called "cognitive pollution"), so the causal chain
    is long, probabilistic, and hard to attribute, and therefore hard to
    regulate.
1.  Pollution and dangerous pharmaceuticals (7 min): the two cases where
    regulation actually worked, and why.
   -   Pollution. Hill and Doll's 1950 study linked smoking to lung cancer; the
       tobacco industry's response was to fund research *designed to produce
       uncertainty*, and it worked for decades (the same playbook ran for leaded
       gasoline, asbestos, and oxycontin, and is running now for social media
       and AI). The remedy was the pollution model: hold the emitter liable for
       the aggregate, not for a specific injury. The ozone layer was protected
       before it cost lives: proof we need not wait for disaster.
   -   Dangerous pharmaceuticals. Thalidomide was approved in West Germany in
       1957; Frances Kelsey, a pharmacologist at the FDA, refused to approve it
       in the US because the safety evidence was insufficient, and the birth
       defects that followed where it *was* approved vindicated her. The result
       was pre-market approval and the precautionary principle.
   -   What worked. Accurate diagnosis of the *actual* harm; the right
       instrument; and a regulator that was not captured. Capture is the
       recurring enemy, and the industries that fight regulation are the same
       ones that manufacture uncertainty about it.
1.  Recap and bridge (3 min): Social-media and AI harms are pollution-model
    harms. The trap is moral-panic framing (e.g., "ban the kids' phones")
    instead of the actual harm: attention extraction, addictive design,
    discrimination, surveillance. Lessons 6 and 7 apply this to media and to
    change.

### Exercises

Rank the harms, then the laws.
:   Consider the list "alcohol, cannabis, heroin, gambling, social media,
    AI-generated misinformation". Rank the items by measured harm, then by how
    the law actually treats them. Discuss the gaps and what explains them.

Two models of harm.
:   Pick a harm (e.g., a bridge collapse, leaded gasoline, a data breach, or
    teen anxiety from Instagram). Classify it as rare-dramatic-attributable or
    diffuse-cumulative, and say which regulatory instrument each model naturally
    suggests. Which model were you trained to think in?

Moral panic vs. real harm.
:   Choose a concern (violent video games, kids and phones, "AI will end
    humanity"). List the features that make it look like a moral panic and the
    features that make it an evidence-backed harm.  What is the *actual* harm
    the panic may be distracting from?

Precautionary vs. wait-and-see.
:   Replay the thalidomide decision: you are the regulator with evidence that is
    suggestive but not conclusive. Do you approve or wait? What does your answer
    imply for "move fast and break things" and for releasing open-weight AI
    models?

Redesign the law.
:   Pick a harm currently regulated on a moral or panic basis rather than an
    evidence basis (e.g., cannabis, a social-media feature).  Propose a
    regulation that tracks the *actual* harm, and name the political obstacles
    to passing it.

### Takeaway

Harm is not a fact that precedes regulation; it is a claim made by the powerful,
the panicked, and the organized. Regulating well means diagnosing the actual
harm rather than the one that generates the best testimony, using the pollution
and product-safety models where they fit, and defending the regulator from
capture.

## 6) Media, ideology, and public opinion

*How do people come to believe what they believe about the world?*

### Learning objectives

-   Distinguish agenda-setting from framing.
-   Describe the shift from human gatekeeping to algorithmic engagement and its consequences.
-   Apply a "manufacturing consent" lens to platform-era media.

### Key concepts

-   Agenda-setting: media may not tell you what to *think*, but they tell you
    what to think *about*. Absence from the agenda is a form of power (recall
    Lesson 1's second face).
-   Framing: how an issue is defined shapes which answers seem reasonable.
    "Screen time" versus "attention extraction"; "AI safety" versus "corporate
    accountability."
-   Gatekeeping and its collapse: for much of the twentieth century a small
    number of editors and broadcasters decided what was newsworthy. That
    concentration had its own distortions: platforms replaced it with
    engagement-maximizing algorithms, which are a different and arguably worse
    concentration.
-   The propaganda model (Edward Herman and Noam Chomsky): five filters
    (ownership, advertising, sourcing, flak, and ideology) shape what gets
    through.  As a result, the range of acceptable debate is narrower than the
    range of actual opinion.
-   Manufactured consent vs. media effects: the debate over how much media shape
    belief versus reflect it; the safe conclusion is that both happen.
-   Epistemic fragmentation: filter bubbles and polarization, with the caveat
    that the empirical "echo chamber" story is more mixed than popular accounts
    claim; the larger problem may be a shared but distorted diet, not total
    separation.
-   Moral panic: a disproportionate, often exaggerated public alarm that can
    coexist with a real, evidence-backed harm.

### Flow

1.  Opening question (3 min): "What did you learn about the world this week, and
    who decided it was worth your attention?"
1.  From gatekeeping to platforms (10 min): The twentieth-century gatekeeper and
    its problems; the platform replacement and its problems.  Concentration did
    not go away; it changed shape and added a profit motive tuned to engagement.
1.  Framing and agenda (10 min): Agenda-setting and framing with concrete
    before/after pairs. Show that a reframe changes the feasible policy menu.
1.  The propaganda model (10 min): Herman and Chomsky's five filters, updated
    for platforms (engagement, algorithmic amplification, influencer economies).
    Manufactured consent: the center of gravity of "respectable" debate is not
    where public opinion actually is.
1.  Epistemic fragmentation (5 min): Polarization and filter bubbles, with the
    empirical caveat. Acknowledge uncertainty rather than overclaiming; this is
    what a rigorous progressive account does.

### Exercises

Framing audit.
:   Find one story covered two ways (e.g., "misinformation" versus "platform
    accountability"). List the frames and metaphors, and note who is cast as the
    agent and who as the victim.

Agenda check.
:   Compare what a news outlet and a social-media feed surfaced about the same
    event. What was on the agenda, and what was conspicuously absent? Who
    benefits from that absence?

Propaganda filters today.
:   Take a tech-policy controversy. Walk through Herman and Chomsky's five
    filters as updated for platforms, and identify which are most active in this
    case.

Manufacturing a panic.
:   Take a moral panic (e.g., kids and screens, "AI will end humanity"). Trace
    how news coverage and platform feeds *frame* it: which experts get quoted,
    what metaphors recur, who is cast as the villain.  How does the framing
    amplify the alarm while suppressing the evidence?

Redesign the gatekeeper.
:   If you had to replace engagement maximization with a different editorial
    principle, what would it be? Name the new distortions it would introduce.

### Takeaway

Belief is produced, not just discovered. Whoever controls the agenda and the
frame controls a large part of what is thinkable. Platforms changed the
*economics* of that production, and with it, the politics.

## 7) How change happens

*Given all of this, what actually produces change, and what should we do about social media and AI?*

### Learning objectives

-   Describe the conditions under which social movements succeed.
-   Explain a "policy window" and assess whether one is open.
-   Connect a specific social-media or AI harm to each of the day's six prior lessons.
-   Sketch a realistic reform strategy and name their own leverage as a technologist.

### Key concepts

-   Social movements and collective action: movements succeed when they combine
    organization, opportunity, and framing (resource mobilization and
    political-process traditions).
-   Policy window (John Kingdon): when the problem stream (a defined crisis),
    the politics stream (a constituency and mood), and the policy stream (a
    ready-made solution) align, change becomes possible. Windows open rarely and
    close quickly.
-   Coalitions: durable change usually requires unusual alliances across groups
    that do not otherwise agree.
-   Exit, voice, and loyalty (Albert Hirschman): the three responses to a
    failing institution, and why voice is usually the only one that changes the
    institution itself.
-   Technologists' leverage: scarce skills, access to systems, and inside
    knowledge vs. constraints (NDAs, golden handcuffs, the myth of the "neutral
    engineer").

### Flow

1.  Opening question (3 min): "Name one thing that is better now than it was
    fifty years ago. Who made it better, and how?"
1.  How change happens (12 min): Organization + opportunity + framing.
    Examples: civil rights, environmental regulation, seat belts, tobacco,
    marriage equality, worker safety. Emphasize: change is slow, non-linear, and
    won by *pressure*, not persuasion alone. Kingdon's three streams and the
    policy window:
    -   Problem: is it defined as a crisis?
    -   Politics: who is the constituency?
    -   Policy: is there a ready solution?
1.  The technologist's role (7 min): Insider/outsider power. Engineers can
    refuse, whistleblow, organize, build alternatives, or work on policy. Their
    leverage is unusual (scarcity, access) and their constraints are real
    (contracts, career risk, the ideology of neutrality).
1.  Applying the toolkit (5 min): Name the harms (attention extraction,
    misinformation, polarization, discrimination, labor deskilling,
    surveillance, concentration, environmental cost). Map each to the day's
    lessons.
1   Outline a realistic menu (5 min): transparency and audits, liability,
    structural remedies (interoperability, breakups), worker power, public
    alternatives, global coordination.  Be honest about capture risk for each.
1.  Synthesis and close (5 min): The arc of the day: "how society works" is
    knowable, and knowing it is the prerequisite for changing it.

### Exercises

Policy-window map.
:   Pick one concrete harm. For Kingdon's three streams: assess whether a window
    is open and what would open it.

Coalition design.
:   Choose a reform (e.g., mandatory algorithmic audits).  List likely
    supporters, likely opponents, and the unexpected allies (parents, small
    business, civil-liberty groups, religious communities) that could make it a
    winning coalition.

Leverage inventory.
:   As a technologist, list your specific sources of leverage (skills, access,
    capital, community) and one concrete action you could take in each of the
    next 1, 6, and 12 months.

Harm-to-lesson mapping.
:   Take one harm (e.g., AI-driven hiring discrimination) and write one sentence
    connecting it to each lesson.  The point is to demonstrate that every real
    harm has structural, economic, psychological, stratificational, regulatory,
    and ideological dimensions.

Reform-menu debate.
:   Assign groups different positions (e.g., audits only, liability, breakups,
    public options, worker power, "it cannot be fixed").  Each group argues its
    case; then the room discusses which *combination* is realistic and coherent.

Backward plan.
:   Pick a target outcome five years out (e.g., "audits of high-impact models
    are mandatory and meaningful"). Work backward to name the milestones,
    coalitions, and political conditions required at each stage.

### Takeaway

The harms are not mysterious and the responses are not untried.  Every tool
discussed in the workshop is available to people who organize. Technologists
hold real cards; the question is whether they play them.

## Closing synthesis (25 min)

If there is time left, use it to make the day's through-line explicit, not to
introduce new material.

1.  Power and institutions set the rules; markets are made, not natural; people
    are social and fallible; inequality is produced, not earned; harm is
    contested, not measured; regulation can and does work when it is not
    captured; media manufacture the thinkable; change comes from organized
    pressure.
1.  Ask each participant to write one sentence naming a specific social-media or
    AI harm, the lesson that best explains it, and one realistic response. Go
    around the room; collect the sentences.
1.  Point to the reading list below and, if running this with colleagues, to a
    follow-up session or reading group.

## Reading list

1.  Power and institutions
    -   Steven Lukes, [*Power: A Radical View*](https://isbnsearch.org/isbn/9781352012347)
    -   Douglass C. North, [*Institutions, Institutional Change and Economic Performance*](https://isbnsearch.org/isbn/9780521397346)
    -   Mancur Olson, [*The Logic of Collective Action*](https://isbnsearch.org/isbn/9780674537507)
1.  Markets are made, not natural
    -   Karl Polanyi, [*The Great Transformation*](https://isbnsearch.org/isbn/9780807056431)
    -   Mariana Mazzucato, [*The Entrepreneurial State*](https://isbnsearch.org/isbn/9781610396134)
    -   George A. Akerlof, ["The Market for 'Lemons'"](https://doi.org/10.1016/B978-0-12-214850-7.50022-X)
    -   Elinor Ostrom, [*Governing the Commons*](https://isbnsearch.org/isbn/9780521405997)
1.  How people actually think
    -   Daniel Kahneman, [*Thinking, Fast and Slow*](https://isbnsearch.org/isbn/9780374533557)
    -   Jonathan Haidt, [*The Righteous Mind*](https://isbnsearch.org/isbn/9780307455772)
    -   Richard H. Thaler and Cass R. Sunstein, [*Nudge*](https://isbnsearch.org/isbn/9780143115267)
1.  Inequality and stratification
    -   Charles Tilly, [*Durable Inequality*](https://isbnsearch.org/isbn/9780520221703)
    -   Kimberlé Crenshaw, ["Demarginalizing the Intersection of Race and Sex"](https://doi.org/10.5771/9783748948049-335)
    -   Thomas Piketty, [*Capital in the Twenty-First Century*](https://isbnsearch.org/isbn/9780674430006)
1.  Deciding what is harmful and how we regulate it
    -   Tom Wainwright, [*Narconomics*](https://isbnsearch.org/isbn/9781610395830)
    -   David Nutt, [*Drugs Without the Hot Air*](https://isbnsearch.org/isbn/9781906860165)
    -   Johann Hari, [*Chasing the Scream*](https://isbnsearch.org/isbn/9781620408902)
    -   Naomi Oreskes and Erik M. Conway, [*Merchants of Doubt*](https://isbnsearch.org/isbn/9781596916104)
    -   Sarah E. Igo, [*The Known Citizen*](https://isbnsearch.org/isbn/9780674244795)
    -   Allan M. Brandt, [*The Cigarette Century*](https://isbnsearch.org/isbn/9780465070473)
    -   Tim Wu, [*The Master Switch*](https://isbnsearch.org/isbn/9780307269935)
1.  Media, ideology, and public opinion
    -   Edward S. Herman and Noam Chomsky, [*Manufacturing Consent*](https://isbnsearch.org/isbn/9780375714498)
    -   Zeynep Tufekci, [*Twitter and Tear Gas*](https://isbnsearch.org/isbn/9780300215120)
    -   danah boyd, [*It's Complicated: The Social Lives of Networked Teens*](https://isbnsearch.org/isbn/9780300166316)
1.  How change happens, and applying it all
    -   John W. Kingdon, [*Agendas, Alternatives, and Public Policies*](https://isbnsearch.org/isbn/9780321121851)
    -   Frances Fox Piven and Richard A. Cloward, [*Poor People's Movements*](https://isbnsearch.org/isbn/9780394726977)
    -   Albert O. Hirschman, [*Exit, Voice, and Loyalty*](https://isbnsearch.org/isbn/9780674276604)

On social media and AI specifically:

-   Shoshana Zuboff, [*The Age of Surveillance Capitalism*](https://isbnsearch.org/isbn/9781610395694)
-   Cathy O'Neil, [*Weapons of Math Destruction*](https://isbnsearch.org/isbn/9780553418811)
-   Ruha Benjamin, [*Race After Technology*](https://isbnsearch.org/isbn/9781509526406)
-   Kate Crawford, [*Atlas of AI*](https://isbnsearch.org/isbn/9780300209570)
-   Virginia Eubanks, [*Automating Inequality*](https://isbnsearch.org/isbn/9781250074317)
-   Safiya Umoja Noble, [*Algorithms of Oppression*](https://isbnsearch.org/isbn/9781479837243)

## Appendix: harm-to-lesson map

A cheat sheet for the synthesis in Lesson 7.

-   Attention extraction and addiction
    -   Power: engagement design is agenda-setting for a billion minds.
    -   Markets: the cost of degraded attention is an unpriced externality.
    -   Psychology: variable rewards exploit System 1 and in-group signaling.
    -   Inequality: the cost falls hardest on those with the fewest resources to opt out.
    -   Harm & regulation: a diffuse, cumulative harm (the pollution model), not a dramatic one;
        regulate the emitter, not the user, and beware the "screen time" moral panic.
    -   Media: framing it as "screen time" blames users rather than the extractor.
-   Algorithmic discrimination
    -   Power: the "neutral model" hides a rule that allocates advantage.
    -   Markets: information asymmetry (the applicant cannot see the decision rule).
    -   Psychology: automation bias leads humans to defer to a confident number.
    -   Inequality: training data encode and compound historical stratification.
    -   Harm & regulation: diagnose the actual harm (discrimination),
        then pick the instrument and guard against capture.
    -   Media: coverage frames it as a "glitch" rather than a design choice.
-   Election misinformation and polarization
    -   Power: whoever sets the feed's agenda shapes the thinkable.
    -   Markets: misinformation is a negative externality; trust is a public good.
    -   Psychology: confirmation bias and identity-protective cognition.
    -   Inequality: targeting is cheap precisely where people are most isolated.
    -   Harm & regulation: a pollution-model harm;
        the pacing problem and global-versus-national jurisdiction complicate the remedy.
    -   Media: the collapse of gatekeeping replaced editors with engagement.
-   Surveillance and labor deskilling
    -   Power: surveillance shifts the balance of power between worker and firm.
    -   Markets: data is a barrier to entry and a source of market power.
    -   Psychology: ambient surveillance changes behavior even without explicit threat.
    -   Inequality: monitoring falls heaviest on the least powerful workers.
    -   Harm & regulation: worker protection and privacy are proven regulatory domains;
        the challenge is diagnosis and capture, not feasibility.
    -   Media: "productivity" framing hides the redistribution of power.
-   Concentration of the industry
    -   Power: a handful of firms set the rules of the game for everyone else.
    -   Markets: network effects produce natural-monopoly tendencies.
    -   Psychology: switching costs exploit inertia and default bias.
    -   Inequality: returns accrue to owners, not to the workers who produce value.
    -   Harm & regulation: antitrust is the classic structural remedy, weakened and due for revival;
        self-preferencing is payola with a new interface.
    -   Media: owned media and advertiser dependence shape the coverage of tech itself.

[sdgc]: @root/sdgc/
