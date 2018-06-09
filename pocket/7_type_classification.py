# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:20:25 2018

@author: 10639497
"""

import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing  import LabelEncoder

plt.style.use('bmh')

path = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult"
train_path = path + "/adult.data"

column_name = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country', 'income']

dataset = pd.read_csv(train_path, names  = column_name )

#  Exploratory Data Analysis

dataset.head()

dataset.info()

encoder = LabelEncoder()
data = dataset
data['workclass'] = encoder.fit_transform(dataset['workclass'])

data['workclass'].value_counts(dropna = False)

dataset['workclass'].value_counts( dropna=True)
dataset['education'].value_counts( dropna=True)

dataset['marital-status'].value_counts( dropna=True)
dataset['occupation'].value_counts( dropna=True)

plt.figure(figsize=(9, 8))


sns.distplot(dataset['age'], color='g', bins=100, hist_kws={'alpha': 0.4});

dataset.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)

dataset.head()
dataset.describe()



