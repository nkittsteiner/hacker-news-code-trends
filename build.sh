#!/bin/sh
cd /home/nkittsteiner/hacker-news-code-trends
rm data.tar.gz
python ycombinator.py
tar zcvf data.tar.gz data.csv
git add .
git commit -m 'Updating dataset'
git pull -q
git push origin master
