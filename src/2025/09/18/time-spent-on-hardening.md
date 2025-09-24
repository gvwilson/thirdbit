---
title: Time Spent on Hardening
date: 2025-09-18
---

I recently received mail from someone working on a software-based approach to fault tolerance.
Their tool makes applications more reliable,
but they think it also makes developers more productive
by reducing the amount of error detection and handling code they need write.

They have never been able to find research
that quantifies how much time developers spend on code for detecting and handling problems
relative to the effort for the "happy path".
they know it's substantial,
and is (probably) increasing as applications become more distributed,
but the only number they've found is from a 1995 book called
*[Software Fault Tolerance](https://isbnsearch.org/isbn/9780471950684)*,
where Dr. Flaviu Cristian says that it often accounts for more than two-thirds of code in production systems.

So I asked a dozen researchers I met through [It Will Never Work in Theory](https://neverworkintheory.org)
if they knew of anything,
and the answer was, "No, there isn't anything that specifically addresses that question."
This strikes me as odd,
because it wouldn't be hard to measure
and the answer would be interesting.

People do throw around questionable numbers about the cost of bugs and bug fixing,
e.g., claim that companies [$2 trillion in 2020](https://www.it-cisq.org/cisq-files/pdf/CPSQ-2020-report.pdf).
Here are some other related resources my contacts were able to give me:

-   [A Systematic Review on Software Robustness Assessment](https://dl.acm.org/doi/10.1145/3448977)

-   [Exceptional Behaviors: How Frequently Are They Tested?](https://conf.researchr.org/details/ast-2025/ast-2025-papers/9/Exceptional-Behaviors-How-Frequently-Are-They-Tested-)

-   [Automating Chaos Experiments in Production](https://dl.acm.org/doi/10.1109/ICSE-SEIP.2019.00012)

-   [The Exception Handling Riddle: An Empirical Study on the Android API](https://www.sciencedirect.com/science/article/abs/pii/S0164121218300724)

-   [Unveiling Exception Handling Guidelines Adopted by Java Developers](https://ctreude.ca/wp-content/uploads/2019/01/saner19.pdf)

-   [Today Was a Good Day: The Daily Life of Software Developers](https://ieeexplore.ieee.org/document/8666786):
    Developers spend about 11% of their time on debugging and bugfixing
    with some days being dedicated to the task (up to 32%)
    and some days being dedicated to meetings and collaboration (4-6%).
    You can also add time spent on testing (up to 16%).

-   [The Work Life of Developers: Activities, Switches and Perceived Productivity](https://ieeexplore.ieee.org/document/7829407)

-   [I Know What You Did Last Summer - An Investigation of How Developers Spend Their Time](https://ieeexplore.ieee.org/document/7181430)

-   [Unveiling Exception Handling Guidelines Adopted by Java Developers](https://arxiv.org/abs/1901.08718)

-   [Studying the Evolution of Exception Handling Anti-Patterns in a Long-Lived Large-Scale Project](https://journal-bcs.springeropen.com/articles/10.1186/s13173-019-0095-5)

-   [A Study on the Effects of Exception Usage in Open-Source C++ Systems](https://plg.uwaterloo.ca/~migod/papers/2019/scam19.pdf)

-   [The Corrective Commit Probability Code Quality Metric](https://arxiv.org/abs/2007.10912)

-   [Debugging Revisited: Toward Understanding the Debugging Needs of Contemporary Software Developers](https://ieeexplore.ieee.org/document/6681382)

-   [Designing robust Java programs with exceptions](https://dl.acm.org/doi/abs/10.1145/355045.355046)

-   [Moonstone: Support for Understanding and Writing Exception Handling Code](https://marybethkery.com/projects/ErrorHandling/kistner_vlhcc17.pdf)

-   [Understanding Exception Handling: Viewpoints of Novices and Experts](https://ieeexplore.ieee.org/document/5383375)

-   [Studying the Relationship Between Exception Handling Practices and Post-Release Defects](https://dl.acm.org/doi/10.1145/3196398.3196435)

-   [Where Do Developers Log?](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/ICSE-2014-SEIP-Where-Do-Developers-Log-An-Empirical-Study-on-Logging-Practices-in-Industry.pdf)

-   [What Leads to a Confirmatory or Disconfirmatory Behavior of Software Testers?](https://ieeexplore.ieee.org/abstract/document/9179007)

Again,
the fact that we don't have reliable figures for this strikes me as odd.
As one of them pointed out,
while everyone is throwing LLMs at often artificial and academic problems
and then claiming to have improved some arbitrary metric X% over a random baseline,
we still don't know fairly basic things about software development.

*My thanks to everyone who responded to my late-night email about this.*

**Later:**
this post made the #8 spot on Hacker News.
It must have been a slow day…

<a href="@/files/2025/hacker-news-hardening.png"><img src="@/files/2025/hacker-news-hardening.png" alt="Hacker News" width="400px"></a>
