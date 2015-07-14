''' 
  * Problem020.py
  *
  * Project Euler: Problem 20
  * 
  * Problem: Find the sum of the digits in the number 100! (factorial 100)
  *          
  *
'''

import time
start_time = time.time()

def factorial(n):
    result = 1
    for i in xrange(1,n+1):
        result *= i
    return result

def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n /= 10
    return sum 

print sum_digits(factorial(100))
   
print("--- %s seconds ---" % (time.time() - start_time))