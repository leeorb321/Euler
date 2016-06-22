'''
  * Problem024.py
  *
  * Project Euler: Problem 24
  *
  * Problem: Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.

.
  *
  *
'''

import itertools
import time
start_time = time.time()

i = 1
for permutation in itertools.permutations(range(0,10)):
    if i == 1000000:
        break
    else:
        i += 1


print ''.join(str(c) for c in list(permutation))

print("--- %s seconds ---" % (time.time() - start_time))
