#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 08:01:16 2017

@author: vishal
"""

 # camra capture 
import cv2

cap = cv2.VideoCapture(-1)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    flip = cv2.flip(frame,1200000)
    print(type(frame))
    
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()

