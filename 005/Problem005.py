'''
  * Problem005.py
  *
  * Project Euler: Problem 5
  *
  * Problem: Find the smallest positive number that is
  * evenly divisible by all of the numbers from 1 to 20.
  *
'''

import time
start_time = time.time()

def is_divisible_to(number, max):
    for i in xrange(max,1,-1):
        if number % i != 0:
            return False
    return True

def divisible_to(n):
    if n < 1:
        return False
    elif n == 1:
        return 1
    else:
        step = divisible_to(n-1)
        current_attempt = 0
        complete = False
        while not complete:
            current_attempt += step
            complete = is_divisible_to(current_attempt,n)
        return current_attempt

print divisible_to(20)

print("--- %s seconds ---" % (time.time() - start_time))
