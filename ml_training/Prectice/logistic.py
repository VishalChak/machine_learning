# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 16:11:35 2017

@author: appladmin
"""

from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

data = datasets.load_iris()
model = LogisticRegression()
model.fit(data.data,data.target)

'''print(data.data)
print(data.target)
print(model)'''

exp = data.target
pre = model.predict(data.data)
clasReport = metrics.classification_report(exp,pre)
conf = metrics.confusion_matrix(exp,pre)
print(clasReport)
print(conf)
