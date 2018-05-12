#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:31:26 2017

@author: vishal
"""

from HousingSpyder import loadin_housing_data
dataset = loadin_housing_data()


#Handling text and categorical attributes
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

dataset_cat = dataset['ocean_proximity']
dataset_encoder_cat = encoder.fit_transform(dataset_cat)
#print(dataset_encoder_cat)
#print(encoder.classes_)

from sklearn.preprocessing import OneHotEncoder

oh_encoder = OneHotEncoder()
dataset_cat_oh = oh_encoder.fit_transform(dataset_encoder_cat.reshape(-1,1))
#print(dataset_cat_oh.toarray())
# Apply both in on shot Text-> catagaries -> oneHotEncoder

from sklearn.preprocessing import LabelBinarizer
encoder_lb = LabelBinarizer()
dataset_cat_lb = encoder_lb.fit_transform(dataset_cat)
print(dataset_cat_lb)


