---
title: "Data Dictionaries"
date: 2021-01-19
---

I was helping some friends analyze some data today,
and discovered that the `./data` directory in the project they had inherited
contained a file called `manifest.csv`
that was loaded and echoed in the top of their analysis notebook.
I can't show you what it contained---their data isn't public---but
the equivalent for Allison Horst's [Palmer Penguins dataset](https://allisonhorst.github.io/palmerpenguins/)
would look something like this:

```
table,column,type,unit,na,meaning
penguins,species,text,NA,false,common name of species
penguins,island,text,NA,false,island where data collected
penguins,bill_length,number,mm,true,bill length (Figure 1)
penguins,bill_depth,number,mm,true,bill depth (Figure 1)
penguins,flipper_length,number,mm,true,flipper length (Figure 2)
penguins,body_mass_g,number,mm,true,bird weight
penguins,sex,text,NA,true,bird sex
```

It's easier to see and appreciate laid out like this:

| table | column | type | unit | na | meaning |
| ----- | ------ | ---- | ---- | -- | ------- |
| penguins | species | text | NA | false | common name of species |
| penguins | island | text | NA | false | island where data collected |
| penguins | bill_length | number | mm | true | bill length (Figure 1) |
| penguins | bill_depth | number | mm | true | bill depth (Figure 1) |
| penguins | flipper_length | number | mm | true | flipper length (Figure 2) |
| penguins | body_mass_g | number | mm | true | bird weight |
| penguins | sex | text | NA | true | bird sex |

The table name is included because
the `manifest.csv` I'm imitating described several related data files;
one of the column descriptions even said,
"Foreign key into `other_table`/`other_name`".

This doesn't include everything---for example,
it doesn't specify which text fields are enumerations (or factors, if you're a statistician)---and
the figures referred to in the original `manifest.csv` aren't anywhere in the project repository---but
wouldn't life be better if every project you worked with came with something like this?
Having once spent several days trying to figure out
which temperature measurements in a dataset were °C and which were °F,
having [SI units](https://en.wikipedia.org/wiki/International_System_of_Units) somewhere discoverable
was enough to make me swoon.
