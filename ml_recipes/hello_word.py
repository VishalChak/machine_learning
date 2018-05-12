#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:29:19 2018

@author: vishal
"""

from sklearn import tree
feature = [[140,1],[130,1],[150,0], [170,0]]
labels = [0,0,1,1]

clf = tree.DecisionTreeClassifier()

clf.fit(feature, labels)

print(clf.predict([[150,0]]))

