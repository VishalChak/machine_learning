#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:41:41 2017

@author: vishal
"""

import numpy as np
import cv2

path = "/home/vishal/ML/OpenCV/lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg"


import numpy as np
import cv2

img = cv2.imread(path,0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('/home/vishal/ML/OpenCV/save.png',img)
    cv2.destroyAllWindows()