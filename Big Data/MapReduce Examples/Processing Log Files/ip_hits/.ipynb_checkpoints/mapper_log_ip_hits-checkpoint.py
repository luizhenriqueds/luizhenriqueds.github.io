#!/usr/bin/python

import sys
import re

regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'

for line in sys.stdin:
    data = line.strip().split('\n')
    extracted_log_message = map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))
    if (len(extracted_log_message) == 7):
        ip, identity, username, time, request, status_code, size = extracted_log_message
        if (ip.find('10.99.99.186')!= -1):
            print "{0}\t{1}".format(ip, 1)
