#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 21:06:56 2018

@author: vishal
"""

arr = ()

def push():
    arr.append(input())
def pop():
    global arr
    arr = arr[:-1]

choice = 0
while choice < 5:
    print("1 for push\n2 for pop\n3 for print\n4 for length")
    choice = int(input())
    if choice ==1:
        push()
    elif choice ==2:
        if len(arr) >0:
            pop()
        else:
            print("Stack is empty")
    elif choice ==3:
        print(arr)
    elif choice ==4:
        print(len(arr))
    