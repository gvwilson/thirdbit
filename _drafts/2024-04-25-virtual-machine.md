---
title: "Software Design by Example in Python 25: A Virtual Machine"
date: 2024-04-25
year: 2024
---

In the end, you return to the beginning.
[This book][sdxpy] started
by showing learners how to implement objects and classes as dictionaries.
[Chapter 25: A Virtual Machine][sdxpy_vm] shows how to build a VM
and translate assembly code into binary instructions for it.
I don't try to explain how those instructions might be implemented in hardware,
but I hope anyone who has stuck with me this far
will come away from this chapter
with a better understanding of how languages like Python work.
For those who want to go deeper,
there is always Nystrom's excellent [*Crafting Interpreters*][crafting_interpreters].

<img class="centered" src="{{'/sdxpy/vm/concept_map.svg' | relative_url}}" alt="Concept map for a virtual machine"/>

> Terms defined: Application Binary Interface, assembler, assembly code, bytecode, conditional jump, disassembler, instruction pointer, instruction set, label (of address in memory), op code, register (in hardware), virtual machine, word (of memory).

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[crafting_interpreters]: https://craftinginterpreters.com/
[sdxpy]: {{'/sdxpy/' | relative_url}}
[sdxpy_vm]: {{'/sdxpy/vm/' | relative_url}}
