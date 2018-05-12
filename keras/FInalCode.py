# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:19:05 2017

@author: 10639497
"""

import keras as kr
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.matplotlib_fname()
import datetime


def data_cleaning(data):
    data.drop(['id', 'member_id', 'emp_title'], axis=1, inplace=True)
    data.replace('n/a', np.nan,inplace=True)
    data.emp_length.fillna(value=0,inplace=True)
    data['emp_length'].replace(to_replace='[^0-9]+', value='', inplace=True, regex=True)
    
    data['emp_length'] = data['emp_length'].astype(int)
    data['term'] = data['term'].apply(lambda x: x.lstrip())
    
    return data

def emp_dur_graph(graph_title, s):
    sns.set_style('whitegrid')
    ax = sns.barplot(x= 'type', y = 'count', data=s)
    ax.set(xlabel = '', ylabel = '', title = graph_title)
    matplotlib.ticker.FuncFormatter(lambda x, p : format(int(x), ','))
    _ = ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    sns.plt.show()
    return ax

def data_preprocessing(data):
    data.issue_d.fillna(value = np.nan, inplace=True)
    data.issue_d = pd.Series(data.issue_d).str.replace('-2015', '')
    data.emp_length.fillna(value=np.nan, inplace=True)
    data.drop(['loan_status'], 1, inplace=True)
    data.drop(['pymnt_plan','url','desc','title' ],1, inplace=True)
    data.earliest_cr_line.fillna(value = np.nan, inplace=True)
    data.earliest_cr_line = pd.to_datetime(data.earliest_cr_line, errors='coerce')
    return data

def feature_selection(data):
    cols = ['loan_amnt', 'funded_amnt', 'funded_amnt_inv', 'int_rate', 'grade', 'purpose', 'emp_length']
    return data[cols], data.term

#Treatment of missing values
def impute_missing_algo(df, target, algo):
    cat_vars = ['term', 'purpose', 'grade']
    
    cols = ['loan_amnt', 'funded_amnt', 'funded_amnt_inv', 'int_rate', 'grade', 'purpose', 'term']
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

path = "D:\\Vishal\\DataSets\\lending-club-loan-data/loan.csv"
data = pd.read_csv(path)

print(data.head())
clean_data = data_cleaning(data)
print(clean_data.head())

s= pd.value_counts(data['emp_length']).to_frame().reset_index()
s.columns = ['type', 'count']

emp_dur_graph('Distribution of employment length for issued loans', s)
#print (plt.style.available)

plt.style.use('fivethirtyeight')
ax = emp_dur_graph('Fivethirty eight style',s)

plt.style.use('seaborn-notebook')
ax = emp_dur_graph('Seaborn-notebook style',s)


plt.style.use('ggplot')
ax = emp_dur_graph('ggplot style',s)

plt.style.use('classic')
ax = emp_dur_graph('classic style',s)

prep_data = data_preprocessing(clean_data)
print(prep_data.head())


from sklearn.ensemble import RandomForestClassifier
rf =  RandomForestClassifier(max_depth=5, n_estimators=100, max_features=1)

selected_data = feature_selection(prep_data)

X, y = feature_selection(data)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.33, random_state = 42) 


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(12, activation='relu', input_shape=(11,)))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.output_shape
model.summary()
model.get_config()
model.get_weights()
model.compile(loss='binary_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
                   
model.fit(X_train, y_train,epochs=20, batch_size=1, verbose=1)






