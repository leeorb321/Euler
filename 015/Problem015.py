''' 
  * Problem015.py
  *
  * Project Euler: Problem 15
  * 
  * Problem: How many routes are there from top-left to bottom-right corner of a 20x20 grid (moving only right and down).
  *          
  *
'''

import time
start_time = time.time()

def factorial(n): return reduce(lambda x,y: x*y if x > 0 else 1, xrange(n+1))

'''Using a combinations formula (path of 2n steps in an n*n grid, of which half (n) are predetermined)
    formula of (n+n)!/(((n+n)/2)!*((n+n)/2)!)'''
n = 20
print factorial(2*n) / (factorial(n)*factorial(n))

print("--- %s seconds ---" % (time.time() - start_time))
