#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv

writer = csv.writer(sys.stdout, delimiter='\t')

keyA = None
keyB = None

def reducer():
    for line in sys.stdin:
    data = line.strip().split('\t')

        if (data[1] == 'A'):
    	    keyA = data[0]
            dataA = data[2:]

        if (data[1] == 'B'):
     	    keyB = data[0]
            dataB = data[2:]

        if keyA == keyB:
    	    writer.writerow(dataB[:3] + [keyA] + dataB[3:] + dataA)
