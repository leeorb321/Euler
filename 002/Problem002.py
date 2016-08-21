'''
  * Problem002.py
  *
  * Project Euler: Problem 2
  *
  * Problem: Find the sum of the even-valued terms
  *          in the Fibonacci sequence under 4 million.
  *
'''

import time
start_time = time.time()

def sumEvenFib(n):
    sum = 0
    first, second = 0, 1
    while second < n:
        first, second = second, first + second
        if second % 2 == 0:
            sum += second
    return sum

print(sumEvenFib(4000000))
print("--- %s seconds ---" % (time.time() - start_time))
