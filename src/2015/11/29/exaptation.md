---
title: "Exaptation and the Future of Software Engineering"
date: 2015-11-29
---
<p>
  Back in the 1980s,
  we knew that software engineering was going to become mathematically rigorous
  like electrical and civil engineering.
  Where they used calculus to figure out an antenna's gain
  and whether a dam would stand up,
  we would use logic and discrete mathematics to prove that programs were correct.
</p>
<p>
  That obviously hasn't happened,
  and isn't going to any time soon<sup><a href="#1">1</a></sup>.
  However,
  I think software engineering actually <em>is</em> going to be mathematized
  over the next few years.
  It's just not going to be the discrete math that we expected;
  instead,
  it's going to be statistics,
  and instead of proving programs correct,
  tomorrow's software engineers are going to analyze data from real projects
  to predict those projects' futures.
</p>
<figure class="center">
  <img src="@root/files/2015/11/obi-wan.jpg" alt="Obi Wan" class="centered">
  <figcaption>This isn't the math you're looking for.</figcaption>
</figure>
<p>
  To explain why,
  I need to borrow an idea from evolutionary biology.
  According to Wikipedia,
  "<a href="https://en.wikipedia.org/wiki/Exaptation">Exaptation</a>…describes
  a shift in the function of a trait during evolution.
  For example,
  a trait can evolve because it served one particular function,
  but subsequently it may come to serve another."
  Bird feathers are a classic example:
  they probably evolved to help dinosaurs stay warm and for display,
  and were only then adapted for flight.
</p>
<p>
  Exaptation (also called "pre-adaptation") is occurring right now
  in thousands of software companies.
  Every day,
  programmers are gathering and analyzing data about how their web sites are used.
  Those statistical methods can also be used
  to predict when the next release will be ready to ship
  based on historical data about past releases.
  And thanks to open source and the Internet,
  software engineers now have the data they need to build useful models.
  Where it tooks pioneers like <a href="https://en.wikipedia.org/wiki/Barry_Boehm">Barry Boehm</a>
  months or years to collect data back in the 1970s,
  today's developers can download and analyze information from thousands of projects.
</p>
<p>
  Mature methods now exist as well.
  The <a href="http://2004.msrconf.org/">first conference on mining software repositories</a>
  was held in 2004;
  by <a href="http://2015.msrconf.org/">2015</a>,
  the number and rigor of submissions had increased significantly.
  New books like
  <a href="http://www.amazon.com/Art-Science-Analyzing-Software-Data/dp/0124115195/"><cite>The Art and Science of Analyzing Sofware Data</cite></a>,
  <a href="http://www.amazon.com/Sharing-Data-Models-Software-Engineering/dp/0124172954/"><cite>Sharing Data and Models in Software Engineering</cite></a>,
  and the upcoming <cite>Perspectives on Data Science for Software Engineering</cite>
  show that this community can answer questions that matter.
</p>
<p>
  As <a href="@root/2014/10/02/a-better-software-engineering-course/">I argued last year</a>,
  the missing piece is an undergraduate textbook
  to organize this and make it digestible to 20-year-olds
  who aren't ready to read primary research literature.
  Once that is in place,
  software engineering will finally become the mathematically rigorous discipline
  it has always aspired to be,
  just not in the way we imagined.
</p>
<p>
  Footnotes:
</p>
<ol>
  <li id="1">
    <p>
      Despite decades of work,
      formal methods are still too hard for everyday use.
      Programmers can't learn enough in their first course to solve real problems,
      and once they do master techniques powerful enough to be useful,
      those techniques are too labor-intensive to be economical for all but the most exacting needs.
    </p>
  </li>
</ol>
