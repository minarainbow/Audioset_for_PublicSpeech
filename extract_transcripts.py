import os
import csv
from html.parser import HTMLParser
from bs4 import BeautifulSoup

# class MyHTMLParser(HTMLParser):
#     def __init__(self):
#         HTMLParser.__init__(self)
#         self.YTID =''
#         self.begin=0
#         self.end=0
#         self.script = ''


#     def handle_starttag(self, tag, attrs):
#         if tag == 'p':
#             for a in attrs:
#                 if a[0] == 'begin':
#                     begin = convert_time(a[1])
#                 elif a[0] == 'end':
#                     end = convert_time(a[1])
#             if (begin > self.begin - 10) or (end < self.end - 10):
#                 self.script += 

#     # def handle_endtag(self, tag):
#     #     print("Encountered an end tag :", tag)

#     # def handle_data(self, data):
#     #     print("Encountered some data  :", data)


def extract(row):
    YTID = row[0]
    start_seconds = int(row[1][:-4])
    end_seconds = int(row[2][:-4])
    # parser = MyHTMLParser()
    filename = 'subtitles/' + YTID + '.en.ttml'
    with open(filename, 'r+') as ttmlfile:
        # parser.feed(ttmlfile.read())
        soup = BeautifulSoup(ttmlfile)
        for tag in soup.find_all('p'):
            begin = convert_time(tag['begin'])
            end = convert_time(tag['end'])
            if (begin > start_seconds - 15) and (begin < end_seconds):
                print(YTID + tag.get_text())

def convert_time(ttml_time):
    tmp = ttml_time[:-4]
    tmp = tmp.split(':')
    time = int(tmp[0])*3600 + int(tmp[1])*60 + int(tmp[2])
    return time

directory = 'subtitles/'
with open('filemove/both_id.csv','r+') as csvfile:
    for filename in os.listdir(directory):
        found = False
        while not found:
            row = next(csv.reader(csvfile))
            # print(row)
            if row[0] == filename[:-8]:
                # print('found: '+row[0])
                extract(row)
                found = True
        csvfile.seek(0) 


    
