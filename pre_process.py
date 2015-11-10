import yaml
import csv
import re

def find_string(str):
    response = {"flag": False, "type": None, "lang": None}
    with open("languages.yml", 'r') as stream:
        yml = yaml.load(stream)

        for key, value in yml.iteritems() :
            reg_exp = "\\b"
            if str.find(key) > -1:
                response['flag'] = True
                response['type'] = value['type']
                response['lang'] = key
                return response

    return response


with open('data.csv', 'rb') as csvfile:
     newsreader = csv.reader(csvfile, delimiter=';')
     for row in newsreader:
        print row[2]
        print (find_string(row[2]))