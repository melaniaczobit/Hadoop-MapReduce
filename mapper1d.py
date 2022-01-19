#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',')  # .csv file as input
    
    if len(columns)==16:
        genre = columns[3]
        sales = columns[9]  # global sales
        print "%s\t%s" % (genre,sales)

                        