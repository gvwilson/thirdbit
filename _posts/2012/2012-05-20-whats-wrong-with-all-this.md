---
date: 2012-05-20 09:00:00
year: 2012
original: swc
title: What's Wrong With All This?
---
<p>Titus Brown <a href="https://twitter.com/ctitusbrown/status/200937511999123456">doesn't like this web site</a>. He's OK with the content (I think), but he finds it awkward to use, and while I don't feel as strongly as he does, I accept that we have outgrown WordPress. The question is, what should we use instead? We need a lot more than just a blog and some static web pages, but learning management systems like <a href="http://moodle.org/">Moodle</a> weren't built with our ad hoc model in mind (they're really teaching administration systems), and newer tools like <a href="http://p2pu.org">P2PU</a> feel like a step backward. I started thinking about requirements for a replacement back in April, but got distracted. Here's a longer look.</p>
<h2>Who are we?</h2>
<ul>
<li>A <em>learner</em> learns new tools and skills.</li>
<li>A <em>tutor</em> passes on their knowledge.</li>
<li>A <em>workshop host</em> organizes and runs a bootcamp.</li>
<li>An <em>author</em> creates content (lessons, blog posts, exercises, etc.).</li>
<li>An <em>admin</em> manages the web site.</li>
<li><em>Innocent bystanders</em> watch and comment from the sidelines :-)</li>
</ul>
<p>An individual might assume any of these roles at different times or in different contexts. For example, workshop hosts are often tutors, a tutor for one topic may be a learner for another, authors are often admins and vice versa, etc.</p>
<h2>What do we do?</h2>
<ul>
<li>A <em>workshop</em> is a live event, typically running all day for two days. A workshop is made up of several <em>lessons</em>, which may use the content we have online (or at least improvise around it), but which usually remix the order.</li>
<li>A <em>course</em> is a slower-paced event, typically running for a few hours once a week for several weeks. Courses use our online material (or don't) just like workshops.</li>
<li>A <em>tutorial</em> is an ad hoc real-time session with one tutor and several learners. Tutorials can be online or live.</li>
<li>A <em>help session</em> is an ad hoc session between one tutor and one learner. Help sessions can be online or live.</li>
<li>A <em>content jam</em> is a live get-together to create or update content. We haven't actually had one of these yet, but I'm hopeful...</li>
</ul>
<h2>What do we use to interact?</h2>
<ul>
<li><a href="http://www.skype.com">Skype</a> and desktop sharing for real-time online events. We've been using <a href="http://www.bluejeans.com">BlueJeans</a> for one-to-many tutorials; it works pretty well, but doesn't seem to allow people to use Skype text chat while in a session, and we've never been able to make recording work. It's also very expensive, but cheaper alternatives (WebEx, Google+ hangouts) haven't scaled as well.</li>
<li>Our WordPress blog. We manually echo posts to Twitter.</li>
<li>Twitter (tweets aren't currently archived on our site, but should be).</li>
<li>Web pages in our WordPress site. This includes the online course material, ads for workshops, and a few bits of advertising.</li>
<li>Comments on the WordPress material. (People have suggested adding forums as well, but I don't believe there would be enough traffic, and we all have too many places to pay attention to already.)</li>
<li>Videos (hosted at <a href="http://www.youtube.com/user/softwarecarpentry/feed">YouTube</a>, embedded in the WordPress site).</li>
<li>Point-to-point email. (This is usually from and to people's personal accounts, so it isn't archived.)</li>
<li>Our own mailing lists: one for workshop organizers and content developers, and others for various regions and workshops. These <em>are</em> archived, but since we use <a href="http://www.gnu.org/software/mailman/index.html">MailMan</a>, they're not integrated with WordPress. (I've experimented with various mailing list plugins for WordPress, and haven't been impressed by any of them.) We manage these lists through the <a href="http://dreamhost.com">Dreamhost</a> control panel.</li>
<li><a href="http://subversion.tigris.org/">Subversion</a>. We have a publicly-readable repository for the course material and a members-only repository for administrative stuff like grant proposals. We also set up one repository for each workshop group, which we keep live for a couple of months. We also manage repos through the Dreamhost control panel, but there's no way to automatically keep their membership and permissions in sync with the group mailing lists.</li>
<li><a href="http://www.eventbrite.com">EventBrite</a> for event registration. We link to EventBrite sign-up pages for events from the corresponding WordPress pages, but the linkage is done manually. EventBrite also gives us a mailing list for each event; we should use these to contact workshop participants immediately before and after workshops rather than our MailMan lists.</li>
<li>Google Calendar and Google Maps to show when and where upcoming workshops are. Our calendar and map are linked into a page on the WordPress site, but updates have to be done manually. In particular, we have to remember to add events to both the calendar and the map, and when an event is over, we have to change the map as well as moving the event's page to the "past" section of the site.</li>
<li><a href="http://www.doodle.com">Doodle</a> to schedule tutorials.</li>
</ul>
<p>One thing we <em>don't</em> have yet is badges. We'd like to issue these to people who have taken part in workshops and the follow-up tutorials (i.e., our "graduates"), and also to instructors and content creators. The <a href="http://openbadges.org/en-US/">Open Badges</a> team is working on a WordPress plugin to do this, which we hope to deploy in June.</p>
<h2>How do we interact?</h2>
<ul>
<li>Synchronously, i.e., taking part in or delivering workshops, courses, tutorials, help sessions, and content jams, both live and online.</li>
<li>Scheduling events using Doodle.</li>
<li>Registering for (and unregistering from) events using EventBrite.</li>
<li>Advertising events using MailMan lists, the blog, and Twitter.</li>
<li>Updating people on changes to workshops and courses using MailMan lists and EventBrite lists.</li>
<li>Writing blog posts.</li>
<li>Writing pages.</li>
<li>Commenting on blog posts and pages.</li>
<li>Tweeting.</li>
<li>Creating or updating content in the main Subversion repository (and then updating the web site if needed).</li>
<li>Creating and uploading videos, and then linking to them in a blog post or from a page.</li>
<li>Discussing things on the "dev" list. There's almost never discussion on the per-workshop lists: I feel like there should be (or should be forums or something), but help sites need critical mass, and I doubt we'll ever have it, so I'd rather put energy into teaching people <a href="http://www.ploscompbiol.org/article/info:doi%2F10.1371%2Fjournal.pcbi.1002202">how to use existing online Q&amp;A sites well</a>.</li>
<li>Giving feedback about events. Right now, we collect good and bad points from people at the end of every workshop, then post them to the blog. We really need to collect feedback on tutorials, and to follow up with people months or years later.</li>
</ul>
<h2>What's wrong with all this?</h2>
<ul>
<li><em>Speed</em> and <em>design</em>: the existing web site is slooooow, and no one would call the existing site beautiful...</li>
<li><em>Identity</em>: scheduling is separate from registration is separate from the mailing lists and from repositories. Badging will only make that more complicated. <a href="http://www.mozilla.org/en-US/persona/">Mozilla Persona</a> (formerly <a href="https://browserid.org/">BrowserID</a>, and not the same thing as <a href="http://openid.net/">OpenID</a>–are you confused yet?) isn't a complete solution: it handles authentication, but not authorization, and "who can do what?" is an authorization issue. <a href="http://oauth.net/">OAuth</a> is supposed to take care of the latter, but it it's a looong way from meeting our needs.</li>
<li><em>Integration</em>: connecting our blog to Twitter would be easy–I just haven't bothered to set it up. But tweets should be archived on the web site (both the ones we make and mentions of us), the mailing list archives should be integrated into the site, and so on. Again, there's a lot more to this than just managing identities.</li>
<li><em>Features</em>: I'd like a live table of registration stats (how many people have signed up for all upcoming events, and how many tickets remain) on the web site, but EventBrite doesn't have embeddable HTML for that. I'd also like a person-by-list table showing who's on which mailing list, and who has access to which repository, but Dreamhost and MailMan don't offer that. And I'd like the colors of map pins to change automatically once a workshop is over, but–you get the picture. All of these things can be fixed with the right glue code, but I have bigger <a href="http://en.wiktionary.org/wiki/yak_shaving">yaks to shave</a>.</li>
<li><em>Conversation</em>: the most important missing element is regular back-and-forth with the people we're trying to help. Again, I think that our goal should be to get them onto existing Q&amp;A sites like Stack Overflow; in particular, we should help them feel confident enough to hang out there, so they don't become part of the dark matter of computational science.</li>
</ul>
<h2>What do I want?</h2>
<p>I've written before about the idea of a GitHub for education, but that wouldn't address all of the issues laid out above. (Event registration, for example, doesn't feel like a GitHub kind of thing; nor does scheduling tutorials.) If we had a truly programmable web, I could hire a summer student to assemble what I want, but that's not a yak, it's a herd of angry mammoths: managing identities and permissions for MailMan, EventBrite, Subversion, and the blog in a single place would require a <em>lot</em> of hacking (or a time machine–if I could go back to 1999 and persuade the startup I was part of to open source SelectAccess, we'd be done by now).</p>
<p>So that leaves me looking for an off-the-shelf solution which I don't think exists. If I'm wrong, I'd welcome a pointer–and if there's something we should be doing that isn't in the discussion above, I'd welcome a pointer to that too.</p>
