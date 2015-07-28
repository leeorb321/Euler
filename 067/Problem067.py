''' 
  * Problem067.py
  *
  * Project Euler: Problem 67
  * 
  * Problem: Find the maximum total from top to bottom of the triangle given (100 rows).
  *          
  *
'''

import time
start_time = time.time()

t = [[int(n) for n in line.split()] for line in open('triangle.txt').readlines()]

def path(triangle):
    for row in xrange(len(triangle)-1, 0, -1):
        for col in xrange(row):
            triangle[row-1][col] += triangle[row][col] if triangle[row][col] > triangle[row][col+1] else triangle[row][col+1]
    return triangle[0][0]
       
print path(t)

print("--- %s seconds ---" % (time.time() - start_time))