# default target
all : commands

## commands   : show all commands.
commands :
	@grep -E '^##' Makefile | sed -e 's/## //g'

## pdf        : generate a book via LaTeX
pdf :
	bin/concat.sh \
	| bin/pre-process.py \
	| pandoc -f markdown -t latex --template=template.tex \
	> temp.tex
	cat temp.tex \
	| bin/post-process.py \
	>  book.tex
	pdflatex book.tex
	pdflatex book.tex

## spelling   : check spelling
spelling :
	cat *.md | aspell list | sort | uniq | diff - words.txt

## wordcount  : how long is the book?
wordcount :
	wc -w *.md

## fixme      : look for undone work.
fixme :
	fgrep -i -n fixme *.md

## clean      : clean up junk files.
clean :
	@rm -f temp.tex book.pdf *.aux *.log *.out *.toc
	@find . -name '*~' -exec rm {} \;
	@find . -name .DS_Store -exec rm {} \;
