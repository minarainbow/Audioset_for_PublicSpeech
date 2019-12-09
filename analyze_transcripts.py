#!/usr/bin/env python

from __future__ import unicode_literals
import csv
import os
import logging.handlers
import multiprocessing_logging
import re

def split_sentences(st):
    sentences = re.split(r'[.?!()]\s*', st)
    if sentences[-1]:
        return sentences
    else:
        return sentences[:-1]

line_end_chars = '!', '?', '.', '(', ')', '...'
regexPattern = '|'.join(map(re.escape, line_end_chars))



inputfile = csv.reader(open('transcripts.csv','r+'))
outputfile = open('transcripts_analysis.csv','w')

# # for r in inputfile:
#     transcript = r[0]
#     url = r[1]
example = "Welcome to SOF! (Applause) This website securely stores U.S. data for the user? (Applause and Cheers) hmm... Hi!"
# line_list = split_sentences(example)
example = re.sub(r'\.+', ".", example)
line_list = re.findall('.*?[.!\?)]', example)
# line_list looks like this:
# ['Welcome to SOF', '(Applause)', ' This website securely stores U.S. data for the user', '(Applause and Cheers)', 'hmm.', Hi!']
# Now we just need to see which lines have our keyword
for i in range(len(line_list)):
    line = line_list[i]
    print('line:' + line)
    # if '(' in line:
    #     keyword = line
    #     print(keyword)

# with open('transcripts.csv', 'r+') as f:
#     for r in csv.reader(f):
#         YTID = r[0]
#         url = 'https://www.youtube.com/watch?v={}'.format(YTID)
#         subtitle_filepath = os.path.join('subtitles/'+YTID+'.en.ttml')
#         if os.path.exists(subtitle_filepath):
#                     info_msg = 'Already downloaded subtitle {} ({} - {}). Skipping.'
#                     LOGGER.info(info_msg)
#                     continue
#         print(url)
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
        
            
 