#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 23:54:47 2017

@author: vishal
"""

from HousingSpyder import loadin_housing_data


dataset = loadin_housing_data()
#print(dataset.head())

from sklearn.preprocessing import Imputer

# Missing value

imputer = Imputer(strategy='median')

# Imputer work on numeric col only so we need to extract numrric call only
dataset_num = dataset.drop('ocean_proximity', axis = 1)
#print(dataset_num.head())
imputer.fit(dataset_num)


#print(imputer.statistics_)
#print(dataset_num.median().values)

X = imputer.transform(dataset_num)

import pandas as pd
dataset_tr = pd.DataFrame(X, columns=dataset_num.columns)
print(dataset_tr.shape)

print(dataset.dis)
