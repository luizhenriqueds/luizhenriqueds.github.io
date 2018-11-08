#!/usr/bin/python
## Calculating Mean with MapReduce

import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, store, item, cost, payment = data
    weekday = datetime.strptime(date, "%Y-%m-%d").weekday()

    #if weekday == 0:
    print "{0}\t{1}".format(weekday, cost)
