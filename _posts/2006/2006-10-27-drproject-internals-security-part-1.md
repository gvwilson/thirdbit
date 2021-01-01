---
title: "DrProject Internals: Security Part 1"
date: 2006-10-27 10:36:52
year: 2006
---
Last time around, I described the architecture of a very simple wiki system that stored pages, along with their histories and meta-data, in a database, and let users view and edit those pages over the web.  In an ideal world, the next step would be to add either a work ticketing system, or an interface to version control.

But our world is far from ideal: there are pranksters out there, and spammers, and outright villains, too.  The next step in our rational reconstruction of <a href="http://www.drproject.org">DrProject</a> is therefore to worry about security.  Bitter experience shows that it's hard---some would say impossible---to make systems secure after the fact.  Security must be designed in, and tested, right from day one.

The simplest useful model of security breaks the problem down into authentication, authorization, and access control. <em>Authentication</em> is the process of binding a session to a stored identity.  This is <em>not</em> the same as establishing who the user is: people can easily share user IDs and passwords, and even biometric systems can be spoofed.  Instead, authentication takes something the user is, has, or knows, like a fingerprint, password, or smart card, and figures out which of the user profiles stored in the system it corresponds to.

<em>Authorization</em> is the determination of who can do what. Can user X read file Y?  Can she append data to it?  Delete it?  Give someone else permission to do any of these operations?  Lastly, <em>access control</em> is the enforcement of these rules; it's what prevents X from reading things she's not allowed to, no matter how cleverly she asks.

The first thing this simple security model does is help us think about possible attacks.  To break in, an attacker must:
<ul>
	<li>convince the system she's someone she's not;</li>
	<li>get permissions she isn't supposed to have; or</li>
	<li>bypass the controls that are supposed to prevent her from doing something.</li>
</ul>
Secondly, this model can help us build a domain model---an abstract picture of what a security system needs to contain.  Here are some of the concepts we have so far:
<ul>
	<li><em>User profile</em>: a unique electronic identity, such as a login account.  A single human being may have many profiles in the system; many human beings may have access to a single profile.</li>
	<li><em>Credentials</em>: what an actual user is, has, or knows that binds her to a user profile.</li>
	<li><em>Authentication mechanism</em>: something that finds the user profile corresponding to a set of credentials.  Every authentication mechanism needs a way to say, "I don't recognize these credentials." This is usually done either by signalling an error, or by returning a specially-marked user profile.</li>
	<li><em>Capability</em>: something that can be done to something in the system, such as reading the contents of a particular file, changing the "last modified" time of a particular directory, deleting a particular user profile, and so on.  The word "particular" is important here, because the system needs to distinguish the capability of deleting file X from the capability of deleting file Y (or all files).</li>
	<li><em>Permission</em>: a pairing of a user profile and a capability, i.e., a representation of user X's right to perform operation Z.</li>
</ul>
Let's start with user profiles.  Most web-based systems start off by managing these themselves: users create uniquely-named accounts and choose passwords, which are then stored in the system's database. These schemes run into all kinds of trouble as the system grows:
<ol>
	<li>People have a hard time remembering dozens of different account names and passwords, so they either forget them (which adds to the user support burden), or re-use them (which means that when one system is compromised, others can be broken as well).</li>
	<li>The more places user information is stored, the harder it is to keep everything up to date.  In our department, for example, we have to keep track of over a thousand students as they add and drop courses, change degree programs, and so on.  Keeping track of all that is hard; keeping track of it twice would be a nightmare.</li>
	<li>Managing passwords and other credentials requires a lot of tricky code.  On one of the systems I used to administer, user passwords had to be at least eight characters long, with at least two non-alphabetic characters.  They couldn't contain dictionary words or use simple spe11ing trix, had to be changed every three months, and couldn't be recycled within a year.  This is <em>not</em> code you want to have to write twice...</li>
</ol>
For all these reasons, <a href="http://www.drproject.org">DrProject</a> doesn't manage accounts itself.  Instead, it passes the credentials users give it (such as IDs and passwords) to an external program called <code>validate</code>. Here in Toronto, that program checks those credentials against the host Linux system's password file (Figure 1).  At Queen's, on the other hand, those credentials are checked against the university-wide Kerberos system.

Time for a quick FAQ:

<dl> <dt>Why use an external program?  Why not just have the CGI program check the credentials?</dt> <dd>The <a href="http://www.drproject.org">DrProject</a> CGI program runs under the same user ID as the web server.  Typically, this is a dummy account called <code>www-data</code> or <code>apache</code> which has very few privileges (to limit the damage an attacker can do by compromising the web server).  We didn't want to give the web server account access to the password file, so we created a separate program that uses Unix's <code>setuid</code> mechanism to run under a different identity.</dd> <dt>How does <a href="http://www.drproject.org">DrProject</a> communicate with <code>validate</code>?</dt> <dd><a href="http://www.drproject.org">DrProject</a> writes the user ID and password to <code>validate</code>'s standard input, and <code>validate</code> then returns either 0 or 1.  It would have been simpler to pass the user ID and password as command-line arguments, i.e., to run <code>validate</code> as a sub-process with <code>validate myName myPassword</code>.  However, this would create a security hole: if an attacker with an account on the host ran the <code>ps</code> command at the right moment, with the right flags, she could see <code>validate</code>'s arguments, and harvest the user ID and password.  Also, more complex credentials such as digital certificates can't be represented as short strings. </dd> <dt>Does everybody with a Unix account automatically have access to <a href="http://www.drproject.org">DrProject</a>?</dt> <dd>No.  The administrator still has to tell <a href="http://www.drproject.org">DrProject</a> which of the underlying Unix accounts to recognize.  However, that's <em>all</em> the administrator has to do: when the user changes her Unix password, <a href="http://www.drproject.org">DrProject</a> automatically "sees" the change.</dd> </dl>Now that our user has authenticated, we can move on to---oops, wait a second.  HTTP is a stateless protocol: each request is completely separate from each other.  We don't want users to have to re-send their credentials every time they click on a link, so we have to find some way to keep track of them after they have logged in.  (In fact, having the system keep track of them after they provide their credentials is what we <em>mean</em> by "logging in".)

The standard way to do this is with <em>cookies</em>.  A cookie is a short piece of text that can be passed back and forth in the headers of HTTP requests and responses.  If a CGI program puts a cookie in the header of an HTTP response, then the client can send it back with the next request.  The technical term for this is a <em>nonce</em>; like half of a torn playing card, someone can use it to <em>re</em>-establish their identity at some future point.

Back in the bad old days, programmers sometimes used real data as cookies: for example, I remember a system (I actually wrote it *cough*) that used the user ID as the cookie value.  Of course, this mean that anyone who knew how to create an HTTP request could impersonate anyone else.  Using a sequence of numbers, such as 1000, 1001, 1002, ... doesn't help: an attacker can still:
<ul>
	<li>log in;</li>
	<li>look at her cookie value;</li>
	<li>add or subtract one; and</li>
	<li>have good odds of hijacking someone else's session.</li>
</ul>
Most modern systems therefore generate a random number (or random string), and use that as a cookie.  Internally, such systems store a dictionary that maps cookie values to sessions; each session has a reference to a user profile, and any other data the system needs to remember.  One piece of data is when the cookie was generated: if the system is presented with a cookie that's a week old, it may decide that someone is trying a <em>replay attack</em>, and refuse to accept it.  (This is why so many web systems throw you out if you're idle for too long.)

By themselves, randomly-generated session IDs aren't enough to make the system secure, because attackers can use packet sniffers and other tools to eavesdrop on network traffic.  We actually offer a course (CSC309: Web Programming) that teaches students the principles behind this, so we had to ensure that <a href="http://www.drproject.org">DrProject</a> wasn't vulnerable to such attacks.  The solution we adopted was simple: every connection to <a href="http://www.drproject.org">DrProject</a> uses HTTPS, the encrypted version of HTTP.  Encrypting and decrypting messages does slow the system down, but (a) the slowdown isn't very large (a few percent), and (b) slowing down is better than plowing into a lamppost.

One last note on sessions: most people never bother to log out of systems that are less important to them than their bank or dating service.  "Stale" sessions can therefore accumulate in the database over time.  The space these take up isn't much of a concern (unless you're Hotmail, Yahoo, or one of the other giants), but each stale session is another point of attack.  <a href="http://www.drproject.org">DrProject</a> and systems like it therefore have to implement some garbage collection mechanism that sweeps through the sessions periodically, closing and deleting any that have expired.

Implementing this would be easy if <a href="http://www.drproject.org">DrProject</a> was a long-running process: we'd just set a timer, and take a couple of seconds every ten minutes or so to check the timestamp on every open session.  But <a href="http://www.drproject.org">DrProject</a> is a CGI: it only runs when a request comes in.  Our choices were therefore:
<ol>
	<li>have it do a little garbage collection each time it ran; or</li>
	<li>use <code>cron</code> to run a separate program every ten minutes or so.</li>
</ol>
We chose the first option, since it was one less thing for the sys admin would have to install, configure, and remember to restart.  The downside is that every once in a while, a user's attempt to view a page is delayed by a second or two.  However, this happens anyway because of network traffic, so people don't notice.

Next time: how we implemented authorization and access control.
