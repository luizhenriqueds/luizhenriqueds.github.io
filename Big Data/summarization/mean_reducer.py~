#!/usr/bin/python

import sys

valuesTotal = 0
count_ = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", float(valuesTotal/count_)
        oldKey = thisKey;
        valuesTotal = 0
    	count_ = 0

    oldKey = thisKey
    valuesTotal += float(thisValue)
    count_ += 1

if oldKey != None:
    print oldKey, "\t", float(valuesTotal/count_)
