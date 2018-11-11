import sys

salesTotal = 0
oldKey = None
count_ = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    thisKey, thisSale = data
    if oldKey and oldKey != thisKey:
      print oldKey, "\t", salesTotal
      oldKey = thisKey
      salesTotal = 0

     oldKey = thisKey
     count_ += 1
     salesTotal += float(thisSale)

 if oldKey != None:
     print("sum: {}".format(salesTotal))
     print("mean: {0}\t{1}".format(oldKey, (salesTotal/count_)))
