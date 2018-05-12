#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 19:04:43 2017

@author: vishal
"""

# Atmospheric CO2 from Continuous Air Samples at Mauna Loa Observatory, Hawaii, U.S.A.
# which collected CO2 samples from March 1958 to December 2001. We can bring in this data as follows


import tensorflow as tf

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = sm.datasets.co2.load_pandas()

co2 = data.data

co2.index

y = co2['co2'].resample('MS').mean()

co2.head()
y.head()

y['1990']

y['1990-10-1':'1995-10-1']

#Handling Missing Values in Time-series Data

y.isnull().sum()

y = y.fillna(y.bfill())

y.isnull().sum()


#Visualizing Time-series Data

y.plot(figsize=(15,6))
plt.show()


#seasonal_decompose

from pylab import rcParams

rcParams['figure.figsize'] = 11, 9

decomposition = sm.tsa.seasonal_decompose(y, model='additive')
fig = decomposition.plot()
plt.show()