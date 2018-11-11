#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re

for line in sys.stdin:
    data = line.strip().split(" ")

    if (len(data) == 10):
        ip, identity, username, time, zone, method, path, protocol, status_code, size = data
	
	cleaned_path = path.replace('http://www.the-associates.co.uk', '')
	print "{0}\t{1}".format(cleaned_path, 1)
