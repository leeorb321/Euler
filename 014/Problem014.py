''' 
  * Problem014.py
  *
  * Project Euler: Problem 14
  * 
  * Problem: Find the starting number under 1 million that produces the longest Collatz sequence.
  *          Collatz sequence: number / 2 if number is even; number * 3 + 1 if number is odd.
  *          
  *
'''

import time
start_time = time.time()

n = 1000000
collatz = {1:1}
def collatz_steps(num):
    if num not in collatz:
        collatz[num] = collatz_steps(3*num + 1) + 1 if (num%2) else collatz_steps(num/2) + 1
    return collatz[num]

for i in xrange(n,1,-1): collatz_steps(i)

longest = 1
for key in collatz:
    if collatz[key] > collatz[longest]:
       # print longest, key
        longest = key
        
print longest, collatz[longest]

print("--- %s seconds ---" % (time.time() - start_time))
