#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',')  # input file is .csv
    
    if len(columns)==16:
        game = columns[0]
        genre = columns[3]
        sales = columns[9]
        print "%s\t%s\t%s" % (game,genre,sales)


