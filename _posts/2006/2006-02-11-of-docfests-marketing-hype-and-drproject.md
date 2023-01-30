---
title: "Of DocFests, Marketing Hype, and DrProject"
date: 2006-02-11 11:46:04
year: 2006
---
Sean, Michelle, and I spent a couple of hours yesterday writing and updating documentation for DrProject.  The first 1.0 release candidate is now up on the web; while there are lots of little things to fix, I'm 99% confident we'll be able to announce it, and open up the Subversion repository, within the week.

Which makes <a href="http://radar.oreilly.com/archives/2006/02/web_development_20.html">this piece</a>, by Marc Hedlund, very timely.  I'm as amused by the invented-for-hype term "Web 2.0" as the next person, but that doesn't change the fact that software development has changed in the last ten years.  Here's my take on Hedlund's list:

<strong>The shadow app</strong> (which is his name for the internal application a company develops in order to figure out how their publicly released application is doing): we don't have anything like this yet for DrProject, but one of the principal reasons we built it was to collect data on how undergraduates program, so that we can improve our courses.  <a href="http://www.cs.utoronto.ca/~reid">Karen Reid</a> and I are taking <a href="http://www.cs.utoronto.ca/~sme">Steve Easterbrook</a>'s grad course on <a href="http://www.cs.toronto.edu/~sme/CSC2130/index.html">Empirical Research Methods in Software Engineering</a> this term, in the hopes of learning how to design studies and experiments that are scientifically credible; our "shadow app" will be driven by what we are learning there.

<strong>Sampling and testing</strong>, i.e., randomly show a small fraction of your visitors the new interface, and see how they use it, before releasing it generally.  I don't think we'll ever be able to do this in the classroom: the code of ethics prevents us from varying the conditions under which students work solely to collect data without first getting informed consent, and experience elsewhere is that less than 10% of students will bother to fill in the appropriate form.  We <em>might</em> be able to do this with non-course projects, like DrProject itself.

<strong>Build your own API</strong>: of course.  <a href="http://www.cmlenz.net">Chris Lenz</a> remounted DrProject on <a href="http://www.python.org/peps/pep-0333.html">WSGI</a> in January, so building a SOAP API (or similar) should be straightforward.  I'd love to see a DrProject-friendly <a href="http://www.eclipse.org">Eclipse</a> plugin…

<strong>Ship timestamps, not versions</strong>: no.  Once we open up the Subversion repository, people can grab whatever they want, whenever they want.  We'll still do old-fashioned releases—it wouldn't be fair to students who are using it in courses to push anything that hadn't been thoroughly tested.

<strong>Developers—and users—do the quality assurance</strong>.  We had to do this for budgetary reasons, but—no, who am I kidding?  We <em>chose</em> to do this: I could have had one of the three people working on the project in January do QA full time.  I know that dedicating some people to QA has been proven over and over again to be a more efficient way of producing usable software; I guess I'm just a sinner at heart.

<strong>Developers—and executives—do the support</strong>.  Yes.

<strong>The eternal beta</strong>.  No.  Beta testing started as a way to give a few valued or experienced customers a sneak preview of what the next release was going to contain; it has degenerated into a two-syllable shorthand for "you can't blame me".  I can't ask students facing hard deadlines in several courses at once to rely on DrProject unless I'm sure it's stable, and if I'm sure, why would I bother to call it a beta?

So, what's next?  More testing infrastructure is at the top of my list: I'm particularly excited by the newly-announced <a href="http://www.openqa.org/selenium-ide/">Selenium IDE</a>, which is a Firefox extension that lets you record, edit, and debug tests. Figuring out a way to run under <a href="http://www.modpython.org">mod_python</a> is up there too—we have to run as a pure CGI right now for security reasons, which won't scale to the kinds of loads we expect fifteen minutes before a major hand-in date.

And then?  We'd like to figure out what the simplest useful requirements management and traceability tool looks like; we'd like to add some sort of continuous integration (that can handle builds in several languages, <em>without</em> requiring students to do a lot of configuration), and progress charts that let students see how they're doing compared to the rest of the class (a la <a href="http://www.cs.ualberta.ca/~stroulia/JRefleX/">JRefleX</a>) would be cool as well.

But first we have to get the 1.0 release out the door…
