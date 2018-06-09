#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 20:38:45 2018

@author: vishal
"""

def reduce(val):
    i = 1
    rev = ""
    while i < len(val):
        if val[i-1] == val[i]:
            rev +=val[i]
            i +=1
        i +=1
    return rev
        
x = reduce('aaabccddd')