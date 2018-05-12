#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:42:10 2017

@author: vishal
"""

import numpy as np
import cv2


path = "/home/vishal/ML/OpenCV/sid.mp4"

cap = cv2.VideoCapture(path)

while(cap.isOpened()):
    print("vishal")
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()