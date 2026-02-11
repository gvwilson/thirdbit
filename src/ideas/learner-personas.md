---
title: "Learner Personas"
template: page
---

A [learner persona][personas] is a short description of a typical
learner. By personalizing learners, personas help instructors figure
out who they’re trying to help and communicate that understanding to
each other and to learners. Each persona has general background,
relevant prior knowledge or experience, the learner’s perception of
their needs, and any special considerations.

Any workshop, tutorial, how-to guide, or reference manual should be
designed for one or two specific personas.  The ones below are derived
from a set originally developed by the author for RStudio.

<table>

  <tr>
    <th>Persona</th>
    <th>In Brief</th>
    <th>Domain Knowledge</th>
    <th>Statistics Knowledge</th>
    <th>Programming Knowledge</th>
  </tr>

  <tr>
    <td><a href="#anya-academic">Anya Academic</a></td>
    <td>A professor who needs training for her research and to pass on to students.</td>
    <td>expert</td>
    <td>competent</td>
    <td>competent</td>
  </tr>

  <tr>
    <td><a href="#celine-certified">Celine Certified</a></td>
    <td>A certified professional instructor.</td>
    <td>competent</td>
    <td>competent</td>
    <td>competent</td>
  </tr>

  <tr>
    <td><a href="#exton-excel">Exton Excel</a></td>
    <td>A proficient Excel user working in industry who wants to switch to Python.</td>
    <td>competent</td>
    <td>novice</td>
    <td>novice</td>
  </tr>

  <tr>
    <td><a href="#jacqui-ofalltrades">Jacqui Ofalltrades</a></td>
    <td>A data science generalist at a small consulting company.</td>
    <td>expert</td>
    <td>expert</td>
    <td>expert</td>
  </tr>

  <tr>
    <td><a href="#katrin-keener">Katrin Keener</a></td>
    <td>A Python enthusiast.</td>
    <td>competent</td>
    <td>competent</td>
    <td>competent</td>
  </tr> 

  <tr>
    <td><a href="#larry-legacy">Larry Legacy</a></td>
    <td>A reluctant learner who would really rather just keep using the tools he knows.</td>
    <td>expert</td>
    <td>expert</td>
    <td>novice</td>
  </tr>

  <tr>
    <td><a href="#mshelle-manager">M'shelle Manager</a></td>
    <td>An ex-programmer who now leads a team and needs to make decisions about tool adoption.</td>
    <td>competent</td>
    <td>novice</td>
    <td>competent</td>
  </tr> 

  <tr>
    <td><a href="#nang-newbie">Nang Newbie</a></td>
    <td>An undergraduate student without statistical knowledge or programming skills.</td>
    <td>novice</td>
    <td>novice</td>
    <td>novice</td>
  </tr> 

  <tr>
    <td><a href="#toshi-techsupport">Toshi Techsupport</a></td>
    <td>A sys admin who has to support data scientists.</td>
    <td>expert</td>
    <td>novice</td>
    <td>expert</td>
  </tr>

</table>

**Notes**

1.  A *novice* is someone who doesn't yet have a mental model of some
    field: as a result, they don't know what they don't know.  Someone
    is *competent* if they know enough to perform routine tasks
    without heroic effort, while they are an *expert* if they are able
    to solve common problems at a glance and harder or more unusual
    problems reliably.

2.  The domains in these personas (such as pharmacy or event
    management) are meant to be placeholders: swap in another domain
    such as finance or logistics as desired.

## Anya Academic {: #anya-academic}

<p>
  <img class="title" src="@root/files/learner-personas/anya-academic.png" alt="Anya Academic" width="50" />
</p>

1. Anya, a professor of neuropsychology, studies color perception in
   infants. She is also responsible for teaching an introduction to
   statistics to 1100 first-year students every year. (Students
   complain that the Stats department's introductory course is too
   theoretical and requires more programming knowledge than they
   have.)

2. Anya runs several experiments on 50–100 infant subjects each
   year. She used to analyze the results with R, but is switching to
   Python (which she taught herself during a sabbatical). She has
   never taken a programming course, and suffers from impostor
   syndrome in discussions about things like GitHub.

3. Anya would like to learn more about tools like Polars and
   Marimo. She also wants guidance on using them to teach her intro
   stats course, which currently uses R.

4. Anya is juggling half a dozen responsibilities at work, and has
   been burned before by investing in technologies that didn't pan out.

Anya needs workshops (so that she can allocate focused time) and
how-to guides (for her research). She would like ready-to-use lesson
material she could remix for her students and some orientation
material to demystify jargon (what the hell is a "pull request"?).
Finally, it's important that she be able to use the same tools in her
research as in her teaching in order to amortize learning costs.

## Celine Certified {: #celine-certified}

<p>
  <img class="title" src="@root/files/learner-personas/celine-certified.png" alt="Celine Certified" width="50" />
</p>

1. Celine has an MBA in finance and is now a certified professional
   instructor working for a full service solution provider. She spends
   her time developing new training material in airports and
   delivering them between flights.

2. Python is the only language Celine has ever learned well, but she
   has learned it very well. She is proficient with a variety of
   packages for modeling and time series analysis, and knows more than
   any sane person should about extracting data from Excel. She
   regularly contributes small fixes to a dozen of the packages she
   teaches most often.

3. Celine is always interested in seeing other people's teaching
   material, but what she appreciates most is up-to-date examples she
   can recycle and build her own lessons around.

4. Celine is sometimes frustrated by how little developers think about
   the learnability or usability of their packages, and wishes she had
   more control over what she's going to be asked to teach.

Celine needs vignettes, worked examples, and cookbooks that she can
mine to create training to meet her audience's needs. She would also
like pointers to material on better teaching practices.

## Exton Excel {: #exton-excel}

<p>
  <img class="title" src="@root/files/learner-personas/exton-excel.png" alt="Exton Excel" width="50" />
</p>

1. Exton taught business at a community college for several years, and
   now does community management for an event management company. He
   still teaches Marketing 101 every year to help people with
   backgrounds like his.

2. Exton uses Excel to keep track of who is registered for webinars,
   workshops, and training sessions. He doesn't think of himself as a
   programmer, but spends hours creating complicated lookup tables to
   figure out how many webinar attendees turn into community
   contributors, who answers forum posts most frequently, and so on.

3. Exton knows there are better ways to do what he's doing, but feels
   overwhelmed by the blog posts and "helpful" recommendations from
   the company's engineering team.

4. Exton is a single parent; the one evening a week he spends teaching
   is the only out-of-work time he's able to take away from family
   responsibilities.

Exton wants an overview that will tell him what laptop-scale data
science is all about, what tools to learn first, how they're going to
help him, and where he should look for introductory tutorials. He
doesn't care if these are the best answers so long as they are clear,
concise, and consistent. He would also benefit from side-by-side
comparisons with Excel.

## Jacqui Ofalltrades {: #jacqui-ofalltrades}

<p>
  <img class="title" src="@root/files/learner-personas/jacqui-ofalltrades.png" alt="Jacqui Ofalltrades" width="50" />
</p>

1. Jacqui works for a three-person consulting company that does
   everything from training to installation and administration to
   building dashboards for clients. She is fluent in Spanish and
   Portuguese as well as English, and much of her business is with
   Latin American firms.

2. Jacqui has been using Python and Pandas for several years, and just
   finished working through some material on PyTorch for the second
   time in preparation for teaching it. She has built a couple of Dash
   dashboards for clients.

3. Jacqui wants updates on new data science packages and tools, and
   advanced guides for making dashboards faster, integrated with
   no-SQL databases, and other high-value topics. She finds most
   self-paced tutorials frustrating because they're answering
   questions she doesn't have today.

4. Jacqui believes that time is money: every minute she spends
   learning something new has to pay off sooner rather than later.

Jacqui wants how-to guides and reference material for her day-to-day
work, webinars to give her a sense of where the industry is going, and
short, intensive online training for very specific topics.

## Katrin Keener {: #katrin-keener}

<p>
  <img class="title" src="@root/files/learner-personas/katrin-keener.png" alt="Katrin Keener" width="50" />
</p>

1. Katrin did a Master's in neuropsychology and a 12-week data science
   bootcamp before getting a job analyzing logistics for a health care
   services company. She has a wide range of interests and loves
   learning new things.

2. Katrin uses Python and SQL daily, and recently talked one of the IT
   staff into teaching her Docker. She has done a couple of online
   short courses in machine learning.

3. Katrin wants to level up her understanding of just about
   everything.  She needs cookbooks and worked examples to show her
   how to accomplish specific tasks or to fill in specific gaps in her
   knowledge.

4. While she is enjoying her new job, Katrin misses the camaraderie of
   grad school and her bootcamp: she prefers learning with others to
   studying on her own.

Katrin wants workshops (as an opportunity to meet people) and
self-paced lessons (so that she can learn new things on her own). She
has a complete set of cheatsheets taped up on her wall, but usually
asks Claude before looking at reference manuals.

## Larry Legacy {: #larry-legacy}

<p>
  <img class="title" src="@root/files/learner-personas/larry-legacy.png" alt="Larry Legacy" width="50" />
</p>

1. Larry got a job with a pharmaceutical company the day after he
   graduated and has been with them through two mergers and an
   acquisition. He refers to company officers by their first names,
   and is always happy to explain what they're doing wrong.

2. Larry has been using Vim and NumPy for 25 years and regards them as
   a perfectly fine tools, thank you very much.

3. Larry has never used a computational notebook, but has decades of
   experience with statistics, messy data, and reporting. He prefers
   very structured learning environments and clear objectives, and his
   most common question, "How would I…" followed by a summary of
   something he has been doing for years in NumPy.

4. Larry is a reluctant learner: he recognizes that he has to learn
   new tools now that management has decided to adopt Marimo, but with
   just eight years to go until early retirement, the thought makes
   him weary. He is very uncomfortable with anything outside his
   normal working environment.

Larry finds tutorials long-winded ("Just show me what function I need
to call!")  or confusing ("Why would they do it that
way?"). Cheatsheets showing him how to map his understanding to
equivalent steps or code in other tools would be his preferred
starting point.

## M'shelle Manager {: #mshelle-manager}

<p>
  <img class="title" src="@root/files/learner-personas/mshelle-manager.png" alt="M'shelle Manager" width="50" />
</p>

1. A programmer who moved into customer support and then into product
   management, M'shelle is now in charge of a ten-person analytics
   group. She is responsible for getting her team trained and
   purchasing the tools they need to do their work.

2. M'shelle used Python to develop statistical models and generate
   reports several years ago, but recognizes that she has fallen
   behind developments since then.

3. M'shelle wants to improve her team's processes, particularly around
   packaging code and making work more reproducible. The new VP of
   engineering has also asked her to turn everything into a web
   service *and* get everyone to vibe code. While all of this is going
   on, she needs to decide how much budget she needs for new software
   that she will personally never use.

4. M'shelle has to work within a strict training budget, and it can
   sometimes take months to get approval to do anything.

M'shelle needs tutorials, reference material, and how-to guides for
everything that isn't data science, including testing, packaging, and
how to use AI. (Her team is satisfied with the existing tutorials on
data manipulation and modeling.)

## Nang Newbie {: #nang-newbie}

<p>
  <img class="title" src="@root/files/learner-personas/nang-newbie.png" alt="Nang Newbie" width="50" />
</p>

1. Nang is 18 years old and in the first year of an undergraduate
   degree in urban planning. He's read lots of gushing articles about
   AI, and was excited by the prospect of learning how to do it, but
   dropped his CS 101 course after six weeks because nothing made
   sense. He's doing better in Anya Academic's course (which he is
   taking as an elective), but still spends most of his time prompting
   and swearing.

2. Nang did well in his high school math classes, and built himself a
   home page with HTML and CSS in a weekend workshop in grade 11. He
   has accounts on nine different social media site, and attends all
   of his morning classes online.

3. Nang wants self-paced tutorials with practice exercises, plus
   forums where he can ask for help.

4. Nang is reluctant to reveal his ignorance: he would rather get a
   low grade and blame it on partying than let his classmates see that
   he's floundering.

Nang needs to build enough understanding of data science to drive LLM
tools effectively.  He prefers short overviews to orient him and
introductory tutorials that include videos or animated GIFs showing
exactly how to drive the tools, and that use datasets he can relate
to.

## Toshi Techsupport {: #toshi-techsupport}

<p>
  <img class="title" src="@root/files/learner-personas/toshi-techsupport.png" alt="Toshi Techsupport" width="50" />
</p>

1. Toshi does internal tech support in a 500-person company. While
   others on his team take care of resetting passwords, he debugs
   setup issues and figures out why the dashboard is displaying
   nonsense. (It's usually something to do with date formatting.) He
   often winds up writing bits of code from Stack Overflow to glue
   things together.

2. Toshi speaks Bash and Python, but only knows a bit of JavaScript.
   He switches back and forth between Linux, Windows, and Mac every
   day. He often finds himself running hour-long internal training
   seminars, and would now like to learn some data science to support
   his users and out of personal interest. He wishes people would take
   a few hours and learn more about the software they're using, but in
   practice, he often only has a 30-minute call in which to diagnose
   the problem and explain a solution.

3. A growing number of analysts inside Toshi's company use Marimo to
   prepare reports. He would like to learn enough about them to be
   useful.

4. Toshi lives in Hawaii, so most of his work is done remotely.

Toshi needs examples and reference material for himself that he can
paraphrase for the people he is supporting, or that they can feed to
AI tools. He also needs tutorials he can remix for hour-long internal
training webinars.

[personas]: http://teachtogether.tech/#s:process-personas
