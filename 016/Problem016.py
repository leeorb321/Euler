''' 
  * Problem016.py
  *
  * Project Euler: Problem 16
  * 
  * Problem: Find the sum of the digits of the number 2^1000.
  *	
  *
'''

import time
start_time = time.time()

num = 2**1000;
sum = 0;
while num != 0:
	sum += num % 10;
	num /= 10;
print sum;

print("--- %s seconds ---" % (time.time() - start_time))