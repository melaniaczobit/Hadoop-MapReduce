#!/usr/bin/env python

from operator import itemgetter
import sys

current_genre = None
current_game = None
best_game = None
current_sales = 0
max_sales = 0

genre_dict = {}

for line in sys.stdin:
    # input from mapper
    game, genre, sales = line.split('\t', 2)
    # sales must be a float
    try:
        sales = float(sales) 
    except ValueError:
        continue

    if genre not in genre_dict:   # add genre to dictionary, no duplictes
        current_genre = genre
        current_game = game
        current_sales = sales
        max_sales = 0
        genre_dict[current_genre] = [current_game, current_sales]
    else:
        if current_sales > max_sales:
            max_sales = current_sales
            best_game = current_game
            genre_dict[current_genre] = [best_game, max_sales] # update best game and max sale for every genre
        current_genre = genre
        current_game = game
        current_sales = sales
       
best_genres = [(i, genre_dict[i]) for i in genre_dict]
# for every key, value pair, print results        
for i, j in best_genres:
    print '%s\t%s\t%s' % (j[0],i,j[1])
    
 

        
        
     


    