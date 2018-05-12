# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:44:11 2017

@author: appladmin
"""

import numpy as np

from sklearn import preprocessing
data =np.array ([[1,2,3,],[2.0,1,0],[0,1,-1]])
print(data)
data_scale = preprocessing.scale(data)

print(data_scale)
print(data_scale.mean(axis = 0))
print(data_scale.std(axis = 0))

min_max= preprocessing.minmax_scale(data)
print(min_max)

min_abs_max = preprocessing.MaxAbsScaler()