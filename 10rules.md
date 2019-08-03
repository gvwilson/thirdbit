---
layout: default
permalink: /10rules/
title: "Ten Simple Rules"
---

# Ten Simple Rules

I've collaborated on a handful of papers that give practical tips on building research software and teaching others how to do it,
all of which are available online:

-   [Best Practices for Scientific Computing](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)
-   [Good Enough Practices in Scientific Computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)
-   [Ten Simple Rules for Making Research Software More Robust](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005412)
-   [Ten Simple Rules for Collaborative Lesson Development](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005963)
-   [Ten Quick Tips for Teaching Programming](https://journals.plos.org/ploscompbiol/article/authors?id=10.1371/journal.pcbi.1006023)
-   [Ten Quick Tips for Creating an Effective Lesson](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006915)
-   [Ten Quick Tips for Delivering Programming Lessons](https://github.com/gvwilson/10-deliver/) (in development)
-   [Ten Simple Rules for Helping Newcomers Become Contributors to Open Source Projects](https://github.com/gvwilson/10-newcomers) (in development)

I also have some shorter sets of guidelines for:

-   [...Teaching](#teaching)
-   [...Being a Good Research Partner](#being-a-good-research-partner)
-   [...Talking People Into Things](#talking-people-into-things)
-   [...Handing Over and Moving On](#handing-over-and-moving-on)

---

## ...Teaching

See *[Teaching Tech Together][t3]* for a much longer discussion.

1.  Be kind: all else is details.
1.  Remember that you are not your learners...
1.  ...that most people would rather fail than change...
1.  ...and that ninety percent of magic consists of knowing one extra thing.
1.  Never teach alone.
1.  Never hesitate to sacrifice truth for clarity.
1.  Make every mistake a lesson.
1.  Remember that no lesson survives first contact with learners...
1.  ...that every lesson is too short from the teacher's point of view and too long from the learner's...
1.  ...and that nobody will be more excited about the lesson than you are.

[t3]: http://teachtogether.tech

---

## ...Being a Good Research Partner

Data scientists often have to bridge the divide between academic research and
commercial practice.  The ten simple rules listed below may help mitigate the
frustration you encounter as you try to o this.

### If you are a researcher in academia...

**1. Remember that companies work in weeks, not seasons.**

Academic semesters are rooted in the seasons of an agricultural era, but
practitioners in industry have to work at a more accelerated pace. In the time
it takes you to write a grant, a company might develop and release two new
versions of their product in order to keep up with their competition. Discuss
timescales with your industrial research partners early on, and be realistic
about how slowly things will proceed.

**2. Be open.**

Research is of no use to practitioners who cannot easily find it and read
it. While Jimmy Wales (the founder of Wikipedia) may not actually have said,
"Open information drives out closed," the principle holds: with so much
information freely available on the Internet, any paywall or login barrier put
between you and your hoped-for audience will send a large number of people
elsewhere.

More importantly, these barriers send a clear signal that you do not care if
practitioners read your work or not: as one colleague observed rather sourly,
it's the equivalent of inviting people to your house for dinner and then
expecting them to pay for the drinks.

**3. Value action over insight.**

The goal for practitioners is not to understand the world, but to change it. "We
know X" is much less useful to them than "we can do Y". When presenting your
findings, you should therefore focus on how someone might act on it.

One way to do this is to add slides titled, "What Difference Does It Make?" at
strategic points in your presentations. If you can't think of what to write
next, you may want to rethink what you're focused on.

**4. Don't hesitate to sacrifice detail for clarity.**

Understanding doesn't have to be complete in order to be actionable. For
example, atoms aren't actually little colored balls connected by springs, but
that's still a useful model in organic chemistry. You may need to hedge
conclusions with qualifiers in order to get your work past Reviewer #3, but
those "maybes" and "howevers" can often be omitted if they don't change what
practitioners should try next.

**5. Apologize in advance for the state of academic publishing.**

Modern academic publishing isn't actually a conspiracy by a handful of large
companies to line their pockets with government money that could and should be
used to lift researchers out of penury, but it is functionally indistinguishable
from a system that was. The best way to prepare your industry partners for its
Kafkaesque production pipelines and interminable delays is to have them watch
Gilliam's *Brazil*.

### If you are a practitioner in industry...

**6. Remember that universities work in seasons, not weeks.**

The timescale mis-match decribed in Rule #1 is due in part to the fact that
academic researchers are almost always multi-tasking, and that many of those
tasks are things they've never been trained to do. As students, they juggle
several courses at once (which effectively means that they answer to several
bosses who don't communicate with each other). Later, they are responsible for
teaching, writing grant proposals, and administrative duties.

Collectively, this mean that their "work week" is only a few hours long, and
that they will often appear to move at a snail's pace. Be as sympathetic as you
can: they are even less happy with the situation than you are.

**7. Remember that academic success is measured in publications, not sales.**

University presidents routinely make about the economic value of research, but
the only things that truly matter for academic advancement are publication,
publication, and publication. Researchers are not given grants or tenure for
doing things that are "merely useful", even if doing so requires a deep
understanding of subtle complexities and months of hard work. For all the jokes
practitioners make about the ivory tower, academic life is hard, uncertain, and
poorly paid. People stay in it for the love of new knowledge; respecting their
priorities is essential to building a productive relationship. (That said,
practical problems often do unlock the door to genuinely new research topics by
pushing researchers out of their comfort zone.)

**8. Do the background reading.**

H.L. Mencken once wrote that, "There is always a well-known solution to every
human problem---neat, plausible, and wrong." Your problem is almost certainly
one of those, and is almost certainly more complex than you first realize. While
Rule #4 tells researchers to sacrifice detail for clarity, this rule asks
practitioners to make an effort to grasp at least some of that detail so that
you don't waste time reinventing wheels and so that your research partner can
think, work, and talk at full speed.

**9. Don't overstate what has been learned.**

This rule is also a complement to Rule #4. The "maybes" and "howevers" that
researchers are so fond of do sometimes matter; if your research partner has
found that regular doses of a new drug seems to slow tumor growth in lab rats,
do not embarrass them by claiming that they have discovered a cure for cancer.

### If you are either...

**10. Apologize in advance for the state of your data.**

The final rule applies equally to both researchers and practitioners. Files'
names and locations, the meanings of column headers in tables, how those tables
relate to one another, how missing values are represented and handles:
everything that has made sense to you for years will suddenly seem a little
foolish when you have to explain it to someone else. Apologize in advance, and
then forgive yourself, because no matter how bad your data is, theirs may well
be worse.

An old proverb says, "If you want to go fast, go alone; if you want to go far,
go together."  In my experience, this is wrong: going alone is good for a fast
start, but after that, both speed and distance come from having partners.
Researchers and practitioners can each do great things on their own, but both
are better able to solve big problems---problems that really matter---if they
find ways to work together.

---

## ...Talking People Into Things

I don't always exhibit good judgment, but I *am* pretty good at talking people
into things.  Here are ten simple rules for doing it that I hope you will only
use for good.

**1. Don't.**

If you have to talk someone into something, odds are that they don't really want
to do it.  Respect that: it's almost always better in the long run to leave some
particular thing undone than to use guilt or any underhanded psychological
tricks that will only engender resentment.

**2. Be kind.**

I don't know if there actually is a book called "Secret Tricks of the Ninja
Sales Masters", but if there is, it probably tells readers that doing something
for a potential customer creates a sense of obligation, which in turn increases
the odds of a sale.  That may work, but (a) it only works once and (b) it's a
skeezy thing to do.  If, on the other hand, you are genuinely kind, and help
other people because it's what good people do, you just might inspire them to be
good people too.

**3. Appeal to the greater good.**

If you open by talking about what's in it for them, you are signalling that they
should think of their interaction with you as a commercial exchange of value to
be bargained over.  Instead, start by explaining how whatever you want them to
help with is going to make the world a better place, and *mean it*.  (If what
you're proposing *isn't* going to make the world a better place, propose
something better.)

**4. Start small.**

Most people are understandably reluctant to dive into things head-first, so give
them a chance to test the waters and to get to know you and everyone else
involved in whatever it is you want help with.  Don't be surprised or
disappointed if that's where things end: everyone is busy or tired or has
projects of their own, or maybe just has a different mental model of how
collaboration is supposed to work.  Remember the 90-9-1 rule (90% of people will
watch, 9% will speak up, and 1% will actually do things) and set your
expectations accordingly.

**5. Don't build a project: build a community.**

I used to belong to a baseball team that never actually played baseball: our
"games" were just an excuse for us to hang out and enjoy each other's company.
If you actually want to accomplish something, you probably don't want to go
quite that far, but sharing a cup of tea with someone or celebrating the birth
of their first grandchild can get you things that no reasonable amount of money
can.

**6. Establish a point of connection.**

"I was speaking to X" or "we met at Y" gives them context, which in turn makes
them more comfortable.  This must be specific: spammers and cold-callers have
trained us all to ignore anything that starts, "I recently came across your
website".

**7. Be specific about what you are asking for.**

People need to know this so that they can figure out whether the time and skills
they have are a match for what you need.  Being realistic up front is also a
sign of respect: if you tell people you need a hand moving a few boxes when
you're actually packing up an entire house, they're probably not going to come
back.

**8. Establish your credibility.**

Mention your backers, your size, how long your group has been around, or
something that you've accomplished in the past so that they'll believe you're
worth taking seriously.

**9. Create a slight sense of urgency.**

"We're hoping to launch this in the spring" is more likely to get a positive
response than "We'd eventually like to launch this."  However, the word "slight"
is also important: if your request is urgent, most people will assume you're
disorganized or that something has gone wrong, and may then err on the side of
prudence.

**10. Take a hint.**

If the first person you ask for help says "no", ask someone else.  If the fifth
or the tenth person says "no", ask yourself if what you're trying to do makes
sense and is worth doing.

---

## ...Handing Over and Moving On

This advice is for founders who are handing on their projects;
see [my CarpentryCon 2018 talk](https://www.youtube.com/watch?v=7xR50ty5DZ0) for more detail.

**1. Be sure you mean it.**

Letting go will be hard on you, but not letting go will be even harder on your
successors, so be sure you're actually going to let go.

**2. Do it when other people think you should.**

Just as you are the last person to realize when you're too tired to be coding,
you will often be the last person to realize that you ought to be moving on, so
ask people and pay attention to what they say.

**3. Be open about what, when, and why.**

Tell people that you're leaving and what the succession plan is as soon as
possible (which in practice means "as soon as you think you won't have to revise
what you have said publicly").

**4. Leave for something.**

People who start things usually aren't good with idleness, and idleness tends
not to be good for them, so when you leave, leave *for* something, even if it's
something small.

**5. Don't choose your successor on your own.**

You may have strong opinions about who should succeed you, but you should still
check those opinions with someone more objective.

**6. Train your successor.**

Share tasks with your successor for a few days or weeks: they will get to see
how things actually work, and you'll discover things you would otherwise forget
to tell them.  Go on holiday for a week and leave your successor temporarily in
charge.  You'll discover even more things you would otherwise forget to pass on.

**7. Celebrate.**

Many people are uncomfortable being praised, but give the organization a chance
to celebrate what you accomplished and thank you for it.

**8. Leave.**

It may be tempting to continue to have a role in the organization, but that
usually leads to confusion, since people are used to looking to you for answers.
It will be easier for your successor, particularly if they weren't a founder as
well, but the best thing you can do to help them is to find something else to do
for a year.

**9. Learn from your mistakes.**

Whatever you have left will almost certainly not be the last thing you ever do.
Take some time to think about what you could have done differently, write it
down, and then move on: obsessing over only-ifs and might-have-beens won't help
anyone.

**10. Do something before you go.**

Everything comes to an end, but you have time before then to do something.  What
are you waiting for?
