---
title: "Sessioncasting"
date: 2022-12-18
---

> INTRODUCTION: [This trend], which everyone knows about,
> and [that trend], which is so incredibly arcane that you probably didn't know about it until just now,
> and [this other trend over here] which might seem, at first blush, to be completely unrelated,
> when all taken together,
> lead us to the (proprietary, secret, heavily patented, trademarked, and NDAed) insight
> that we could increase shareholder value by [doing stuff].
> We will need $ [a large number] and after [not too long]
> we will be able to realize an increase in value to $ [an even larger number],
> unless [hell freezes over in midsummer].
>
> Neal Stephenson, *Cryptonomicon*, 1999, [pg. 238][cryptonomicon-pdf].

Teaching and learning programming is much harder than actually programming:
the mental models required are more complex ([1][teaching-3d])
and the tools we need don't exist ([2][code-in-textbooks], [3][memory-diagram]).
Following Stephenson's guideline quoted above,
though,
I think we could combine a couple of existing technologies in a new way
to make this process easier, faster, and more enjoyable.

## Step 1: Replay

Let's start with [asciinema][asciinema],
which allows you to record and play back a terminal session *as text*
rather than as a video.
The difference is important:
"text" in a video is just pixels that happen to be arranged in the shapes of letters,
while asciinema records and replays actual text with timings.
If you pause an asciinema recording you can select and copy the text,
and search engines and accessibility tools can "see" the text as well.

Replay isn't limited to text.
Tools like [Selenium][selenium] can capture mouse events
as well as keystrokes
and save them with timings
so that you can replay your interactions with a browser.
This is obviously useful for testing,
but most people don't take advantage of three corollary benefits:

1.  The sequence of events ("move the mouse here, right click, press J, press U")
    is a searchable, editable artifact.
    You can,
    for example,
    find all the interaction records that involve scrolling
    or stitch together two existing interactions
    to see what happens if they run consecutively
    without having to re-do either.

2.  The browser is still in its final state when replay finishes,
    so you can do "what if?" experiments.

3.  You can single-step or interrupt a sequence during playback,
    which allows "what if?" experiments in the middle of replay.

The first property is very useful for teachers,
but the second and third are potentially game changers for learners.
As an analogy,
people can learn to fly by reading books that have photographs of cockpit controls,
but interactive flight simulators are more effective and more engaging.

## Step 2: Voiceover

Replay-with-branching has two shortcomings,
the first of which is,
where is the explanation?
[Wasim Lorgat][lorgat] has written a brief tutorial on
[how to turn terminal demos into animated SVGs][svg-replay]
that can be embedded in a page beside an explanation,
but reading the latter while watching the former is a heavy [cognitive load][cognitive-load].
What we want is a voiceover that's synchronized with the event stream
that's driving the animation,
which is what [Scrimba][scrimba] provides.
Their "scrims" aren't videos:
instead,
each one is a narrated replay of a programming session in an in-browser coding sandbox.
If you pause at any point,
you can search or copy the text from the animated coding window;
if you scroll backward or forward you see that text change
just as you would using "undo" and "redo" in an editor.

> Note: I wanted to embed a demo scrim in this blog post,
> but it looks like their creators have gone into the coding bootcamp business
> and the tools to make and replay scrims are now closed-source.
> If I'm wrong, please correct me and I'll update this post.

## Step 3: Branching

I don't know if anyone has married voiceover with a browser testing tool,
but as we discovered during the Browsercast project,
modern browser APIs make it pretty easy to synchronize media with browser events.
(You may have to dismiss some warnings or press the space bar to start that demo:
the code is ten years old and I haven't had time to update it.)
However,
that still leaves us with our second problem: exploration.
Learners don't want to *watch* programming—they want to change things and play "what if?"
and then come back back to the lesson and pick up where they left off.

But if learners change things, the lesson might stop working.
For example,
a learner might delete a column from a dataframe
that the rest of the lesson depended on.
The instructor can try to accommodate this by creating checkpoints
that learners can restart from,
but I've always hated it when game designers tell me I'm only allowed to save the game at certain points.
Checkpointing also puts a heavy burden on instructors:
if they change something early in the lesson,
they often have to go through and manually re-create all of the subsequent checkpoints.
In practice,
lesson maintenance is as hard as software maintenance
(see the note above about Browsercast),
and any tool that makes it harder is unlikely to be popular.

Luckily, there's a solution.
As far back as 2009,
projects like [Snowflock][snowflock] proved that
cloning a virtual machine can be almost as fast as forking a process.
The [technical details][snowflock-pdf] are fascinating,
but in brief,
the trick is that the new VM shares pages of virtual memory with its parent
until one or the other tries to modify something,
at which point the child VM gets its own copy of the affected page to scribble on.
This "copy on write" strategy means that the child VM can start running almost immediately,
but it also means that the parent can be cloned at any time,
which is exactly what we need for teaching.

## Step 4: The Stephenson Moment

So let's pull this together.
What I want is a tool that:

1.  Records my interactions with my desktop as a stream of logical events rather than as video.

2.  Simultaneously, records what I'm saying.

3.  Allows me to edit the combination in the way that [Camtasia][camtasia] or [OBS][obs]
    lets me edit screencasts.

4.  Lets a learner replay the result in a sandbox VM on their computer or in the cloud.

5.  Lets the learner stop the replay at any point and fork a new VM to play around in.

6.  When she's done, lets her throw away that VM and resume the lesson where she left off.

Let's call recordings like this "sessioncasts".
They're better than screencasts, computational notebooks, and coding sandboxes
for all the reasons given in the previous sections,
but *they're more general and therefore more authentic*.
if your lesson switches between VSCode, a terminal, the browser, and back to VSCode,
you can record it all in one sessioncast
so that learners can see *and do* real-life programming.
I don't know of anything else that can offer this.

What would it take to build a sessioncasting tool?
What's the "large number" after the dollar sign in the *Cryptonomicon* quote?
I honestly don't know,
but all the pieces exist—we just need to assemble them
(for some admittedly large value of "just").
I doubt vulture capitalists would fund a tool to make teaching and learning easier,
but sessioncasts would be a boon for tech support as well:
if I can't reproduce your bug,
you can record a sessioncast and send it to me so I can poke around.
There are obvious security and privacy concerns,
but there have been times when I would have traded minor but useful body parts for this.
If you're already working on this or something better,
please give me a shout.

> After taking vows of celibacy and abstinence and foregoing all of our material possessions for homespun robes,
> we (viz. appended resumes) will move into a modest complex of scavenged refrigerator boxes in the central Gobi Desert,
> where real estate is so cheap that we are actually being paid to occupy it,
> thereby enhancing shareholder value even before we have actually done anything.
> On a daily ration consisting of a handful of uncooked rice and a ladleful of water,
> we will [begin to do stuff].
>
> Neal Stephenson, *Cryptonomicon*, 1999, [pg. 240][cryptonomicon-pdf].

[asciinema]: https://asciinema.org/
[camtasia]: https://www.techsmith.com/video-editor.html
[code-in-textbooks]: @root/2022/11/30/what-i-want-for-code-in-textbooks/
[cognitive-load]: https://teachtogether.tech/en/index.html#s:architecture-load
[cryptonomicon-pdf]: @root/files/2022/cryptonomicon-business-plan.pdf
[lorgat]: https://wasimlorgat.com/
[memory-diagram]: @root/2022/12/04/i-want-a-memory-diagram-generator/
[obs]: https://obsproject.com/
[scrimba]: https://scrimba.com/
[sdxjs-regex]: @root/sdxjs/pattern-matching/
[selenium]: https://www.selenium.dev/
[snowflock]: http://aosabook.org/en/snowflock.html
[snowflock-pdf]: https://www.cs.toronto.edu/~brudno/snowflock_eurosys.pdf
[svg-replay]: https://wasimlorgat.com/tils/how-to-share-terminal-demos-as-razor-sharp-animated-svg.html
[teaching-3d]: @root/2022/12/14/teaching-in-the-third-dimension/
