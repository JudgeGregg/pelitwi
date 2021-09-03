#!/bin/bash
# Transforms rst.txt pages to rst pelican compatible
python utils/script.py
# Copy from source to content input
cp -r ~/Projects/Python/twisource/twistedmatrix.com/documents/current/_sources/* ~/Projects/Python/pelitwi/content/pages/
# Restore index pages to git
git checkout -- content/pages
# Clean files not needed
find content/pages/ -name "index.html" -exec rm {} \;
find content/pages/ -name "*.txt" -exec rm {} \;
# Generate content output
pelican content -s pelicanconf.py -t themes/pelitwi
