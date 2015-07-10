''' 
  * Problem004.py
  *
  * Project Euler: Problem 4
  * 
  * Problem: Find the largest palindrome made from the product of two 3-digit numbers.
  *          
  *
'''
import time
start_time = time.time()

def is_palindrome(n):
    num = str(n)
    
    if len(num) % 2 == 0:
        max = len(num) / 2
    else:
        max = (len(num) - 1) / 2

    for i in range(max):
        if  num[i] == num[len(num) - 1 - i]:
            pali = True
        else:
            pali = False
            break
    
    return pali

for i in xrange(999,899,-1):
    for j in xrange(999,899,-1):
        if is_palindrome(i*j):
            print i*j
            break
    if is_palindrome(i*j):
        break

print("--- %s seconds ---" % (time.time() - start_time))
