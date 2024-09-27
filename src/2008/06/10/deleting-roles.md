---
title: "Deleting Roles"
date: 2008-06-10
---
One of the ways DrProject improves on <a href="http://trac.edgewall.org">Trac</a> is role-based access control. A role is a set of capabilities, such as WIKI_VIEW or TICKET_EDIT, and users' relationships to projects are represented by triples of the form (user, project, role). It makes administration a lot easier, and once Qiyu Zhu's <a href="http://qzdrproject.wordpress.com/">web-based role editor</a> comes online, it'll be easier still.

But nothing worth having comes without some kind of price. Suppose a portal administrator decides to delete a role—what should happen to people who actually have that role with respect to one or more projects? For example, if the MEMBERSHIP table looks like this:
<table class="centered">
<tr>
<td colspan="3" align="center">MEMBERSHIP</td>
</tr>
<tr>
<td>USER</td>
<td>PROJECT</td>
<td>ROLE</td>
</tr>
<tr>
<td>Greg</td>
<td>Telepathy</td>
<td>developer</td>
</tr>
<tr>
<td>Greg</td>
<td>Antigravity</td>
<td>developer</td>
</tr>
<tr>
<td>Qiyu</td>
<td>Telepathy</td>
<td>developer</td>
</tr>
<tr>
<td>Qiyu</td>
<td>Antigravity</td>
<td>viewer</td>
</tr>
<tr>
<td>Sandeep</td>
<td>Telepathy</td>
<td>viewer</td>
</tr>
</table>
then what should happen if the "viewer" role is deleted?  Options include:
<ol>
  <li>Nothing—leave the MEMBERSHIP table as it is. That seems bad because role values like "viewer" are foreign keys for the CAPABILITY table, and dangling foreign keys would make joins and other operations scary.</li>
  <li>Delete all records from MEMBERSHIP that have the role being deleted. This effectively removes everyone who had that role from those projects (if you don't have an explicit role, you have whatever rights the anonymous user has). This solves the dangling foreign key problem, but now the admin might have to go through all of the users in the portal and give them new roles in those projects one by one.</li>
  <li>Only allow admins to delete roles that aren't being used. This option forces admins to reassign people <em>before</em> deleting the role, so they're easier to find, but still means a lot of hand-work.</li>
  <li>Allow admins to reassign users' roles during the deletion process.</li>
</ol>
We've decided to go with #4, and Liz Blankenship has mocked up a UI for it. Aninteractive version is <a href="http://lizblankenship.com/drproject/admin_panelv3/Configure_roles.html">online</a> (follow the trail of green arrows), or you can check out the screenshots below. Comments would as always be welcome.

<strong>Step 1</strong>

<img src="@root/files/2008/06/step1.png" alt="Step 1" class="centered">

<strong>Step 2</strong>

<img src="@root/files/2008/06/step2.png" alt="Step 2" class="centered">

<strong>Step 3</strong>

<img src="@root/files/2008/06/step3.png" alt="Step 3" class="centered">
