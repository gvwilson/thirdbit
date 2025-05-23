---
title: "Teaching For Loops"
date: 2015-12-10
original: swc
---

A few days ago,
Karin Lagesen asked people what metaphors they use when teaching for loops.
It kicked off an
entertaining thread.
When we talk about pedagogical content knowledge (PCK) in instructor training,
this is exactly the kind of thing we mean:

-   A weekly travel card/multiride card on whatever the local public transport is.
    (On GM buses, this used to be a real piece of cardboard that would be clipped by a machine,
    giving a visual representation).
    It kind of breaks down as you do other things at either end of the journey, rather than remaining within the loop.

-   A dental checkup.
    There are a finite number of teeth, and the dentist checks each one in turn for cavities and gum disease.

-   Checking your email in the morning,
    treating each item of mail in the inbox as an item to be dealt with
    (although the cognitive load of deciding whether to deal with an email does defeat us all in the end).

-   One example that I've used in words, and want to try in reality
    is to take an egg box with one row of eggs,
    then take them out one at a time and crack them (into a jug).
    We could also number the eggs with a marker from 0 and use this to display list access.
    The main reason for doing this with an egg box is that it extends to two dimensions,
    so the metaphor can extends to numpy array examples with two indices,
    which always seems to cause more issues.

-   I just flip pages on a book.
    I like the book analogy because the action could be, read the page, search for a string or fill the "o"s.
    Additionally, since the books have page numbers I could get the "index" too (i.e., enumerate),
    but I don't explain the two examples at the same time–I introduce the enumerate function
    to people is already confident with the loop.

-   I like the example about pixels in an image.
    For each pixel in an image row by row, do something
    (for example convert color to grayscale).
    Most students have a good intuition about images, pixels, and other media examples.
    (Note: Matt Davis built a very cool module for the Jupyter notebook called <a href="http://ipythonblocks.org/">ipythonblocks</a>
    that rendered small images using HTML and CSS–you can grab the plugin
    from <a href="https://github.com/jiffyclub/ipythonblocks">GitHub</a>.
    Mike Hansen built the <a href="http://scikit-image.org/docs/stable/api/skimage.novice.html">skimage.novice</a> module
    to provide similar functionality on top of SciPy's image manipulation
    as a bridge between the simple-but-slow and the real-but-harder-to-understand.)

-   A couple of metaphors I've used in a course for a Master's degree in bioinformatics.
    The first one is,
    "Your boss asks for 20 flasks of a solution.
    You get the first flask, add water, add the solute, put the flask away from the empty ones, repeat the same procedure for every flask.
    Do you have to change something if the flasks are 30? 100?
    If you use a different solute, do you have to change a lot in this procedure?"

    The second one aims to introduce the concept of many operations on each item
    by trying to move away from the single activity per item.
    "We want to compute the average height and the distribution of hair colors of the people in the room.
    I could call you one by one,
    ask for the height,
    perform the summation and, after everyone showed up,
    divide the value by your number.
    Then I call you again, one by one, and ask for hair color.
    In this way you have to stand up twice,
    wasting a lot of time,
    while I could instead ask for height <em>and</em> hair color while it is your turn in the queue".
    After that,
    I usually re-use the queue metaphor to introduce nested loops,
    i.e., for each person in the queue a clerk asks for each item in a checklist list.

-   The main conceptual hang-up seems to be how the variable gets reassigned each time. 
    I use a shopping basket and then <code>for item in basket</code>.
    The fact that the item could be a single thing or a carton of eggs (i.e., a sub-list) which could also be looped through helps.  

-   You can start with the unrolled version and then introduce for as a better way to write it.
    For example:

    ```
    print "hi there, bill"
    print "hi there, sue"
    print "hi there, bob"
    ```

    Ask what is similar about all these?  What is the underlying "template"?  Try and get them to identify something like:

    ```
    print "hi there", name
    ```

    From there it isn't such a big stretch to go to:

    ```
    for name in ["bill", "sue", "bob"]:
    ```

-   I've taught basic programming to kids and in these cases it's always nice to have a metaphor with candy:

    ```
    def Halloween:
      plan costume
      get in costume
      go outside
      for house on street:
         walk to house
         ring doorbell
         get candy
         say thank you
    ```

    If you've already taught if statements, you can do:

    ```
    if trick:
      run away screaming
    else:
      take candy
    ```

-   Take an empty cup: this is going to be your variable (a "container").
    Write something on a sticky note, and put the sticky note in the cup.
    Now your variable has a value.
    Ask a student or helper to "echo" the content of the variable,
    i.e., read what is written on the sticky note.
    Replace the sticky note with another one with some other data, "echo" again.

    When it comes to loops,
    ask a few students (e.g., the front row) to each write their name on a sticky note.
    Take your (empty) cup and go to the first student,
    ask her/him to place the sticky note in the cup.
    Go to the "echo" student/helper and ask for him/her to read the content.
    Go to student number 2,
    replace the sticky note with this student's note,
    and redo the echo.
    Repeat until all names have been read.
    Remark that the cup still contains the name of the last student.

There was also a suggestion that we should teach loops after functions
so that learners have something to do inside their loops.
We actually used to do this,
but learners didn't seem to find small functions without any control flow inside them compelling.
Teaching loops first gives us something to put into our functions,
but we haven't done any rigorous comparisons to see if it actually works better.