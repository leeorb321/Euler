'''
  * Problem010.py
  *
  * Project Euler: Problem 10
  *
  * Problem: Find the sum of all primes under 2 million.
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

print sum(sieve(2000000))

print("--- %s seconds ---" % (time.time() - start_time))
