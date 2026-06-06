---
title: "Setting the Standard"
date: 2026-05-20
category: sdgc ethics
---

In May 1886,
American railroads completed the largest coordinated industrial operation the country had seen.
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

A technical standard is an agreement about how things connect.
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
Microsoft repeatedly used standards capture as a business strategy.
The company would adopt an open standard like HTML, Java, or Kerberos,
and then add proprietary extensions that were convenient but tied developers to Microsoft's version.
Once enough code was written against the extensions,
interoperability with non-Microsoft systems degraded.
The strategy had a name inside the company: embrace, extend, extinguish.
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
the patent holder typically commits to license it on FRAND terms:
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

The structural remedy for this is  interoperability mandates:
legal requirements that platforms accept connections from competing services
on terms that do not depend on the platform's goodwill.
Phone number portability,
which required carriers to let customers keep their numbers when switching providers,
eliminated one of the most effective lock-in mechanisms in telecoms.
Messaging interoperability requirements in the EU's Digital Markets Act
are attempting to do the same thing for social platforms.
Whether they succeed depends on implementation details that are actively contested,
and on enforcement that companies have historically resisted every way they can.

*[see the whole series](@root/sdgc/) · [email me](mailto:gvwilson@third-bit.com?subject=SDGC)*

<span id="Russell2014">Russell2014</span>
:   Andrew L. Russell:
    *Open Standards and the Digital Age: History, Ideology and Networks*.
    Cambridge University Press,
    2014,
    [9781107612044](https://isbnsearch.org/isbn/9781107612044).

<span id="Shapiro1999">Shapiro1999</span>
:   Carl Shapiro and Hal R. Varian:
    *Information Rules: A Strategic Guide to the Network Economy*.
    Harvard Business School Press,
    1999,
    [9780875848631](https://isbnsearch.org/isbn/9780875848631).

<span id="Wu2010">Wu2010</span>
:   Tim Wu:
    *The Master Switch: The Rise and Fall of Information Empires*.
    Knopf,
    2011,
    [9780307390998](https://isbnsearch.org/isbn/9780307390998).
