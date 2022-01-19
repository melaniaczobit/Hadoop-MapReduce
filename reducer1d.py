#!/usr/bin/env python

from operator import itemgetter
import sys

current_genre = None
best_genre = None
total_sales = 0
max_total = 0
genre = None

for line in sys.stdin:
    
    genre, sales = line.split('\t',1)
    
    try:
        sales = float(sales)
    except ValueError:
        # sales was not a float value, so discard line
        continue

    if current_genre == genre:
        total_sales += sales     # add to total for each genre
    else:
        if current_genre:
            if total_sales > max_total:
                max_total = total_sales
                best_genre = current_genre
        current_genre = genre
        total_sales = sales
# print genre with highest global sales        
print '%s\t%s' % (best_genre, max_total)