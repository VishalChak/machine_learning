#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 11:30:55 2017

@author: vishal
"""

from sklearn.datasets import fetch_mldata
custom_data_home = 'dataset/mnist'
mnist = fetch_mldata('MNIST original', data_home=custom_data_home)
X , y = mnist['data'], mnist['target']

def split():
    return X[:6000],X[6000:],y[:6000],y[6000:]

X_train, X_test ,y_train, y_test = split()

import numpy as np
shuffle_index = np.random.permutation(6000)
X_train , y_train = X_train[shuffle_index], y_train[shuffle_index]



from sklearn.linear_model import SGDClassifier
sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, y_train)

ans = sgd_clf.predict(X_train[1])
print(ans)
np.set_printoptions(threshold=np.nan)
print(y_train)


from sklearn.cross_validation import StratifiedKFold
from sklearn.base import clone

skfolds = StratifiedKFold(y_train, n_folds=3, random_state=42)

for train_index, test_index in skfolds:
    clone_clf = clone(sgd_clf)
    X_train_folds = X_train[train_index]
    y_train_folds = y_train[train_index]
    X_test_fold = X_test[test_index]
    y_test_fold = y_test[test_index]
    
    clone_clf.fit(X_train_folds,y_train_folds)
    y_pred = clone_clf.predict(X_test_fold)
    n_correct = sum(y_pred == y_test_fold)
    #print(n_correct/len(y_pred))
    
from sklearn.cross_validation import cross_val_score

score = cross_val_score(sgd_clf, X_train, y_train, cv=3, scoring="accuracy")

'''import pandas as pd
import numpy as np
import cv2
img = cv2.imread("five.jpg")'''



from sklearn.base import BaseEstimator

class Never5Classifier(BaseEstimator):
    def fit(self, X, y=None):
        pass
    def predict(self, X):
        return np.zeros((len(X), 1), dtype=bool)
    

