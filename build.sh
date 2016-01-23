#!/bin/sh

rm data.tar.gz

#python ycombinator.py

tar zcvf data.tar.gz data.csv

git add .

git commit -m 'Updating dataset'

git pull

git push origin master
