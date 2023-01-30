---
title: "Real World Data Causes Perl"
date: 2008-04-03 15:44:15
year: 2008
---
The title was <a href="http://weblog.latte.ca/">Blake Winton</a>'s reaction to my re-telling of <a href="http://web.simmons.edu/~menzin/">Margaret Menzin</a>'s story from this year's "It Seemed Like a Good Idea at the Time" session at <a href="http://www.cs.duke.edu/sigcse08/">SIGCSE</a>.  She asked her students to write a program that would sort names in library order (i.e., "Gregory V. Wilson" would be sorted under "W"). Turns out the rules are, well, real-world-ish:
<ul>
  <li><em><strong>L</strong></em>eonardo da Vinci ("da Vinci" just means "from Vinci")</li>
  <li>Catherine de <em><strong>M</strong></em>edici (family name)</li>
  <li>Juan <em><strong>P</strong></em>once de Leon (full family name is "Ponce de Leon")</li>
  <li>Jean de <em><strong>L</strong></em>a Fontaine (family name is "La Fontaine")</li>
  <li>Gabriel <em><strong>G</strong></em>arcia Marquez (double-barrelled Spanish surnames)</li>
  <li>Wernher <em><strong>v</strong></em>on <em><strong>B</strong></em>raun (depending on whether he was in Germany or the US)</li>
  <li><em><strong>E</strong></em>lizabeth Alexandra May Windsor (monarchs sort by the name under which they took the throne)</li>
  <li><em><strong>T</strong></em>homas a Beckett (special rules for saints, too)</li>
  <li><em><strong>M</strong></em>ao Tse-tung (Chinese family names come first)</li>
</ul>
Oh, and if you have names written in multiple languages? You sort the languages first, according to their names in English, then sort within each language using its own rules. And we haven't even started on:
<ul>
  <li>Hon. Father Robert F. Drinan, S.J., L.L.D.</li>
  <li>Rev. Dr. Martin Luther King, Jr.</li>
  <li>Augusta Ada Byron King, Lady Lovelace</li>
  <li>Major General Stanley</li>
</ul>
<em>Later: the indefatigable <a href="http://adam.goucher.ca/">Adam Goucher</a> pointed me at <a href="http://www.loc.gov/catdir/pcc/naco/">NACO</a>, who decide such things. Real world data is guilty of a lot more than Perl…</em>
