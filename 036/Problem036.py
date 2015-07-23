''' 
  * Problem036.py
  *
  * Project Euler: Problem 36
  * 
  * Problem: Find the sum of all numbers under one million that are palindromic in base 10 and base 2.
  *          
  *
'''

import time
start_time = time.time()

is_palindrome = lambda x: str(x) == str(x)[::-1]

print sum(x for x in xrange(1,1000000) if is_palindrome(str(x)) and is_palindrome(str(bin(x))[2:]))

print("--- %s seconds ---" % (time.time() - start_time))
