''' 
  * Problem025.py
  *
  * Project Euler: Problem 25
  * 
  * Problem: Find the index of the first term in the Fibonacci 
  * sequence to contain 1000 digits.
  *          
  *
'''

import time
start_time = time.time()


def fibo(n):
    if n <= 1:
        return n
    first, second = 0, 1
    for i in xrange(n, 1, -1):
        first, second = second, first + second
    return second

i = 0
while len(str(fibo(i))) < 1000:
    i += 1

print i
   
print("--- %s seconds ---" % (time.time() - start_time))