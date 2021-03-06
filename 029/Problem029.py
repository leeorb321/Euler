''' 
  * Problem029.py
  *
  * Project Euler: Problem 29
  * 
  * Problem: How many distinct terms are in the sequence generated by a^b for 2 <= a <= 100 and 2 <= b <= 100?
  * 
  *
'''

import time
start_time = time.time()

print len(set(a**b for a in xrange(2, 101) for b in xrange(2, 101)))

print("--- %s seconds ---" % (time.time() - start_time))