---
title: "Software Design by Example 13: Module Loader"
date: 2023-01-17
---

The [previous chapter][sdxjs_interpolator] showed how to use `eval` to load code dynamically.
[This chapter][sdxjs_loader] uses some of those ideas
to build a small version of JavaScript's `require` function.
This function takes the name of a source file as an argument and returns whatever that file exports
(typically, a bunch of constants and functions).
The key requirement for such a function is to avoid accidentally overwriting things:
if we just `eval` some code and it happens to assign to a variable called `x`,
anything called `x` already in our program might be overwritten.

The real focus of the chapter is therefore how to encapsulate what we're loading,
i.e.,
how closures work and how to use them to implement namespaces.
Our approach is based on
the excellent tutorial in Casciaro and Mammino's book
[*Node.js Design Patterns*][node_patterns],
which contains a lot of other useful information as well.

<div class="row">
  <div class="col-6">
    <figure id="module-loader-iife-a" class="center">
      <img src="@root/sdxjs/module-loader/iife-a.svg" alt="Implementing modules with IIFEs (part 1)" class="centered">
      <figcaption>Figure 13.2: Using IIFEs to encapsulate modules and get their exports (part 1).</figcaption>
    </figure>
  </div>
  <div class="col-6">
    <figure id="module-loader-iife-b" class="center">
      <img src="@root/sdxjs/module-loader/iife-b.svg" alt="Implementing modules with IIFEs (part 2)" class="centered">
      <figcaption>Figure 13.3: Using IIFEs to encapsulate modules and get their exports (part 2).</figcaption>
    </figure>
  </div>
</div>

> Terms defined: absolute path, alias, circular dependency, closure, directed graph, encapsulate, immediately-invoked function expression (IIFE), inner function, Least Recently Used cache, namespace, plugin architecture.

[node_patterns]: https://www.packtpub.com/product/nodejs-design-patterns-third-edition/9781839214110
[sdxjs]: @root/sdxjs/
[sdxjs_interpolator]: @root/sdxjs/file-interpolator/
[sdxjs_loader]: @root/sdxjs/module-loader/
