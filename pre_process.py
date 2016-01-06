import sys
import yaml
import csv
import re


class YProcess():
    
    def __init__(self):
        with open("languages.yml", 'r') as stream:
            self.yml = yaml.load(stream)


    def find_string(self, word):
        response = None


        for key, value in self.yml.iteritems() :
            reg_exp = "\\b"
            if key in word and len(key) > 4:
                #print key, word
                response = key
            elif len(key) <= 4:
                if key.lower() == word.lower():
                    #print key, word
                    response = key

        return response



def init():

    yprocess = YProcess()

    with open('data.csv', 'r') as csvfile, open('pre-process.csv', 'wb') as outfile, open('data.csv', 'r') as csvfile2:
         newsreader = csv.reader(csvfile, delimiter=';')
         rowreader = csv.reader(csvfile2, delimiter=';')
         newswriter = csv.writer(outfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)

         count = sum(1 for row in rowreader)
         i = 1
         for row in newsreader:
            sys.stdout.write('\r')
            sys.stdout.write("Completed: %d%%" % ((i * 100) / count))
            sys.stdout.flush()
            i += 1

            pre_clean = row[2]

            for word in pre_clean.split(" "):
                response = yprocess.find_string(word)
                if  response is not None:
                    clean = row[2].replace(";","").replace("|", "")                    
                    newswriter.writerow([row[0], row[1], response, clean])

if __name__ == "__main__":    
    init()                    