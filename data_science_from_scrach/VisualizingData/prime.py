#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 08:55:42 2018

@author: vishal
"""

def is_prime(num):
    if num ==2:
        return True
    elif num <2 or not num % 2:
        return False
    for i in range(3, int(num ** .5 +1), 2):
        if not num % i:
            return False
    return True

def get_primes(n):
    if n < 1:
        return
    primes = [2,]
    testNum = 3
    while n > 1:
        if is_prime(testNum):
            primes.append(testNum)
            n -=1
        testNum +=2
    return primes


print(get_primes(6))

arr = [3,3,4,4,9]

for i in reversed(arr):
    print (i)