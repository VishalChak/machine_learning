#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:28:14 2017

@author: vishal
"""


import cv2

path = "/home/vishal/ML/OpenCV/lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg"

img = cv2.imread(path)

px = img[100, 100]
print(px)

# print only blue 

print(img[100,100,0])

img[100,100] = [255,255,255]

#  accessing RED value

red = img[10,10,2]
print(img[10,10])
print(red)

# modify red 

img.itemset((10,10,2),100)

print(img[10,10,2])

print(type(img))

print(img.shape)

print(img.size)

print(img.dtype)


#Splitting
b,g,r = cv2.split(img)
 
print(r.size)


# border 

from matplotlib import pyplot as plt

BLUE = [255,0,0]
constant= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.imshow(constant)

replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)

plt.imshow(replicate)

