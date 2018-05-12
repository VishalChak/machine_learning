#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 16:35:12 2017

@author: vishal
"""

import pandas as pd
path = "/home/vishal/ML/datasets/LedinClub_Loan/loan.csv"

data = pd.read_csv(path)

data.info()
data.head()
data.tail()
data.sample(5)
data.shape

data.drop(['id', 'member_id', 'emp_title'], axis=1, inplace=True)
data.shape

import numpy as np
data.replace('n/a', np.nan,inplace=True)
data.emp_length.fillna(value=0,inplace=True)
data['emp_length'].replace(to_replace='[^0-9]+', value='', inplace=True, regex=True)

data['emp_length'] = data['emp_length'].astype(int)
data['term'] = data['term'].apply(lambda x: x.lstrip())

import seaborn as sns
import matplotlib

s= pd.value_counts(data['emp_length']).to_frame().reset_index()
s.columns = ['type', 'count']


def emp_dur_graph(graph_title):
    sns.set_style('whitegrid')
    ax = sns.barplot(x= 'type', y = 'count', data=s)
    ax.set(xlabel = '', ylabel = '', title = graph_title)
    matplotlib.ticker.FuncFormatter(lambda x, p : format(int(x), ','))
    _ = ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    
emp_dur_graph('Distribution of employment length for issued loans')

from matplotlib import pyplot as plt
print (plt.style.available)

plt.style.use('fivethirtyeight')
ax = emp_dur_graph('Fivethirty eight style')

plt.style.use('seaborn-notebook')
ax = emp_dur_graph('Seaborn-notebook style')


plt.style.use('ggplot')
ax = emp_dur_graph('ggplot style')

plt.style.use('classic')
ax = emp_dur_graph('classic style')



# WOrkming with data

import datetime

data.issue_d.fillna(value = np.nan, inplace=True)
issue_d_todate = pd.to_datetime(data.issue_d, errors='coerce')

data.issue_d = pd.Series(data.issue_d).str.replace('-2015', '')

data.emp_length.fillna(value=np.nan, inplace=True)

data.drop(['loan_status'], 1, inplace=True)

data.drop(['pymnt_plan','url','desc','title' ],1, inplace=True)

data.earliest_cr_line.fillna(value = np.nan, inplace=True)

data.earliest_cr_line = pd.to_datetime(data.earliest_cr_line, errors='coerce')

'''import datetime as dt
data['earliest_cr_line'] = data['earliest_cr_line']
data['earliest_cr_line']'''    

#  Making faceted graphs using Seaborn
import matplotlib.pyplot as plt

s = pd.value_counts(data['earliest_cr_line']).to_frame().reset_index()
s.columns = ['date', 'count']

type(s.date[0])
s['year'] = s['date'].dt.year
s['month'] = s['date'].dt.month
 
d = s[s['year'] > 2008]
plt.rcParams.update(plt.rcParamsDefault)
sns.set_style("whitegrid")

g = sns.FacetGrid(d, col="year")
g = g.map(sns.pointplot, "month", "count")
g.set(xlabel = 'Month', ylabel = '')
axes = plt.gca()
_ = axes.set_ylim([0, d.year.max()])
plt.tight_layout()
 


mths = [s for s in data.columns.values if "mths" in s]
mths

data.drop(mths, axis=1, inplace=True)



group = data.groupby('grade').agg([np.mean])
loan_amt_mean = group['loan_amnt'].reset_index()

plt.style.use('fivethirtyeight')

sns.set_style("whitegrid")
ax = sns.barplot(y = "mean", x = 'grade', data=loan_amt_mean)
ax.set(xlabel = '', ylabel = '', title = 'Average amount loaned, by loan grade')
ax.get_yaxis().set_major_formatter(
matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
_ = ax.set_xticklabels(ax.get_xticklabels(), rotation=0)



#Treatment of missing values

from sklearn.ensemble import RandomForestClassifier
rf =  RandomForestClassifier(max_depth=5, n_estimators=100, max_features=1)

data['emp_length'].replace(to_replace=0, value=np.nan, inplace=True, regex=True)

cat_variables = ['term', 'purpose', 'grade']
columns = ['loan_amnt', 'funded_amnt', 'funded_amnt_inv', 'int_rate', 'grade', 'purpose', 'term']


def impute_missing_algo(df, target, cat_vars, cols, algo):

    y = pd.DataFrame(df[target])
    X = df[cols].copy()
    X.drop(cat_vars, axis=1, inplace=True)

    cat_vars = pd.get_dummies(df[cat_vars])

    X = pd.concat([X, cat_vars], axis = 1)

    y['null'] = y[target].isnull()
    y['null'] = y.loc[:, target].isnull()
    X['null'] = y[target].isnull()

    y_missing = y[y['null'] == True]
    y_notmissing = y[y['null'] == False]
    X_missing = X[X['null'] == True]
    X_notmissing = X[X['null'] == False]

    y_missing.loc[:, target] = ''

    dfs = [y_missing, y_notmissing, X_missing, X_notmissing]
    
    for df in dfs:
        df.drop('null', inplace = True, axis = 1)

    y_missing = y_missing.values.ravel(order='C')
    y_notmissing = y_notmissing.values.ravel(order='C')
    X_missing = X_missing.as_matrix()
    X_notmissing = X_notmissing.as_matrix()
    
    algo.fit(X_notmissing, y_notmissing)
    y_missing = algo.predict(X_missing)

    y.loc[(y['null'] == True), target] = y_missing
    y.loc[(y['null'] == False), target] = y_notmissing
    
    return(y[target])

data['emp_length'] = impute_missing_algo(data, 'emp_length', cat_variables, columns, rf)

#data['earliest_cr_line_year'] = impute_missing_algo(data, 'earliest_cr_line_year', cat_variables, columns, rf)


y = data.term
cols = ['loan_amnt', 'funded_amnt', 'funded_amnt_inv', 'int_rate', 'grade', 'emp_length', 'purpose']
X = pd.get_dummies(data[cols])

from sklearn import preprocessing

y = y.apply(lambda x: x.lstrip())
le = preprocessing.LabelEncoder()
le.fit(y)
y = le.transform(y)

from sklearn import linear_model

logistic = linear_model.LogisticRegression()
logistic.fit(X, y)


import keras as kr