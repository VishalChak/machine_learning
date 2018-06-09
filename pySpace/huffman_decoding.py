#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 09:55:58 2018

@author: vishal
"""
huff_dict = {}

huff_dict["a"] = "vishal"

x = huff_dict.get('b')
if x is None:
    print("not there")

a = [1,2,3,4,5]

t = a.pop()
stack_list = []
max_ele = 0
max_list = []
n = int(input())
for i in range(n):
    temp = input()
    temp = temp.split(" ")
    if int(temp[0]) ==1:
        ele = int(temp[1])
        stack_list.append(ele)
        if len(max_list) == 0 or max_ele < ele:
            max_ele = ele
            max_list.append(ele)
    elif int(temp[0]) ==2:
        if len(stack_list)>0:
            del_ele = stack_list.pop()
            if del_ele == max_ele:
                max_list.pop()
                max_ele = max_list[-1]
    elif int(temp[0]) ==3:
        print(max_ele)