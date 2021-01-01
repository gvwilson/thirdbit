---
title: "Gini Coefficients as a Measure of Team Effort"
date: 2007-10-12 15:06:28
year: 2007
---
The <a href="http://en.wikipedia.org/wiki/Gini_coefficient"><em>Gini coefficient</em></a> is a widely-used measure of inequality in which 0 corresponds to perfect equality (e.g., everyone is equally wealthy), while 1 corresponds to perfect inequality (e.g., one person owns everything, nobody else has anything).  I calculated the Gini coefficient for each team in my CSC301 class based on the number of lines of Java code each team member contributed to what was in version control at the deadline.

The results are shown below.  The first number shows the Gini coefficient taking into account only those people who actually contributed lines of code to the final solution, while the second shows the value when people who didn't contribute (or whose contributions didn't survive in the final submission) are given a score of 0.  By comparison, the Gini coefficient for incomes in highly unequal countries like Brazil is about 0.6, while Canada's is about 0.32.

I'm the first to acknowledge that this isn't an accurate assessment of how equally work was divided among team members.  For example, one member of one team did a "reformat all" in Eclipse shortly before the submission, so almost all of their code appears to have been written by him.  Similarly, people in other teams used pair programming (which means two people did the work, but only one gets the commit credit), while the written part of the assignment (which was submitted as a PDF) wasn't included in this count at all.  But I still the numbers are interesting and revealing: twenty-to-one line count ratios are common, and a few are fifty-to-one.
<table>
<tr>
<td>0.00 / 0.50</td>
</tr>
<tr>
<td>0.01 / 0.75</td>
</tr>
<tr>
<td>0.10 / 0.32</td>
</tr>
<tr>
<td>0.17 / 0.59</td>
</tr>
<tr>
<td>0.23 / 0.43</td>
</tr>
<tr>
<td>0.24 / 0.43</td>
</tr>
<tr>
<td>0.25 / 0.25</td>
</tr>
<tr>
<td>0.25 / 0.63</td>
</tr>
<tr>
<td>0.27 / 0.51</td>
</tr>
<tr>
<td>0.28 / 0.46</td>
</tr>
<tr>
<td>0.29 / 0.47</td>
</tr>
<tr>
<td>0.29 / 0.47</td>
</tr>
<tr>
<td>0.32 / 0.32</td>
</tr>
<tr>
<td>0.36 / 0.52</td>
</tr>
<tr>
<td>0.38 / 0.38</td>
</tr>
<tr>
<td>0.38 / 0.54</td>
</tr>
<tr>
<td>0.39 / 0.55</td>
</tr>
<tr>
<td>0.41 / 0.41</td>
</tr>
<tr>
<td>0.42 / 0.42</td>
</tr>
<tr>
<td>0.42 / 0.71</td>
</tr>
<tr>
<td>0.45 / 0.45</td>
</tr>
<tr>
<td>0.45 / 0.45</td>
</tr>
<tr>
<td>0.46 / 0.79</td>
</tr>
<tr>
<td>0.55 / 0.55</td>
</tr>
<tr>
<td>0.56 / 0.56</td>
</tr>
<tr>
<td>0.56 / 0.56</td>
</tr>
<tr>
<td>0.56 / 0.67</td>
</tr>
</table>
