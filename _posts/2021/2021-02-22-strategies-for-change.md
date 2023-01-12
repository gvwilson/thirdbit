---
title: "Strategies for Change"
date: 2021-02-22
year: 2021
---

I've written before
about Henderson et al's work on theories of change in education,
and a recent conversation made me wonder if anyone had built a similar theoretical basis
for adoption of new software development practices.
This diagram from [Borrego & Henderson 2014](https://onlinelibrary.wiley.com/doi/abs/10.1002/jee.20040)
sums up the kind of model I'm looking for:

<div align="central">
<img src="{{ '/files/2021/borrego-henderson-change-strategies.svg' | relative_url }}" alt="Borrego & Henderson change strategies" />
</div>

I think the categories translate pretty directly to tech:
in the upper left we can teach people new coding practices directly,
in the lower left we can change policies to require evidence of the use of continuous integration and unit testing,
and so on.
What would be equally interesting would be a theory of *resistance* to change,
or more generously,
studies of why developers *don't* adopt better practices
even when research has proven their value.
For that,
I would look to work such as [Barker et al 2015](https://dl.acm.org/doi/10.1145/2676723.2677282),
which explored several related issues:

How do faculty hear about practices?
:   They are motivated to solve a problem;
    they become aware through funded and institutional initiatives;
    they bump into new ideas at conferences;
    they learn from colleagues;
    or (in many cases) they simply don't find out.

Why do faculty try out practices?
:   Sometimes their institutions encourage or require it
    (though there is often a tension between this and getting research done);
    they do an ad hoc cost-benefit analysis;
    or they are influenced by role models or other trusted sources or colleagues.
    There is often a tension between pedagogical innovation and covering the required material,
    and physical classroom layout can either help or hinder efforts;
    unfortunately,
    "Despite being researchers themselves,
    the CS faculty we spoke to for the most part did not believe
    that results from educational studies were credible reasons to try out teaching practices."
    This echoes what Herckis has found,
    and part of the explanation is that
    [people are afraid of looking stupid](https://www.insidehighered.com/news/2017/07/06/anthropologist-studies-why-professors-dont-adopt-innovative-teaching-methods).

Why do faculty keep using practices?
:   "Perhaps the single strongest kind of evidence that supports a decision to routinize practices was student feedback."
    Requirements from funders and faculty buy-in are also important,
    but "do the students like it?" (or "will they put up with it?") is clearly the most important factor.

Once again,
I think many of these ideas translate pretty directly to adoption of better software development practices.
But that doesn't mean such a translation would be correct:
plausible analogies often turn out to be wrong,
so I hope one day to see studies like these replicated in software engineering.
If you're doing this or know someone who is,
I'd be grateful if you'd reach out.
