---
title: "Explaining Code"
date: 2023-07-20
---

I've been trying to avoid and ignore the current hype around AI,
but [Jon Udell][udell] has convinced me that
there's more to it than yet another Silicon Valley hype cycle.
Yesterday,
Jon took a short code sample from [Chapter 7][sdxjs-7] of [*Software Design by Example*][sdxjs]
and the accompanying explanation
and asked ChatGPT if the two were consistent.
This is a big headache for the authors of technical books:
you write and describe a bit of code,
but then a month later you refactor the code a bit
to make some later part of the book easier to write
and forget to update the explanation.

A tool that could point out places where this had happened
would save me dozens of hours and prevent dozens of mistakes from getting into print.
Jon's prompt and ChatGPT's response are below;
I will want to try a lot more examples before I trust it,
but damn…

## Prompt

I'm going to show you some code followed by a description.
Does the description accurately reflect the code?

```
import assert from 'assert'

const select = (root, selector) => {
  const selectors = selector.split(' ').filter(s => s.length > 0)
  return firstMatch(root, selectors)
}

const firstMatch = (node, selectors) => {
  assert(selectors.length > 0, 'Require selector(s)')

  // Not a tag.
  if (node.type !== 'tag') {
    return null
  }

  // This node matches.
  if (matchHere(node, selectors[0])) {
    // This is the last selector, so matching worked.
    if (selectors.length === 1) {
      return node
    }

    // Try to match remaining selectors.
    return firstChildMatch(node, selectors.slice(1))
  }

  // This node doesn't match, so try further down.
  return firstChildMatch(node, selectors)
}

export default select
```

> Description: 
>
> The firstMatch function handles three cases:
>
> 1.  This node isn't an element, i.e., it is plain text or a comment.
>     This can't match a selector,
>     and these nodes don't have children,
>     so the function returns null to indicate that matching has failed.
>
> 2.  This node matches the current selector.
>     If there aren't any selectors left then the whole pattern must have matched,
>     so the function returns this node as the match.
>     If there are more selectors,
>     we try to match those that remain against this node's children
>     and return whatever result that produces.
>
> 3.  This node doesn't match the current selector,
>     so we search the children one by one to see if there is a match further down.

## Response

Yes, the provided description does accurately reflect
the functionality of the `firstMatch` function within the given code.

Here's a step-by-step explanation:

1.  It first checks if there are any selectors to be matched,
    throwing an error if not.

2.  Then it checks if the node's type is not a tag.
    If the node is not a tag (meaning it could be a text node, a comment, etc.),
    it cannot be matched to a CSS selector,
    so it returns null.

3.  After that, it checks if the current node matches the first selector.
    If it does match,
    and there are no more selectors to be matched,
    it returns the current node,
    indicating a successful match.

4.  If the current node matches the first selector,
    but there are more selectors left to match,
    it attempts to match the remaining selectors against the node's children.
    It returns the result of that operation.

5.  Lastly, if the current node doesn't match the first selector,
    it checks the node's children one by one to see if a match can be found
    further down in the tree structure,
    returning the result of that operation.

Thus, the description provided does give a correct and detailed account
of the `firstMatch` function's behavior.

[sdxjs]: @root/sdxjs/
[sdxjs-7]: @root/sdxjs/pattern-matching/
[udell]: https://blog.jonudell.net/
