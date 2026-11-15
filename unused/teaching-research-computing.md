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

## 1. Segregation (sociology)

-   How do self-organized clusters emerge from mild individual preferences?
-   The Schelling model places two kinds of agent on a grid
-   Each agent moves when too few of its neighbors are like it

### Lecture 1: a grid, two kinds, one rule

-   Represent the city as a two-dimensional array of two kinds of cell plus empty cells
-   An agent is satisfied when at least a given fraction of its neighbors are the same kind as it
-   Each tick, move one unsatisfied agent to a random empty cell
-   Plot the grid before and after many ticks
-   The surprise: mild preferences (a threshold near one third) still produce large same-kind clusters

### Lecture 2: measuring segregation

-   Define a segregation score as the average fraction of an agent's neighbors that are unlike it
-   Sweep the similarity threshold from near zero to near one and record the final score
-   Show that segregation rises sharply at a modest threshold rather than gradually
-   Discuss the tipping point: a small change in preference, a large change in outcome
-   Introduce a random seed so every run is repeatable

### Lecture 3: testing and reproducibility

-   Test that a fully mixed board gives a segregation score near zero
-   Test that a fully sorted board gives a segregation score near one
-   Test that the score does not decrease when the threshold increases, all else equal
-   Test that the number of agents is conserved across ticks
-   Record the seed, the parameters, and the code version so a result can be reproduced

## 2. Epidemics (epidemiology)

-   How does an infection spread through a population and then fade?
-   The SIR model splits a fixed population into susceptible, infectious, and recovered people

### Lecture 1: three compartments

-   Define S, I, and R as the counts of susceptible, infectious, and recovered people
-   Write the rates of change: new infections grow as S times I, recoveries grow as I
-   Integrate the equations with an ODE solver over a fixed time span
-   Plot the three curves and the daily new cases
-   Identify the basic reproduction number as the ratio of the transmission and recovery rates

### Lecture 2: fitting to data

-   Replace the hand-tuned rates with parameters estimated from an observed case curve
-   Use least squares to fit the transmission and recovery rates to synthetic case counts
-   Compute the epidemic peak and the final size from the fitted parameters
-   Discuss identifiability: how well the data pin down each parameter

### Lecture 3: testing and reproducibility

-   Test that the total population is conserved: S plus I plus R equals N at every time
-   Test the no-transmission limit: when the transmission rate is zero, no new infections occur
-   Test that the epidemic curve has exactly one peak when the reproduction number is above one
-   Test that fitting recovers the true parameters from noiseless data
-   Pin the environment and the solver tolerances so the curves are reproducible

## 3. Predator and Prey (ecology)

-   How do predator and prey populations cycle together?
-   The Lotka-Volterra model can be written as a discrete-time map that computes next year's populations from this year's

### Lecture 1: a discrete-time map

-   Write the populations as two difference equations updated year by year
-   Choose a starting point and iterate the map for many steps
-   Plot prey and predator against time and against each other
-   Observe that the two populations cycle rather than settle
-   Contrast the discrete map with the continuous equations of the epidemics example

### Lecture 2: fixed points and stability

-   Find the fixed point where the map leaves the populations unchanged
-   Check whether small perturbations shrink or grow away from the fixed point
-   Sweep a growth parameter and watch the orbit move from a fixed point to a cycle to chaos
-   Discuss period doubling and the limits of simple population models

### Lecture 3: testing and reproducibility

-   Test that both populations stay positive for all time
-   Test that a fixed point stays fixed under one more iteration
-   Test the period of a cycle against a hand-computed value
-   Test that the no-predation limit gives geometric prey growth
-   Record the seed, the parameters, and the number of steps for reproducibility

## 4. Flood risk (hydrology)

-   How big a flood should a structure be designed to survive?
-   The annual maximum flow is modeled with an extreme-value distribution

### Lecture 1: return levels

-   Load a table of annual maximum river flows
-   Fit a log-normal distribution to the logarithms of the flows
-   Turn the fitted distribution into a return level for a given return period
-   Interpret the 100-year flood as a quantile, not a guarantee
-   Plot the data against the fitted curve

### Lecture 2: extremes and plotting positions

-   Compute plotting positions with the Weibull formula to compare data to fitted quantiles
-   Order the flows and check that the sorted values are non-decreasing
-   Examine the largest observations and whether they follow the fitted tail
-   Discuss why a few big floods dominate the estimate of extreme risk

### Lecture 3: testing and reproducibility

-   Test that the log-flows are close to normal by comparing sample quantiles with normal quantiles
-   Test that return levels increase as the return period increases
-   Test the identity that a return level satisfies the fitted cumulative distribution
-   Test that the plotting positions all lie strictly between zero and one
-   Fix the random seed and the fitting procedure so the numbers reproduce

## 5. Exoplanets (astronomy)

-   How do we infer the existence of a planet from the wobble of its star?
-   A planet tugs its star, causing a small periodic shift in the star's velocity toward or away from us

### Lecture 1: a star's wobble

-   Model the radial velocity as a sinusoid with a period, an amplitude, and an offset
-   Generate a synthetic velocity series from a known planet, sampled at irregular times
-   Plot the velocity series against time
-   Explain why the period is the scientifically interesting quantity
-   Note that the observations are unevenly spaced, which rules out a plain Fourier transform

### Lecture 2: finding the period in the spectrum

-   Compute a Lomb-Scargle periodogram of the velocity series
-   Find the highest peak in the periodogram and read off the period it implies
-   Show that a stronger planet signal gives a taller, sharper peak
-   Discuss false alarms and how a peak can be noise rather than a planet

### Lecture 3: testing and reproducibility

-   Test periodicity: shifting time by one full period leaves the model unchanged
-   Test that the periodogram of a noiseless series has a single peak at the true period
-   Test that the periodogram of pure noise has no peak above the false-alarm level
-   Test that the peak height grows with the signal amplitude
-   Record the noise model, the seed, and the periodogram settings so a detection can be audited

## 6. Perception (psychology)

-   How do we tell a real signal from background noise, and how good are we at it?
-   Signal detection theory separates sensitivity from bias using hits and false alarms

### Lecture 1: hits and false alarms

-   Given a list of trials with true labels and a decision on each, build a confusion table
-   Compute the hit rate among signal trials and the false-alarm rate among noise trials
-   Check the extreme cases: all hits, and no false alarms
-   Explain sensitivity versus bias: the criterion an observer chooses changes both rates

### Lecture 2: the receiver operating characteristic

-   Rank trials by a decision score rather than a single cutoff
-   Sweep a threshold across the scores to trace out the receiver operating characteristic curve
-   Confirm the curve starts at the origin and ends at the top right corner
-   Compute the area under the curve as a single summary of discrimination

### Lecture 3: testing and reproducibility

-   Test that hit and false-alarm rates are correct on small hand-built examples
-   Test that the curve is monotonic and passes through the corner for perfect scores
-   Test that a diagonal curve gives an area of one half and a perfect curve gives one
-   Test that separable score distributions give an area above one half
-   Record the scoring rule and the trial labels so the analysis reproduces

## 7. Evolutionary trees (biology)

-   How do we reconstruct the family tree of species from their traits or sequences?
-   Distance-based methods build a tree from pairwise distances between species
-   Lecture 1 builds a tree from a distance matrix with a simple method
-   Lecture 2 checks the tree against the assumption of a molecular clock
-   Lecture 3 tests the reconstruction on simulated data and measures support

### Lecture 1: distances and a tree

-   Start with pairwise distances between species taken from aligned sequences
-   Build a tree by joining the closest pair at each step
-   Plot the resulting tree and read off the distances between leaves
-   Explain why a tree, not a table, is the right object for ancestry

### Lecture 2: the molecular clock

-   Define an ultrametric distance matrix where all leaves are equally far from the root
-   Check whether the input distances satisfy the ultrametric condition
-   Explain what a violated clock implies about rates of change across lineages
-   Discuss neighbor joining as a method that does not assume a clock

### Lecture 3: testing and reproducibility

-   Simulate sequence evolution along a known tree and record the true tree
-   Test that the reconstruction recovers the known tree from clean distances
-   Test the additive property: distances along the reconstructed tree match the input
-   Test that a bootstrap resample gives high support for well-resolved branches
-   Record the simulation seed and the model of sequence change

## 8. Chemical fingerprints (chemistry)

-   How do we identify a molecule from the masses of its fragments?
-   A mass spectrum is a set of peaks at mass-to-charge ratios with intensities

### Lecture 1: peaks and calibration

-   Load a spectrum as a list of mass-to-charge values and intensities
-   Find local maxima above a noise floor to detect peaks
-   Calibrate the mass axis using two or more known reference peaks
-   Report the calibrated masses of the detected peaks
-   Discuss resolution: how close two peaks can be and still be told apart

### Lecture 2: matching to a library

-   Load a library of reference spectra for known molecules
-   Score how well the detected peaks match each library entry
-   Rank the library entries by match score
-   Discuss false matches and why a top score is not proof of identity

### Lecture 3: testing and reproducibility

-   Test that the calibration maps known reference masses to their true values
-   Test that peak detection finds injected synthetic peaks and ignores the noise floor
-   Test that matching against a copy of the same molecule ranks it first
-   Test that the result is stable when the noise seed changes
-   Record the calibration, the library version, and the noise model

## 9. Minerals (geology)

-   How do we name a rock or mineral from its measured composition?
-   A classifier maps a vector of measured features to a known category

### Lecture 1: nearest neighbors

-   Load a table of mineral samples with measured features and known labels
-   Split the data into a training set and a held-out test set
-   Classify each test sample by the label of its nearest training neighbor
-   Report accuracy as the fraction of correct labels
-   Discuss distance metrics and feature scaling

### Lecture 2: evaluation

-   Build a confusion matrix from the test predictions
-   Read off per-class precision and recall, not just overall accuracy
-   Sweep the number of neighbors and the distance metric
-   Discuss overfitting and why the test set must be untouched during training

### Lecture 3: testing and reproducibility

-   Test that a sample identical to a training sample is classified with its label
-   Test the classifier on a boundary case and inspect the decision
-   Test that accuracy never exceeds one and never falls below zero
-   Test that a shuffled-label run does not beat the real labels as a sanity check
-   Record the split, the seed, and the feature scaling so the numbers reproduce

## 10. Inequality (economics)

-   How unequally is wealth or income spread across a population?
-   The Lorenz curve and the Gini coefficient summarize inequality in one number

### Lecture 1: one number for inequality

-   Start with a list of incomes or wealth values for a population
-   Sort the values and accumulate shares of the total
-   Compute the Gini coefficient from the area formula or the mean absolute difference
-   Interpret the value: zero means equal, one means one person holds everything
-   Compute the Gini for a small hand-checkable example

### Lecture 2: the Lorenz curve

-   Plot the Lorenz curve: cumulative share of income against cumulative share of people
-   Relate the Gini coefficient to the area between the curve and the line of equality
-   Compare two distributions with the same mean but different inequality
-   Discuss what the Gini misses: it is one summary, not the whole distribution

### Lecture 3: testing and reproducibility

-   Test that a perfectly equal distribution gives a Gini of zero
-   Test that a maximally concentrated distribution gives a Gini approaching one
-   Test that the Gini is unchanged when all values are scaled by a constant
-   Test the Gini of a known distribution against its analytic value
-   Record the data source and the sorting convention so the number reproduces

## 11. Authorship (digital humanities)

-   How do we tell who wrote an anonymous text from word choice?
-   Stylometry measures subtle habits of word frequency that survive changes of topic

### Lecture 1: word-frequency features

-   Load a corpus of texts with known authors
-   Count the frequency of common function words such as "the", "of", and "and"
-   Normalize the counts so text length does not dominate
-   Explain why function words are better than topic words for authorship
-   Build a feature table of texts by word frequencies

### Lecture 2: principal component analysis

-   Center and scale the feature table so each word has equal weight
-   Compute the principal components of the feature table with a singular value decomposition
-   Project each text onto the first two components and plot the result
-   Check whether texts by one author separate in the projection
-   Discuss what the principal components mean and how many dimensions matter

### Lecture 3: testing and reproducibility

-   Test that the projection is stable when the feature list changes slightly
-   Test that a held-out text projects near the correct author's texts
-   Test that the principal components are orthogonal and sorted by variance explained
-   Test a shuffled-label baseline and confirm the authors no longer separate
-   Record the corpus, the feature list, and the scaling so the result reproduces

## 12. Heat flow (physics)

-   How does temperature settle across a wall between a warm and a cold side?
-   Steady-state heat conduction obeys a simple equation with known analytic answers

### Lecture 1: a one-dimensional wall

-   Model a wall as a line of grid points between a warm left edge and a cold right edge
-   Write the steady-state heat equation as a finite difference on the grid
-   Solve the linear system for the temperature at each interior point
-   Plot the temperature profile across the wall
-   Check the simple case: the profile should be a straight line

### Lecture 2: refinement and convergence

-   Solve the same problem on progressively finer grids
-   Compare each solution with the known analytic straight-line answer
-   Measure the error and show it shrinks as the grid refines
-   Discuss the order of the method and why finer is not always better

### Lecture 3: testing and reproducibility

-   Test that the solution matches the analytic linear profile within a tolerance
-   Test that the temperature at each boundary equals the imposed value
-   Test conservation: the heat entering one side equals the heat leaving the other
-   Test that a finer grid gives a smaller error than a coarser one
-   Record the grid size, the solver, and the boundary values so the result reproduces
