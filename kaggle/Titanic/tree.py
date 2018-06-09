#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 09:52:19 2018

@author: vishal
"""


name = "vishal"

rev = ""

j = len(name)-1

for i in range(6,0):
    print(i)
for i in range(len(name)//2):
    temp = name[i]
    name[i] = name[j]
    name[j] = temp
    
def rev_line(line):
    temp = line.split()
    j = len(temp) -1
    for i in range(len(temp)//2 ):
        x = temp[i]
        temp[i] = temp[j]
        temp[j] = x
        j -=1
    
    return " ".join(temp)

line = "this is line"
print(rev_line(line))



arr =  [1, 4, 3, 0, 5]
n = len(arr)


sum_arr = 0

sum_n = (n * (n+1))/2

 
for i in range(len(arr)):
    sum_arr +=arr[i]        
    
sum_n-sum_arr

dict_map = {'A':'B','B':'C'}

def is_reachable(src, dest):
    while(src != dest):
        if (dict_map.contain(src)):
            if src == dest:
                return "True"
            else:
                src = dict_map[src]
        else:
            return "False"
    return "True"
    


a = [[1,2,3],[4,5,6]]

a[0][2]   


d = {'a':59, 'b':34}
d['a'] + d['b']

for a in range(5):
    for b in 'abc':
        print(b, end='.')
        
import copy
list_1 = ['a','b','c']

list_2 = copy.deepcopy(list_1)


a = [1,2,3] * 2
a = [3,5,7,9] + [3,5,7,9]    
import math
math.pow


for i, x in enumerate(['a','b','c']):
    output = x
print(output)

ss ="Hello World"

x = 0
for c in ss:
    if c.isupper():
        x +=10
    else:
        x+=1
        
print(x)


try:
    1/0
except ZeroDivisionError:
    print("a")
except:
    print('b')
else:
    print('c')
finally:
    print('d')
    
counter = 0     
while counter <7:
    counter +=1
    if counter ==4:
        continue
    elif counter == 6:
        break
    print(counter, end = ' ')
    
    
    
def x_():
    for i in range(5):
        yield(i)
        print(i)
        
m = x_()