#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 16:29:14 2017

@author: vishal
"""
import cv2

import numpy as np
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]


#print(flags)

cap = cv2.VideoCapture(-1)

while(1):
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    #lower_red = np.array([0,255,255])
    #upper_red = np.array([30,255,255])
    
    #mask = cv2.inRange(hsv, lower_red, upper_red)
    
    
    res = cv2.bitwise_and(frame,frame , mask=mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()

green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print (hsv_green)