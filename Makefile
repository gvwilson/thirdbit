# Settings
JEKYLL=jekyll

all : commands

## commands   : show all commands
commands :
	@grep -E '^##' Makefile | sed -e 's/## //g'

## serve          : run a local server.
serve :
	${JEKYLL} serve --config _config.yml,_config_dev.yml

## site           : build files but do not run a server.
site :
	${JEKYLL} build --config _config.yml,_config_dev.yml

## clean      : clean up.
clean :
	rm -rf _site $$(find . -name '*~' -print)
