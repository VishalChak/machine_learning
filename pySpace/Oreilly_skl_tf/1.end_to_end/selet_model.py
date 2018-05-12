#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 21:10:04 2017

@author: vishal
"""
from sklearn.linear_model import LinearRegression

from ML_Pipeline import getPrepatredData_Lables
housing,housing_labels = getPrepatredData_Lables()

lin_reg = LinearRegression()
lin_reg.fit(housing, housing_labels)


from HousingSpyder import loadin_housing_data

dataset = loadin_housing_data()
some_data = dataset.iloc[:5]
some_labels = housing_labels.iloc[:5]
print(some_labels)
print(some_data)

#some_data = housing.iloc[:5]
#some_labels = housing_labels.iloc[:5]
#print(some_labels)
