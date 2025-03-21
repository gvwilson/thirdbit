.DEFAULT: commands

## commands: show available commands
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## build: rebuild site without running server
build:
	ark build

## serve: build site and run server
serve:
	ark serve

## count: count words in book
.PHONY: count
ifeq (${book},)
count:
	@echo "'book' not defined"
else
count:
	@python bin/count.py src/fiction/$${book}/index.md $${prev}
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
	linkchecker -F text http://localhost:8080

## clean: clean up stray files
clean:
	@find . -name '*~' -exec rm {} \;
	@find . -name '.DS_Store' -exec rm {} \;

## sterile: clean up and erase generated site
sterile:
	@make clean
	@rm -rf docs
