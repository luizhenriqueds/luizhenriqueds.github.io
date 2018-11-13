#!/usr/bin/python

import sys

hitCount = 0
maxHit= 0
oldKey = None
maxKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        if hitCount > maxHit:
		maxHit = hitCount
		maxKey = oldKey
        hitCount = 0

    oldKey = thisKey
    hitCount += 1

if oldKey != None and hitCount > maxHit:
    maxHit = hitCount
    maxKey = oldKey
   
print maxKey, "\t", maxHit

