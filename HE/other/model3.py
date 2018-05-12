#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 13:57:29 2017

@author: vishal
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split # function for splitting data to train and test sets

import nltk
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt


path = "/home/vishal/ML/HackerEarthML/Happiness/"

data = pd.read_csv(path+"train.csv")

data= data[['Description','Is_Response']]

train, test = train_test_split(data,test_size = 0.1)

train_pos = train[ train['Is_Response'] == 'happy']
train_pos = train_pos['Description']
train_neg = train[ train['Is_Response'] == 'not happy']
train_neg = train_neg['Description']



def wordcloud_draw(data, color = 'black'):
    words = ' '.join(data)
    cleaned_word = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and not word.startswith('#')
                                and word != 'RT'
                            ])
    wordcloud = WordCloud(stopwords=STOPWORDS,
                      background_color=color,
                      width=2500,
                      height=2000
                     ).generate(cleaned_word)
    plt.figure(1,figsize=(13, 13))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    
print("Positive words")
wordcloud_draw(train_pos,'white')

print("Negative words")
wordcloud_draw(train_neg)


data.dtypes