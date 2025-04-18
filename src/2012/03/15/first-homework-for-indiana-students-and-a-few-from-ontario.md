---
date: 2012-03-15
original: swc
title: First Homework for Indiana Students (and a few from Ontario)
---
<p>We ran our first online tutorial yesterday for students from our recent bootcamp in Indiana (plus a few from Toronto). Despite some technical difficulties with web conferencing, we managed to get through some basic image processing. The learners all now have homework for next week (shown below); considering that most of them have little prior programming experience, and only a half day of Python, it's pretty cool that they're able to do things like this.</p>
<p>1. Install the <a href="http://www.pythonware.com/products/pil/">Python Imaging Library</a>. Everything we'll need is in the <a href="http://www.pythonware.com/library/pil/handbook/image.htm">documentation</a> for the core module.</p>
<p>2. The <code>picture.py</code> program attached will either double the blue and green in an image, or cut the red in half, depending on how you run it:</p>
<pre>$ python picture.py double input.jpg output.jpg
$ python picture.py half input.jpg output.jpg</pre>
<p>The actual work is done in the functions <code>half_red</code> and <code>double_blue_green</code>. There's a lot of redundant code in there–in fact, other than their names, those functions only differ by one half of one line. Have a look at our lessons to review how functions work in Python, and then at the first half of the lesson on object-oriented programming (you don't need to know about variable numbers of arguments for this exercise), and then try to rewrite <code>picture.py</code> so that the loop over the X and Y dimensions of the picture only appears once, in one function called <code>adjust_colors</code>. That function may <em>not</em> contain any <code>if</code> statements; instead, it should take four parameters:</p>
<ol>
<li>the X size of the image</li>
<li>the Y size of the image</li>
<li>the image data</li>
<li>one other thing that you have to figure out</li>
</ol>
<p>3. Write a new program called <code>average.py</code> that takes a single image filename as a command-line argument, and prints out three integers on a single line showing the average red, green, and blue values of the image's pixels. For example:</p>
<pre>$ python average.py maddie.jpg
112 83 85</pre>
<p>4. Write another new program called <code>exaggerate.py</code> that takes two filenames as command-line arguments. The first is the name of an existing image; the second is the name of a new image that is to be created. The program sets the red, green, and blue values of each pixel to either 0 (the minimum possible) or 255 (the maximum possible) according to whether they are less than or greater than the average value for that color over the whole image. For example, using the average red-green-blue values from Question #3, if a pixel's original value is (10, 100, 200), its new value is (0, 255, 255), because there's less red than average, but more green and more blue. If your starting image is maddie-coy-flower.jpg (attached), your final image should be the exaggerated.jpg image (also attached).</p>
