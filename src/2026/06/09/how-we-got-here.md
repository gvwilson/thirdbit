---
title: "How We Got Here"
date: 2026-06-09
category: sdgc
---
<div class="callout" markdown="1">

*These posts are Version 2 of this material.
Please [email me](mailto:gvwilson@third-bit.com?subject=SDGC) with feedback.*

1.  [Sex and Drugs and Guns and Code Restart](@root/2026/06/08/sex-and-drugs-and-guns-and-code-restart/)
1.  [A Little Psychology](@root/2026/06/09/a-little-psychology/)
1.  [How We Got Here](@root/2026/06/09/how-we-got-here/)
1.  [More Psychology](@root/2026/06/10/more-psychology/)
1.  [When the Model is the Harm](@root/2026/06/11/harmful-models/)
1.  [Privacy, Power, and the Self](@root/2026/06/12/privacy/)
1.  [Who Gets What and Why](@root/2026/06/13/who-gets-what-and-why/)
1.  [More Analogies](@root/2026/06/14/more-analogies/)

[Bibliography](@root/2026/04/13/a-bibliography/) &middot; [Glossary](@root/2026/05/20/glossary/)

</div>

In order to understand how the world works,
we have to understand how we got here.
That's also a bit much for one blog post,
but the sections below summarize a few things I didn't know
when I started trying to figure it out.

## The Creation of Money

In the 1660s,
London merchants who needed somewhere safe to store their gold and silver
began using the vaults of goldsmiths,
who already had the locks and the reputation.
The goldsmith would issue a paper receipt;
merchants quickly discovered that it was easier to pay each other with receipts
than to cart metal through the streets.
The receipts circulated as currency.

The goldsmiths making these transactions noticed that
at any given time,
only a fraction of depositors came to claim their metal.
The rest left it in the vault, trusting the paper.
A goldsmith willing to issue *more* receipts than he actually had gold in the vault
could lend out the extras and collect interest,
as long as depositors never all came at once.
This is the origin of fractional reserve banking,
a name that makes it sound more principled than it is.

This matters for understanding the modern financial system
because the same basic mechanism is still operating,
at much larger scale,
with slightly more oversight,
in digital form.
The story is also the origin of the periodic bank run:
when depositors suspect the receipts exceed the gold,
everyone tries to claim their metal at once,
which confirms the suspicion,
which guarantees the collapse.
In September 2007,
people queued outside branches of Northern Rock, a British mortgage lender,
for three days—the first run on a British bank in 150 years.
The queues were orderly and very British,
but the mechanism was identical to panics that had destroyed banks in Amsterdam in 1763,
in the United States repeatedly between 1873 and 1907,
and in Argentina in 2001.

In 2014,
the Bank of England published a paper with the dry title
"Money Creation in the Modern Economy."
Its core claim was not subtle:
when a commercial bank makes a loan,
it does not lend out money that was previously deposited.
It creates the deposit simultaneously with the loan.
The loan and the deposit appear on the bank's books at the same moment.
Money that did not previously exist comes into existence through the act of lending.

This is just as ridiculous as it sounds, but very useful.
When you repay a loan,
the deposit disappears from your account and the corresponding debt disappears from the bank's books.
Money is destroyed.
The money supply expands when banks are lending
and contracts when loans are being repaid or written off.

The anthropologist David Graeber spent years studying debt across cultures and centuries.
In *Debt: The First 5,000 Years*,
he showed that the story economists tell about money—that barter came first,
that money was invented to make barter easier,
and that credit developed on top of money—has
almost no support in the historical or anthropological record.
The fish-for-axes economy that appears in introductory economics textbooks
has never actually existed anywhere.
What appears in the record instead are systems of mutual obligation and accounting:
I owe you,
you owe me,
the village keeps track.
Credit relationships are older than markets and older than money.
Money emerged not to simplify barter but to settle and record debts
[Graeber2011,McLeay2014].

Who gets to create money,
and under what constraints,
are political questions.
Andrew Jackson ran his 1832 presidential campaign substantially on the question
of whether a private institution should have the power
to create the country's money.
The financial panics that followed
eventually produced the Federal Reserve Act of 1913,
passed in the aftermath of the 1907 panic,
to give the money-creation system a lender of last resort.

Contemporary fintech companies are participating in this long argument
without usually acknowledging it.
Klarna, Afterpay, and Affirm extend credit to consumers at the point of purchase.
In doing so they are creating money,
but they are doing it without the deposit insurance,
capital requirements,
or regulatory oversight that apply to licensed banks.
PayPal holds tens of billions of dollars in customer balances that do not carry deposit insurance,
and Stripe extends credit to merchants.
These companies are, in each case, capturing the profit of money creation
while avoiding the obligations that historically came with it—the same maneuver
that London goldsmiths discovered in the 1660s [Kindleberger2005,Chang2012].

## The Invention of the Corporation

The limited liability corporation is the dominant form of business organization,
and its history is stranger than most people realize.
**Joint-stock companies** with limited liability appeared in England and the Netherlands in the early 1600s.
The Dutch East India Company, founded in 1602,
is often called the world's first publicly traded corporation:
it issued shares to outside investors,
its shareholders could not lose more than they invested,
and those shares were traded on what became the Amsterdam Stock Exchange.
The whole structure was designed to let wealthy merchants finance long and risky trading voyages
without betting their entire fortunes on any single ship.

Limited liability is a legal invention,
created by governments to encourage private investment
in ventures too expensive for any one person to fund alone.
It is not a natural feature of commerce.
It is a grant from the state—a deliberate decision to limit the consequences that flow from a business's failures.
Before it existed,
a merchant who invested in a failing venture could lose everything they owned.
After it, investors could only lose what they put in.
This changed who was willing to invest, in what, and on what scale.

<div class="callout" markdown="1">

Why do so many Canadian tech startups end up incorporated in Delaware?
Not because Delaware law is superior, but because American venture capital funds require Delaware C-corporations.
Their legal documents were drafted for that structure,
their lawyers know it,
and their limited partners expect it.
A Canadian founder who takes US venture money
often has to execute what is called a **Delaware flip**:
creating a new Delaware holding company above the existing Canadian entity,
transferring the intellectual property,
and essentially making the company American on paper.
This is an expensive process that produces no operational benefit for the company;
it is pure path dependency imposed by the capital markets.

</div>

What tech companies have innovated on is not the basic corporate form
but the voting structure within it.
**Dual-class share structures**,
in which founders hold shares with ten or more votes each
while public investors hold shares with one vote,
have become standard in major tech IPOs.
When Google went public in 2004,
Larry Page and Sergey Brin wrote a letter to shareholders explicitly explaining
that they intended to run the company unconventionally
and that investors who disagreed should not buy the stock.
The practical effect is that founders retain effective control regardless of how many shares they have sold:
the company is publicly traded but not publicly governed,
which is exactly what most founders want.

The usual excuse for why tech companies aren't worker cooperatives or other equitable structures
is that cooperative governance is too slow and cooperative financing too limited.
This explanation is conveniently incomplete.
It omits the fact that the founders, lawyers, and venture capitalists making the choice
benefit most from the conventional structure.
A Delaware C-corp with dual-class shares concentrates decision-making authority and financial upside
in the hands of a small number of people at the top.
Describing this as a neutral response to market conditions,
rather than as a choice made by self-interested parties who control the available alternatives,
takes a certain kind of nerve [Whyte1991,Kelly2012].

## The Monopolist's Playbook

Venture-funded platform competition is a **tontine**.
In European finance from the seventeenth through the nineteenth centuries,
a tontine was a pooled investment in which,
as each subscriber died,
the remaining subscribers' shares increased,
with the last survivor inheriting the entire fund.
Most governments eventually banned tontines because they created obvious incentives
to hasten the death of other participants.

In platform competition,
the explicit goal from the first investment round
is to be the one platform that achieves dominance while all competitors fail.
Operating below cost to build market share,
sometimes for years,
makes financial sense
if it eliminates alternatives and enables the extraction of monopoly rents afterward.
Investors who hold positions in multiple competing platforms profit regardless of which one wins;
the workers, users, and communities that depended on those platforms do not.

The life cycle of a dominant firm in a network industry follows a pattern:
enter the market with a genuinely useful product,
use that position to acquire or drive out competitors,
then extract maximum value from the resulting captive market.
Standard Oil, railway companies, the Bell telephone system, cable television,
and major record labels all followed this playbook.
The constraints that eventually constrained them
were the result of political struggles that the industries fought at length.

At its peak,
Standard Oil controlled roughly ninety percent of US oil refining capacity.
It didn't achieve this through superior efficiency
but through secret railroad rebates,
**predatory pricing** against competitors,
and strategic acquisitions of rivals.
The Sherman Antitrust Act of 1890 was written in direct response,
and the landmark 1911 Supreme Court decision that broke Standard Oil into thirty-four separate companies
is often cited as the definitive antitrust remedy.
What is less often noted is that several successor companies immediately reconsolidated,
and that John D. Rockefeller's personal fortune *increased* after the breakup
as the stock prices of the subsidiaries rose.
The remedy addressed the legal structure of the monopoly
without fundamentally altering the underlying concentration of wealth or market power [Stoller2019].

The Bell network evolved along slightly different lines than Standard Oil.
AT&T's control over telephone infrastructure from the 1910s until its breakup in 1984
was maintained by a **regulatory compact**
in which AT&T accepted rate regulation in exchange for a protected monopoly position.
That compact produced genuine achievements:
Bell Labs generated an extraordinary concentration of fundamental research,
including the transistor, the laser, information theory, and Unix.
It also suppressed the development of competitive long-distance service
and technologies that threatened the core telephone business [Wu2010].

The British railway mania of the 1840s followed the same cycle earlier and more visibly.
The consolidation that followed produced a small number of large regional monopolies.
Parliament responded with rate controls and mandated third-party access to track,
which the railway companies contested for decades,
making the same arguments that social media and AI companies make today:
the industry was too complex to regulate effectively,
regulation would destroy investment incentives,
and the market would eventually take care of things anyway.

**Network effects** and **switching costs**
are what make monopolies in network industries self-reinforcing.
A telephone network becomes more valuable as more people join it,
giving the dominant network an advantage separate from the quality or price of the underlying service.
Switching costs compound this:
users who have built workflows and contact lists around a platform
can't afford to move to a competitor even when the competitor offers a better product.

In 2005, a Dutch startup called Booking.com offered hotels a deal:
list your rooms on our platform for a 12% commission,
and we will send you customers you would not otherwise reach.
Hotels signed up;
travelers followed, because the inventory was there,
and by the early 2010s,
Booking.com was the dominant hotel search platform across Europe and much of Asia.

Then the commissions started climbing.
By 2019, many hotels were paying 25-30% per booking,
plus additional fees for "preferred placement" near the top of search results.
Hotels that declined to pay for placement found themselves buried behind those that did.
The traveler experience degraded too:
search results increasingly reflected who had paid for prominence,
not which hotel best matched the search.

Hotels understood what had happened,
but they were locked in.
Their repeat customers now booked through Booking.com rather than directly,
because that was where travelers looked.
A hotel that left the platform did not take its customers with it—those
relationships belonged to the platform.
Leaving meant losing access to a market the platform now controlled.

Cory Doctorow named this pattern **enshittification**.
A platform enters a market by offering a service below cost to build a user base.
Once users are locked in,
it begins subsidizing business customers,
using the captive user base as leverage.
Once business customers are also locked in,
it harvests both by
degrading service quality,
raising prices,
and extracting the maximum value from a market it now controls.
The platform can do this because the switching costs that lock users in
also protect it from competitive consequences [Doctorow2022].

Enshittification depends on two things:
network effects and **structural lock-in**.
Neither is not specific to digital platforms.
The record club Columbia House ran the same play in a different era.
Launched in the 1950s in the United States and Canada
and later extended to the United Kingdom, Australia, and Brazil,
it offered new members twelve records or cassettes for a penny.
The first transaction was a real deal.
The extraction came later:
members committed to purchasing eight more titles at "regular club prices,"
which were two to three times the retail price of the same albums in a shop.
If a member forgot to decline the monthly selection,
it arrived automatically and the cost appeared on their bill.
The penny offer built the membership;
the commitment structure extracted the value.
Columbia House recruited around sixteen million members in the United States alone
before the model collapsed when digital music eliminated the inventory advantage.

<div class="callout" markdown="1">

In 1986, a corporation better known for making women's underwear
acquired JanSport and, over the following decades,
bought nearly every backpack brand with a reputation for durability.
Controlling more than half the US backpack market,
it had no competitive pressure to maintain quality.
Fabric thickness dropped, cheaper zippers replaced better ones, and stitching density fell.
The products looked identical on the shelf;
customers discovered what they had actually bought when the stitching pulled apart at the stress points.

JanSport continued to advertise a lifetime warranty,
and the suggestion "just use the warranty" sounds entirely reasonable.
In practice, using it required paying $12 to $25 in return shipping,
waiting three to six weeks,
and arguing that a failure qualified as a "defect in materials and workmanship"
rather than "normal wear and tear."
(The warranty language was not incidental;
it was written to exclude precisely the kind of failure
that was now designed into the product.)
One customer,
when told their zipper failure was wear and tear,
got quotes of $50 to $100 from local tailors,
then bought a used bag at a thrift store for four dollars rather than a new one.

</div>

Grab, the ride-hailing and delivery platform dominant across eight countries in Southeast Asia,
followed the same trajectory at scale.
It entered markets including Malaysia, Indonesia, Vietnam, Thailand, and the Philippines
with driver incentives and passenger subsidies
that made rides cheaper than local alternatives.
It acquired Uber's Southeast Asian operations in 2018,
eliminating its main competitor outright.
With competition gone,
driver commissions rose and passenger fees increased.
The platform began requiring restaurants and drivers to pay for placement
in its food-delivery and services listings.
The pattern was identical to Booking.com's,
conducted in markets where regulatory capacity to respond was considerably thinner.

Investor dynamics accelerate enshittification.
Platforms in their subsidy phase operate at significant losses,
funded by venture capital in expectation of eventual monopoly returns.
Once the platform achieves dominance,
those investors demand extraction.
Losses during the subsidy phase are booked as investment;
extraction during the harvest phase is booked as profit.
The users who benefited from below-cost service in year one
fund those returns in year ten.

Antitrust enforcement has provided limited relief.
Because acquisitions of potential competitors are evaluated on
whether they raised consumer prices immediately—not
whether they reduced competition structurally—dominant platforms can acquire dozens of rivals
before those rivals threaten their market share.
The result is that enshittification faces no real competitive check:
alternatives are acquired or driven out during the subsidy phase.

Antitrust law in the United States was supposed to prevent this.
Beginning in the 1970s,
however,
it was weakened by a legal school that argued courts should evaluate mergers solely
on whether they reduced consumer welfare in the short run.
Under this standard,
acquisitions of nascent competitors were not anticompetitive
if the acquired company had not yet raised prices.
Platform companies used this framework to acquire dozens of potential competitors
before they could grow large enough to threaten market share.
The current debate over platform regulation is therefore partly a debate about
whether antitrust law should return to its original concern with concentration of power
[Doctorow2025,Shapiro1999].

## Intellectual Property as Invention

Copyright, patent, and trademark are not natural rights:
they are legal instruments invented at specific times to serve specific interests.
The expansion of intellectual property rights over the past forty years was a deliberate political project,
pursued by specific industries,
over the objection of economists who predicted (correctly) that it would harm innovation.
Understanding this history is essential for evaluating current claims
about AI training data, open source licensing, and platform ownership of content created by users.

The Statute of Anne,
enacted in England in 1710,
is generally identified as the first copyright law.
It was not passed to protect authors,
but to end a monopoly held by the London Stationers' Company,
a guild of printers that had controlled the trade in printed books since the sixteenth century,
and to create a new system of publisher monopolies that would operate for limited terms.
Authors received rights in the statute,
but only to the extent that they assigned those rights to publishers,
who were the real beneficiaries of the act.
The framing of copyright as a natural right of creators,
which dominates popular and political discussion today,
was a later construction that reversed the actual historical origin [Bracha2019].

Patent and copyright terms have been extended repeatedly,
almost always to be longer, broader, and allow fewer exceptions.
United States copyright terms have moved from 14 years under the Copyright Act of 1790
to the current life-plus-70 years.
(The 1998 Sonny Bono Copyright Term Extension Act was timed
to prevent the earliest Mickey Mouse films from entering the public domain.)
Patent terms have been less dramatically extended,
but the scope of what is patentable has expanded substantially,
particularly with the rise of software patents.
Each extension was the result of lobbying by specific industries,
over the objections of economists
who consistently argued that the existing terms were already longer than necessary to incentivize creation.

<div class="callout" markdown="1">

Pharmaceutical companies have been extremely effective at shaping intellectual property law globally.
Beginning with the Agreement on Trade-Related Aspects of Intellectual Property Rights (TRIPS) in 1994,
high-income countries required all members of the World Trade Organization
to adopt patent standards that matched or exceeded their own.
Countries that had deliberately excluded pharmaceutical products from patentability
in order to build domestic generic drug industries,
including India, Brazil, and several African countries,
were required to change their laws.
The result was a substantial transfer of rents to pharmaceutical companies operating in rich countries,
and a significant increase in drug prices in countries that could least afford them.

</div>

Software patents are a category of intellectual property right
whose practical operation differs substantially from the stated purpose of the patent system.
The original argument for patents is that they encourage disclosure:
an inventor gets a time-limited monopoly
in exchange for publishing a description of the invention
sufficient to allow others to replicate it after the term expires.
In contrast,
software patents are often written at high levels of abstraction,
covering broad categories of computational method rather than specific implementations.
They are concentrated in the portfolios of large technology companies, financial institutions,
and **patent assertion entities**:
organizations that hold patents without producing anything,
but derive revenue entirely from licensing and litigation.
Software patents are used primarily against smaller companies and open source projects,
which lack the resources to defend extended litigation.

Open source licensing emerged in part as
a response to the expansion of intellectual property rights over software.
The **GNU Public License** (GPL) and its relatives use copyright law against itself:
the license grants broad permissions
that apply only on the condition that derivative works carry the same license,
making it legally difficult to take open source software and close it.
This kind of **copyleft** has only been a partial success:
big tech companies have learned to extract enormous value from open source software
while contributing relatively little back,
because their primary product is not the software but the service running on it
[Doctorow2022,Baldwin2014,Bellos2024].

## Setting the Standard

In May 1886,
American railroads completed the largest coordinated industrial operation the world had ever seen.
Over two days,
work crews across the South pulled up thousands of miles of track
and relaid it three inches closer together,
converting the region's idiosyncratic gauge to match the rest of the country.
The process was planned, organized, and executed in less time than most tech companies take
to schedule a product launch.

The southern railroads had resisted this change for decades
because the incompatibility was not an accident.
Different gauges meant that northern rolling stock could not run on southern track,
so freight crossing a gauge boundary had to be unloaded, transferred, and reloaded.
Every cargo shipment lost time and money at the border,
and that money went to the carriers who controlled the boundary.
The technical choice was a market weapon.

A **technical standard** is an agreement about how things connect.
The value of having a standard usually far exceeds
the value of any particular outcome in the format war that precedes it,
which is exactly why control of the format is worth fighting for.

Thomas Edison understood this in the 1880s,
when he and George Westinghouse fought over whether the United States would run on direct or alternating current.
Edison had bet on DC infrastructure and stood to lose if AC won,
so he electrocuted animals at exhibitions
and lobbied for AC to be used in the first electric chair,
hoping to fix the association of alternating current with execution in the public mind.
None of this changed the underlying physics, though;
AC transmits over longer distances at lower cost,
and Westinghouse won.

A century later,
Microsoft repeatedly used **standards capture** as a business strategy.
The company would adopt an open standard like HTML, Java, or Kerberos authentication,
and then add proprietary extensions that were convenient but tied developers to Microsoft's version.
Once enough code was written against the extensions,
**interoperability** with non-Microsoft systems degraded.
The strategy had a name inside the company: embrace, extend, extinguish [Russell2014].
(The "extinguish" referred to both the open standard and Microsoft's competitors.)

Google's Accelerated Mobile Pages, launched in 2015,
was presented as an open standard for fast-loading mobile web pages.
To receive preferential treatment in Google's mobile search results,
however,
pages had to be hosted on Google's own servers and delivered through Google's infrastructure.
Publishers who adopted AMP handed Google control over their content delivery
in exchange for a favorable page rank.
Google eventually backed away from the hosting requirement,
but only under regulatory pressure.

Apple took a different approach.
Rather than capturing an open standard, it simply refused to implement one.
RCS is a modern successor to SMS that supports end-to-end encryption,
read receipts,
high-resolution media,
and group chat.
For years after Android phones had adopted it,
Apple kept cross-platform messaging on unencrypted SMS,
so messages between iPhones and Android phones appeared as green bubbles.
Internal documents revealed in US antitrust litigation showed Apple executives explicitly acknowledging
that adopting RCS would reduce the social cost of switching from iPhone to Android,
particularly for teenagers for whom the green-bubble distinction had become a social marker.
The EU's Digital Markets Act eventually compelled Apple to support RCS in 2024.

When a technology becomes embedded in a formal standard,
the patent holder typically commits to license it on **FRAND** terms:
fair, reasonable, and non-discriminatory.
This sounds reassuring,
but the word "reasonable" has funded decades of litigation.
Qualcomm's licensing practices for mobile baseband patents
(the technology that connects a phone to a cellular network)
were subject to antitrust proceedings simultaneously in the United States, Europe, South Korea, China,
and Taiwan in the late 2010s.
The core allegation was consistent across jurisdictions:
Qualcomm was using its position as the patent holder
o charge fees that bore no relationship to any recognizable interpretation of "reasonable."
The legal outcomes varied by country;
Qualcomm remained profitable throughout.

<div class="callout" markdown="1">

During the browser wars of the late 1990s,
Microsoft bundled Internet Explorer with Windows,
deliberately undercutting Netscape's business model.
IE's market dominance then allowed Microsoft to implement proprietary HTML extensions
that worked only in its browser.
What finally broke this cycle was not antitrust action—which produced a consent decree
and little structural change—but the arrival of Firefox and then Chrome,
backed by organizations with different incentives.

</div>

If you are a developer building a product,
every choice between an open standard and a proprietary API is
a bet on the future behavior of the platform that owns the API.
History suggests the bet is a bad one.
From Instagram's third-party API and Twitter/X's developer API
to Google Reader and Firebase's original pricing structure,
platforms have repeatedly changed terms after developers are so invested that they can't walk away.
Each time,
the platform points to its terms of service,
which always reserves the right to change.

The structural remedy for this is interoperability mandates:
legal requirements that platforms accept connections from competing services
on terms that do not depend on the platform's goodwill.
Phone number portability,
which required carriers to let customers keep their numbers when switching providers,
eliminated one of the most effective lock-in mechanisms in telecoms.
Messaging interoperability requirements in the EU's Digital Markets Act
are attempting to do the same thing for social platforms.
Whether they succeed depends on implementation details that are actively contested,
and on enforcement that companies have historically resisted every way they can
[Shapiro1999,Wu2010].

## Public Subsidy, Private Profit

When Steve Jobs unveiled the iPhone in January 2007,
the crowd responded as if Apple had conjured something from nothing.
What neither Jobs nor the press mentioned was that
every technology in that device had been developed with government money.
The internet it connected to had been built by the Defense Advanced Research Projects Agency.
The GPS it used had been developed and maintained by the US Air Force,
which had turned off the deliberate signal degradation for civilian users only seven years earlier.
Its touchscreen came from research supported by the National Science Foundation,
which Apple had acquired by buying a small company called FingerWorks in 2005.
Siri, added to the iPhone 4S in 2011, had started as a DARPA-funded project at SRI International.
The government took the risk;
the investors who held Apple stock reaped the benefits.

This pattern is not unique to Apple.
The internet began as ARPANET, a network funded by the Department of Defense from 1969
to connect university research computers.
The initial packet-switching protocols,
the domain name system,
and the basic architecture of what became the web
were all developed in publicly funded laboratories and universities.
The commercial internet of the 1990s built on this foundation without paying for it.
The browser itself emerged from the National Center for Supercomputing Applications,
funded by the National Science Foundation.
Mosaic was not a startup product:
It was a research project paid for by American taxpayers.

The drug industry runs the same arrangement at enormous scale.
The National Institutes of Health spends roughly $47 billion annually on biomedical research.
Much of this money funds the basic science
that pharmaceutical companies would not fund themselves because the returns are too distant and uncertain.
When that basic science produces a promising compound,
private companies license it, conduct clinical trials, and patent the result.
The public paid for the underlying knowledge.
The private company captures the patent and sets the price.
Unlike every other wealthy country.
the United States has no legal mechanism to negotiate that price.
As a result,
insulin costs American patients ten times what Canadians pay.

<div class="callout" markdown="1">

The mRNA vaccine platform that produced the Pfizer-BioNTech and Moderna COVID-19 vaccines
illustrates this dynamic precisely.
The fundamental science of mRNA delivery
was developed over decades by Katalin Karikó and Drew Weissman at the University of Pennsylvania,
supported by the National Institutes of Health.
When COVID-19 hit,
the US government funded the clinical trials and pre-purchased hundreds of millions of doses
before any vaccine had received authorization.
The government provided the science, the capital, and the guaranteed market.
Moderna became a $200 billion company,
and its executives became very rich.
The NIH's claim to a share of the intellectual property—which
would have given the government some leverage over pricing—was
disputed by Moderna and ultimately not enforced.

</div>

The economist Mariana Mazzucato has called this arrangement
the privatization of gains and the socialization of losses.
Her argument is not that private companies add no value:
they obviously do, in manufacturing, distribution, and application.
Her argument is that
the standard story of heroic private entrepreneurs taking risks that timid governments would never accept
inverts the actual history.
Governments took the foundational risks
by funding research that might produce nothing,
maintaining infrastructure that would not attract private capital,
and training the scientists and engineers that firms would later hire.
Technology transfer moves the results into private hands,
almost always at prices that dramatically undervalue the public's investment
[Mazzucato2013].

The tech companies that have benefited most from publicly funded research
are also among the most sophisticated users of international tax structures
designed to minimize what they pay back into the public systems that enabled them.
Apple's arrangements in Ireland,
described in a 2016 European Commission ruling,
allowed the company to pay an effective tax rate of 0.005% on European profits.
Over and over,
public investment creates the technology,
private firms capture the profits,
and international tax structures ensure that
only a tiny fraction of those profits flow back into the public budget.
The cycle is effectively a permanent subsidy.

The arrangement looks different in Europe,
partly because European governments built in mechanisms that Americans left out.
Germany's Fraunhofer-Gesellschaft,
a network of applied research institutes funded jointly by the federal government,
state governments,
and industry,
licenses its discoveries under terms that return revenue to the institutes themselves
rather than transferring intellectual property to private buyers at knockdown prices.
The European Medicines Agency negotiates drug prices on behalf of member states,
which is why the same cancer drugs that cost American patients six figures a year
cost Germans and French patients a fraction of that.
When Moderna tried to sell COVID-19 vaccines to the European Union,
EU negotiators paid roughly half the per-dose price that American buyers paid,
for the same product developed with the same publicly funded science.
The European model still lets private firms profit substantially from public investment.
What it does not do is treat the transfer as a gift.

China has taken a third path that makes the American arrangement look like an oversight rather than a design.
Programs like Made in China 2025, announced in 2015,
identify strategic industries like semiconductors, electric vehicles, robotics, and artificial intelligence,
and pour in state capital with the explicit goal of domestic ownership of the results,
not just the benefits.
Companies like CATL,
which now supplies roughly a third of the world's electric vehicle batteries,
grew to global scale with protected home markets and state-backed financing before competing internationally.
The distinction between public and private in this system is deliberately blurry:
the government can require access to technology developed with state support,
block the international transfer of profits,
and redirect corporate strategy in ways that American or European regulators legally cannot.
This does solve the problem Mazzucato describes,
since the state that takes the foundational risk never fully loses its claim on the result.
It creates a different problem, though:
accountability runs upward to the Communist Party rather than outward to citizens,
and the line between a national champion and an instrument of state policy
disappears entirely [Acemoglu2023,Chang2012,Webber2011].
