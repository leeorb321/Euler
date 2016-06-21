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

def sum_digits_pwr5(num):
    total = 0
    while num:
        total += (num % 10)**5
        num /= 10
    return total

print sum(n for n in xrange(2,6*9**5) if n == sum_digits_pwr5(n))

print("--- %s seconds ---" % (time.time() - start_time))
