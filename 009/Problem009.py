
''' 
  * Problem009.py
  *
  * Project Euler: Problem 9
  * 
  * Problem: Find the product abc of the Pythagorean triplet (a,b,c) for which a + b + c = 1000
  *          
  *
'''

import time
start_time = time.time()

print [(x*y*(1000-x-y)) for x in xrange(1,500) for y in xrange(x+1,500) if 1000 == x + y + (x**2+y**2)**0.5]

print("--- %s seconds ---" % (time.time() - start_time))
