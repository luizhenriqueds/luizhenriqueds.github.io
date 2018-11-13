#!/usr/bin/python

import sys

valuesTotal = 0
oldKey = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", valuesTotal
        oldKey = thisKey
        salesTotal = 0

    oldKey = thisKey
    valuesTotal += int(thisValue)

if oldKey != None:
    print oldKey, "\t", valuesTotal

