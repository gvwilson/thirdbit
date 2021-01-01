---
title: "Writing Blackboard Plugins"
date: 2006-11-30 12:15:00
year: 2006
---
Two of my students (Billy Chun and Darren Jung) spent the term writing a plugin for <a href="http://www.blackboard.com">Blackboard</a>, the Java-based learning management system (LMS) that the <a href="http://www.utoronto.ca">University of Toronto</a> is moving to.  Here are there experiences:
Billy Chun:

When first attempting to develop a 'Hello World' plug-in for Blackboard, I needed to do some research to find the basic structure of a Blackboard plug-in. The Blackboard developer site (http://www.blackboard.com/extend/dev/) had some sample code available, but only contained the JSP files for the plug-in. Further searching the site led me to the Blackboard SDK, and here was where I obtained that information.

With the SDK in hand, I started to create the plug-in. The sample plug-in found accompanying the SDK provided excellent reference to follow when coding my own. The documentation PDF for the sample provided a fairly simple explanation of the structure of the plug-in and the code found in the sample JSP and XML manifest files. Although this documentation followed a specific method in generating the packaged plug-in, it was still simple to follow.

Two difficult areas when learning Blackboard were in reading the general developer documentation and finding APIs. The general developer documentation explained the plug-in structure quite well, but the syntactic details for some aspects were puzzling. Two examples of this ambiguity were in the explanation for the bb-manifest file and tag libraries. The documentation did provide explanation for what was or was not required but gave fairly brief information about items like expected input values. I had to google to find details on this. Next, finding APIs for Blackboard classes would have been difficult if it were not for the help of Andrew Wang (Blackboard developer over at UTM). No where on the Blackboard developer site could I find a link to APIs.

A good suggestion I would make when learning Blackboard would be to get a demo of the system with someone experienced in developing Blackboard plug-ins. The demo Andrew presented really gave me a head start as a beginner into creating future plug-ins.

Darren Jung:

Experiencing blackboard was a great oppotunity for me. In my case, I started off late because of my personal situation, and moreover, previously I had no experience with jsp files and javascript. So I was frustrated, I didn't know what's going  on, I even had no idea what blackboard is!

Billy, my partner of this project, helped me a lot. He showed me where to  get references, and explained me about that. So after that I felt that I'm going to  the right direction.

My difficulty happened at very first : I had no idea at all, I felt like lost. Getting help from Billy was a great choice, because sometimes when anybody is placed at whole new world, he/she will try to understand what's going on in that world. And that takes a LOT of time if you're alone and don't get help from people in that new world.

From that, I've written my bb_manifest.xml and .jsp files. Trying to get 'Hello world' from the server was quite easy. One more comment for users of Mac OSX. I need to investigate why this is so later, but I've found that when I build .war file on my windows XP machine, the file size is well below 70kb. It took about 5 seconds to upload building block. But on my Mac machine, (Macbook 2.0GHZ) .war file has size of about 20 megabytes! It took more than 10 minutes to upload plug-in. I guess this is partly because windows uses .zip and mac uses .jar files as external  library, but I'm not sure at this point.
