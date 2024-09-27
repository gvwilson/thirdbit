---
title: "Replacing Make"
date: 2023-11-13
---

I'd like to find a laptop-scale build/workflow tool to teach to data scientists instead of Make.
I've looked at [Snakemake][snakemake], [doit][doit], [invoke][invoke], [Metaflow][metaflow],
and several others,
but none quite meet my criteria:

1.  Workflow descriptions written in pure Python
    (not a syntactic superset and not YAML).

2.  Supports file dependencies and pattern rules (see the example below).

3.  Easy to see which files are required or produced by which rules.

4.  Can run shell commands as well as Python code.
    (Yes, I know that anything capable of running Python can use it to launch a shell command,
    but I'd like that out of the box.)

5.  Actively maintained.

Here's the kind of example I'd like to translate from Make to whatever;
if you know of something that'll do the job,
please [give me a shout](mailto:gvwilson@third-bit.com).

```make
# Pattern-match on all CSV files in the 'raw' directory.
RAW_FILES := $(wildcard raw/*.csv)

# Translate the names of the raw files into names of cooked files.
DATA_FILES := $(patsubst raw/%.csv,data/%.csv,${RAW_FILES})

# Define a single value for a variable explicitly.
SUMMARY_FILE := data/summary.csv

# Tell Make that 'all' and 'clean' don't alter any files.
.PHONY: all clean

# Define a default target that depends on the summary file, so that
# 'make' or 'make all' will try to regenerate it.
all: ${SUMMARY_FILE}

# Regenerate the summary file from the cooked data files.  This
# command only runs if the summary is out of date compared to any of
# the cooked data files.
${SUMMARY_FILE}: ${DATA_FILES} bin/summarize.py
	python bin/summarize.py ${DATA_FILES} > ${SUMMARY_FILE}

# Pattern rule to regenerate a cooked data file from a raw data
# file. The syntax of Make's automatic variables is horrible, but it's
# hard to argue with the simplicity of the rule itsef.
data/%.csv: raw/%.csv bin/cook.py
	python bin/cook.py < $< > $@

# Clean up.
clean:
	rm -f ${SUMMARY_FILE} ${DATA_FILES}
```

[doit]: https://pydoit.org/
[invoke]: https://www.pyinvoke.org/
[metaflow]: https://metaflow.org/
[snakemake]: https://snakemake.readthedocs.io/
