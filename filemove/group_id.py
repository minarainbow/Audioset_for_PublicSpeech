import csv
import os



with open('../dataset/eval_segments.csv') as infile:
    for i in range(3):
        next(infile)  # Skip the header rows
    for r in csv.reader(infile):
        YTID, start_seconds, end_seconds = (r[0:3])
        positive_labels = r[3:]
        positive_labels = "".join(positive_labels)
        if "/m/028ght" in positive_labels and "/m/09x0r" in positive_labels:
            with open('both_id.csv', 'r+') as f:
                if YTID not in f.read():
                    row_list = (r[0:3])
                    writer = csv.writer(f)
                    writer.writerow(row_list)
                else:
                    continue
            with open('both_id.txt', 'r+') as f:
                if YTID not in f.read():
                    f.write('https://www.youtube.com/watch?v={}'.format(YTID)+'\n')
                else:
                    continue
        # else:
        #     print("skip")

with open('../dataset/balanced_train_segments.csv') as infile:
    for i in range(3):
        next(infile)  # Skip the header rows
    for r in csv.reader(infile):
        YTID, start_seconds, end_seconds = (r[0:3])
        positive_labels = r[3:]
        positive_labels = "".join(positive_labels)
        if "/m/028ght" in positive_labels and "/m/09x0r" in positive_labels:
            with open('both_id.csv', 'r+') as f:
                if YTID not in f.read():
                    row_list = (r[0:3])
                    writer = csv.writer(f)
                    writer.writerow(row_list)
                else:
                    continue
            with open('both_id.txt', 'r+') as f:
                if YTID not in f.read():
                    f.write('https://www.youtube.com/watch?v={}'.format(YTID)+'\n')
                else:
                    continue
        # else:
        #     print("skip")

with open('../dataset/unbalanced_train_segments.csv') as infile:
    for i in range(3):
        next(infile)  # Skip the header rows
    for r in csv.reader(infile):
        YTID, start_seconds, end_seconds = (r[0:3])
        positive_labels = r[3:]
        positive_labels = "".join(positive_labels)
        if "/m/028ght" in positive_labels and "/m/09x0r" in positive_labels:
            with open('both_id.csv', 'r+') as f:
                if YTID not in f.read():
                    row_list =(r[0:3])
                    writer = csv.writer(f)
                    writer.writerow(row_list)
                else:
                    continue
            with open('both_id.txt', 'r+') as f:
                if YTID not in f.read():
                    f.write('https://www.youtube.com/watch?v={}'.format(YTID)+'\n')
                else:
                    continue
        # else:
        #     print("skip")
