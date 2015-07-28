''' 
  * Problem021.py
  *
  * Project Euler: Problem 21
  * 
  * Problem: Find the maximum total from top to bottom of the triangle given.
  *          
  *
'''

import time
start_time = time.time()

def sum_divisors(num): return sum([x + num // x for x in xrange(1, int(num**0.5)+1) if num % x == 0]) - num

total = 0
for i in xrange(10001):
    current = sum_divisors(i)
    if sum_divisors(current) == i and current != i:
        total += i

print total

print("--- %s seconds ---" % (time.time() - start_time))