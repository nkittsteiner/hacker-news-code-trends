import json
import csv


def find_news(lang):
    news = []
    with open('pre-process.csv', 'rU') as csvfile:
        newsreader = csv.reader(csvfile, delimiter=';')
        for row in newsreader:
            if len(row) == 4 and row[2] == lang:
                news.append({'id': row[0], 'timestamp': row[1], 'lang': row[2], 'text': row[3]})


    return json.dumps(news)

def write_news(lang, news):
    with open("".join(('json/', lang, '.json')), 'w') as file:
        file.write(news)        


def init():
    file = open('json/count.json', 'rU')
    lines = file.readlines()
    json_array = json.loads(lines[0].strip())

    for item in json_array:
        lang = item['name']
        news = find_news(lang)
        write_news(lang, news)


if __name__ == "__main__":    
    init()                      