---
date: 2019-03-30
title: "Online Teaching Setup"
---

As [I mentioned last week](@root/2019/03/20/educational-paramedics/),
a colleague and I have been teaching
[RStudio's instructor training and certification](https://blog.rstudio.com/2019/02/28/rstudio-instructor-training/) online,
and I'm pretty pleased with our setup:

1.  *Zoom for video conferencing.*
    Our class had 13 participants at peak,
    but I've used Zoom for up to two dozen in
    [the Carpentries' instructor training](https://carpentries.github.io/instructor-training/),
    and it's handled the load well.

2.  *Zoom chat for real-time coordination.*
    We initially used a slack channel to keep track of speaking order (/hand for the win)
    and to remind people how long exercises were supposed to take,
    but relying on Zoom's built-in chat meant that participants had one less window to check,
    which helped a lot.

3.  *A Google Doc for exercises.*
    The Carpentries have relied on Etherpad for years,
    but I'm finding it increasingly unstable.
    Google Docs do have to be shared with participants,
    and don't colorize contributions to show authorship,
    but they handle two dozen simultaneous cursors quite easily,
    allow participants to format their contributions,
    and to be honest,
    the lack of coloring makes them a lot easier to read.
    As with Etherpad,
    it's crucial to paste a list of names into the doc at the start of the exercise
    so that everyone knows where to type;
    without that,
    the initial flurry of overwrites makes the exercise a really compelling demonstration
    of why concurrent programming is hard.

4.  One other great advantage Google Docs have is that people can paste images directly into them,
    rather than pasting in a link that opens up the image in another tab.
    I was surprised at how much of a difference this made for some of the exercises:
    having people draw a concept map,
    take a picture with their phone,
    and then paste that picture in the doc where everyone could see it
    was remarkably effective.
    And yes,
    you can draw directly in a Google Doc just like you can in Word or PowerPoint,
    but we encouraged people to draw elsewhere and then paste their finished diagram;
    I'll ask people to draw in the doc in real time in the next class and see how that goes.

5.  *Google Slides for slides.*
    Google Slides lets me do everything I do in PowerPoint or Keynote
    (which isn't to say it does everything they do—like most people,
    I only use a small fraction of what desktop productivity software provides.)
    More importantly,
    Google Slides seems to be the best option for collaborating on graphics-rich slides:
    -   People can add comments on individual elements of slides, including individual graphical elements.
    -   Keynote and PowerPoint in GitHub are a waste of time,
        since Git doesn't know how to diff and merge anything more sophisticated than punch cards.
    -   It's a lot harder to create and position graphics using slideshow packages based on Markdown or HTML
        than in WYSIWYG editors,
        and even if you go the extra kilometer,
        Git still can't diff or merge the actual graphics.

6.  *[Pear Deck](https://www.peardeck.com/) for presenting.*
    When you launch a presentation with Pear Deck,
    it gives you a link to share with your audience.
    Instead of watching a video stream,
    they then view your slides in a browser tab;
    Pear Deck automatically keeps their views in sync with the presenter's.
    It's pretty cool,
    and much more accessible for people in low-bandwidth environments or with visual impairments.
    Pear Deck also allows you to embed formative assessments like multiple choice questions in your slides,
    and collects and displays viewers' responses in real time.
    However,
    presenting from Firefox was problematic—I had to restart in Chrome—and one viewer using IE
    occasionally had to advance slides manually
    (although again, once he switched to Chrome it all started to work again).

I don't know how well this setup would work for a programming class,
but I'm keen to try.
RStudio Server Pro will allow people to share live coding sessions,
and so will other tools like [Jupyter](https://jupyterhub.readthedocs.io/en/stable/).
I'm not slated to teach R, Python, or JavaScript in the next few months,
but when I am,
I'd like to give this a try.

Stepping back,
I now believe that MOOCs are going to prove to be an evolutionary backwater.
Yes,
they scale to hundreds of thousands of users,
but what they scale is mediocre.
My daughter regards the internet as a way to collaborate in real time:
her friends held a surprise birthday party for her in Minecraft this morning,
and I think that kind of interaction the future of online education.
[Peer instruction](https://en.wikipedia.org/wiki/Peer_instruction) works better than videos and robo-graded hand-ins,
and discussing problems with peers is a lot better for mental health than sitting in a basement or cubicle
and staring at a screen while you watch the same damn explanation for the fourth time.
There's a place for solo study and review,
but as the saying goes,
if you want to learn further,
learn together.
I'm pretty excited to have the chance to explore ways of helping people do that.

<img src="@root/files/2019/03/minecraft.png" alt="Minecraft" width="80%" class="centered">
