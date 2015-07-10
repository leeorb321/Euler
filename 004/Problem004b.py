''' 
  * Problem004b.py
  *
  * Project Euler: Problem 4
  * 
  * Problem: Find the largest palindrome made from the product of two 3-digit numbers.
  *          
  *
'''

import time
start_time = time.time()

def reverse(n):
    reversed = 0
    while n > 0:
        reversed = 10 * reversed + n % 10
        n = n / 10
    return reversed

def is_palindrome(n):
    return n == reverse(n)

for i in xrange(999,899,-1):
    for j in xrange(999,899,-1):
        if is_palindrome(i*j):
            print i*j
            break
    if is_palindrome(i*j):
        break

print("--- %s seconds ---" % (time.time() - start_time))
