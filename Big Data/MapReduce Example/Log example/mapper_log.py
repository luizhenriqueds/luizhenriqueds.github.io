#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re

regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'

for line in sys.stdin:
    data = line.strip().split('\n')
    extracted_log_message = map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))
    if (len(extracted_log_message)):
        ip, identity, username, time, request, status_code, size = extracted_log_message
        print(ip, username, request, status_code)
