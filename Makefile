.DEFAULT: commands

SLIDES_SRC = $(wildcard src/talks/*/index.qmd)
SLIDES_DST = $(patsubst src/%.qmd,docs/%.html,$(SLIDES_SRC))
SLIDES_FLAGS = \
  -f markdown \
  -t revealjs \
  -s \
  -V theme=simple \
  -V slideNumber=true \
  --css=../../mccole/mccole-slides.css \
  --mathjax \
  --syntax-highlighting=tango

## commands: show available commands
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## site: rebuild site without running server
site:
	python bin/reading-list.py reading.csv src/reading-list.md
	ark build
	@$(MAKE) slides

## slides: build the talk slide decks with pandoc (reveal.js)
slides: $(SLIDES_DST)

docs/%.html: src/%.qmd
	@mkdir -p $(@D)
	pandoc $< $(SLIDES_FLAGS) -o $@
	@sed -i '' '/simple\.css/d' $@

## overflow: check slides for overflow
overflow:
	~/overflow/bin/slides-overflow.js -q $(SLIDES_DST)

## serve: build site and run server
serve:
	ark serve

## categories: show categories
categories:
	@python bin/find-tags.py

## count: count words in book
.PHONY: count
ifeq (${book},)
count:
	@echo "'book' not defined"
else
count:
	@python bin/count.py src/fiction/$${book}/index.md $${prev}
endif

## spelling: check spelling in book
.PHONY: spelling
ifeq (${book},)
spelling:
	@echo "'book' not defined"
else
spelling:
	@cat src/fiction/$${book}/index.md | aspell list | sort | uniq | diff - src/fiction/$${book}/words.txt
endif

## ----

## validate: check the generated HTML
validate:
	@html5validator --root docs \
	--blacklist btt js4ds mrsp sdxjs sdxpy \
	--ignore \
	'An "img" element must have an "alt" attribute' \
	'Attribute "markdown" not allowed on element' \
	'The "align" attribute on the "div" element is obsolete.' \
	'The "align" attribute on the "h2" element is obsolete.' \
	'The "align" attribute on the "p" element is obsolete.' \
	'The "align" attribute on the "td" element is obsolete.' \
	'The "align" attribute on the "th" element is obsolete.' \
	'The "bgcolor" attribute on the "td" element is obsolete.' \
	'The "cellpadding" attribute on the "table" element is obsolete.' \
	'The "center" element is obsolete.' \
	'The "font" element is obsolete.' \
	'The "frameborder" attribute on the "iframe" element is obsolete.' \
	'The "strike" element is obsolete.' \
	'The "tt" element is obsolete.' \
	'The "valign" attribute on the "td" element is obsolete.' \
	'The "valign" attribute on the "th" element is obsolete.' \
	'The "width" attribute on the "table" element is obsolete.' \
	'The "width" attribute on the "td" element is obsolete.' \
	'The "width" attribute on the "th" element is obsolete.' \
	--ignore-re 'Bad value ".+" for attribute "width" on element "img"'

## links: check links in local site
links:
	linkchecker --threads=50 -F csv http://localhost:8080

## clean: clean up stray files
clean:
	@find . -name '*~' -exec rm {} \;
	@find . -name '.DS_Store' -exec rm {} \;

## sterile: clean up and erase generated site
sterile:
	@make clean
	@rm -r docs/20*
	@rm -r docs/about docs/archive docs/atom.xml docs/blog
	@rm -r docs/colophon docs/conduct docs/cv docs/fiction
	@rm -r docs/ideas docs/index.html docs/license docs/projects
	@rm -r docs/selected docs/talks
