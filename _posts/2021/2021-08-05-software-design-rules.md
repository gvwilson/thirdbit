---
title: "Software Design Rules"
date: 2021-08-05 14:05:07
year: 2021
---

My webinar on "[Software Design for Data Scientists]({{'/talks/sd4ds/' | relative_url}})" raised over $600 for [Books for Africa](https://www.booksforafrica.org/). The key points are summarized below; if you'd like me to give the talk to your company, university, or other organization, I'd be happy to do so in exchange for a donation to BfA or some other mutually-agreed charity.

Rule 0: Computer scientists aren't taught software design either, so don't feel like you've missed something.

Rule 1: Design for people's cognitive capacity (7±2, chunking, and all that).

Rule 2: Design toward widely-used abstractions and maximize the ratio of "what's unique in this statement" to boilerplate, but remember that the tradeoff between abstraction and comprehension depends on how much people already know.

Rule 3: Design for evolution, because the problem, the tools, and your understanding will all change each other. The key tool for this is information hiding; the Liskov Substitution Principle and Design by Contract will help.

Rule 4: Design for testability - not just because you want to test, but because it's a way to validate designs.

Rule 5: Design as if code was data, because it is. Programs are just text files; code in memory is just another data structure, and taking advantage of this can make designs much more elegant (but also less comprehensible to newcomers).

Rule 6: Design for delivery - organize your code the way your packaging system expects, handle errors instead of printing them and discarding them, and use a proper logging system.

Rule 7: Design graphically (but don't try to create software blueprints). Flowcharts, informal architecture diagrams, entity-relationship diagrams, and use case maps will all help people understand the overall design.

Rule 8: Design after the fact. The most important thing isn't to follow any particular process, it's to look as though you did so that the next person can retrace your steps.

Rule 9: Design with villains in mind, because security, privacy, and fairness can't be sprinkled on after the fact.

Rule 10: Design collaboratively and inclusively, because it will produce a better design (and because it's just the right thing to do).
