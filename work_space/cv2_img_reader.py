# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 12:24:29 2018

@author: 10639497
"""


import numpy as np
import cv2


img_path = 'D:\\Vishal\\ml_projects\\bobby-deol.jpg'
img = cv2.imread(img_path,0)

cv2.imshow('bobby', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    print(gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()