'''
  * Problem022.py
  *
  * Project Euler: Problem 22
  *
  * Problem: Find the total of name score times alphabetical position for all names in the file
  *
  *
'''

import time
start_time = time.time()

def get_score(name):
  return sum([ ord(c) - 64 for c in name ])

f = open('p022_names.txt')
sorted_names = sorted(f.read().replace('"','').split(','))
f.close()

print sum([ get_score(sorted_names[i])*(i+1) for i in xrange(len(sorted_names)) ])

print("--- %s seconds ---" % (time.time() - start_time))
