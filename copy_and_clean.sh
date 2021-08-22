#!/bin/bash
python utils/script.py
cp -r ~/Projets/twisource/twistedmatrix.com/documents/current/_sources/* ~/Projets/pelitwi/content/pages/
find content/pages/ -name "index.html" -exec rm {} \;
find content/pages/ -name "index.rst" -exec rm {} \;
find content/pages/ -name "*.txt" -exec rm {} \;
pelican content -s pelicanconf.py -t themes/pelitwi
