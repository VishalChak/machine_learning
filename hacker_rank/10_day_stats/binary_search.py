#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:41:42 2018

@author: vishal
"""


a = [1,2,4,6,8,10,12,33,56,78]
a.sort()
mid = 0
def search(x, left, right):
    if right >= left:
        global mid
        mid = (right + left)//2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            return search(x, left, mid-1)
        else:
            return search(x, mid+1, right)
    else:
        return -1

indx = search(10,0, len(a)-1)

if indx != -1:
    print("val found @ index ", indx)
else:
    print('Not Found and closest value is', a[mid])
