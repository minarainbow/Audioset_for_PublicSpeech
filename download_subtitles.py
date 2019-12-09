#!/usr/bin/env python

from __future__ import unicode_literals
import youtube_dl
import csv
import os
import logging.handlers
import multiprocessing_logging

LOGGER = logging.getLogger('audiosetdl')
LOGGER.setLevel(logging.DEBUG)

ydl_opts = {
    'writeautomaticsub': True,
    'subtitleslangs': ['en'],
    'subtitlesformat': 'ttml',
    'outtmpl': 'subtitles/%(id)s',
    'skip_download': True,
    'ignoreerrors': True }

# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])


with open('filemove/both_id.csv', 'r+') as f:
    for r in csv.reader(f):
        YTID = r[0]
        url = 'https://www.youtube.com/watch?v={}'.format(YTID)
        subtitle_filepath = os.path.join('subtitles/'+YTID+'.en.ttml')
        if os.path.exists(subtitle_filepath):
                    info_msg = 'Already downloaded subtitle {} ({} - {}). Skipping.'
                    LOGGER.info(info_msg)
                    continue
        print(url)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
            
 