#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:44:39 2018

@author: vishal
"""

from sklearn import datasets
from sklearn import tree
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split

import ep5

iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size = .5)

#clf = tree.DecisionTreeClassifier()
#clf = neighbors.KNeighborsClassifier()
clf = ep5.ScappyKnn()


clf.fit(X_train, y_train)

pred = clf.predict(X_test)

print(accuracy_score(y_test, pred))