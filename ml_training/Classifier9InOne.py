#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 09:24:27 2017

@author: vishal
"""

import matplotlib
import matplotlib.pyplot as plt
matplotlib.matplotlib_fname()
import pandas as pd

from sklearn import model_selection

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', "sepal-width", "petal_length","petal-width", "class"]
dataset = pd.read_csv(url, names = names)



# 1-------Understand Data Shape, Rows, cols , index etc----------#

# I. data shape
print(dataset.shape)

# II . Data look
print(dataset.head(10))

# III Data Describe
print(dataset.describe())

# iV data calss description
print(dataset.groupby('class').size())

# 2 ---- UNder stand data by Visualization

#  I Data Visualization Unibirate plot Whsiker Plot and box plot
dataset.plot(kind = 'box', subplots = True, layout = (2,2), sharex = False, sharey = False)


# II see by histogram
dataset.hist()

# III --Multi variate plote or Scatter Plot
scatter_matrix(dataset)


# Till here we under stood data .. Based on our understanding we will apply all Data cleaning  and Data Preprocession method
# So .. Afer doing preprossing we will get cleaned Data

# Divide data in labels and targetor



#print(dataset['class'].value_counts())
# find ans replace -- Kind of dfata encoder for catagarical data

clagarigal_encoder = {"class": {"Iris-setosa": 0, "Iris-virginica": 1, "Iris-versicolor": 2}}
dataset.replace(clagarigal_encoder, inplace = True)

'''list_class = ['Iris-setosa','Iris-virginica','Iris-versicolor']
for cl in list_class:
        dataset.loc[dataset['class'] ==list_class[i], 'class'] = i'''
        
npArr = dataset.values
X = npArr[:,0:4]
y = npArr[:,4]

validation_size = 0.7
seed = 7
X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y, test_size = validation_size, random_state = seed)

scoring = 'accuracy'
models = []
models.append(('LR', LogisticRegression()))
models.append(('Dicision Tree', DecisionTreeClassifier()))
models.append(('SVM', SVC()))
models.append(("NB", GaussianNB()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('MLP_nn', MLPClassifier()))
models.append(('Randm Forest', RandomForestClassifier()))
models.append(('Ada', AdaBoostClassifier()))
models.append(("QDA", QuadraticDiscriminantAnalysis()))


res = []
names = []

for name , clf in models:
    kfold = model_selection.KFold(n_splits = 10, random_state = seed)
    cv_result = model_selection.cross_val_score(clf, X_train, y_train, cv = kfold, scoring = scoring)
    names.append(name)
    res.append(cv_result)
    msg = "%s : %f %f" % (name, cv_result.mean(), cv_result.std())
    print(msg)
    
fig = plt.figure()
fig.suptitle("Algo Comparission")
ax = fig.add_subplot(111)
plt.boxplot(res)
ax.set_xticklabels(names)
plt.show()