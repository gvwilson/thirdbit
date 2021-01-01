---
title: "Gini Coefficients"
date: 2019-12-23 15:53:00
year: 2019
---

A [Gini coefficient](https://en.wikipedia.org/wiki/Gini_coefficient)
is a simple measure of income equality.
A coefficient of 0 indicates perfect equality (everyone has the same amount),
while a coefficient of 1 indicates perfect inequality
(one person has everything while everyone else has nothing).
Highly unequal countries like South Africa have an (official) Gini coefficient around 0.65,
while less unequal countries like Canada have a coefficient around 0.35.

Gini coefficients can be applied to other things,
such as the number of commits made by each contributor to a Git repository.
I was curious:
how (un)equal are contributions to software projects?
And are contributions to lessons more or less unequal?
To find out,
I crawled the histories of five Software Carpentry lessons
and five widely-used numerical Python libraries.
The results are undoubtedly wrong
(I'm not trying to merge records for people with multiple email addresses, for example),
but I was surprised:

1.  that the coefficients are so similar,
2.  and that they are so unequal when measuring the number of commits,
3.  but that they are so much more equal when counting insertions minus deletions
    (i.e., number of lines contributed),
4.  and that there is so much more variability when counting lines.
    (I don't know if taking the ratio of Gini coefficients is meaningful,
    but it gives an idea of the scale of the disparities.)

I have a stack of background reading to do,
but it's shaping up to be a fun little project.
If you know of other simple ways to measure the evenness of contributorship,
or if you can explain why measuring by contributions and by lines gives such different answers,
I'd enjoy hearing from you.

<table>
  <tr>
    <th>Project</th>
    <th>Gini (Commits)</th>
    <th>Gini (Lines)</th>
    <th>Ratio</th>
  </tr>
  <tr>
    <td><a href="https://github.com/swcarpentry/git-novice/">Git Lesson</a></td>
    <td class="right">0.7867</td>
    <td class="right">0.0306</td>
    <td class="right">25.69</td>
  </tr>
  <tr>
    <td><a href="https://github.com/swcarpentry/python-novice-gapminder/">Python Lesson</a></td>
    <td class="right">0.8250</td>
    <td class="right">0.0982</td>
    <td class="right">8.40</td>
  </tr>
  <tr>
    <td><a href="https://github.com/swcarpentry/r-novice-gapminder/">R Lesson</a></td>
    <td class="right">0.7899</td>
    <td class="right">0.0299</td>
    <td class="right">26.42</td>
  </tr>
  <tr>
    <td><a href="https://github.com/swcarpentry/shell-novice/">Shell Lesson</a></td>
    <td class="right">0.7955</td>
    <td class="right">0.0362</td>
    <td class="right">21.96</td>
  </tr>
  <tr>
    <td><a href="https://github.com/swcarpentry/sql-novice-survey/">SQL Lesson</a></td>
    <td class="right">0.8101</td>
    <td class="right">0.0462</td>
    <td class="right">17.52</td>
  </tr>
  <tr>
    <td><strong>Lessons Average</strong></td>
    <td class="right"><strong>0.8014</strong></td>
    <td class="right"><strong>0.0482</strong></td>
    <td class="right"><strong>20.00</strong></td>
  </tr>
  <tr>
    <td><a href="https://github.com/numpy/numpy/">NumPy</a></td>
    <td class="right">0.9097</td>
    <td class="right">0.0105</td>
    <td class="right">86.89</td>
  </tr>
  <tr>
    <td><a href="https://github.com/pandas-dev/pandas/">Pandas</a></td>
    <td class="right">0.8743</td>
    <td class="right">0.0306</td>
    <td class="right">28.55</td>
  </tr>
  <tr>
    <td><a href="https://github.com/scikit-image/scikit-image/">Scikit-Image</a></td>
    <td class="right">0.8547</td>
    <td class="right">0.2495</td>
    <td class="right">3.42</td>
  </tr>
  <tr>
    <td><a href="https://github.com/scikit-learn/scikit-learn/">Scikit-Learn</a></td>
    <td class="right">0.8836</td>
    <td class="right">0.0492</td>
    <td class="right">179.51</td>
  </tr>
  <tr>
    <td><a href="https://github.com/scipy/scipy/">SciPy</a></td>
    <td class="right">0.8821</td>
    <td class="right">0.0047</td>
    <td class="right">185.94</td>
  </tr>
  <tr>
    <td><strong>Projects Average</strong></td>
    <td class="right"><strong>0.8809</strong></td>
    <td class="right"><strong>0.0601</strong></td>
    <td class="right"><strong>96.86</strong></td>
  </tr>
</table>
