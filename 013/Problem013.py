'''
  * Problem013.py
  *
  * Project Euler: Problem 13
  * 
  * Problem: Find the first ten digits of the sum of the given one-hundred 50-digit numbers.
  *
  *
'''

import time
start_time = time.time()

f = open("p13.txt", "r")

print str(sum([int(line) for line in f]))[:10]

f.close()

print("--- %s seconds ---" % (time.time() - start_time))