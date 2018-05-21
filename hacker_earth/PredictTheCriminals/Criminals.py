# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:07:53 2018

@author: 10638120
"""

import pandas as pd
#import matplotlib.pyplot as plt
#from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import numpy as np

path = "D:\\Vishal\\Dataset\\HE\\PredictTheCriminals\\"
train_path = path+"criminal_train.csv"
test_path = path+"criminal_test.csv"

dataset = pd.read_csv(train_path)

y = dataset['Criminal']
X = dataset.drop(["PERID", "Criminal"], axis = 1)
X.head()

scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

clf = RandomForestClassifier(n_estimators=35)
#clf  = RandomForestClassifier(max_depth=5, n_estimators=20, max_features=1)
clf = clf.fit(X, y)
clf.score(X, y)


from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(hidden_layer_sizes=(30,30,30) , alpha=1)
clf = clf.fit(X, y)
clf.score(X, y)


'''imp = clf.feature_importances_
len(imp)
imp

srt_list = sorted(imp)

srt_list.index(0.15736448661255004)

help(list)
for feture in imp:
    print(feture)

fe_imp = dict(zip(X.columns, clf.feature_importances_.tolist()))
for key in fe_imp:
    print(fe_imp[key])
        
    #print(key, fe_imp[key])

test_data = pd.read_csv(test_path)

PERID = test_data['PERID']

X_test = test_data.drop(['PERID'],  axis = 1)

X_test = scaler.transform(X_test)

res= pd.DataFrame()
res['PERID'] = PERID
res['Criminal'] = clf.predict(X_test)

res.to_csv(path+"res.csv", index = False)'''