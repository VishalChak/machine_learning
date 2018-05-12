#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 10:45:56 2018

@author: vishal
"""

import cv2

img_path = "/home/vishal/ml_projects/Kaaenaat/img.jpg"

# Parameters
IMG_SIZE_X = 640
IMG_SIZE_Y = 360
center = (320,180)
radious = 180
color = (255,0,0)

import random 
random.randrange(0,IMG_SIZE_X)

import numpy as np
def is_inside(x, y):
    a = np.array((x ,y ))
    b = np.array((320,180))    
    dist = np.linalg.norm(a-b)
    if (dist <= 180):
        return True
    else:
        return False

for i in range(10):
    x = random.randrange(0,IMG_SIZE_X)
    y = random.randrange(0,IMG_SIZE_Y)
    print('({0}, {1}) IsInside: {2}'.format(x,y,is_inside(x,y)))

img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (640,360))
cv2.circle(img,center, radious, color, thickness=1, lineType=8, shift=0)


circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
