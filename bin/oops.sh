rm -f $(fgrep -l -e '<!-- content --><!-- /content -->' $(find docs -name '*.html'))
find docs -empty -type d -delete
