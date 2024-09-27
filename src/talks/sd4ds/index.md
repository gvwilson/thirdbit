---
title: "Software Design in 50 Minutes"
template: slides
---

<div class="center padtop">
  <h1>Software Design<br>in 50 Minutes</h1>
  <p><img src="@root/files/talks/codebender-logo.svg" alt="Third Bit logo" width="20%"></p>
  <p>Greg Wilson</p>
  <p><a href="http://third-bit.com/talks/sd4ds/">http://third-bit.com/talks/sd4ds/</a></p>
  <p><img src="@root/files/talks/cc-by.svg" width="20%" alt="CC-BY"></p>
</div>

---

## Why Should You Listen to Me?

- I've built a lot of complicated software…
- …and have been lucky enough to hang out with some very smart people

<div class="center">
  <img src="@root/files/talks/beautiful-code.png" alt="Beautiful Code cover">
  <img src="@root/files/talks/aosa1.png" alt="AOSA vol 1 cover">
  <img src="@root/files/talks/aosa2.png" alt="AOSA vol 2 cover">
</div>

---

## The Most Important Thing

<p class="center"><strong>Computer scientists aren't taught how to design software</strong></p>

- The most design-intensive "engineering" discipline there is
- But courses where students analyze and critique others' programs are rare
- So no, you haven't missed something obvious

---

## 1. Design after the fact

- The most important thing is to *look* as though you designed things (<a href="#Parnas1986">Parnas1986</a>)
- So that the next person can understand it
- Many designers explain architecture by recapitulating history (<a href="#Brown2011">Brown2011</a>,<a href="#Brown2012">Brown2012</a>)
- Challenge and response
  - Can only understand why it does what it does by understanding the problem it was designed to solve

---
      
## 1. Design after the fact

- *Refactoring* is the process of reorganizing or rewriting code without changing behavior
  - By which we mean "high-level behavior" because of course if you look closely enough...
- <a href="#Fowler2018">Fowler2018</a> describes common refactoring moves for code
- These do to code what tidying steps in a data pipeline do to data (<a href="#Wickham2017">Wickham2017</a>):
  move it toward well-understood forms (<a href="#Kerievsky2004">Kerievsky2004</a>)

---

## 2. Design for cognitive capacity

- Short-term memory vs. long-term memory
- You can manage 7±2 things at a time (<a href="#Miller1956">Miller1956</a>)
- So design software to keep *cognitive load* manageable

---

## 2. Design for cognitive capacity

- Constants are easier to remember than varying values…
  - …unless those values vary in predictable ways
- Keep number of parameters or variables in (mental) scope at any time below this threshold
- Pipes with strict left-to-right reading order are easier to understand than nested function calls
- *Build frameworks that encourage this*

---

## Aside

- Some people say that if you need to comment your code you should have written clearer code
- That is *expert blind spot* at work
- Newcomers need help building a *mental model* of the code and problem
- And everyone needs the "why" that code alone doesn't capture

---

## 3. Design in coherent levels

- Functions should be short, shallow, and single-purpose
  - Of course, no one would argue the opposite…
- If I read a function aloud, are all the steps at the same conceptual level?

```
 def main():
     config = buildConfig(sys.argv)
     state = initState(config)
     while (config.currentTime < config.haltTime):
         updateState(config, state)
     report(config, state)
```

---

## 3. Design in coherent levels

- Functions should be short, shallow, and single-purpose
  - Of course, no one would argue the opposite…
- If I read a function aloud, are all the steps at the same conceptual level?

```
 def main():
     config = buildConfig(sys.argv)
     state = initState(config)
*    while (config.currentTime < config.haltTime):
         updateState(config, state)
     report(config, state)
```

---

## 3. Design in coherent levels

- Functions should be short, shallow, and single-purpose
  - Of course, no one would argue the opposite…
- If I read a function aloud, are all the steps at the same conceptual level?

```
 def main():
     config = buildConfig(sys.argv)
     state = initState(config)
*    while stillEvolving(config):
         updateState(config, state)
     report(config, state)
```

---

<h2>Levels</h2>

- <a href="#Schon1984">Schon1984</a> and others have found that
  experts jump between levels looking for concrete refutations of plans as soon as possible
- Depth-first design is therefore a good strategy *if* you write the hard parts first
  - Which most of us avoid

---

## 4. Design for evolution

- Software changes over time because the problem changes *and* because we learn more
  - The tool shapes the hand
- A good design makes independent evolution of parts easier
  - A fix *here* shouldn't require changes *there*
  - Realistically, should only require a small number of changes in limited, predictable places
- The switch to `stillEvolving` in the previous slide insulates `main` from lower-level changes

---

## 4. Design for evolution

- Key ideas are *information hiding* and *loose coupling*
- Which manifest as *interface vs. implementation*
  - Many of the more advanced features of programming languages exist to check this
- Examples
  - Deriving classes
  - Polymorphic functions
  - Explicit interfaces or traits

---

## 4. Design for evolution

- Design by contract (<a href="#Meyer1994">Meyer1994</a>) extends this idea through time
  - *Pre-conditions* have to be true in order for the function to run
  - *Post-conditions* are what the function guarantees will be true when it completes
  - Can be used to define and verify tests

---

## 4. Design for evolution

- But wait, there's more
- Pre-conditions can only be *relaxed*
  - I.e., the function can take input the earlier implementation wouldn't
- Post-conditions can only be strengthened
  - I.e., the function can only produce a subset of the earlier implementation's output

---

## 5. Group related information

- Brains use *chunks* to expand effective size of short-term memory
- So combine things into structures

<hr>

```
def enclose(x0, y0, z0, x1, y1, z1, nearness):
    …
```

<hr>

```
def enclose(p0, p1, nearness):
    …
```

---

## 6. Use common patterns

- Experts have *design patterns* in mind when building code
- Learning them makes you a better programmer (<a href="#Tichy2010">Tichy2010</a>)
- But also makes your code seem more familiar to others
- Examples include:
  - "Most valuable" variable (<a href="#Byckling2005">Byckling2005</a>)
  - Nested loops over 2D array
  - Filter-group-summarize

---

## 6. Use common patterns

- A near miss is worse than no pattern at all

```
 for (i=0; i<a.width; i++) {
     for (j=0; i<a.height; j++) {
         a[i][j] = cos(abs(a[i][j]) - lemaitre(b_norm, a[j][i]))
     }
 }
```

---

## 6. Use common patterns

- A near miss is worse than no pattern at all

```
 for (i=0; i<a.width; i++) {
*    for (j=0; i<a.height; j++) {
         a[i][j] = cos(abs(a[i][j]) - lemaitre(b_norm, a[j][i]))
     }
 }
```

- The eye (literally) doesn't see it

---

## 6. Use common patterns

- Maximize "what's unique to this operation / boilerplate"

```
a = cos(abs(a) - lemaitre(b_norm, a.transpose()))
```

- *Build frameworks that encourage this*

---

## 6. Use common patterns

- Balance of abstraction and comprehension depends on how much people know

<div class="row">
  <div class="col-6 center"><img src="./comprehension-01.svg" alt="Novice comprehension" width="80%"></div>
  <div class="col-6 center"><img src="./comprehension-02.svg" alt="Expert comprehension" width="80%"></div>
</div>

---

## 6. Use common patterns

- Patterns can be taught (but only by example)

<img src="@root/files/talks/design-patterns-ruby.jpg" alt="cover of 'Design Patterns in Ruby'" width="40%" class="center">

---

## 7. Design for delivery

- Development operations (DevOps) has become a buzzword
  - Like "data science" or "computational thinking", the term is popular because people can use it to mean whatever they want
- But the core idea is a good one (<a href="#Kim2016">Kim2016</a>,<a href="#Forsgren2018">Forsgren2018</a>)
  - The code you ship is surrounded and supported by software (and practices) that deliver that code
- Investment in automation pays off many times over
  - *If* you design things so that they can be automated

---

## 7. Design for delivery

- Use whatever *build tool* your language expects
  - `pip` or `conda` for Python
  - `devtools` for R
  - Many conflicting options for JavaScript
- Organize code and files the way your build system expects

---

## 7. Design for delivery

- Use a logging library
  - A volume control is really helpful in production…
  - …particularly if messages are collated…
  - …but only if the messages are helpful
- And follow the rest of <a href="#Taschuk2017">Taschuk2017</a>

---
      
## 8. Design for testability

- *Legacy code:* we're afraid to modify it because things will break unexpectedly (<a href="#Feathers2004">Feathers2004</a>)
- Comprehensive tests make us less afraid
  - But we need testable pieces in order to create tests economically
  - Brings us back to pre-and-post rather than how

---
      
## 8. Design for testability

- How easy is it to create a *fixture*?
- How easy is it to invoke just the behavior we want?
- How easy is it to check the result?
- How easy is it to figure out what "right" is?
- How easy is it to delete the feature?

---

<h2>Test-Driven Development</h2>

- Test-driven development (TDD) is the practice of writing the tests
  *before* writing the code
- Multiple studies have shown that it doesn't actually improve productivity
  (<a href="#Fucci2016">Fucci2016</a>)
- But alternating rapidly between testing and coding seems to

---

## 9. Design as if code was data

- The insight on which modern computing is based
- Programs are just text files
  - Style-checking tools
  - Specially-formatted comments as embedded documentation
- But wait…

---

## 9. Design as if code was data

<p class="center"><strong>Code in memory is just another data structure</strong></p>

- Functions as arguments
- Functions in data structures
- Dynamic loading
  - Interface vs. implementation
- Lazy evaluation in R
- Decorators in Python

---

## 9. Design as if code was data

- Count the number of values that pass a test

```
 def count_positive(array):
     number = 0
     for value in array:
*        if value >= 0:
             number = number + 1
     return number
```

---

## 9. Design as if code was data

- Count the number of values that pass a test

```
*def count_interesting(array, test):
     number = 0
     for value in array:
*        if test(value):
             number = number + 1
     return number

*def is_positive(value):
*    return value >= 0
*
*count_interesting(array, is_positive)
```

---

## The Audience Matters

- But see the discussion earlier of comprehension curves
- What is powerful in the hands of experts is spooky action-at-a-distance for novices

---

## 10. Design graphically

- Very few programmers use UML the "right" way (<a href="#Petre2013">Petre2013</a>)
- But almost all draw pictures to help them design (<a href="#Cherubini2007">Cherubini2007</a>)
- Blueprints versus brainstorming

---

## 10. Design graphically

- Flowcharts are unfairly maligned (<a href="#Scanlan1989">Scanlan1989</a>)

<img src="flowchart.svg" alt=" complaint flowchart" width="30%" class="center">

---

## 10. Design graphically

- Architecture diagrams: probably the most widely used (probably because of their informality)

<img src="architecture-diagram.png" alt="Architecture diagram" width="60%" class="center">

---

## 10. Design graphically

- Entity-relationship diagrams: widely used because they are actually helpful

<img src="er-diagram.png" alt="Entity-relationship diagram" width="80%" class="center">

---

## 10. Design graphically

- Use case maps: actions overlaid on architecture

<img src="use-case-map.png" alt="Use case map" width="70%" class="center">

---

## 11. Design with everyone in mind

- Fairness, privacy, and security cannot be sprinkled on afterward
- *Principle of Least Privilege:* what is the least information this part of the software absolutely needs to do its job?
- But that's not all
  - If users have to reset passwords frequently, they will choose insecure passwords (<a href="#Smalls2021">Smalls2021</a>)
  - Systems that email attachments train people to be vulnerable to phishing attacks
  - Most social media isn't designed with abusive ex-partners in mind…

---

## 11. Design with everyone in mind

- Accessibility can't be sprinkled on afterward either
- Close your eyes and try to navigate your department's website
  - Or tape popsicle sticks to your fingers to simulate severe arthritis
- More important as the population ages (<a href="#Johnson2017">Johnson2017</a>)

---

## 12. Design for contribution

- Diversity improves outcomes in fields from business to healthcare
  (<a href="#Gompers2018">Gompers2018</a>,<a href="#Gomez2019">Gomez2019</a>)
- But you should do it because *it's the right thing to do*

---

## 12. Design for contribution

- Licensing is a design issue
  - You cannot use components whose licenses are incompatible with yours
- Plugin architectures make small additions more approachable
- Discoverable designs do too (<a href="#Sholler2019">Sholler2019</a>)

---

## Conclusion

- This is not art
- But it *is* beautiful

<img src="derosa.jpg" alt="bicycle" width="50%" class="center">

- I believe we can make bicycles too

---

<div class="center">
  <h2>Thank You</h2>
  <p><img src="@root/files/talks/gvwilson.png" width="40%"></p>
  <p><a href="http://third-bit.com">Greg Wilson</a></p>
  <p><a href="mailto:gvwilson@third-bit.com">gvwilson@third-bit.com</a></p>
  <p><a href="http://third-bit.com/talks/sd4ds/">http://third-bit.com/talks/sd4ds/</a></p>
</div>

---

class: bibliography

## Bibliography

<p id="Brown2011">[Brown2011]
Amy Brown and Greg Wilson (eds.):
<em><a href="http://aosabook.org">The Architecture of Open Source Applications: Elegance, Evolution, and a Few Fearless Hacks</a></em>.
Lulu, 2011, 978-1257638017.
</p>

<p id="Brown2012">[Brown2012]
Amy Brown and Greg Wilson (eds.):
<em><a href="http://aosabook.org">The Architecture of Open Source Applications: Structure, Scale, and a Few More Fearless Hacks</a></em>.
Lulu, 2012, 978-0201103427.
</p>

<p id="Byck2005">[Byck2005]
Pauli Byckling, Petri Gerdt, and Jorma Sajaniemi:
"<a href="https://doi.org/10.1145/1094855.1094972">Roles of Variables in Object-Oriented Programming</a>".
<em>2005 Conference on Object-Oriented Programming, Systems, Languages, and Applications (OOPSLA'05)</em>, <a class="doi" href="https://doi.org/10.1145/1094855.1094972">10.1145/1094855.1094972</a>.
</p>

<p id="Cher2007">[Cher2007]
Mauro Cherubini, Gina Venolia, Rob DeLine, and Amy J. Ko:
"<a href="https://doi.org/10.1145/1240624.1240714">Let's Go to the Whiteboard: How and Why Software Developers Use Drawings</a>".
<em>2007 Conference on Human Factors in Computing Systems (CHI'07)</em>, <a class="doi" href="https://doi.org/10.1145/1240624.1240714">10.1145/1240624.1240714</a>.
</p>

<p id="Feathers2004">[Feathers2004]
Michael C. Feathers:
<em>Working Effectively with Legacy Code</em>.
Prentice-Hall, 2004, 978-0131177055.
</p>

<p id="Forsgren2018">[Forsgren2018]
Nicole Forsgren, Jez Humble, and Gene Kim:
<em>Accelerate: Building and Scaling High Performing Technology Organizations</em>.
IT Revolution Press, 2018, 978-1942788331.
</p>

<p id="Fowler2018">[Fowler2018]
Martin Fowler:
<em>Refactoring</em> (2nd edition).
Addison-Wesley Professional, 2018, 978-0134757599.
</p>

---

class: bibliography

## Bibliography

<p id="Fucci2016">[Fucci2016]
Davide Fucci, Giuseppe Scanniello, Simone Romano, Martin Shepperd, Boyce Sigweni, Fernando Uyaguari, Burak Turhan, Natalia Juristo, and Markku Oivo:
"<a href="https://doi.org/10.1145/2961111.2962592">An External Replication on the Effects of Test-driven Development Using a Multi-site Blind Analysis Approach</a>".
<em>ESEM'16</em>, <a class="doi" href="https://doi.org/10.1145/2961111.2962592">10.1145/2961111.2962592</a>.
</p>

<p id="Gomez2019">[Gomez2019]
L.E. Gomez and Patrick Bernet:
"<a href="https://doi.org/10.1016/j.jnma.2019.01.006">Diversity improves performance and outcomes</a>".
<em>Journal of the National Medical Association</em>, 111(4), 2019, <a class="doi" href="https://doi.org/10.1016/j.jnma.2019.01.006">10.1016/j.jnma.2019.01.006</a>.
</p>

<p id="Gompers2018">[Gompers2018]
Paul Gompers and Silpa Kovvali:
"The Other Diversity Dividend".
<em>Harvard Business Review</em>, 96(4), 2018.
</p>

<p id="Hook2009">[Hook2009]
D. Hook and D. Kelly:
"Testing for trustworthiness in scientific software."
<em>Proc. 2009 ICSE Workshop on Software Engineering for Computational Science and Engineering</em>,
2009,
<a class="doi" href="https://doi.org/10.1109/secse.2009.5069163">10.1109/secse.2009.5069163</a>.
</p>

<p id="Johnson2017">[Johnson2017]
Jeff Johnson and Kate Finn:
<em>Designing User Interfaces for an Aging Population: Towards Universal Design</em>.
Morgan Kaufmann, 2017, 978-0128044674.
</p>

<p id="Kanewala2014">[Kanewala2014]
U. Kanewala and JM Bieman: "Testing scientific software: A systematic literature review."
<em>Information and Software Technology</em>. 56(10), 2014, <a class="doi" href="https://doi.org/10.1016/j.infsof.2014.05.006">10.1016/j.infsof.2014.05.006</a>.
</p>

<p id="Kerievsky2004">[Kerievsky2004]
Joshua Kerievsky:
<em>Refactoring to Patterns</em>.
Addison-Wesley Professional, 2004, 978-0321213358.
</p>

---

class: bibliography

## Bibliography

<p id="Kim2016">[Kim2016]
Gene Kim, Patrick Debois, John Willis, and Jez Humble:
<em>The DevOps Handbook</em>.
IT Revolution Press, 2016, 978-1942788003.
</p>

<p id="Meyer1994">[Meyer1994]
Bertrand Meyer:
<em>Object-Oriented Software Construction</em>.
Prentice-Hall, 1994, 978-0136290490.
</p>

<p id="Miller1956">[Miller1956]
George A. Miller:
"The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information".
<em>Psychological Review</em>, 63(2), 1956, <a class="doi" href="https://doi.org/10.1037/h0043158">10.1037/h0043158</a>.
</p>

<p id="Parnas1986">[Parnas1986]
David Lorge Parnas and Paul C. Clements:
"A Rational Design Process: How and Why to Fake It".
<em>IEEE Transactions on Software Engineering</em>, SE-12(2), 1986, <a class="doi" href="https://doi.org/10.1109/tse.1986.6312940">10.1109/tse.1986.6312940</a>.
</p>

<p id="Petre2013">[Petre2013]
Marian Petre:
"UML in practice".
<em>Proc. ICSE'13</em>.
</p>

<p id="Scanlan1989">[Scanlan1989]
David A. Scanlan:
"Structured Flowcharts Outperform Pseudocode: An Experimental Comparison".
<em>IEEE Software</em>, 6(5), 1989, <a class="doi" href="https://doi.org/10.1109/52.35587">10.1109/52.35587</a>.
</p>

<p id="Schon1984">[Schon1984]
Donald A. Schon:
<em>The Reflective Practitioner: How Professionals Think in Action</em>.
Basic Books, 1984, 978-0465068784.
</p>

<p id="Sholler2019">[Sholler2019]
Dan Sholler, Igor Steinmacher, Denae Ford, Mara Averick, Mike Hoye, and Greg Wilson:
"Ten simple rules for helping newcomers become contributors to open projects".
<em>PLOS Computational Biology</em>, 15(9), 2019, <a class="doi" href="https://doi.org/10.1371/journal.pcbi.1007296">10.1371/journal.pcbi.1007296</a>.
</p>

---

class: bibliography

## Bibliography

<p id="Smalls2021">[Smalls2021]
Danielle Smalls and Greg Wilson: "Ten quick tips for staying safe online."
<em>PLoS Computational Biology</em>, 17(3), 2021, <a class="doi" href="https://doi.org/10.1371/journal.pcbi.1008563">10.1371/journal.pcbi.1008563</a>.
</p>

<p id="Taschuk2017">[Taschuk2017]
Morgan Taschuk and Greg Wilson:
"Ten simple rules for making research software more robust."
<em>PLoS Computational Biology</em>, 13(4), 2017, <a class="doi" href="https://doi.org/10.1371/journal.pcbi.1005412">10.1371/journal.pcbi.1005412</a>.
</p>

<p id="Tichy2010">[Tichy2010]
Walter Tichy:
"The Evidence for Design Patterns".
In 
Andy Oram and Greg Wilson (eds.):
<em>Making Software.</em>
O'Reilly, 2010, 978-0596808327.
</p>

<p id="Wickham2017">[Wickham2017]
Hadley Wickham and Garrett Grolemund:
<em>R for Data Science: Import, Tidy, Transform, Visualize, and Model Data</em>.
O'Reilly, 2017, 978-1491910399.
</p>
