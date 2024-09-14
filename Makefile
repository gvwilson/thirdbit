JEKYLL=jekyll
SITE=./_site

CONFIG=_config.yml
INCLUDES=$(wildcard _includes/*.html)
LAYOUTS=$(wildcard _layouts/*.html)
POSTS=$(wildcard _posts/*/*.md)
PAGES=\
	atom.xml\
	$(wildcard *.html)\
	$(wildcard */index.md)\
	$(wildcard archive/*.html)\
	bib/index.html\
	blog/index.html\
	talks/speaking.md
STYLES=$(wildcard _sass/*/*.scss) $(wildcard css/*.css) $(wildcard css/*.scss)

.DEFAULT: commands

## commands: show available commands
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## build: rebuild site without running server
build:
	${JEKYLL} build

## serve: build site and run server
serve:
	${JEKYLL} serve

## drafts: build site and run server showing drafts
drafts:
	${JEKYLL} serve --future --drafts

## ----

## status: create table showing status
.PHONY: status
status:
	@python bin/status.py --chart fiction/status.svg --info _data/info.csv --status _data/status.csv

## count: count words
.PHONY: count
ifeq (${book},)
count:
	@echo "'book' not defined"
else
count:
	@python bin/count.py fiction/$${book}/index.md
endif

## ----

## validate: check the generated HTML
validate:
	@html5validator --root _site \
	--blacklist blog btt js4ds mrsp sdxjs sdxpy \
	--ignore \
	'An "img" element must have an "alt" attribute' \
	'Attribute "align" not allowed' \
	'Attribute "label" not allowed on element "span"' \
	'The "align" attribute' \
	'The "bgcolor" attribute' \
	'The "border" attribute' \
	'The "cellpadding" attribute' \
	'The "font" element' \
	'The "strike" element is obsolete.' \
	'The "tt" element is obsolete.' \
	'The "valign" attribute' \
	'The "valign" attribute' \
	'The "width" attribute on the "td" element is obsolete' \
	--ignore-re 'Bad value ".+" for attribute "width" on element "img"'

## links: check links in published site
links:
	linkchecker -F text https://third-bit.com > LINKS.txt

## clean: clean up stray files
clean:
	@find . -name '*~' -exec rm {} \;

## sterile: clean up and erase generated site
sterile:
	@make clean
	@rm -rf ${SITE}
