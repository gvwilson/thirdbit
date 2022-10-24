---
title: "Rationalizing the Admin Interface"
date: 2008-02-15 08:40:25
year: 2008
---
Anyone who has ever worked with me knows that I should <em>not</em> be allowed to design user interfaces. Nature, nurture---dunno why, but anything that I find intuitive and pleasing leaves most people queasy and confused.

Which is why I'm appealing for help.  <a href="http://www.drproject.org">DrProject</a>'s browser-based administration interface is invaluable, but we're finding the workflow frustrating. For example, in order to add a new user, make her a member of the 'All' and 'fribble' projects, and turn on mail forwarding for her for both of those lists, I have to:
<ol>
	<li>Go to the 'add user' page.</li>
	<li>Fill in her user ID, default email address, real name, and affiliation.</li>
	<li>Submit.</li>
	<li>Go to the 'list users' page (the refreshed 'add users' page tells me her user ID has been added, but that ID isn't a hyperlink to a page where I can administer her information, and even if it was, what would I do if I was adding a bunch of people at once, which the 'add user' page also supports?).</li>
	<li>Scroll down to her ID.</li>
	<li>Click on it to bring up a page where I can edit her personal settings.</li>
	<li>Add her to the 'All' project as a 'viewer' and submit.</li>
	<li>Add her to the 'fribble' project as a 'developer' in the refreshed page and submit.</li>
	<li>Scroll down to the bottom of the refreshed page and tick off the boxes, turn on mail forwarding for her for 'All' and 'fribble', and submit.</li>
</ol>
Other tasks are similarly arduous. The screens in question are below the cut; if you have suggestions for redesign, I'd love to hear them.

<img src="{{'/files/2008/02/add-users.png' | relative_url}}" alt="Add Users" />

<hr />

<img src="{{'/files/2008/02/list-users.png' | relative_url}}" alt="List Users" />

<hr />

<img src="{{'/files/2008/02/create-projects.png' | relative_url}}" alt="Create Projects" />

<hr />

<img src="{{'/files/2008/02/project-list.png' | relative_url}}" alt="List Projects" />

<hr />

<img src="{{'/files/2008/02/instance-settings.png' | relative_url}}" alt="Instance Settings" />
