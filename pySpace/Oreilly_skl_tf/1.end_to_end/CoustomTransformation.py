#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:35:33 2017

@author: vishal
"""
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

room_ix, bedroom_ix,population_ix,household_ix = 3,4,5,6
class CombinedAttributesAdder (BaseEstimator, TransformerMixin):
    def __init__(self,add_bedrooms_per_room =True):
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self,X, y=None):
        return self
    def transform(self,X, y=None):
        rooms_per_household = X[:,room_ix]/X[:,household_ix]
        population_per_household = X[:,population_ix]/X[:,household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:,bedroom_ix]/ X[:, room_ix]
            return np.c_[X,rooms_per_household,population_per_household,bedrooms_per_room]
        else :
            return np.c_[X,rooms_per_household,population_per_household]


'''from HousingSpyder import loadin_housing_data
attr_adder = CombinedAttributesAdder(add_bedrooms_per_room = False)
dataset = loadin_housing_data()

housing_extra_attribs = attr_adder.transform(dataset.values)
print(housing_extra_attribs)'''
