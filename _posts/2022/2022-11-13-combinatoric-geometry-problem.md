---
title: "A Combinatoric Geometry Problem"
date: 2022-11-13
year: 2022
---

Suppose you have a grid that's W squares wide and H squares tall.
How many different ways can you cover it with rectangular tiles?
It's easy enough to work out the answer for specific cases:

| Grid Size | Number of Tilings |
| --------- | ----------------- |
| 1x1       | 1                 |
| 1x2       | 2                 |
| 2x2       | 8                 |

but I can't figure out the formula for the general case—a simple recursive formula
double-counts configurations like the four size-one squares in the diagram above.
I also can't figure out a simple way to calculate the answer programmatically;
help with both would be greatly appreciated.

<div align="center"><img src="{{'/files/2022/combinatorics.svg' | relative_url}}" alt="Tilings" /></div>

*Later: several people have suggested divide-and-conquer strategies,
but so far I haven't seen one that would generate this case,
where there isn't a seam spanning either the entire height or width:*

<div align="center"><img src="{{'/files/2022/combinatorics-2.svg' | relative_url}}" alt="Another Tiling" /></div>
