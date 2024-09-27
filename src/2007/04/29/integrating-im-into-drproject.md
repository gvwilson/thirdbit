---
title: "Integrating IM into DrProject"
date: 2007-04-29
---
We'd like to try to integrate instant messaging into a software project management portal like DrProject, so that users who prefer IM to email will find DrP more appealing (i.e., use it of their own free will), and (more importantly) so that their conversations won't evaporate, but instead will stick around and be searchable.  Here are a few random thoughts:
<ol>
  <li>Students have made it clear that they'll only use it if they can use their current favorite IM clients—no downloads, no switching to Trillian, no in-browser chat.</li>
  <li>Students have also made it clear that they're worried about privacy.  IM conversations tend to wander a lot, and they don't want Big Brother listening in to their griping about the course and prof.</li>
</ol>
These are the two big ones: if we can't solve both of them, students will pay lip service to in-portal IM, then go back to doing what they do now (swap IM handles at the start of term, do all their talking off the record, then argue three months later about who actually said/promised/invented what).

Here are some other thoughts:
<ol start="3">
  <li>In-portal IM will be a <em>lot</em> more powerful if participants can use wiki syntax in their messages to hyperlink painlessly to tickets, wiki pages, etc.  Assuming traffic is routed through a server built into DrProject, this shouldn't be too hard (parse as the message passes through, insert appropriate linkage)—except that it means everyone <em>except the original author</em> will get the hyperlink, while she will not.  Hm…</li>
  <li>How do you search IM logs?  A two-student, one-term project can be treated like one long document, but what about something larger (10 students at a time for two years with heavy traffic)?  Has anyone looked into pagination or segmentation for searching long-lived narratives?</li>
  <li>How do you link into IM logs?  If I want to refer to a portion of an IM conversation from a wiki page or ticket, what's the link syntax? Again assuming all traffic is routed through a server built into DrProject, I could enumerate the messages, and invent some link syntax for individual messages or message ranges…  Is there a better way?</li>
  <li>IM meetings tend to be unproductive and frustrating because of time lag problems—I think we're done topic A, so I move on to item B, not knowing that Jane is still adding a comment on A, which now appears interleaved with the start of B.  The way I handle this in conference calls is to do a roll call (basically, ask everyone if they're ready to move on).  The IM equivalent would be support for some kind of voting, which would be useful for more than just keeping the meeting moving.  I <em>think</em> it could be layered on top (have a bot at the server parsing the message text looking for roll calls and votes); the problem is that many people multi-task while they're in online meetings, so there'd likely be long lags waiting for people to respond.  Would social pressure fix this over time?</li>
</ol>
