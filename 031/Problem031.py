# -*- coding: utf-8 -*-

'''
  * Problem031.py
  *
  * Project Euler: Problem 31
  *
  * Problem: Find how many different ways can £2 be made using any number of coins.
  *
  *
'''

import time
start_time = time.time()

def brute_force():
    ways = 0
    for a in xrange(200, -1, -200):
        for b in xrange(a,-1,-100):
            for c in xrange(b,-1,-50):
                for d in xrange(c,-1,-20):
                    for e in xrange(d,-1,-10):
                        for f in xrange(e,-1,-5):
                            for g in xrange(f,-1,-2):
                                ways += 1
    return ways

def dynamic_programming(total=200):
    coins = [1,2,5,10,20,50,100,200]
    ways = [1] + [0]*total

    for coin in coins:
        for j in range(coin, total+1):
            ways[j] += ways[j - coin]
    return ways[-1]

def recursive(total, coins=[1,2,5,10,20,50,100,200]):
    if total < 0 or not coins:
        return 0
    if total == 0:
        return 1

    return recursive(total, coins[:-1]) + recursive(total - coins[-1], coins)

print("--- %s seconds ---" % (time.time() - start_time))


