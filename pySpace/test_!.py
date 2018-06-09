#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 18:20:47 2018

@author: vishal
"""

def test (grades):
    new_g = []
    for i in range(len(grades)):
        if grades[i] < 38:
            new_g.append(grades[i])
        elif ((grades[i]//5 + 1)*5 -grades[i] ) < 3:
            new_g.append((grades[i]//5 + 1)*5)
        else:
            new_g.append(grades[i])
    return new_g
    

a = [73,67,38,33]

print(test(a))            