---
title: Resilience Advice
date: 2025-03-12
---

I wish we didn't have to talk about this,
but given the Trump administration's brutal assault on science
and its equally brutal bullying of scientists,
we need to start making plans.
What happens if they come for you, your research, and your data?
What happens if Nadella doesn't kiss ass hard enough or fast enough
and Musk gets a judge to restrict access to GitHub?
(It wouldn't be hard:
find a repository with some DEI-related content or copyrighted material and say,
"Turn it off until everything can be reviewed.")

I wish there were more training programs like [this one][mitchell-ford].
Until there are,
here are my thoughts on what you can do:

1.  Accept that the threat is both real and random.
    -   There's a continuum of risk, but everyone scientist in the US is now a potential target.
        -   As with censorship, the turmoil is the point: hurt a few to frighten the rest into acquiescence.
    -   And the damage might spread:
        Canada's previous Conservative prime minister [muzzled scientists][harper-muzzle],
        and the current Conservative leader will undoubtedly go further if he wins the upcoming election.
    -   Remember, nobody at the Climate Research Unit thought they were might be a target until [Climategate][climategate] happened.
1.  Threat models (taken from [this paper][plos] with modifications):
    -   Casual threat ("drive by"): opportunistic but not determined (but see "institutional threat" below).
    -   Intimate threat: a life partner (not a big one for this conversation).
    -   Insider threat: "inside the fortress" (i.e., the departmental sys admin is a DOGE appointee or MAGA sympathizer).
    -   Institutional threat: the rules change and now you're a target: this was loony tunes two months ago and is now our reality.
1.  Recognize that getting people to adopt secure habits is as hard as getting people to practice safe sex was in the 1980s.
    -   "Security theatre" on the part of institutions is a big part of the problem.
    -   "We will send your performance review as a Word document" practically trains people to be unsafe.
    -   Programmers have made security needlessly painful.
        -   ["Why Johnny Can't Encrypt"][johnny] was published a quarter of a century ago and nothing has gotten easier.
1.  Immediate actions (in order):
    1.  Don't open that attachment, install that software, or click on that link without checking.
        -   Or talk to the "journalist" who just cold-called you without verifying their credentials.
    1.  Put open licenses on everything you can, make sure colleagues have copies, and [copy their data and code][sciop] return.
        -   This isn't just about human threats: talk to anyone who lost work because of Hurricane Katrina.
    1.  Use a password manager (I recommend [1Password][1password]),
        two-factor authentication,
        and [Signal][signal] (it's the only trustworthy messaging app out there).
    1.  Identify services you could migrate to,
        e.g., [Sync][sync] (hosted in Canada) and [Whereby][whereby] (in Norway) instead of Dropbox and Zoom (US).
    1.  Ask (require) IT to make "what if" plans *and test them out*.
        -   E.g., make nightly backups of your GitHub issues (which aren't stored in the Git repositories),
	    your Slack conversations,
	    and everything in your Google Drive.
    1.  Lobby your professional association to put policies and plans in place *and enforce them*.
        -   The Royal Society's decision not to expel Musk was as shortsighted as it was cowardly.

And now a request:
if you are taking steps like these right now,
I would be very grateful if you could [share your experience][email]
(or better yet, a checklist of what you've done that other people could do).
I'm not looking for "we could X", "you should Y", or "maybe it's time to think about Z",
but rather a list of what you've done and what you're doing.

[1password]: https://1password.com/
[climategate]: https://en.wikipedia.org/wiki/Climatic_Research_Unit_email_controversy
[email]: mailto:gvwilson@third-bit.com
[harper-muzzle]: https://www.cbc.ca/news/health/second-opinion-scientists-muzzled-1.4588913
[johnny]: https://dl.acm.org/doi/10.5555/1251421.1251435
[mitchell-ford]: https://www.fordfoundation.org/work/learning/learning-reflections/keeping-those-on-the-front-lines-of-change-safe-five-years-of-the-ford-foundation-grantee-safety-program/
[plos]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008563
[sciop]: https://sciop.net/datasets/
[signal]: https://signal.org/
[sync]: https://www.sync.com/
[whereby]: https://whereby.com/
