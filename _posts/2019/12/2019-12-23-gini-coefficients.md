---
title: "Gini Coefficients"
date: 2019-12-23 15:53:00
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

1.  that the coefficients are so similar, and
2.  that they are all so unequal.

I have a stack of papers to dig through as background reading,
but it's shaping up to be a fun little projects...

<table>
  <tr>
    <th>Project</th>
    <th>Gini Coefficient</th>
  </tr>
  <tr>
    <td><a href="https://github.com/swcarpentry/git-novice/">Git Lesson</a></td>
    <td>0.786</td>
  </tr>
  <tr>
    <td><a href="https://github.com/swcarpentry/python-novice-gapminder/">Python Lesson</a></td>
    <td>0.825</td>
  </tr>
  <tr>
    <td><a href="https://github.com/swcarpentry/r-novice-gapminder/">R Lesson</a></td>
    <td>0.790</td>
  </tr>
  <tr>
    <td><a href="https://github.com/swcarpentry/shell-novice/">Shell Lesson</a></td>
    <td>0.795</td>
  </tr>
  <tr>
    <td><a href="https://github.com/swcarpentry/sql-novice-survey/">SQL Lesson</a></td>
    <td>0.810</td>
  </tr>
  <tr>
    <td><strong>Lessons Average</strong></td>
    <td><strong>0.837</strong></td>
  </tr>
  <tr>
    <td><a href="https://github.com/numpy/numpy/">NumPy</a></td>
    <td>0.910</td>
  </tr>
  <tr>
    <td><a href="https://github.com/pandas-dev/pandas/">Pandas</a></td>
    <td>0.874</td>
  </tr>
  <tr>
    <td><a href="https://github.com/scikit-image/scikit-image/">Scikit-Image</a></td>
    <td>0.855</td>
  </tr>
  <tr>
    <td><a href="https://github.com/scikit-learn/scikit-learn/">Scikit-Learn</a></td>
    <td>0.884</td>
  </tr>
  <tr>
    <td><a href="https://github.com/scipy/scipy/">SciPy</a></td>
    <td>0.882</td>
  </tr>
  <tr>
    <td><strong>Projects Average</strong></td>
    <td><strong>0.845</strong></td>
  </tr>
</table>
