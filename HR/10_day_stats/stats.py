#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 10:40:00 2018

@author: vishal
"""
x = [3,7,8,5,12,14,21,13,18]
n = 9
x.sort()
print(x)

def get_quartiles(x , left, right):
    half  = (left + right)//2
    print(left , right)
    if (left + right) % 2 ==0:
        return (x[half] + x[half -1]) //2
    else:
        return x[half]


q1 = 0
q3 = 0
if n %2 ==0:
    q1 = get_quartiles(x, 0, n//2 -1)
    q3 = get_quartiles(x, n//2 +1, n)
else:
    q1 = get_quartiles(x, 0, n//2)
    q3 = get_quartiles(x, n//2 +1, n)
q2 =  get_quartiles(x,0,n)
    
print(q1)
print(q2)
print(q3)