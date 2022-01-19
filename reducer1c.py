#!/usr/bin/env python

from operator import itemgetter
import sys

current_year = None
best_year = None
total_sales = 0
max_total = 0
year = None

for line in sys.stdin:
    # year and sales values from mapper
    year, sales = line.split('\t',1)
    
    try:
        sales = float(sales)
    except ValueError:
        # sales was not a float value, discard this line
        continue
    
    if current_year == year:
        total_sales += sales    # add sales to total for each year
    else:
        if current_year:
            if total_sales > max_total:
                max_total = total_sales    
                best_year = current_year
        total_sales = sales
        current_year = year
# print year with maximum sales
print '%s\t%s' % (best_year, max_total)
        
