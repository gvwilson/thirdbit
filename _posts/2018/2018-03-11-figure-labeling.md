---
title: "Wanted: A Tool for Figure Labeling Exercises"
date: 2018-03-11 01:30
year: 2018
---

I'd like to be able to do the following:

Step 1: Create a simple SVG diagram, some of whose labels are marked with `{% raw %}{{…}}{% endraw %}` or something similar:

<img src="{{'/files/2018/03/provinces-original.png' | relative_url}}" alt="Original diagram" width="500" />

Step 2: Include that diagram in a web page, giving it a special class.

Step 3: Include a small JavaScript library in the same web page (not shown).

Step 4: When the page loads, the JS looks for SVGs that have the magic class and transforms them so that:

- All the specially-marked text is pulled over to one side and displayed without the `{% raw %}{{…}}{% endraw %}` delimiters.
  (Any undelimited text is left where it was.)
- Markers are put in the figure to show where the delimited text was.

<img src="{{'/files/2018/03/provinces-unlabeled.png' | relative_url}}" alt="Labels on the side" width="600" />

Step 5: The person viewing the page can now drag labels from the side and drop them on the markers to re-label the diagram.
(If they change their mind about where a label should go, they can re-drag it as many times as they want.)

Step 6: When they're done, the library can compare the diagram they've reconstructed against the original and determine whether all the labels are in the right place.

This tool would let instructors create [many different kinds of exercises]({{'/2017/10/16/exercise-types.html' | relative_url}}),
since Parsons Problems and "match things in Column A with things in Column B" are just special cases of "put these bits of text in the right places".
More importantly,
it would let people who aren't programmers create them:
Anyone who can use a drawing tool capable of exporting SVG would just have to remember to include the `{% raw %}{{…}}{% endraw %}` delimiters
(or whatever the tool author chooses to use).
If you're interested in helping to build this,
please [give me a shout](mailto:gvwilson@third-bit.com?subject=re:%20diagram%20labeling%20tool).
