#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 15:07:35 2017

@author: vishal
"""

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, Imputer, LabelBinarizer

from HousingSpyder import loadin_housing_data
from CoustomTransformation import CombinedAttributesAdder
from DataFrameSlector import DataFrameSelector

from sklearn.cross_validation import StratifiedShuffleSplit

import numpy as np

#print(dataset.head())
housing= loadin_housing_data()
housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)


split = StratifiedShuffleSplit(housing["income_cat"], test_size=0.2)
train_indices, test_indices = next(iter(split))
strat_train_set = housing.loc[train_indices]
strat_test_set = housing.loc[test_indices]

housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()

dataset = housing

dataset_num = dataset.drop('ocean_proximity', axis = 1)

ml_pipeline = Pipeline([('imputer', Imputer(strategy= 'median')),
                        ('attribs_adder',CombinedAttributesAdder()), 
                        ('std_scaller', StandardScaler())])

housing_num_tr = ml_pipeline.fit_transform(dataset_num)





from sklearn.pipeline import FeatureUnion

num_attribs = list(dataset_num)
cat_attribs = ["ocean_proximity"]

num_pipeline = Pipeline([('selector', DataFrameSelector(num_attribs)),
                         ('imputer', Imputer(strategy="median")),
                         ('attribs_adder', CombinedAttributesAdder()),
                         ('std_scaler', StandardScaler()),])

cat_pipeline = Pipeline([('selector', DataFrameSelector(cat_attribs)),
                         ('label_binarizer', LabelBinarizer()),])


full_pipeline = FeatureUnion(transformer_list=[("num_pipeline", num_pipeline),
                                               ("cat_pipeline", cat_pipeline),])

housing_prepared = full_pipeline.fit_transform(dataset)

def getPrepatredData_Lables():
    return housing_prepared, housing_labels
