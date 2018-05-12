#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 16:58:00 2017

@author: vishal
"""


import cv2
import numpy as np

path = "/home/vishal/ML/OpenCV/lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg"

img = cv2.imread(path,0)
cv2.imshow('image',img)


# Scaling
res1 = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('res1',res1)

#OR

height, width = img.shape[:2]
res2 = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.imshow("res2", res2)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
    

#Translation