---
title: "Teaching Research Computing"
date: 2026-11-15
category: education software-carpentry
---

This post outlines a twelve-week course on research computing
for programmers who haven't studied science or humanities beyond high school.
Each week presents one example drawn from a different discipline;
the first lecture of each week builds a simple version of the example,
the second adds realism,
and the third tests the science and makes the analysis reproducible.
The tests check properties such as conservation laws,
analytic identities,
parameter recovery, and limiting cases
rather than merely checking that the code runs.
Each lecture is written to fill a full hour:
motivation, the core idea, a worked example, a common pitfall,
a check-in for the students, and a pointer to what comes next.

## 1. Segregation (sociology)

-   How do self-organized clusters emerge from mild individual preferences?
-   The Schelling model places two kinds of agent on a grid
-   Each agent moves when too few of its neighbors are like it
-   Computational approach: an agent-based simulation that steps a grid

### Lecture 1: a grid, two kinds, one rule

-   Motivation: segregation looks like it needs strong prejudice, but Schelling showed it does not
-   Represent the city as a two-dimensional array of two kinds of cell plus empty cells
-   An agent is satisfied when at least a given fraction of its neighbors are the same kind as it
-   Each tick, move one unsatisfied agent to a random empty cell
-   Worked example: a 50 by 50 grid, 30 percent empty, satisfaction threshold one third
-   Plot the grid before and after many ticks and count the clusters that form
-   Pitfall: an agent's neighbors include empty cells, so the denominator varies from agent to agent
-   Check-in: have students predict how clustered the final board will be, then run it
-   Pointer: next lecture measures that clustering instead of eyeballing it

### Lecture 2: measuring segregation

-   Motivation: "looks clustered" is not a number, and a course needs numbers to compare runs
-   Define a segregation score as the average fraction of an agent's neighbors that are unlike it
-   Worked example: compute the score by hand on a tiny 3 by 3 board with two agents
-   Sweep the similarity threshold from near zero to near one and record the final score
-   Show that segregation rises sharply at a modest threshold rather than gradually
-   Discuss the tipping point: a small change in preference, a large change in outcome
-   Pitfall: a single run is noisy, so average several runs at each threshold
-   Introduce a random seed so every run is repeatable
-   Pointer: next lecture turns the sharp rise into tests

### Lecture 3: testing and reproducibility

-   Motivation: how do we know the simulation is right rather than merely plausible
-   Test that a fully mixed board gives a segregation score near zero
-   Test that a fully sorted board gives a segregation score near one
-   Test that the score does not decrease when the threshold increases, all else equal
-   Test that the number of agents is conserved across ticks
-   Pitfall: a test that always passes is not a test, so break each property on purpose once
-   Check-in: have students name one property of segregation they could test next
-   Record the seed, the parameters, and the code version so a result can be reproduced

## 2. Epidemics (epidemiology)

-   How does an infection spread through a population and then fade?
-   The SIR model splits a fixed population into susceptible, infectious, and recovered people
-   Computational approach: integrating a system of ordinary differential equations and fitting it with least squares

### Lecture 1: three compartments

-   Motivation: public health needs to predict how fast a disease spreads and how many it will infect
-   Define S, I, and R as the counts of susceptible, infectious, and recovered people
-   Write the rates of change: new infections grow as S times I, recoveries grow as I
-   Worked example: population 10000, 10 initially infectious, transmission 0.3 per day, recovery 0.1 per day
-   Integrate the equations with an ODE solver over a fixed time span
-   Plot the three curves and the daily new cases
-   Identify the basic reproduction number as the ratio of the transmission and recovery rates
-   Pitfall: the solver returns continuous curves, but case counts are integers per day
-   Check-in: have students guess which curve peaks first and by how much
-   Pointer: next lecture estimates the rates from data instead of assuming them

### Lecture 2: fitting to data

-   Motivation: in a real outbreak the rates are unknown and must be estimated from the case curve
-   Replace the hand-tuned rates with parameters estimated from an observed case curve
-   Use least squares to fit the transmission and recovery rates to synthetic case counts
-   Worked example: fit the model to a synthetic curve and recover rates near the true values
-   Compute the epidemic peak and the final size from the fitted parameters
-   Discuss identifiability: how well the data pin down each parameter
-   Pitfall: an optimizer can land in a local minimum, so restart from several starting points
-   Check-in: have students say which of the two rates is easier to pin down and why
-   Pointer: next lecture tests whether the model is physically consistent

### Lecture 3: testing and reproducibility

-   Motivation: a fitted curve can look right and still violate the model's laws
-   Test that the total population is conserved: S plus I plus R equals N at every time
-   Test the no-transmission limit: when the transmission rate is zero, no new infections occur
-   Test that the epidemic curve has exactly one peak when the reproduction number is above one
-   Test that fitting recovers the true parameters from noiseless data
-   Pitfall: a conservation test that passes at loose tolerance can hide a real drift
-   Check-in: have students propose a limiting case the tests have not covered
-   Pin the environment and the solver tolerances so the curves are reproducible

## 3. Predator and Prey (ecology)

-   How do predator and prey populations cycle together?
-   The Lotka-Volterra model can be written as a discrete-time map that computes next year's populations from this year's
-   Computational approach: iterating a discrete-time map, distinct from the continuous ODEs of the epidemics example

### Lecture 1: a discrete-time map

-   Motivation: many populations are counted once a year, not continuously, so a discrete model is more honest
-   Write the populations as two difference equations updated year by year
-   Worked example: start with 50 prey and 20 predators and step the map for 100 years
-   Choose a starting point and iterate the map for many steps
-   Plot prey and predator against time and against each other
-   Observe that the two populations cycle rather than settle
-   Pitfall: a step that overshoots can make a population negative, which is impossible
-   Check-in: have students predict whether the cycle grows, shrinks, or stays the same
-   Pointer: next lecture finds where the map does not change at all

### Lecture 2: fixed points and stability

-   Motivation: a fixed point tells us where the system would sit still, and stability tells us whether it returns there
-   Find the fixed point where the map leaves the populations unchanged
-   Check whether small perturbations shrink or grow away from the fixed point
-   Worked example: perturb the fixed point by one percent and watch it over twenty steps
-   Sweep a growth parameter and watch the orbit move from a fixed point to a cycle to chaos
-   Discuss period doubling and the limits of simple population models
-   Pitfall: stability is a property of a specific fixed point, not of the map as a whole
-   Check-in: have students find a parameter where the orbit settles to a two-cycle
-   Pointer: next lecture tests the properties the model should always have

### Lecture 3: testing and reproducibility

-   Motivation: a discrete map should preserve the things a population cannot lose
-   Test that both populations stay positive for all time
-   Test that a fixed point stays fixed under one more iteration
-   Test the period of a cycle against a hand-computed value
-   Test that the no-predation limit gives geometric prey growth
-   Pitfall: an exactly zero population can hide a division by zero in the next step
-   Check-in: have students name a property of real populations the model ignores
-   Record the seed, the parameters, and the number of steps for reproducibility

## 4. Flood risk (hydrology)

-   How big a flood should a structure be designed to survive?
-   The annual maximum flow is modeled with an extreme-value distribution
-   Computational approach: fitting a log-normal distribution and reading off quantiles

### Lecture 1: return levels

-   Motivation: a dam built for the wrong flood fails, and the right answer is a probability, not a guess
-   Load a table of annual maximum river flows
-   Fit a log-normal distribution to the logarithms of the flows
-   Worked example: fit flows whose logarithms have mean 4.8 and standard deviation 0.4
-   Turn the fitted distribution into a return level for a given return period
-   Interpret the 100-year flood as a quantile, not a guarantee
-   Pitfall: "100-year flood" does not mean one flood every hundred years
-   Check-in: have students say why the logarithms are modeled rather than the raw flows
-   Pointer: next lecture looks at whether the largest floods really follow the fitted tail

### Lecture 2: extremes and plotting positions

-   Motivation: the most important floods are the biggest ones, which are also the rarest and hardest to check
-   Compute plotting positions with the Weibull formula to compare data to fitted quantiles
-   Order the flows and check that the sorted values are non-decreasing
-   Worked example: plot the sorted flows against the fitted quantiles and spot the departure
-   Examine the largest observations and whether they follow the fitted tail
-   Discuss why a few big floods dominate the estimate of extreme risk
-   Pitfall: a straight-looking middle does not mean the tail is well fit
-   Check-in: have students identify which points they would distrust and why
-   Pointer: next lecture tests the distributional identities

### Lecture 3: testing and reproducibility

-   Motivation: extreme-value estimates are only as trustworthy as the distributional assumptions
-   Test that the log-flows are close to normal by comparing sample quantiles with normal quantiles
-   Test that return levels increase as the return period increases
-   Test the identity that a return level satisfies the fitted cumulative distribution
-   Test that the plotting positions all lie strictly between zero and one
-   Pitfall: a test on one synthetic sample is weak, so repeat it over many seeds
-   Check-in: have students name an assumption the log-normal model makes about the data
-   Fix the random seed and the fitting procedure so the numbers reproduce

## 5. Exoplanets (astronomy)

-   How do we infer the existence of a planet from the wobble of its star?
-   A planet tugs its star, causing a small periodic shift in the star's velocity toward or away from us
-   Computational approach: finding a period with a Lomb-Scargle periodogram, distinct from least-squares fitting

### Lecture 1: a star's wobble

-   Motivation: most exoplanets cannot be seen directly, so we infer them from the star's motion
-   Model the radial velocity as a sinusoid with a period, an amplitude, and an offset
-   Generate a synthetic velocity series from a known planet, sampled at irregular times
-   Worked example: a planet with a 10 day period and a 10 meter per second amplitude
-   Plot the velocity series against time
-   Explain why the period is the scientifically interesting quantity
-   Note that the observations are unevenly spaced, which rules out a plain Fourier transform
-   Pitfall: real observations come at irregular times set by weather and telescope schedules
-   Check-in: have students say what pattern they would look for in the plot
-   Pointer: next lecture turns that pattern into a number

### Lecture 2: finding the period in the spectrum

-   Motivation: a periodogram turns a messy time series into a picture with a peak at the true period
-   Compute a Lomb-Scargle periodogram of the velocity series
-   Worked example: compute the periodogram over periods from 1 to 30 days and find the tallest peak
-   Find the highest peak in the periodogram and read off the period it implies
-   Show that a stronger planet signal gives a taller, sharper peak
-   Discuss false alarms and how a peak can be noise rather than a planet
-   Pitfall: the tallest peak is not always the true period when the data are sparse
-   Check-in: have students say how they would tell a real peak from a noise peak
-   Pointer: next lecture tests the periodogram's guarantees

### Lecture 3: testing and reproducibility

-   Motivation: a detection claim must survive the question "could this be noise"
-   Test periodicity: shifting time by one full period leaves the model unchanged
-   Test that the periodogram of a noiseless series has a single peak at the true period
-   Test that the periodogram of pure noise has no peak above the false-alarm level
-   Test that the peak height grows with the signal amplitude
-   Pitfall: a test that only checks the noiseless case says nothing about real data
-   Check-in: have students name a second planet property the tests could check
-   Record the noise model, the seed, and the periodogram settings so a detection can be audited

## 6. Perception (psychology)

-   How do we tell a real signal from background noise, and how good are we at it?
-   Signal detection theory separates sensitivity from bias using hits and false alarms
-   Computational approach: sweeping a decision threshold and computing the area under a curve

### Lecture 1: hits and false alarms

-   Motivation: two observers can make different decisions for the same reason or the same decision for different reasons
-   Given a list of trials with true labels and a decision on each, build a confusion table
-   Compute the hit rate among signal trials and the false-alarm rate among noise trials
-   Worked example: four signal trials and four noise trials with three hits and one false alarm
-   Check the extreme cases: all hits, and no false alarms
-   Explain sensitivity versus bias: the criterion an observer chooses changes both rates
-   Pitfall: accuracy alone hides the tradeoff between hits and false alarms
-   Check-in: have students build a confusion table for a memory test of their own
-   Pointer: next lecture varies the criterion to trace a curve

### Lecture 2: the receiver operating characteristic

-   Motivation: a single criterion gives one point, but the whole curve shows what the observer could do
-   Rank trials by a decision score rather than a single cutoff
-   Sweep a threshold across the scores to trace out the receiver operating characteristic curve
-   Worked example: sweep a threshold over scores from two normal distributions one and a half units apart
-   Confirm the curve starts at the origin and ends at the top right corner
-   Compute the area under the curve as a single summary of discrimination
-   Pitfall: the curve is built from scores, not from the decisions at a single threshold
-   Check-in: have students sketch the curve for a perfect observer and a coin flip
-   Pointer: next lecture tests the curve's geometry

### Lecture 3: testing and reproducibility

-   Motivation: the curve and its area have exact properties that a correct implementation must satisfy
-   Test that hit and false-alarm rates are correct on small hand-built examples
-   Test that the curve is monotonic and passes through the corner for perfect scores
-   Test that a diagonal curve gives an area of one half and a perfect curve gives one
-   Test that separable score distributions give an area above one half
-   Pitfall: an area below one half means the labels were likely reversed
-   Check-in: have students name a real decision where a false alarm is worse than a miss
-   Record the scoring rule and the trial labels so the analysis reproduces

## 7. Evolutionary trees (biology)

-   How do we reconstruct the family tree of species from their traits or sequences?
-   Distance-based methods build a tree from pairwise distances between species
-   Computational approach: building a tree by repeated closest-pair joining, with bootstrapping
-   Lecture 1 builds a tree from a distance matrix with a simple method
-   Lecture 2 checks the tree against the assumption of a molecular clock
-   Lecture 3 tests the reconstruction on simulated data and measures support

### Lecture 1: distances and a tree

-   Motivation: species inherit traits from ancestors, and a tree is the natural way to show that history
-   Start with pairwise distances between species taken from aligned sequences
-   Worked example: five species with a small hand-built distance matrix
-   Build a tree by joining the closest pair at each step
-   Plot the resulting tree and read off the distances between leaves
-   Explain why a tree, not a table, is the right object for ancestry
-   Pitfall: the closest pair in the matrix is not always the closest pair on the true tree
-   Check-in: have students join the first two species of the example by hand
-   Pointer: next lecture asks whether the tree's branch lengths are consistent

### Lecture 2: the molecular clock

-   Motivation: if change accumulates at a steady rate, distances tell us time, and time tells us the root
-   Define an ultrametric distance matrix where all leaves are equally far from the root
-   Check whether the input distances satisfy the ultrametric condition
-   Worked example: test a small matrix and show which leaf violates the clock
-   Explain what a violated clock implies about rates of change across lineages
-   Discuss neighbor joining as a method that does not assume a clock
-   Pitfall: a matrix can look close to ultrametric and still hide a real violation
-   Check-in: have students say what a violated clock means for dating the tree
-   Pointer: next lecture tests the reconstruction on data with a known answer

### Lecture 3: testing and reproducibility

-   Motivation: we can only trust a method when we check it on data where we know the true tree
-   Simulate sequence evolution along a known tree and record the true tree
-   Test that the reconstruction recovers the known tree from clean distances
-   Test the additive property: distances along the reconstructed tree match the input
-   Test that a bootstrap resample gives high support for well-resolved branches
-   Pitfall: high support means the branches are stable, not that the tree is correct
-   Check-in: have students say which branch of the tree they expect to be least certain
-   Record the simulation seed and the model of sequence change

## 8. Chemical fingerprints (chemistry)

-   How do we identify a molecule from the masses of its fragments?
-   A mass spectrum is a set of peaks at mass-to-charge ratios with intensities
-   Computational approach: peak detection and calibration, then matching against a library

### Lecture 1: peaks and calibration

-   Motivation: a molecule breaks into fragments whose masses are a fingerprint of its structure
-   Load a spectrum as a list of mass-to-charge values and intensities
-   Find local maxima above a noise floor to detect peaks
-   Worked example: a spectrum with peaks at 100 and 150 plus a noisy baseline
-   Calibrate the mass axis using two or more known reference peaks
-   Report the calibrated masses of the detected peaks
-   Discuss resolution: how close two peaks can be and still be told apart
-   Pitfall: a noise spike can look like a peak if the noise floor is set too low
-   Check-in: have students say how they would choose the noise floor
-   Pointer: next lecture matches the peaks to known molecules

### Lecture 2: matching to a library

-   Motivation: the peaks are only useful if they can be matched to a known molecule
-   Load a library of reference spectra for known molecules
-   Score how well the detected peaks match each library entry
-   Worked example: match the 100 and 150 peaks against a library of three molecules
-   Rank the library entries by match score
-   Discuss false matches and why a top score is not proof of identity
-   Pitfall: two different molecules can share many fragment masses
-   Check-in: have students propose a second piece of evidence to confirm identity
-   Pointer: next lecture tests the calibration and the matching

### Lecture 3: testing and reproducibility

-   Motivation: a match is a claim about chemistry, and claims need to be checked
-   Test that the calibration maps known reference masses to their true values
-   Test that peak detection finds injected synthetic peaks and ignores the noise floor
-   Test that matching against a copy of the same molecule ranks it first
-   Test that the result is stable when the noise seed changes
-   Pitfall: a test on one spectrum is weak, so run it over many noise seeds
-   Check-in: have students name a case where the top match is wrong
-   Record the calibration, the library version, and the noise model

## 9. Minerals (geology)

-   How do we name a rock or mineral from its measured composition?
-   A classifier maps a vector of measured features to a known category
-   Computational approach: nearest-neighbor classification with a held-out test set

### Lecture 1: nearest neighbors

-   Motivation: a geologist recognizes a mineral by eye, but a reproducible name comes from measured features
-   Load a table of mineral samples with measured features and known labels
-   Split the data into a training set and a held-out test set
-   Worked example: three minerals and two numeric features, split four fifths to one fifth
-   Classify each test sample by the label of its nearest training neighbor
-   Report accuracy as the fraction of correct labels
-   Discuss distance metrics and feature scaling
-   Pitfall: features on different scales dominate the distance unless they are scaled
-   Check-in: have students say why the test set must not be used for training
-   Pointer: next lecture reads accuracy more carefully

### Lecture 2: evaluation

-   Motivation: overall accuracy hides which minerals are confused with which
-   Build a confusion matrix from the test predictions
-   Read off per-class precision and recall, not just overall accuracy
-   Worked example: a 3 by 3 confusion matrix with one heavily confused pair
-   Sweep the number of neighbors and the distance metric
-   Discuss overfitting and why the test set must be untouched during training
-   Pitfall: a rare class can be mostly wrong while overall accuracy stays high
-   Check-in: have students say which class the confusion matrix shows is hardest
-   Pointer: next lecture tests the classifier's edge cases

### Lecture 3: testing and reproducibility

-   Motivation: a classifier is a piece of software and needs the same tests as any other
-   Test that a sample identical to a training sample is classified with its label
-   Test the classifier on a boundary case and inspect the decision
-   Test that accuracy never exceeds one and never falls below zero
-   Test that a shuffled-label run does not beat the real labels as a sanity check
-   Pitfall: an accuracy of one on a tiny test set proves little
-   Check-in: have students name a feature that would separate their chosen minerals
-   Record the split, the seed, and the feature scaling so the numbers reproduce

## 10. Inequality (economics)

-   How unequally is wealth or income spread across a population?
-   The Lorenz curve and the Gini coefficient summarize inequality in one number
-   Computational approach: sorting values, accumulating shares, and computing an area

### Lecture 1: one number for inequality

-   Motivation: a single number lets us compare inequality across countries and across years
-   Start with a list of incomes or wealth values for a population
-   Worked example: five people with incomes 1, 1, 1, 1, and 10
-   Sort the values and accumulate shares of the total
-   Compute the Gini coefficient from the area formula or the mean absolute difference
-   Interpret the value: zero means equal, one means one person holds everything
-   Pitfall: the same Gini can come from very different distributions
-   Check-in: have students compute the Gini for the five-person example by hand
-   Pointer: next lecture draws the curve the Gini summarizes

### Lecture 2: the Lorenz curve

-   Motivation: the Gini is one number, but the Lorenz curve shows the whole shape of inequality
-   Plot the Lorenz curve: cumulative share of income against cumulative share of people
-   Worked example: plot the curve for the five-person example and for a perfectly equal one
-   Relate the Gini coefficient to the area between the curve and the line of equality
-   Compare two distributions with the same mean but different inequality
-   Discuss what the Gini misses: it is one summary, not the whole distribution
-   Pitfall: the Gini treats a transfer between two rich people the same as one between rich and poor
-   Check-in: have students say which of two plotted curves is more unequal and why
-   Pointer: next lecture tests the Gini at its limits

### Lecture 3: testing and reproducibility

-   Motivation: the Gini has exact values at its extremes that a correct implementation must reproduce
-   Test that a perfectly equal distribution gives a Gini of zero
-   Test that a maximally concentrated distribution gives a Gini approaching one
-   Test that the Gini is unchanged when all values are scaled by a constant
-   Test the Gini of a known distribution against its analytic value
-   Pitfall: a Gini computed on unrounded values differs from one on rounded cents
-   Check-in: have students name a population whose Gini they would expect to be high
-   Record the data source and the sorting convention so the number reproduces

## 11. Authorship (digital humanities)

-   How do we tell who wrote an anonymous text from word choice?
-   Stylometry measures subtle habits of word frequency that survive changes of topic
-   Computational approach: principal component analysis of word-frequency vectors

### Lecture 1: word-frequency features

-   Motivation: authors leave a fingerprint in the small words they use, not the topics they discuss
-   Load a corpus of texts with known authors
-   Count the frequency of common function words such as "the", "of", and "and"
-   Worked example: ten short texts by two authors, counted over twenty function words
-   Normalize the counts so text length does not dominate
-   Explain why function words are better than topic words for authorship
-   Build a feature table of texts by word frequencies
-   Pitfall: a single long text is one row, not many, so corpus size is the number of texts
-   Check-in: have students name a word they use more than the people around them
-   Pointer: next lecture reduces the table to a picture

### Lecture 2: principal component analysis

-   Motivation: twenty word frequencies are too many to plot, so we project them to two informative axes
-   Center and scale the feature table so each word has equal weight
-   Compute the principal components of the feature table with a singular value decomposition
-   Worked example: project the ten texts onto the first two components and plot them
-   Check whether texts by one author separate in the projection
-   Discuss what the principal components mean and how many dimensions matter
-   Pitfall: scaling is essential, or the most frequent words dominate the components
-   Check-in: have students guess which author a new text belongs to from the plot
-   Pointer: next lecture tests whether the separation is real

### Lecture 3: testing and reproducibility

-   Motivation: a pretty separation can be noise, so the projection must be checked
-   Test that the projection is stable when the feature list changes slightly
-   Test that a held-out text projects near the correct author's texts
-   Test that the principal components are orthogonal and sorted by variance explained
-   Test a shuffled-label baseline and confirm the authors no longer separate
-   Pitfall: orthogonality is a property of the components, not evidence of authorship
-   Check-in: have students name a second corpus the method could be tried on
-   Record the corpus, the feature list, and the scaling so the result reproduces

## 12. Heat flow (physics)

-   How does temperature settle across a wall between a warm and a cold side?
-   Steady-state heat conduction obeys a simple equation with known analytic answers
-   Computational approach: solving a partial differential equation on a finite-difference grid

### Lecture 1: a one-dimensional wall

-   Motivation: the temperature in a wall is the simplest case of an equation that governs heat everywhere
-   Model a wall as a line of grid points between a warm left edge and a cold right edge
-   Write the steady-state heat equation as a finite difference on the grid
-   Worked example: a wall with a warm side at 100 degrees and a cold side at 0 degrees
-   Solve the linear system for the temperature at each interior point
-   Plot the temperature profile across the wall
-   Check the simple case: the profile should be a straight line
-   Pitfall: the finite-difference equation must match the physical equation, sign and all
-   Check-in: have students predict the temperature at the midpoint
-   Pointer: next lecture asks how the answer changes as the grid gets finer

### Lecture 2: refinement and convergence

-   Motivation: an approximate answer is only useful if it gets closer as the grid gets finer
-   Solve the same problem on progressively finer grids
-   Compare each solution with the known analytic straight-line answer
-   Worked example: grid sizes 5, 9, 17, and 33 points, recording the error at each
-   Measure the error and show it shrinks as the grid refines
-   Discuss the order of the method and why finer is not always better
-   Pitfall: the error may not shrink if the boundary conditions are applied incorrectly
-   Check-in: have students predict roughly how much the error drops when the grid doubles
-   Pointer: next lecture tests the solution against the physics

### Lecture 3: testing and reproducibility

-   Motivation: a heat solver must conserve heat and satisfy its boundary conditions
-   Test that the solution matches the analytic linear profile within a tolerance
-   Test that the temperature at each boundary equals the imposed value
-   Test conservation: the heat entering one side equals the heat leaving the other
-   Test that a finer grid gives a smaller error than a coarser one
-   Pitfall: a conservation test that sums over the wrong cells passes for the wrong reason
-   Check-in: have students name a second physical system the same equation describes
-   Record the grid size, the solver, and the boundary values so the result reproduces
