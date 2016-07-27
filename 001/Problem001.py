'''
  * Problem001.py
  *
  * Project Euler: Problem 1
  *
  * Problem: Find sum of all natural numbers
  * that are multuples of 3 or 5 below 1000.
  *
'''

import time
start_time = time.time()

# print sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, xrange(1,1000))) // slower, brute-force approach

print(sum(x for x in range(0,1000,3)) + sum(x for x in range(0,1000,5)) - sum(x for x in range(0,1000,15)))

print("--- %s seconds ---" % (time.time() - start_time))
