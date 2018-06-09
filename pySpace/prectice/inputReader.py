#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 22:38:38 2018

@author: vishal
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        while (j >=0 and key < arr[j]):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
                
        

choice = 1
arr = []

while (choice >0 and choice <=3):
    print("1 Insert \n2 for Sorting \n3 Print")
    choice = int(input())
    if choice == 1:
        arr.append(int(input()))
    elif choice == 2:
        arr = insertion_sort(arr)
        print("After Sorting", arr)
    elif choice ==3:
        print("arr :",arr)
