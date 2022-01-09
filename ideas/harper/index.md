---
title: "Harper-Lite: Simple Lesson Discovery and Aggregation"
layout: page
---

[Harper][harper]'s goal is better learning outcomes with less effort;
Harper-Lite's is to get the ball rolling with as little effort as possible.
Its design principles are:

1.  Instead of building another repository or portal,
    we will make it easier for teachers to make their lessons findable,
    then aggregate the information they give us.
2.  We will use tagging, voting, and direct online annotation
    to provide feedback to lesson creators.
3.  We will assume that people are going to adapt and remix material
    instead of using it as-is.
4.  We will not require people to be technically sophisticated
    in order to comment, contribute, and collaborate.

## Background

Harper's design is shaped by:

-   The success of RSS for decentralized content syndication.
-   Mike Caulfield's analysis of [Stack Overflow][stack]
    in terms of [choral explanations][choral-explanations].
-   [This list][oer-landmines] of what has been learned from previous open educational resource (OER) projects.

Please see [this page][harper] for the full proposal.
The project is named after [William Rainey Harper][harper-william],
first president of the University of Chicago,
who encouraged universities to offer distance education courses in the 1890s.
"Harper" also happens to be the name of my youngest niece.

I'm grateful to
Mike Caulfield,
Mine Çetinkaya-Rundel,
Neal Davis,
Garrett Grolemund,
Alison Hill,
Alyson Indrunas,
François Michonneau,
Bracken Mosbacker,
Nick Radcliffe,
Raniere Silva,
Alasdair Smith,
Jon Udell,
and David Wiley
for comments,
and to Peter Quill for show us that
[you only need twelve percent of a plan][guardians-video] to save the galaxy.

## Proposal

To make a lesson easier to find and re-use,
authors create one extra text file called `harper.yml` and put it in the lesson's root directory.
This single-file convention is inspired by the `feed.xml` and `feed.rss` files used for blogging,
and by the `README.md` and `LICENSE.md` files now commonly used in software projects;
we use the name `harper.md` because Alasdair Smith pointed out that
some systems use `lesson.md` for the actual content of the lesson.

`harper.yml` is formatted as YAML and must contain all of the fields shown below:

```
schema: "harper-lite 0.1"
title: "The Title of the Lesson"
url: https://where.to.find/lesson
abstract: >
  A single-paragraph summary of the lesson, the shorter the better.
  It can be broken across multiple lines as shown here, and can
  use [Markdown](https://en.wikipedia.org/wiki/Markdown) formatting.
version: "1.3"
contributor:
  - "Some Name <email@address>"
  - "Another Name <their@address>"
package: http://package.url/lesson.zip
license: http://license.url/
requirements:
  some_technology:
  - "package_1"
  - "package_2>=1.2.3.4"
objectives:
  - "A short sentence."
  - "Another short sentence."
pre:
  - "[A pre-requisite concept](https://simple.wikipedia.org/wiki/some-key)"
  - "[A pre-requisite skill](https://glosario.carpentries.org/some-other-key)"
post:
  - "[An outcome concept](https://glosario.carpentries.org/some-key)"
  - "[An outcome skill](https://simple.wikipedia.org/wiki/some-other-key)"
notes: >
  One or more sentences describing things instructors ought to know, formatted with Markdown.
  For example, the notes could explain how long the lesson usually takes to do.
```

**Notes:**

-   The `schema` field identifies this as Harper-Lite Version 0.1.

-   The `title` and `abstract` fields should be self-explanatory.

-   The `version` field is the version of the lesson (typically also the version of the package it's for).

-   Contributors do not need to provide email addresses.

-   The `license` value is the URL of the license rather than an abbreviation.
    We will strongly encourage people to point to licenses at <https://opensource.org/>.

-   The `package` field is the URL for the downloadable lesson materials.

-   `requirements` specifies any packages required,
    organized under one sub-key per language,
    using the syntax preferred by that language's default package manager.

-   Learning objectives should be single sentences, each with an active verb,
    describing something
    [specific, measurable, attainable, relevant, and time-bound](https://ii.library.jhu.edu/2016/07/20/writing-effective-learning-objectives/).

-   The `pre` field is a list of terms or skills the lesson requires learners to have;
    the `post` field is a list of terms or skills the lesson teaches.
    (We use these names to avoid collision with `requirements`, which here means "software requirements").
    The items under these keys should be keywords, not full explanations;
    where possible,
    they should link to something like [Wikipedia](https://simple.wikipedia.org/)
    or [Glosario](https://glosario.carpentries.org/)
    to optimize search and help people stitch lessons together
    (e.g., "The lesson I want requires X---where can I learn about it?").

-   `notes` is for anything else that might be helpful.

An example of a Harper file is shown below;

```
schema: "harper-lite 0.1"
title: "Tests of Univariate Normality"
abstract: >
  How can we tell if univariate data is normally distributed?
  This lesson describes two tests and explains the strengths and weaknesses of each.
version: "1.3.1"
contributor:
  - "Walter Bishop <w.bishop@fringe.tv>"
package: http://stats.fringe.tv/stats454/normality/stats454-normality.zip
license: https://creativecommons.org/licenses/by-nc/4.0/
requirements:
  R:
  - "nickr (>=1.2.3.4)"
objectives:
  - "Describe the 68-95-99.7 rule and explain why it works and when it fails."
  - "Describe and apply the Shapiro-Wilk test for normality of univariate data."
pre:
  - "[Normal distribution](https://simple.wikipedia.org/wiki/Normal_distribution)"
  - "[Quantiles](https://glosario.carpentries.org/en/#quantile)"
  - "[Statistical power](https://en.wikipedia.org/wiki/Power_of_a_test)"
  - "Install R package"
post:
  - "[68/95/99.7 rule](https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule)"
  - "[Shapiro-Wilk test](https://en.wikipedia.org/wiki/Shapiro%E2%80%93Wilk_test)"
  - "`quantile` function in R"
notes: >
  This material was originally developed as part of a sequence on data integrity
  for seniors and graduate students in statistics, then modified for delivery in
  conference workshops.  The Shapiro-Wilk material  has only been used a couple
  of times, and probably needs more work.
```

## Usage

Harper supports collaboration with a voting mechanism like [Stack Overflow][stack]'s,
using subject headings drawn from lessons as terms:

1.  An author registers a lesson by providing the URL to its Harper file,
    just as someone can register a blog by providing a URL to an aggregator.

2.  The site extracts data from the file and displays the lesson under each of `teaches` headings
    to make it easier to find.

3.  When someone views the page for a keyword,
    they can provide comments on the lessons that appear there and upvote or downvote them.
    This means that a single lesson could appear as the top "answer" for one keyword and the third "answer" to another.

4.  We will provide an interactive upload mode:
    after providing a URL for a lesson,
    the author is walked through a very simple online form that asks for the information that goes in the lesson's Harper file.
    We save that information and give it back to them to download and add to the lesson.
    We still require that the Harper file be in the lesson's root directory as a check on authenticity:
    allowing person X to describe a lesson created by person Y opens up too many opportunities for abuse.

## Scenarios

### How does an instructor find a lesson?

1. She does a DuckDuckGo search for the word "lesson" and the keywords she's interested in.
   If we've done our job right,
   the lessons indexed by our site show up near the top of her search,
   just as Stack Overflow answers show up near the top of a search for a technical question.
2. She comes to our site and does a targeted search for her keywords.

### How does an author register a lesson?

1. They create a directory on their website with a meaningful name that includes a Harper file
   and possibly a zip file containing starter materials (if the lesson's exercises need any).
2. They sign into their account on our site and register the URL of the lesson directory.
3. Our site validates their Harper file.

As noted above,
we don't allow people to register lessons that they don't control,
i.e.,
they have to be able to add `harper.md` to the lesson's website in order for us to accept the registration.

Critically,
our site does some fuzzy matching to suggest rewording of terms
to match ones in lessons that are already registered.
The term "[folksonomy][folksonomy]" seems to have lost its luster,
but encouraging convergence on a shared vocabulary seems crucial to making all of this work.

### How does someone ask for a lesson?

Rather than waiting for people to register their own lessons,
we provide a "please register this" workflow:

1.  Jeanne stumbles across a lesson she finds interesting.

2.  She checks if there's a record of it.

3.  If there isn't,
    but someone before her has expressed an interest,
    we add one to the "wanna have" count in our database.

4.  If there isn't any record in our database,
    we scrape the site to get contact info for the lesson's author, Vlad.
    We then send Vlad a single message saying, "Hey, someone's interested in your lesson."

5.  Vlad will probably ignore the message,
    but if he responds by creating a record for his lesson,
    we stash that so that future inquiries will resolve
    and notify Jeanne that the record is now available.
    This workflow serves the triple purpose of attracting more authors,
    not spamming them,
    and ensuring that the record for a lesson comes from someone identified in the lesson's content
    (i.e., probably not a disgruntled former student).

### How does an author update a lesson?

1.  They sign into their account,
    go to "My Lessons",
    and push the "update" button next to the lesson in question.

Note that we archive past Harper files but not the actual lesson content.
(We're an index not a repository.)

[choral-explanations]: https://hapgood.us/2016/05/13/choral-explanations/
[folksonomy]: https://en.wikipedia.org/wiki/Folksonomy
[guardians-video]: https://www.youtube.com/watch?v=XC8qrH3Zwog
[harper]: {{'/ideas/harper/harper-full/' | relative_url}}
[harper-william]: https://en.wikipedia.org/wiki/William_Rainey_Harper
[oer-landmines]: http://third-bit.com/2018/12/02/oer-landmines/
[stack]: http://stackoverflow.com
[swc-shell]: http://swcarpentry.github.io/shell-novice/
