import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    words = re.split('\s*[,.!?:;"()<>\[\]#$=\-/\s]+\s*',line[4].lstrip().lower()+' ')
    #print words
    for word in words[:-1]:
        #writer.writerow([word, line[0]])
        print (word, '\t', line[0])