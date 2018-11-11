#!/usr/bin/python
import sys

count_ = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    thisKey, thisValue = data

    if thisKey == "fantastically":
		print thisKey, "\t", thisValue


    if oldKey and oldKey != thisKey:
        if oldKey == "fantastic":
            print oldKey, "\t", count_
        oldKey = thisKey
        count_ = 0

    oldKey = thisKey
    count_ += 1

if oldKey != None:
    print oldKey, "\t", count_
