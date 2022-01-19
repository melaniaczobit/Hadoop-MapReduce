#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',')  # csv file input, split on comma

    if len(columns)==16:
        game = columns[0]   
        sales = columns[5]  
        print "%s\t%s" % (game,sales)
        

