import csv
import re 
from collections import Counter


def clean_string(s):
	s = s.lower()
	rx = re.compile('[^a-zA-Z-+#]+')
	res = rx.sub(' ', s).strip()
	return res

news = []
with open('data.csv', 'rb') as csvfile:
     newsreader = csv.reader(csvfile, delimiter=';')
     for row in newsreader:
     	pre_clean = clean_string(row[2])
        for word in pre_clean.split(" "):
        	news.append(word)


ordered = []
for (k,v) in Counter(news).iteritems():        	
	ordered.append({"name": k, "count": v})

for obj in sorted(ordered):
	print "%s:%s" % (obj['name'], obj['count'])