#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 22:38:43 2018

@author: vishal
"""

class Node:
    def __init__(self):
        self.left = None
        self.right= None
        self.data = None

def insert(root, temp):
    if root.data <= temp.data:
        if root.right == None:
            root.right = temp
        else:
            insert(root.right, temp)
    else:
        if root.left == None:
            root.left = temp
        else:
            insert(root.left, temp)
            
def print_(temp):
    if temp != None:
        print_(temp.left)
        print(temp.data)
        print_(temp.right)
        

if "__main__" == __name__:
    ch = 0
    root = None
    while ch < 4:
        print("1 for insertion\n2 for print\n3 for search")
        ch = int(input())
        if ch == 1:
            temp = Node()
            temp.data = int(input())
            if root == None:
                root = temp
            else:
                insert(root, temp)
        elif ch ==2:
            print_(root)