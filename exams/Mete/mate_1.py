#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 20:56:10 2018

@author: vishal
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
import statsmodels.api as sm
plt.style.use('fivethirtyeight')

### Data preprossing
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/event-detection/"
calIt_data_names=['Flow_ID','Date','Time','Count']
calIt_data = pd.read_csv(url+'CalIt2.data', names = calIt_data_names)
calIt_events_names = ['Date', 'Begin event time', 'End event time', 'Event name']
calIt_events = pd.read_csv(url+'CalIt2.events', names = calIt_events_names)
dodgers_data = pd.read_csv(url+'Dodgers.data')
Dodgers_events = pd.read_csv(url+'Dodgers.events', encoding = "ISO-8859-1")

calIt_data.head(10080)
calIt_data = calIt_data.dropna()
calIt_data['Date_Time'] = pd.to_datetime(calIt_data['Date'] + ' ' + calIt_data['Time'])
calIt_data.index = calIt_data.Date_Time
calIt_data = calIt_data[['Date_Time','Flow_ID', 'Count']]

# Sea Born plot
sns.set(rc={'figure.figsize':(12,8)})
sns.tsplot(calIt_data, time='Date_Time', unit='Flow_ID', condition='Flow_ID', value='Count')


# matplotlib plot
calIt_data = calIt_data.drop(['Date_Time', 'Flow_ID'],axis=1)
calIt_data.plot(figsize=(15, 6))
plt.show()

### ARIMA MOdel prepretion
p = d = q = range(0, 2)
    
# Generate all different combinations of p, q and q triplets
pdq = list(itertools.product(p, d, q))

# Generate all different combinations of seasonal p, q and q triplets
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(calIt_data,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)

            results = mod.fit()

            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue


mod = sm.tsa.statespace.SARIMAX(calIt_data,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)

results = mod.fit()

print(results.summary().tables[1])

results.plot_diagnostics(figsize=(15, 12))
plt.show()