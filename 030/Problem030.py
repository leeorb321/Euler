''' 
  * Problem029.py
  *
  * Project Euler: Problem 29
  * 
  * Problem: Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
  * 
  *
'''

import time
start_time = time.time()

def is_sum_nth(num): return sum(int(str(num)[i])**5 for i in xrange(len(str(num)))) == num

print sum([x for x in xrange(2,6*9**5) if is_sum_nth(x)])


print("--- %s seconds ---" % (time.time() - start_time))