
## Elevator Pitch

Once you know where the goalposts are, the next thing is to get everyone to
agree on what you're supposed to accomplish.  The best way to do this is write
an [%g elevator_pitch "elevator pitch" %][%i "elevator pitch" %] like the
one shown below to figure out what problem you're trying to solve, who it
affects, and why your solution is a good one.

> **The problem of**
> developing software in a predictable and reliable manner
> **affects**
> the management of software projects.
> Developers are not able to predict reliably how long it takes them to complete tasks
> which makes it impossible to effectively plan a project.
> **As a result,**
> users and managers are never sure whether the produced software will meet its requirements,
> how reliable the software will be,
> or whether the software will be delivered on time.
>
> **A successful solution would**
> help developers become more aware of what they do,
> how they spend their time,
> and the kinds of defects they find in their work.
> **For**
> software development teams
> **who**
> need to better understand how and when defects are introduced into their products,
> **our product**
> gathers and reports performance metrics
> **in order to**
> help developers track and analyze personal software development metrics.
> **Unlike**
> not gathering data or trying to gather it manually,
> **our approach**
> helps users gather data unobtrusively
> and provides objective feedback that allows them to improve both individual and team performance.

Have everyone on the team fill in the template independently and then compare
the results.  If your team is like most I've worked with, you'll be surprised by
how varied the answers are.  Once you have done that, pick one and turn it into
a short paragraph that everyone is happy with like the one below:

> Most programmers can't predict how long it will take them to do things because
> they don't know how long previous tasks have taken.  Gathering data manually is
> annoying enough that programmers won't do it, so we're building a tool that will
> monitor what applications they use and how long they use them.  This feedback
> will help them improve their working habits and allow them to give their
> managers more accurate input for scheduling.

You now have the first paragraph for your project's home page and the abstract
for your final report.

An alternative to writing an elevator pitch is to build the product's home page,
i.e., to make up the website for your software as if it already existed.  What
catchphrase would you put across the top to catch people's eyes?  What features
would you list on the back to make your software more appealing than its
competitors?  What would its system requirements be?  Its license?  Its price?
Once your team agrees on these things, you're ready to start designing and
coding.

## Project Structure

All right: you have some idea of what you're going to build. How should you
organize the project itself?

Every language has its own conventions for what files should go where in a
project, for the simple reason that they all need different files.  In a Jekyll
website like this one, for example, the layout is:

`_config.yml`
:   A configuration file with the author's name, a list of any plugins that the
    site needs to build, the rules for generating URLs for blog posts, and so
    on.

`_layouts`
:   A directory containing templates for pages.

`_includes/`
:   A directory containing any snippets shared between those templates.

`_site`
:   The directory containing the generated web pages. If the site doesn't need
    any special plugins, this directory doesn't have to be included in version
    control: GitHub will re-create it automatically. If the site does use
    plugins, on the other hand, the authors have to generate the HTML and
    commit it themselves.

If your project's goal is to build a package, on the other hand, you will have
to organize your files according to the packaging system's rules;
[%x design %] gives an example.  In all cases, learning what goes where is like
learning when to signal when driving a car: the rules may vary from place to
place, but everywhere *has* rules, and knowing them will help prevent you from
crashing.

## Standard Files

Regardless of language or packaging system, every project should have a handful of
standard files[%i "standard project files" "project organization!standard files" %] in its root directory.  These may have UPPERCASE names
without an extension, or may be plain text (`.txt)` or Markdown (`.md`) files.

`README`[%i "README file" %]
:   A brief overview of the project that often serves as its home page on
    GitHub.

`CONTRIBUTING`[%i "CONTRIBUTING file" %]
:   How to contribute to the project. Should people file an issue when they have
    a question, email a list, or post something on chat, and if so, where?  What
    code formatting conventions does the project use?  Research shows that clear
    contribution guidelines increase the odds of people contributing
    ([%x fairness %]); in my experience, they also reduce friction between team
    members.

`CONDUCT`[%i "CONDUCT file" %]
:   The project's Code of Conduct, i.e., how people are required to treat one
    another.  As we'll discuss below, "be polite" or "use your common sense"
    aren't enough.

`LICENSE`[%i "LICENSE file" %]
:   Describes who can do what with the project materials.  We discuss various
    licenses below as well.

## Code of Conduct

In order to get the most out of a team, it must do more than allow people to
contribute: it has to be clear that the teams *wants* contributions.  Saying
"the door is open" is not enough, since many people have painful personal
experience of being less welcome than others.  A project must therefore
acknowledge that some people are treated unfairly in society and actively take
steps to remedy this.  Putting a Code of
Conduct[%i "Code of Conduct" %] in place isn't just compassionate: it also makes the team more
diverse, which in turn makes it more productive [%b Zhan2020 %]:

-   It reassures people who have experienced harassment or unwelcoming behavior
    before that this project takes inclusion seriously.

-   It ensures that everyone knows what the rules are.  What you think is polite
    or common sense depends on where you are from; since many projects have
    participants from different backgrounds, making the rules explicit avoids
    angry arguments starting with, "But *I* thought that…"

-   It prevents people who misbehave from [%g feigning_ignorance "feigning
    ignorance" %], i.e., claiming after they say or do something offensive
    that they didn't realize it was out of bounds or that they were "just
    kidding". (See also [%g schrodingers_asshole "Schrödinger's
    asshole" %].)

Having a Code of Conduct is an empty gesture if you don't also have a way to
respond to violation.  [%b Aurora2018 %] describes how, and learning the
basics is a good first step toward becoming an ally[%i "ally" %]
([%x fairness %]).

<div class="callout" markdown="1">
### What they really mean

In the early 2010s a lot of open source developers resisted the adoption of
codes of conduct, saying that they were unnecessary or that that they infringed
freedom of speech.  What they usually meant (and what the few people still
arguing against them usually mean) is that thinking about how they have
benefited from past inequity makes them feel uncomfortable.  If having a Code of
Conduct makes them decide to go elsewhere, your project will be better off.
</div>
