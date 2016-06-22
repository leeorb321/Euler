# -*- coding: utf-8 -*-

'''
  * Problem032.py
  *
  * Project Euler: Problem 32
  *
  * Problem: Find the sum of all products whose multiplicand/multiplier/product identity
  * can be written as a 1 through 9 pandigital.
  *
  * An n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
  *
'''

import time
start_time = time.time()

def is_pandigital(number):
  if len(number) > 9 or int(number)%9:
    return False
  return ''.join(sorted(number)) == '123456789'

output = {}

for i in range(1,49):
  for j in range(i,1964):
    current = str(i*j) + str(i) + str(j)
    if int(current) >= 123456789:
      if i*j not in output and is_pandigital(current):
        output[i*j] = i*j
print sum(output.values())

print("--- %s seconds ---" % (time.time() - start_time))


