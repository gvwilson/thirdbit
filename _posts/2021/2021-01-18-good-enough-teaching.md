---
title: "Good Enough Teaching"
date: 2021-01-18
year: 2021
---

I'm blocked by a tech issue at work right now. I should do diagrams for [*Software Design by Example Using JavaScript*]({{'/sdxjs/' | relative_url}}), but instead I'm going to talk about good enough practices in teaching. Years ago we wrote a paper called "[Best Practices for Scientific Computing](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)". A lot of people found it useful, but a lot of other people found it intimidating (like, triathlete's daily workout intimidating), so we followed it up with "[Good Enough Practices in Scientific Computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)" to describe more approachable things that the majority could do right away.

The "Good Enough" paper did more than just describe "start here" practices. It also told readers, "You don't have to be running CI on Docker with 100% test coverage to be a good person. It's OK if you work this way." Lang's book *[Small Teaching](https://www.wiley.com/en-ca/Small+Teaching%3A+Everyday+Lessons+from+the+Science+of+Learning-p-9781118944493)* did the same for me when I read it—it said, "It's OK not to do _all_ the right things." 
I say this myself in [the instructor training class I run for RStudio](https://drive.google.com/drive/folders/13ohFt3D0EJ5PDbMaWTxnHH-hwA7G0IvY) and in *[Teaching Tech Together](https://teachtogether.tech/)*, but I get pushback. Ironically, some of the same education experts who would tell you to start novices with a simplified mental model of any other topic will get very huffy if you leave out the details when it comes to teaching and learning.

All of which is preface to me saying, here are the things I think the average programmer or data scientist can do to improve their teaching right away, _in order_. I'd be grateful for additions and corrections.

1.  Add descriptive text to your slides. This helps people with vision or language comprehension issues; it also helps your future self (why do I have a picture of the Eiffel Tower labeled "Not Leaning (Yet)"?), but most importantly, it makes your material discoverable. Search engines struggle with images, diagrams, and spatially-significant layout of text. Give them prose to search so people can find your stuff.

2.  Use formative assessment every 5-15 minutes while teaching. Each one should take at most a minute to do (so it doesn't derail teaching) and be designed to check for flaws in learners' mental models rather than simple factual recall.

3.  Always tell them how long they have to work on an in-class exercise or how long a homework problem should take; keep notes of how long the former actually took (and ask them to report the latter) so that you can correct your optimism.

4.  Have learners share work in real time. Google Docs or HackMD's shared in groups of 5-15 works pretty well; if you're teaching in person (remember that?), have a few people join a Zoom call with you so that they can share their screen with you and you can project it for the class. (You'd have them show each other what they've made in a drawing or cooking class, wouldn't you?)

5.  Keep track of who has spoken so that you can distribute attention fairly throughout the class. Take-down stickies on laptops works in person; online, I keep a text file with learners' names and cross them off.

6.  Write the code in front of them so you can follow up their "what if" questions, and so that they learn how to use the tools. (Some people use VS Code or the RStudio IDE 2-10 times more effectively than others, and it adds up very quickly.)

7.  When you make a mistake live coding, always (a) tell them how you know it's wrong, (b) talk through how you diagnose the problem, (c) explain the fix, and (d) point out the difference in the correct behavior or output.

Now here's the sting in the tail: take a moment and compare the tutorials for your favorite software to these seven practices. If the tutorial scores more than 3/7, please give me a shout—I'd really like to see it.
