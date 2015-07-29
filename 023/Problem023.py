''' 
  * Problem023.py
  *
  * Project Euler: Problem 23
  * 
  * Problem: Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
  *          A number is abundant if the sum of its proper divisors is greater than that number (if lesser: deficient, equals: perfect).
  *          
  *
'''

import itertools
import time
start_time = time.time()

n = 28123+1

def is_abundant(num): return sum(set(itertools.chain.from_iterable([x, num//x] for x in xrange(1,int(num**0.5)+1) if num % x == 0))) > 2*num

abundant_list = filter(is_abundant, xrange(n))

def abundant_sums(nlist): return sum(set([nlist[i]+nlist[j] for i in xrange(len(nlist)) for j in xrange(i, len(nlist)) if nlist[i]+nlist[j] < n]))

print n*(n-1)/2 - abundant_sums(abundant_list)

print("--- %s seconds ---" % (time.time() - start_time))