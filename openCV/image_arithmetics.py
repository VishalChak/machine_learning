#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:50:48 2017

@author: vishal
"""



import cv2

path = "/home/vishal/ML/OpenCV/lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg"

path1 = "/home/vishal/ML/OpenCV/lfw/Adolfo_Aguilar_Zinser/Adolfo_Aguilar_Zinser_0001.jpg"

img1 = cv2.imread(path)

img2 = cv2.imread(path1)

dst = cv2.addWeighted(img1,0.5,img2,0.5,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()



