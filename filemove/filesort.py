import csv
import os

# SOURCE_ROOT = '../dataset/data/eval_segments/audio'
SOURCE_ROOT = '../dataset/sorted_audio/applause'
DEST_ROOT = '../dataset/sorted_audio'



def format_path(path):
    new_path = '_'.join(path.split())
    new_path = new_path.replace('.000', '000')
    new_path = new_path.replace('_0000', '_0')
    return new_path

with open('../dataset/eval_segments.csv') as infile:
    for i in range(3):
        next(infile)  # Skip the header rows

    for YTID, start_seconds, end_seconds, positive_labels in (r[0:4] for r in csv.reader(infile)):
        src = os.path.join(SOURCE_ROOT, YTID + start_seconds  + end_seconds + '.flac')
        src = format_path(src)
        dest = src
        # if '/m/028ght' in positive_labels:
        #     dest = os.path.join(DEST_ROOT, 'applause', YTID + start_seconds + end_seconds + '.flac')
        #     dest = format_path(dest)
        #     if os.path.exists(src):
        #         print('applause: ' + src)
        # if '/m/09x0r' in positive_labels:
        #     dest = os.path.join(DEST_ROOT, 'speech', YTID + start_seconds + end_seconds + '.flac') 
        #     dest = format_path(dest)
        #     if os.path.exists(src):
        #         print('speech: ' +src)
        if ('/m/028ght' in positive_labels) and ('/m/09x0r' in positive_labels):
            dest = os.path.join(DEST_ROOT, 'both', YTID + start_seconds + end_seconds + '.flac') 
            dest = format_path(dest)
            if os.path.exists(src):
                print('both: ' +src)
        # else:
        #     # print(positive_labels)
        #     dest = src

        if os.path.exists(src):
            try:
                os.rename(src, dest)
            except OSError as e:
                print(e)


