#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 21:38:21 2018

@author: vishal
"""

import pandas as pd
from sklearn import linear_model

train_fp = "/home/vishal/datasets/kaggle/titanic/train.csv"
test_fp = "/home/vishal/datasets/kaggle/titanic/test.csv"

dataset = pd.read_csv(train_fp)

def data_preprocessing(dataset , is_train = True):
    data = dataset[['PassengerId','Survived', 'Pclass','Sex','Age','SibSp', 'Parch']]
    data.loc[data['Sex'] == 'male', 'Sex'] = 1
    data.loc[data['Sex'] == 'female', 'Sex'] = 0
    return data.dropna()

data = data_preprocessing(dataset)        

dataset.dtypes
data.dtypes
data.isnull().sum()
pl_data = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Survived']]

pl_data.dtypes

import matplotlib.pyplot as plt
plt.matshow(pl_data.corr())

data.plot(x="Survived", y=["Pclass", "Sex", "SibSp", 'Parch'], kind="bar")







X = data[['Pclass','Sex', 'Age', 'SibSp', 'Parch']]
y = data['Survived']



logreg = linear_model.LogisticRegression()
logreg.fit(X,y)

logreg.predict(X)