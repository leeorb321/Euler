''' 
  * Problem003.py
  *
  * Project Euler: Problem 3
  * 
  * Problem: Find the largest prime factor of the number 600851475143
  *          
  *
'''

import math

def largest_prime_factor(n):
    largest = 1
    
    # if even, remove factors of 2
    if n % 2 == 0:
        largest, n = 2, n/2
    
    # odd factors
    p, current = n, 3
    while n != 1 and current <= math.sqrt(p):
        while n % current == 0:
            largest = current
            n /= current
        current += 2
    
    return largest

print largest_prime_factor(600851475143)
