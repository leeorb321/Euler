'''
  * Problem004c.py
  *
  * Project Euler: Problem 4
  *
  * Problem: Find the largest palindrome made from the product of two 3-digit numbers.
  *
  *
'''

import time
start_time = time.time()

is_palindrome = lambda x: str(x) == str(x)[::-1]


for i in xrange(999,899,-1):
    for j in xrange(999,899,-1):
        if is_palindrome(i*j):
            print i*j
            break
    if is_palindrome(i*j):
        break

print("--- %s seconds ---" % (time.time() - start_time))
