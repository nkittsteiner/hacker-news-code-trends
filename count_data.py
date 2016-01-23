import csv
import re 
import json
from collections import Counter


def ignore_word(word):
	response = False
	ignore_file = open('ignore_words.txt', 'r')
	lines = ignore_file.readlines()
	for line in lines:		
		if line.strip().lower() == word.lower():			
			return True

	return response

news = []
with open('pre-process.csv', 'rU') as csvfile:
     newsreader = csv.reader(csvfile, delimiter=';')
     
     for row in newsreader:
     	if len(row) == 4 and not ignore_word(row[2]):
    	    news.append(row[2])


ordered = []
for (k,v) in Counter(news).iteritems():        	
	ordered.append({"name": k, "count": v})


print json.dumps(sorted(ordered))	
