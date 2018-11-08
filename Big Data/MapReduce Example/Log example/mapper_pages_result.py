#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

count_ = 0
arr = []
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 2:
        page, count = data
        arr.append((page, count))

for item in (sorted(arr, key= lambda row: row[1], reverse=True)[:10]):
	print("{0}\t{1}".format(item[0], item[1]))

