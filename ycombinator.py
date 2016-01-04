import requests
import datetime
import csv
import json
import sys
from collections import deque

def append_row(row):
	with open('data.csv','a') as csv_file:
		writer = csv.writer(csv_file, delimiter=";")
		writer.writerow(row) 


def get_last_row_id():
     with open('data.csv', 'rU') as f:
         s = deque(csv.reader(f), 1)[0]
         return int(', '.join(s).split(";")[0])


def init():
	url = 'https://hacker-news.firebaseio.com/v0/item/'
	count = get_last_row_id() + 1
	text = None

	last_id = int(requests.get("https://hacker-news.firebaseio.com/v0/maxitem.json").text)

	while count <= last_id:
		try:
			r = requests.get(url + str(count) + ".json")
			text = r.text
			json_array = json.loads(r.text)

			
			if json_array != None and json_array['type'] == 'story' and r.text.find("\"title\"") > -1:						
				append_row([count, json_array['time'], json_array['title']])
			count = count + 1
		except KeyboardInterrupt:
			print "Bye"
			sys.exit()
		except:
			count = count + 1


if __name__ == "__main__":
	init()
