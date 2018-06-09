#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 17:24:13 2018

@author: viiv
"""
bin(8)
val = bin(7)
val = val[2:]
print(2 ** (len(val)-1))

def is_rotation(val):
    val_dict = {}
    for i in val:
        if val_dict.get(i) is None:
            val_dict[i] = 1
        else:
            temp = val_dict.get(i)
            val_dict[i] = temp+1
    print(val_dict)
    if len(val) % 2 is 0:
        for key in val_dict:
            if val_dict[key]%2 is not 0:
                return False
        return True
    else:
        flag = False
        for key in val_dict:
            if val_dict[key]%2 is not 0:
                if flag is True:
                    return False
                else:
                    flag = True
        return True
    
print(is_rotation('aaacsab'))
        

    
            
    
    