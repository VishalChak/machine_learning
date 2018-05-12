#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 22:03:20 2017

@author: vishal
"""

import os
import tarfile
import urllib.request

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"

def fetchHousingData(housing_url = HOUSING_URL, housing_path = HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path,"housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path= housing_path)
    housing_tgz.close()
    
import pandas as pd

def loadin_housing_data(housing_path = HOUSING_PATH):
    csv_path = os.path.join(housing_path,"housing.csv")
    return pd.read_csv(csv_path)

#fetchHousingData()

dataset = loadin_housing_data()

#print(dataset.shape)
#print(dataset.head())
#print(dataset.info())

#print(dataset['ocean_proximity'].value_counts())

#print(dataset.describe())

# ploting
#dataset.hist(bins = 50, figsize=(20,15))

import numpy as np
import numpy.random as rnd

def split_train_test(data, test_ratio):
    shuffled_indices = rnd.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

def add_index(dataset):
    return dataset.reset_index()




train_set, test_set = split_train_test(dataset, 0.2)

'''
import hashlib

def test_set_check(identifier, test_ratio, hash):
    return hash(identifier).digest()[-1] < 256 * test_ratio

def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]

housing_with_id = dataset.reset_index()

train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")'''

#print(train_set.shape)
#print(test_set.shape)

from sklearn.cross_validation import train_test_split, KFold

train_set, test_set = train_test_split(dataset, test_size=0.2, random_state=42)

#print(train_set.shape)
#print(test_set.shape)

dataset["income_cat"] = np.ceil(dataset["median_income"]/1.5)

#dataset.hist(bins = 50, figsize = (25,20))
dataset["income_cat"].where(dataset["income_cat"] < 5.0 , 5.0, inplace= True)


dataset.drop(["income_cat"], axis=1, inplace=True)

# Data Visualization

housing = dataset
#housing.plot(kind = "scatter", x= "longitude", y = "latitude")
#housing.plot(kind = "scatter", x= "longitude", y = "latitude", alpha = 0.1)

import matplotlib.pyplot as plt
import matplotlib
matplotlib.matplotlib_fname()


'''
housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
s=housing["population"]/100, label="population",
c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
)
plt.legend()'''

corr_matrix = housing.corr()
#print(corr_matrix.shape)

#print(corr_matrix['median_house_value'].sort_values(ascending = False))


from pandas.tools.plotting import scatter_matrix

#scatter_matrix(housing, figsize= (10,8))

attributes = ["median_house_value", "median_income", "total_rooms",
"housing_median_age"]
#scatter_matrix(housing[attributes], figsize=(12,8))

# Find Most promising value is net_income

#housing.plot(kind = "scatter", x= 'median_income', y = 'median_house_value', alpha= .01)
housing['room_per_household'] = housing['total_rooms']/housing["population"]
housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"]=housing["population"]/housing["households"]

corr_matrix = housing.corr()
#print(corr_matrix)

median_ = corr_matrix["median_house_value"].sort_values(ascending=False)
#print(median_)

