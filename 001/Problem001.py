''' 
  * Problem001.py
  *
  * Project Euler: Problem 1
  * 
  * Problem: Find sum of all natural numbers
  * that are multuples of 3 or 5 below 1000.
  *
'''

print sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, xrange(1,1000)));
