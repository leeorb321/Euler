''' 
  * Problem006.py
  *
  * Project Euler: Problem 6
  * 
  * Problem: Find the difference between the sum of the 
  *	squares of the first one hundred natural numbers and the square of the sum.
  *
'''

import time
start_time = time.time()

def sum_square_diff(n):
    return (n * (n+1)/2)**2 - (n * (2*n + 1) * (n+1)/6)

print sum_square_diff(100)

print("--- %s seconds ---" % (time.time() - start_time))