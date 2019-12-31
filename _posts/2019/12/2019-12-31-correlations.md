---
title: "Correlations"
date: 2019-12-31 01:31:00
---

A [previous post]({{site.github.url}}/2019/12/23/gini-coefficients.html)
presented the Gini coefficients for contributions to 10 Git repositories
measuring number of commits and number of lines committed.
The two were very different,
and the reason appears to be an error in how I calculated number of lines committed.
Summing (insertions - deletions) per commit doesn't account for splitting, combining, or renaming files,
or for moving lines from one file to another.
None of the libraries I've looked at
([GitPython](https://gitpython.readthedocs.io/),
[pygit2](https://www.pygit2.org/),
or [PyDriller](https://pydriller.readthedocs.io/))
will do this on their own,
so I have switched from summing lines to looking at the final state of the repository using `git blame`,
which identifies the author of the last change made to each line of every file.
Measuring the Gini coefficient that way tracks the Gini coefficient for number of commits per author
much more closely:

| filename | commits | blame |
| :------- | -----------: | ---------: |
| git-novice | 0.7866 | 0.9157 |
| python-novice-gapminder | 0.8249 | 0.9272 |
| r-novice-gapminder | 0.7898 | 0.9321 |
| shell-novice | 0.7955 | 0.9655 |
| sql-novice-survey | 0.8100 | 0.9157 |
| numpy | 0.9097 | 0.9624 |
| pandas | 0.8742 | 0.9443 |
| scikit-image | 0.8547 | 0.8673 |
| scikit-learn | 0.8836 | 0.9162 |
| scipy | 0.8821 | 0.9464 |

But now I have another problem.
If I count the number of commits per author in each repo,
and the number of lines in each repo credited to each author by `git blame`,
I can then calculate the correlation between them in two ways:
the [Pearson correlation](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
(which uses the actual values)
and [Spearman's rank correlation](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)
(which uses the order of the values rather than the values themselves).
For 9 of the 10 repos,
the two measures of correlation track reasonably well.
For one of them,
though,
the Pearson correlation is moderately positive (about 0.35)
while the Spearman rank correlation is moderately negative (about -0.26).

| stem | pearson | spearman |
| :--- | ------: | -------: |
| git-novice | 0.3572 | -0.2618 |
| python-novice-gapminder | 0.2018 | 0.2569 |
| r-novice-gapminder | 0.5725 | 0.5342 |
| shell-novice | 0.4187 | 0.3468 |
| sql-novice-survey | 0.2921 | 0.2248 |
| numpy | 0.6003 | 0.4140 |
| pandas | 0.5810 | 0.4752 |
| scikit-image | 0.6206 | 0.5822 |
| scikit-learn | 0.5853 | 0.3980 |
| scipy | 0.6565 | 0.4850 |

<div align="center">
  <img src="{{site.github.url}}/files/2019/12/correlation.svg" width="500" alt="Correlation of correlations" />
  <p>Correlation of correlations</p>
</div>

My question is,
what does this difference between the two types of correlation tell me?
For example,
if the mean of a distribution is much higher than the median
then I know that the distribution has a few high-valued outliers
(think income distribution in the US).
What general intuition should I have about a positive Pearson's correlation
coupled with a negative Spearman's rank correlation and why?

Addendum: if it helps,
here are the scatter plots of commits vs. lines (log scale on both axes)
for three repositories.
The first is NumPy (a large code repository);
the second is the Software Carpentry lesson on the Unix shell,
and the third is the lesson on Git (which has the puzzling mis-match between correlations).
I can share others,
but honestly,
nothing jumps out in any of them.

<div align="center">
  <img src="{{site.github.url}}/files/2019/12/commits-lines-numpy.svg" width="500" alt="NumPy commits vs. lines" />
  <p>NumPy commits vs. lines</p>
</div>

<div align="center">
  <img src="{{site.github.url}}/files/2019/12/commits-lines-shell-novice.svg" width="500" alt="Shell lesson commits vs. lines" />
  <p>Shell lesson commits vs. lines</p>
</div>

<div align="center">
  <img src="{{site.github.url}}/files/2019/12/commits-lines-git-novice.svg" width="500" alt="Git lesson commits vs. lines" />
  <p>Git lesson commits vs. lines</p>
</div>
