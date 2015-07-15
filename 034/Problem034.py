''' 
  * Problem034.py
  *
  * Project Euler: Problem 34
  * 
  * Problem: Find the sum of all numbers which are equal to the sum of the factorial of their digits (excluding 1, 2).
  * 
  *          
  *
'''

import time
start_time = time.time()

def factorial(n): return reduce(lambda x,y : x*y, xrange(1,n+1),1)

max = factorial(9)*7 + 1

def sum_fact_digits(n):
    sum = 0
    while n > 0:
        sum += factorial(n%10)
        n /= 10
    return sum

print sum(i for i in xrange(10, max) if i == sum_fact_digits(i))

print("--- %s seconds ---" % (time.time() - start_time))
