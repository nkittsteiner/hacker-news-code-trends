import csv
import re 
import json
from collections import Counter


def clean_string(s):
	s = s.lower()
	rx = re.compile('[^a-zA-Z-+#]+')
	res = rx.sub(' ', s).strip()
	return res

news = []
with open('pre-process.csv', 'rU') as csvfile:
     newsreader = csv.reader(csvfile, delimiter=';')
     for row in newsreader:
     	if len(row) == 4:
    	    news.append(row[2])


ordered = []
for (k,v) in Counter(news).iteritems():        	
	ordered.append({"name": k, "count": v})

for obj in sorted(ordered):
	print "%s:%s" % (obj['name'], obj['count'])

print json.dumps(sorted(ordered))
