#!/usr/bin/env python
import sys

for line in sys.stdin:
    columns = line.strip().split(',') 
    
    if len(columns)==16:  # checks if columns in missing inputs
        year = columns[2]
        sales = columns[5]
        print "%s\t%s" % (year,sales)
         