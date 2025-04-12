---
title: Filling a Grid
date: 2025-04-12
---

I have a discrete NxN grid and a potentially infinite supply of specimens to place on it.
I will keep generating and addings specimens until the grid is full;
the constraint is that each specimen *i* has a neighborhood radius r<sub>i</sub>
such that no two specimens' neighborhoods may overlap.
(Basically,
each specimen has a territory that other specimens don't enter.)

My brute-force algorithm for filling the grid has O(N<sup>3</sup>) running time.
Is there a better way?
I value simplicity over speed, and working Python code over either.
