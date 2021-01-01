---
title: "It Feels Good to be Useful"
date: 2019-08-14 08:33
year: 2019
---

<em>
A notification landed in my email earlier today because
my GitHub ID had been mentioned in [an issue](https://github.com/python-trio/trio/issues/1187),
and I couldn't be happier about its content.
@njsmith wrote:
</em>

@pquentin pointed me to this great essay by @gvwilson and collaborators: "Ten simple rules for helping newcomers become contributors to open source projects"

Going to take notes here as I read it, on ideas for things we could/should adopt.

(Possibly useful context for others reading it: I'm pretty sure this is slated for publication in PLoS Computational Biology as part of their "Ten simple rules" series. So the target audience is something like, academic researchers who are into openness and sharing code, but may or may not be super familiar with the open source community and professional programming norms, and are probably working more on smallish projects for others in their field, rather than like, the Linux kernel or CPython or something.)

Rule 1: "Be welcoming".

We're pretty good at the basics here, of telling people they're welcome and keeping a generally positive tone. More specific ideas triggered by this section:

-   Maybe we should explicitly encourage folks who are interested in contributing to say hi, and suggest where? (Chat, and/or a dedicated thread or category on the discourse?) + tips on how to do it (e.g. say what you're interested in)
-   We should have more explicit docs on exactly how one could go about getting more involved: set up environment, introduce yourself, check for good first issues, etc.
-   List contact points for users who aren't comfortable just throwing their beginner questions into a public channel

Rule 2: "Help potential contributors evaluate if the project is a good fit" – not sure I have any brilliant ideas here. We certainly have lots of different things to work on, but

Rule 3: "Make governance explicit" – I'm comfortable that I know how to handle this part :-)

Rule 4: "Keep knowledge up to date and findable" – I think we're pretty good about maintaining the issue tracker as a compendium of knowledge and project status, and about referencing it as appropriate.

Rule 5: "Have and enforce a code of conduct" – we're on top of this.

Rule 6: "Develop forms of legitimate peripheral participation" – we're doing all the specific things they suggest, but I'm still not sure we do a great job of this. Probably our most effective version of this right now is just for people to hang out in the chat, so they're exposed to what's happening and have the option of joining in in low-commitment ways? Maybe this means we should really emphasize the value of "hanging out in chat" as part of the "how to become a contributor" guidelines?

Rule 7: "Make it easy for newcomers to get started" – pretty much covered this in my comments on Rule 1.

Rule 8: "Use opportunities for in-person interaction---with care" – we haven't been great about this so far. There have been the BoF sessions at PyCon and sprints, but they haven't been super organized. Partly this is just because of scale (we're not at a point where we could organize our own meetups!) and my limits, which are sort of unavoidable. But it would be great to do more here. The mentored sprints at PyCon this year were amazing, because the organizers did such a good job of getting things organized. Maybe as the project grows, we should look out for folks who are good at that kind of organizing and try to suck them in? That might be something to add to the "how to contribute" docs for those who aren't ready to dive into super technical details of kernel APIs and coroutine schedulers.

Rule 9: "Acknowledge all contributions" – There's definitely more we could do here. Some ideas:

-   In my pycon talk, I used a script to make the wall o' contributors slide. I'm pretty happy about how that came out. One idea we batted around at some point was to do something similar in our release notes: include a tiny little wall-o-contributors at the bottom of each section of everyone who contributed to that release. (Ideally in a relatively expansive fashion, e.g. including folks who commented on included PRs, or fixed issues.)

-   Maybe we can do a better job of respecting contributors time, e.g. by giving new contributors useful suggestions on what to expect, or automatically pinging PRs/issues that need a review and might have slipped through the cracks?

Rule 10: "Follow up on both success and failure" – I feel like right now we aren't so bad at helping people make their first contribution, but are really really bad at helping people make their second contribution. An absolutely tiny fraction of folks make a second PR, or join in reviewing other PRs. To some extent that's fine and normal – folks have a single itch, they scratched it, they have other stuff to do with their lives – but I think we could do a way better job here of figuring out why this happens and making it easier for people to continue.

Maybe it would be helpful to explicitly ask people whether they want to keep contributing after their first PR is merged, and if they say yes then follow up with them later? Of course this would have to be opt-in because we don't want to harass people, but I feel like there is probably some percentage of contributors who would genuinely want to follow-up and would appreciate the option to ask for one.

We could also like, offer people one of those "how was your experience?" surveys, like seemingly every business does now...

<em>
If you don't want to wait for the paper to appear on PLoS,
you can read it [here](https://github.com/gvwilson/10-newcomers/).
</em>
