#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 19:03:22 2017

@author: vishal
"""

from sklearn.base import BaseEstimator, TransformerMixin


from HousingSpyder import loadin_housing_data

dataset = loadin_housing_data()

class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y= None):
        return self
    def transform(self,X):
        return X[self.attribute_names].values
        

'''print(dataset.info())
print(dataset.describe())


print(dataset.shape)
set1 = dataset.describe()
print(dataset.columns)
print(set1.columns)

print (set(dataset.columns) - set(set1.columns))'''