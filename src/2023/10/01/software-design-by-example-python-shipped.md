---
title: "Software Design by Example (Python edition) Has Shipped"
date: 2023-10-01
---

The Python version of [*Software Design by Example*][sdxpy] has just gone off to the publisher.
It will be several months before you can buy a copy,
but [the online version][sdxpy] will always be available online.
I am very grateful to everyone who got me this far:
I couldn't have done it without you.

<ul>
<li><a href="https://aosabook.org/"><em>The Architecture of Open Source Applications</em></a> series;</li>
<li><a href="https://maryrosecook.com/">Mary Rose Cook's</a> <a href="http://gitlet.maryrosecook.com/">Gitlet</a>;</li>
<li><a href="https://limpet.net/mbrubeck/">Matt Brubeck's</a> <a href="https://limpet.net/mbrubeck/2014/08/08/toy-layout-engine-1.html">browser engine tutorial</a>;</li>
<li><a href="https://browser.engineering/"><em>Web Browser Engineering</em></a>
    by <a href="https://pavpanchekha.com/">Pavel Panchekha</a> and Chris Harrelson;</li>
<li><a href="https://connorstack.com/">Connor Stack's</a> <a href="https://cstack.github.io/db_tutorial/">database tutorial</a>;</li>
<li><a href="https://arcanis.github.io/">Maël Nison's</a> <a href="https://classic.yarnpkg.com/blog/2017/07/11/lets-dev-a-package-manager/">package manager tutorial</a>;</li>
<li><a href="https://viewsourcecode.org/">Paige Ruten's</a> <a href="https://viewsourcecode.org/snaptoken/kilo/index.html">kilo text editor</a>
    and <a href="https://wasimlorgat.com/">Wasim Lorgat's</a> <a href="https://github.com/seem/editor">editor tutorial</a>;</li>
<li><a href="http://journal.stuffwithstuff.com/">Bob Nystrom's</a> <a href="https://craftinginterpreters.com/"><em>Crafting Interpreters</em></a>; and </li>
<li>the posts and <a href="https://wizardzines.com/">zines</a> created by <a href="https://jvns.ca/">Julia Evans</a>.</li>
</ul>
<p>I am grateful to Miras Adilov, Alvee Akand, Rohan Alexander, Alexey Alexapolsky, Lina Andrén, Alberto Bacchelli, Yanina Bellini Saibene, Adrienne Canino, Marc Chéhab, Stephen Childs, Hector Correa, Socorro Dominguez, Christian Drumm, Julia Evans, Davide Fucci, Thomas Fritz, Francisco Gabriel, Florian Gaudin-Delrieu, Craig Gross, Jonathan Guyer, McKenzie Hagen, Han Qi, Fraser Hay, Bahman Karimi, Carolyn Kim, Jenna Landy, Peter Lin, Becca Love, Dan McCloy, Ramiro Mejia, Michael Miller, Firas Moosvi, Joe Nash, Sheena Ng, Reiko Okamoto, Juanan Pereira, Mahmoodur Rahman, Arpan Sarkar, Dave W. Smith, Stephen M. Sturdevant, Ece Turnator, and Yao Yundong for feedback on early drafts of this material.</p>
<p>I am also grateful to Shashi Kumar for help with LaTeX,
to <a href="https://www.drafolin.ch/">Odin Beuchat</a> for help with JavaScript,
and to the creators of
<a href="https://black.readthedocs.io/">Black</a>,
<a href="https://flake8.pycqa.org/">flake8</a>,
<a href="https://glosario.carpentries.org/">Glosario</a>,
<a href="https://www.gnu.org/software/make/">GNU Make</a>,
<a href="https://pycqa.github.io/isort/">isort</a>,
<a href="https://www.dmulholl.com/docs/ark/main/">ark</a>,
<a href="https://www.latex-project.org/">LaTeX</a>,
<a href="https://pip.pypa.io/">pip</a>,
<a href="https://www.python.org/">Python</a>,
<a href="https://remarkjs.com/">Remark</a>,
<a href="https://wave.webaim.org/">WAVE</a>,
and many other open source tools:
if we all give a little,
we all get a lot.</p>
<div class="center">
<p><em>This one's for Mike and Jon: I'm glad you always found time to chat.</em></p>
<p>All royalties from this book will go to the <a href="https://www.reddoorshelter.ca/">Red Door Family Shelter</a> in Toronto.</p>
</div>

## Chapter 1: Introduction

The best way to learn design is to study examples, and the best programs to use as examples are the ones programmers use every day. These lessons therefore build small versions of tools that programmers use every day to show how experienced software designers think. Along the way, they introduce some fundamental ideas in computer science that many self-taught programmers haven't encountered. The lessons assume readers can write small programs and want to write larger ones, or are looking for material to use in software design classes that they teach.

## Chapter 2: Objects and Classes

Object-oriented programming was invented to solve two problems: what is a natural way to represent real-world "things" in code, and how can we organize that code so that it's easiser to undrestand, text, and extend? This chapter shows how object-oriented systems solve those problems by implementing a very simple object system using simpler data structures.

## Chapter 3: Finding Duplicate Files

The naïve way to find duplicated files is to compare each file to all the others, but that is unworkably slow for large sets of files. A better approach is to generate a short label that depends only on the file's contents so that we only need to compare files with the same label. This idea is the basis of many real-world applications, including the cryptographic systems used for secure online communication.

## Chapter 4: Matching Patterns

Pattern matching is ubiquitous in computer programs. Whether we are selecting a set of files to open or finding names and email addresses inside those files, we need an efficient way to find matches for complex patterns. This chapter therefore implements the filename matching used in the Unix shell to show how more complicated tools like regular expressions works.

## Chapter 5: Parsing Text

A parser turns text that's easy for a human being to read into a data structure that a computer can work with. The complete parser for a language like Python can be very complex, but this chapter illustrates the key ideas by building a parser for the simple filename matching patterns implemented in the previous chapter.

## Chapter 6: Running Tests

Every programming language has tools to collect tests, run them, and report their results. This chapter shows how such tools are built, both to help programmers use them more effectively, and to illustrate the single most important idea in this book: that programs are just another kind of data.

## Chapter 7: An Interpreter

A program in memory is just a data structure, each of whose elements triggers some operation in the interpreter that's executing it. This chapter builds a very simple interpreter to show how this process works, and to show that we can evaluate the quality of a program's design by asking how extensible it is.

## Chapter 8: Functions and Closures

This chapter extends the little interpreter of the previous one to allow users to define functions of their own. By doing so, it shows that the way programs handle variable scope is a design choice, and that the use of a particular technique called closures enables programs written in Python (and other modern programming languages) to encapsulate information in useful ways.

## Chapter 9: Protocols

This chapter starts by showing how we can simplify testing by temporarily replacing real functions with ones that return predictable values, then uses our need to do that to motivate discussion of ways that programmers can hook their own code into the Python interpreter. Unlike other chapters in this book, this one focuses on Python itself rather than the things we can build with it.

## Chapter 10: A File Archiver

Most programmers would agree that once they have a text editor and a way to run their programs, the next tool they need is version control. This chapter therefore shows how the core of a simple version control system works by building a file archiver that avoids creating duplicate copies of the same files.

## Chapter 11: An HTML Validator

This chapter builds a tool to check the structure of web pages in order to show how programs can process HTML, and to introduce a design pattern that is frequently used to manage irregular data structures.

## Chapter 12: A Template Expander

Writing and updating HTML pages by hand is time-consuming and error-prone, so most modern websites use some kind of static site generator (SSG) to create pages from templates. This chapter builds a simple SSG to show how they work and to reinforce earlier lessons about creating little programming languages.

## Chapter 13: A Code Linter

This chapter brings together pieces from the preceding few lessons to show how one program can check the structure of another. Tools that do this, called linters, rely once again on the fact that programs are just another kind of data.

## Chapter 14: Page Layout

Browsers, e-book readers, and text editors all rely on some kind of layout engine that takes text and formatting instructions as input and decides where to put each character and image. To explore how they work, this chapter builds a small HTML layout engine, and in doing so, introduces some useful ideas about recursion and multiple inheritance.

## Chapter 15: Performance Profiling

This chapter implements the kind of multi-column table frequently used in data science in two different ways in order to reinforce earlier ideas about the value of abstraction and to show how systematic performance testing can be used to decide between different implementation strategies.

## Chapter 16: Object Persistence

Some simple kinds of data can be saved as lines of text, but more complex data structures require a framework capable of handling aliasing and circularity. This chapter shows how to build such a framework, and in doing so demonstrates how libraries for handling JSON and other formats work.

## Chapter 17: Binary Data

Python and other high-level languages shield programmers from the low-level details of how computers actually store and manipulate data, but sooner or later someone has to worry about bits and bytes. This chapter explores how computers represent numbers and text and shows how to work with data at this level.

## Chapter 18: A Database

Almost every real-world application relies on some kind of database that allows code to look up data without loading everything into memory. To show how they work, this chapter builds a very simple database that appends every new copy of a record to a running log of operations.

## Chapter 19: A Build Manager

Programmers frequently need to chain operations together so that if one file is updated, everything that depends on it is also updated, and then things that depend on them are updated as well. This chapter builds a simple build manager to show how such tools work, and to introduce some fundamental algorithms on directed graphs.

## Chapter 20: A Package Manager

Most languages have an online archive from which people can download packages, each of which has a name, one or more versions, and a list of dependencies. In order to install a package, we need to figure out exactly what versions of its dependencies to install; this chapter explores how to find a workable installation or prove that there isn't one.

## Chapter 21: Transferring Files

A typical web application is made up of clients that send messages to servers and then wait for them to respond. This chapter shows how they work at a low level by building a simple low-level client-server program to move files from one machine to another.

## Chapter 22: Serving Web Pages

The Hypertext Transfer Protocol (HTTP) defines a way for programs to exchange data over the web. Clients (such as browsers) send requests to servers, which respond by copying files from disk, pulling records from a database, or in any of dozens of other days. This chapter shows how to build a simple web server that understands the basics of HTTP and how to test programs of this kind.

## Chapter 23: A File Viewer

Even simple editors like Notepad and Nano do a lot of things: moving a cursor, inserting and deleting characters, and more. This is too much to fit into one lesson, so this chapter builds a tool for viewing files, which the next chapters extends to create an editor with undo and redo.

## Chapter 24: Undo and Redo

Viewing text files is useful, but we'd like to be able to edit them as well. This chapter therefore modifies the file viewer of the preceding chapter so that we can add and delete text. And since people make mistakes, it also implements undo, which introduces another commonly-used design pattern.

## Chapter 25: A Virtual Machine

The standard version of Python is implemented in C, but C is compiled to instructions for a particular processor. To show how that lower layer works, this chapter builds a simulator of a small computer and an assembler for a very simple language that can be used to program it.

## Chapter 26: A Debugger

Debuggers are as much a part of good programmers' working lives as version control but are taught far less often. This chapter therefore builds a simple single-stepping debugger for the virtual machine of the previous chapter and shows how we can test it and other interactive applications.

## Chapter 27: Conclusion

We have long accepted that software can and should be critiqued by asking if it does what it's supposed to do and if it's pleasurable to use. What is often missing is the question of whether its design facilitated its manufacture and maintenance. We hope that this book has helped you move one step closer to being able to ask and answer that question about the things you build.

[sdxpy]: @root/sdxpy/
