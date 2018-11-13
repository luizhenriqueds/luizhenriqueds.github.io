#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    data = line.strip().split(" ")

    if (len(data) == 10):
        ip, identity, username, time, zone, method, path, protocol, status_code, size = data
	
	cleaned_path = path.replace('http://www.the-associates.co.uk', '')
	print "{0}\t{1}".format(cleaned_path, 1)
