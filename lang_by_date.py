import json
import csv
import pandas as pd
from datetime import datetime


def find_news(lang):
    df = pd.DataFrame()
    with open('pre-process.csv', 'rU') as csvfile:
        newsreader = csv.reader(csvfile, delimiter=';')
        for row in newsreader:
            if len(row) == 4 and row[2] == lang:
            	temp_df = pd.DataFrame({'timestamp': pd.Timestamp(datetime.fromtimestamp(float(row[1]))), 'lang': row[2] }, index=[pd.Timestamp(datetime.fromtimestamp(float(row[1])))])
                df = df.append(temp_df)


    print df.groupby(lambda x: df['timestamp'][x].year)
    return json.dumps(df)

def write_news(lang, news):
    with open("".join(('json/', lang, '.json')), 'w') as file:
        file.write(news)        


def init():
    file = open('json/count.json', 'rU')
    lines = file.readlines()
    json_array = json.loads(lines[0].strip())

    json_array = json_array[len(json_array)-20:]

    for item in json_array:
        lang = item['name']
        news = find_news(lang)
        write_news(lang, news)


if __name__ == "__main__":    
    init()                      