---
title: "It Shouldn't Still Hurt This Much"
date: 2011-06-13
---
Silly me: I want to use <a href="http://rapidsvn.tigris.org/">RapidSVN</a> on Windows Vista. Which means I need to install <a href="http://winmerge.org/">WinMerge</a> so that I can view and merge diffs. So I do that, then try to diff a file that's in my working copy with the HEAD that's in the repo. Which fails because it can't create a tunnel. Say what? Oh–it can't create a tunnel because I haven't set an environment variable called SVN_SSH to point to an SSH client. Oh. OK. Let me go and download <a href="http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html">plink.exe</a> and then set an environment variable to point to it (pop quiz: how many Windows users know how to set environment variables these days?) Hm. That still doesn't work. I wonder why not? The error message doesn't tell me, so I've gone from, "It would be nice to view diffs graphically when I'm pair programming" to shaving a yak in less than five minutes.

And yes, I'm sure I could figure it out. My point is, I shouldn't have to.

<em>Later: several people have left comments saying (roughly), "Well, what do you expect from Windows?" Personally, I don't think any honest person can claim that Mac OS X, or any Linux distro, is any easier. The pain might show up in different places, at different times, but it's still there all too often.</em>
