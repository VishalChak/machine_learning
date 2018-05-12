#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:47:33 2018

@author: vishal
"""

from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree


iris = load_iris()

test_idx = [0,50,100]

#training data

train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis = 0)

#test data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]


clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print(test_target)
print(clf.predict(test_data))

# viz code

import graphviz
dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = graphviz.Source(dot_data)  
graph 
