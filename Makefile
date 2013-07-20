PAGES=index.html about.html blog.html cv.html
POSTS=$(wildcard _posts/*.html)
LAYOUTS=$(wildcard _layouts/*.html)
INCLUDES=$(wildcard _includes/*.html)

all : _site/feed.xml

_site/feed.xml : _config.yml feed.xml $(PAGES) $(LAYOUTS) $(INCLUDES) $(POSTS)
	jekyll build

clean :
	rm -rf _site $$(find . -name '*~' -print)
