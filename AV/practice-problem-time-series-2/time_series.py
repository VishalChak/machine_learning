# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:36:53 2018

@author: 10639497
"""

import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

path = "D:\\Vishal\\Dataset\\AV\\"
project = "practice-problem-time-series-2"
train_path =path + project +"\\Train_.csv"
test_path =path + project +"\\Test_.csv"


dataset = pd.read_csv(train_path)

def get_date(x):
    return pd.to_datetime(x, format='%Y%m%d', errors='ignore')

def get_float(x):
    return float(x)


dataset['Count'] = dataset['Count'].apply(get_float)
dataset['Datetime'] = dataset['Datetime'].apply(get_date)

tm = dataset['Count']
tm.index = dataset['Datetime']

model = ARIMA(tm, order=(5,1,0))
model_fit = model.fit(disp=0)

print(model_fit.summary())
residuals = pd.DataFrame(model_fit.resid)
residuals.plot( figsize = (12,8))
residuals.plot(kind='kde', figsize = (12,8))
print(residuals.describe())

test_data = pd.read_csv(test_path)

for index, row in test_data.iterrows():
    model = ARIMA(tm, order=(5,1,0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    print(output[0][0])
    s = pd.Series([output[0][0]], index=[row[1]])
    tm = tm.append(s)
