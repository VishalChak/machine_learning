#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 22:38:13 2017

@author: vishal
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

path = "/home/vishal/ML/HackerEarthML/Happiness/"

data = pd.read_csv(path+"train.csv")

data.head()

X = data[['Description','Is_Response']]
from nltk.tokenize import word_tokenize
dictionary = set(word.lower() for passage in X for word in word_tokenize(passage[0]))

t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in X]

classifier = nltk.NaiveBayesClassifier.train(t)

test_data = "Manchurian was hot and spicyddddd"
test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
  
print (classifier.classify(test_data_features))