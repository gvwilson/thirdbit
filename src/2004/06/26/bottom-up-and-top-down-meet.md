---
title: "Bottom Up and Top Down Meet"
date: 2004-06-26
---
Among other Helium tasks, I've working on has been some rough screenshots of what our web interface might end up looking like. What I've found interesting about the very high-level design process, is that I kept needing to go lower and lower in order to make the design steps easier. And all of a sudden found myself hitting where those doing the low-level design (and working their way higher) were sitting.

The screenshots started as doodles on the whiteboard. These doodles were soon converted into paper format, to make them more permanent. But as we needed them changed more and more frequently, it became difficult to manage them in paper format, so I made some rough HTML pages.

But then I started finding it tiresome to create a similar top and sidebar for every page, so I wrote a quick hacky Python script to generate these automatically. But as the pages developed in complexity, simply generating a common top and sidebar wasn't enough: I needed more control over the pages. So I started writing some Python classes to represent projects that the mock user belonged to, so that I could just tweak the class objects in order to make site-wide changes easily.

Anyway, to make a long story short, this week I've found my hacky scripts inadequate again. What I really need are some User objects, and Project objects, and Membership objects, and Message objects and Conversations, and…well…basically exactly what we've been designing to represent the backend of Helium. I finally hit a point where I needed the backend to drive the frontend: and what I needed matched exactly with what we'd designed to build.

To me, this is cool. Means we're doing <em>something</em> right, at least.

<hr />

Greg Wilson adds: one of Helium's must-have features is a scripting interface, so that instructors can quickly write little programs to add a hundred projects, file an identical bug report against each, and so on. Michelle has discovered that developers have the same need: once <em>anything</em> is running, you can accelerate further development by scripting it.
