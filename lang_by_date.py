import sys
import json
import csv
import pandas as pd
from datetime import datetime


def find_news(lang):
    response = []
    x =[]
    values = []
    df = pd.DataFrame()
    with open('pre-process.csv', 'rU') as csvfile:
        newsreader = csv.reader(csvfile, delimiter=';')
        for row in newsreader:
            if len(row) == 4 and row[2] == lang:
                date = pd.Timestamp(datetime.fromtimestamp(float(row[1])))
                temp_df = pd.DataFrame({'lang': row[2] }, index=[date])
                df = df.append(temp_df)

    group = df.groupby(lambda x: x.year).count()
    for element in group.to_dict()['lang'].iteritems():
        x.append(element[0])
        values.append(element[1])

    response.append(x)
    response.append(values)
    return response

def write_news(lang, news):
    with open("".join(('json/', lang, '.json')), 'w') as file:
        file.write(json.dumps(news))        


def init():
    file = open('json/count.json', 'rU')
    lines = file.readlines()
    json_array = json.loads(lines[0].strip())

    json_array = json_array[len(json_array)-20:]
    news = []
    xs = {}

    i = 1
    count = len(json_array)

    for item in json_array:
        sys.stdout.write('\r')
        sys.stdout.write("Completed: %d%%" % ((i * 100) / count))
        sys.stdout.flush()
        i += 1

        lang = item['name']
        xs[lang] = "x_" + lang
        arr = find_news(lang)

        keys = arr[0]
        keys.insert(0, xs[lang])
        values = arr[1]
        values.insert(0, lang)

        news.append(keys)
        news.append(values)
    

    response = {'xs': xs, 'news': news}

    write_news('yearmonth', response)


if __name__ == "__main__":    
    init()                      