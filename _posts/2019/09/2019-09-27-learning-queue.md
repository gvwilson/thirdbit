---
layout: post
title: "Managing a Queue of Learners"
date: 2019-09-27 06:37
---

More than 200 people will have taken [RStudio instructor training](https://education.rstudio.com/trainers/) by the end of this year.
Unlike many courses,
participants don't sign up for a specific class at a fixed time;
instead,
they [apply to take part](https://docs.google.com/forms/d/e/1FAIpQLSdnybZ-Zs64QE1h7bk67uRs1UCUi1Tibi3noefyStrTHplSDA/viewform)
and we then arrange times to accommodate as many of them as we can.

At present, we are using a home-brewed mix of Google Forms and scripts to track who wants what kind of training,
when they are going to get it,
when they actually *did* take part (if they have),
what happened afterward,
and whether or not they have paid us.
We'd like to use an off-the-shelf solution,
but have explored and ruled out several possibilities:

1. **Storing information in a CRM like Salesforce.**
   These are contacts,
   and it allows us to define workflows that people move through,
   but (a) seats are expensive
   and (b) it doesn’t help us manage facts like "Jane Bloggs has completed two exams but still needs to do a third".

1. **An LMS like Blackboard or Lessonly.**
   Most of what they provide is irrelevant to our needs—we aren’t handing out grades—and they also don't manage queues of registrants.
   It also looks like we'd have to write our own glue to connect the information from the application form
   to the LMS's database.

1. **Event management systems like Eventbrite and Cvent** seem the closest fit,
   but so far I haven't figured out how to get them to manage application queues and post-event workflows.

Requirements

1. All information storage is GDPR compliant.
1. The system can manage queues for several different kinds of training.
1. People can apply for training without having to create YAFA (yet another account).
1. We can customize the information we collect from people when they apply,
   and that information feeds directly into a database we can easily query and integrate.
1. We can set up particular training events and offer spots to specific people,
   who can then accept or decline.
   If they decline, they remain in queue.
1. We can mark people as "no longer interested" so that we don't bother them again.
1. We can mark people as having completed specific trainings or tasks (i.e., exams).
1. We can search by various criteria,
   e.g., "Who has done the teaching course but hasn’t yet completed the tidyverse exam?"
1. It's easy to integrate the tool with invoicing systems
   so that people can be invoiced when they get a spot
   *without* any information having to be copied manually from one system to another.

So: what's out there?
