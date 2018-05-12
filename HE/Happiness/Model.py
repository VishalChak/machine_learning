#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 18:03:32 2017

@author: vishal
"""


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

path = "/home/vishal/ML/HackerEarthML/Happiness/"

data = pd.read_csv(path+"train.csv")
#print(data.head())


vader = SentimentIntensityAnalyzer()
def vader_polarity(text):
    """ Transform the output to a binary 0/1 result """
    score = vader.polarity_scores(text)
    return 1 if score['pos'] > score['neg'] else 0



sid = SentimentIntensityAnalyzer()
def analisezer(sentence):
    ss = sid.polarity_scores(sentence)
    return ss['compound']


data['senti'] = data.apply(lambda x: analisezer(x['Description']), axis=1)
data.loc[data['Device_Used'] == 'Mobile', 'Device_Used'] = 0
data.loc[data['Device_Used'] == 'Desktop', 'Device_Used'] = 1
data.loc[data['Device_Used'] == 'Tablet', 'Device_Used'] = 2


data.loc[data['Browser_Used'].str.lower().isin(['Internet Explorer', 'InternetExplorer', 'IE', 'Internet','Explorer']), 'Browser_Used'] = 0
data.loc[data['Browser_Used'].str.lower().isin(['Google Chrome','Google Chrome', 'GoogleChrome', 'Google', 'Chrome','GC']), 'Browser_Used'] = 1
data.loc[data['Browser_Used'].str.lower().isin(['Mozilla','Firefox', 'Firefox', 'Mozilla Firefox']), 'Browser_Used'] = 2
print(data.head(1000))

data.describe()



from sklearn import preprocessing
lb = preprocessing.LabelBinarizer()
X = data[['Device_Used','senti']]
y = data['Is_Response']



'''list_month = ['JAN','FEB','MAR','APR','MAY','JUN']
for i in range (len(list_month)) :
			X_data_plan_change.loc[X_data_plan_change['month'] ==list_month[i], 'month'] = i+1'''

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(X,y)
res = clf.predict(X)

data['res'] = res
data.head(100)


#import numpy as np
#data['senti'] = np.where(analisezer(data['Description']))

#data['senti'] = data.apply(lambda x: analisezer(data['']))


