''' 
  * Problem017.py
  *
  * Project Euler: Problem 17
  * 
  * Problem: Find the number of letters used to write out all the numbers from
  * 1 to 1000 (British usage, i.e., with "and" (e.g., three hundred and forty-two)).
  *          
  *
'''

import time
start_time = time.time()

TO_19 = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8] # 0 - 19
TENS = [0,3,6,6,5,5,5,7,6,6] # tens digit
HUNDRED = 7 

def sum_num_letters(n):
	sum = 0
	for i in xrange(1,n+1):
		if n < 20:
			sum += TO_19[n]
		elif n >= 20 and n < 100:
			sum += TENS[n/10] + sum_num_letters(n%10)
		elif n >= 100 and n < 1000:
			sum += TO_19[n/100] + HUNDRED + sum_num_letters(n%100)
			if n % 100 != 0:
				sum += 3 # for the word 'and'
		elif n == 1000:
			sum += 11 # 'one thousand'
	return sum

print sum_num_letters(1000)
   
print("--- %s seconds ---" % (time.time() - start_time))