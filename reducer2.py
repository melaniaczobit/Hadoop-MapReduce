#!/usr/bin/env python

from operator import itemgetter
import sys

words = {}

for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        # count not a number, discard line
        continue

    if word not in words:
        words[word] = count # add word to dictionary
    else:
        words[word] += 1
# sort dictionary in reverse order, based on count value        
sorted_rev = [(i, words[i]) for i in sorted(words, key=words.get, reverse=True)]
# from the sorted values, select the top 10
sorted_10 = sorted_rev[:10]
# print the top 10 key, value pairs 
for i,j in sorted_10:
    print '%s\t%s' % (i,j)

        
        