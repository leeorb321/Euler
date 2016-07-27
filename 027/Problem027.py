'''
  * Problem027.py
  *
  * Project Euler: Problem 27
  *
  * Problem: Find the product of the coefficients, a and b, for the quadratic expression n^2 + an + b
  * where |a| < 1000 and where |b| < 1000 that produces the maximum number of primes for consecutive values of n, starting with n = 0.
  *
'''

import time
start_time = time.time()


def sieve(n):
  is_prime = [False] * 2 + [True] * (n-1)
  for i in xrange(int(n**0.5)+1):
    if is_prime[i]:
      for j in xrange(i*i, n+1, i):
        is_prime[j] = False
  return [i for i in xrange(n) if is_prime[i]]

def is_prime(n): return n in sieve(n+1)

def num_primes(a,b):
  n = 0
  while (n**2 + a*n + b > 0) and (n**2 + a*n + b) in sieve(n**2 + a*n + b + 1): n += 1
  return n

highest = 0
for b in sieve(1000):  # n^2 + an + b, where n=0 yields b; b therefore must be prime
  for a in range(-b,0,2):
    if num_primes(a,b) > highest:
      highest = num_primes(a,b)
      solution = a*b
      ab = [a,b]

print "Solution: ", solution, "; most primes: ", highest, ", a,b = ", ab

print("--- %s seconds ---" % (time.time() - start_time))
