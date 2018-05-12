# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:52:26 2018

@author: 10639497
"""

# Load data


import pandas as pd
import seaborn as sns

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/event-detection/"
calIt_data_names = ['Flow ID','Date','Time', 'Count']

data_calIt = pd.read_csv(url+'CalIt2.data', names = calIt_data_names)

def get_time(row):
    return pd.to_datetime(str(row[1] +' '+row[2]))

data_clt['data_time'] = data_clt.apply(get_time,  axis=1)

data_clt_selected = data_clt[['data_time', 'Flow ID', 'Count']]

#data_clt_selected = data_clt_selected[0:100]

data_clt_selected[['Count', 'data_time']].plot()
import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))

grid = sns.FacetGrid(data_clt_selected, size=4)
grid.map(sns.tsplot, data = data_clt_selected, time = "data_time", unit = "Flow ID", condition='Flow ID', value='Count')

sns.tsplot(data_clt_selected, time='data_time', unit = "Flow ID", condition='Flow ID', value='Count')



data_clt_selected.head()

data_clt['Flow ID'].value_counts(dropna = False)
max(data_clt['Date'].value_counts(dropna = False))
len(data_clt['Count'].value_counts(dropna = False))


data_clt.groupby(['Date', 'Time','Flow ID']).agg(['sum']).plot(figsize = [20,10])

data_clt.dtypes
sns.tsplot(data_clt, time='Date', unit='Time', condition='Flow ID', value='Count')



in_data_clt = data_clt.loc[data_clt['Flow ID'] == 7]

in_data_clt.head()


# 7 is out flow and 9 is in flow

clt_event_name = ['Date','Begin event time','End event time', 'Event name']
event_clt = pd.read_csv(url+'CalIt2.events', names = clt_event_name)

event_clt.head()

dodgers_data_names = ['Date','Time', 'Count']
data_dodgers = pd.read_csv(url+'Dodgers.data', names = dodgers_data_names)

data_dodgers.head(1)

dodgers_events_names = ['Date','Begin event time', 'End event time', 'Game attendance' , 'Away team' ,' W/L score']
event_dodgers = pd.read_csv(url+'Dodgers.events', names = dodgers_events_names, encoding = "ISO-8859-1")

event_dodgers.head()



