---
title: "A Model Experiment"
date: 2020-01-04 14:25:00
year: 2020
---

A couple of years ago,
I pointed out that no one has ever done an empirical study to determine whether version control
is actually a better way to manage software projects than throwing files in a shared drive
or emailing them around.
I *think* it is,
but [dentists were wrong about flossing](https://www.bbc.com/news/health-36962667),
and as I said in [that earlier post]({{'/2018/03/13/base-case-for-empirical-software-engineering/' | relative_url}}),
designing an experiment to assess the value of version control
would force us to be explicit about how we're measuring the productivity benefits of software tools and practices.

I would like something similar for functional-with-a-small-f programming,
which I think would be easier to design and understand.
For thirty-five years I wrote code like this:

```
output = []
for item in input
    if passes_test(item)
        new_value = some_function(item)
        output.append(new_value)
    end if
end for
```

But these days I mostly write something like:

```
output = input
    .filter(item => passes_test(item))
    .map(item => some_function(item))
```

or:

```
output = input
    %>% filter(passes_test)
    %>% map(some_function)
```

Is this functional style easier or harder for novices to read or write?
More importantly (at least for me),
what study would produce an answer you would believe had settled the question?
"Take a bunch of non-programmers,
randomly assign them one of two groups,
teach each group one style,
then see how quickly they can solve some sample problems"
isn't a study design;
what I'm after is a description precise enough to pass review
as the "Methods" and "Analysis" sections of a research paper.

I think a couple of graduate students could have a lot of fun
designing an experiment like this
and then writing a detailed explanation of its parts.
I also think it would help bridge the gap between research and practice,
since it would help practitioners understand what researchers do and why.
If you're interested in giving it a try,
I'm [always happy to chat](mailto:gvwilson@third-bit.com).
