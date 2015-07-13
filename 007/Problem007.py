''' 
  * Problem007.py
  *
  * Project Euler: Problem 7
  * 
  * Problem: Find the 10,001st prime number.
  * 
  *
'''

import time
start_time = time.time()

from math import sqrt

def is_prime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 ==0:
        return False
    else:
        if int(sqrt(n)) % 2 == 0:
            max_check = int(sqrt(n)) - 1
        else:
            max_check = int(sqrt(n))
        for i in xrange(max_check, 1, -2):
            if n % i == 0:
                return False
    return True

def nth_prime(num):
    current_test, counter = 2, 0
    while counter < (num):
        if is_prime(current_test):
            counter += 1
        current_test += 1
    return current_test - 1

print nth_prime(10001)

print("--- %s seconds ---" % (time.time() - start_time))