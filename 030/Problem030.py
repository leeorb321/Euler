''' 
  * Problem030.py
  *
  * Project Euler: Problem 30
  * 
  * Problem: Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
  * 
  *
'''

import time
start_time = time.time()

print sum([x for x in xrange(2,6*9**5) if sum(int(str(x)[i])**5 for i in xrange(len(str(x)))) == x]) 

print("--- %s seconds ---" % (time.time() - start_time))