INSTALL_DIR=$(HOME)/sites/third-bit.com
PAGES=$(wildcard *.html) $(wildcard pages/*.html)
POSTS=$(wildcard _posts/*.html)
LAYOUTS=$(wildcard _layouts/*.html)
INCLUDES=$(wildcard _includes/*.html)

all : commands

## commands   : show all commands
commands :
	@grep -E '^##' Makefile | sed -e 's/## //g'

## site       : build locally into _site directory for checking.
site :
	jekyll build

## drafts     : build locally into _site directory for checking with drafts.
drafts :
	jekyll build --drafts

## install    : build into installation directory for sharing.
install :
	rm -rf $(INSTALL_DIR)
	cp -r _site $(INSTALL_DIR)

## serve      : serve locally (builds files).
serve :
	jekyll serve

## clean      : clean up.
clean :
	rm -rf _site $$(find . -name '*~' -print)
