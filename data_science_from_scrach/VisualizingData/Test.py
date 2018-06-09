#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 22:00:45 2018

@author: vishal
"""


def isBalanced(s):
    stack = []
    for ch in s:
        if ch in ('(', '{' , '['):
            stack.append(ch)
        elif ch == ')':
            if len(stack) >0 and stack[len(stack) -1 ] == '(':
                stack.pop()
            else:
                return 'NO'
        elif ch == '}':
            if len(stack) >0 and stack[len(stack) -1 ] == '{':
                stack.pop()
            else:
                return 'NO'
        elif ch == ']':
            if len(stack) >0 and stack[len(stack) -1 ] == '[':
                stack.pop()
            else:
                return 'NO'
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"
print(isBalanced("{{[[(())]]}}"))