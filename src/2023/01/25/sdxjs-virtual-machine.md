---
title: "Software Design by Example 19: Virtual Machine"
date: 2023-01-25
---

To explain how languages like JavaScript actually work,
[Chapter 19][sdxjs_vm] of [*Software Design by Example*][sdxjs]
builds a very simple virtual machine (VM)
and shows how to turn a low-level programming language into instructions for it.
The VM has three parts:

1.  An instruction pointer that holds the memory address of the next instruction to execute.

1.  Four registers that instructions can access directly.
    There are no memory-to-memory operations:
    everything happens in or through registers.

1.  256 words of memory, each of which can store a single value.

I was surprised that this chapter didn't need to be longer.
Looking over it again,
though,
I realize there's a lot of code I didn't have to explain.
Once readers have seen how `add` works, they don't need to see `subtract`;
once they've seen how to copy a value from memory into a register,
they don't need to see how to copy values in the other direction,
and so on.

I really wish I'd had enough [spoons][spoons] to build
an interactive visualization of this VM.
Since I didn't,
I suggest you check out the game [Human Resource Machine][hmr].
And if you want to know (a lot) more about this level in the tower of computing,
Bob Nystrom's [*Crafting Interpreters*][crafting] is free to read online
and one of the most beautifully crafted books on computing I've ever seen.

<figure id="virtual-machine-architecture" class="center">
  <img src="@root/sdxjs/virtual-machine/architecture.svg" alt="Virtual machine architecture" class="centered">
  <figcaption>Figure 19.1: Architecture of the virtual machine.</figcaption>
</figure>

> Terms defined: Application Binary Interface, assembler, assembly code, bitwise operation, disassembler, instruction pointer, instruction set, label (address in memory), op code, register, virtual machine, word (of memory).

[crafting]: https://craftinginterpreters.com/
[hmr]: https://tomorrowcorporation.com/humanresourcemachine
[sdxjs]: @root/sdxjs/
[sdxjs_vm]: @root/sdxjs/virtual-machine/
[spoons]: https://en.wikipedia.org/wiki/Spoon_theory
