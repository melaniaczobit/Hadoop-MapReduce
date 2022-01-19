#!/usr/bin/env python

from operator import itemgetter
import sys

game = None
current_game = None
best_game = None
current_sales = 0
highest_sales = 0

for line in sys.stdin:

    game, sales = line.split('\t',1)
    
    # check is sales is a numerical (float) value
    try:
        sales = float(sales)
    except ValueError:
        continue

    if current_game == game:
        current_sales = sales
    else:
        if current_sales > highest_sales:
            highest_sales = current_sales
            best_game = current_game
        current_game = game
        current_sales = sales
        
print '%s\t%s' % (best_game, highest_sales)





