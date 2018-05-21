# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:12:17 2018

@author: 10639497
"""

import pandas as pd


import nltk

from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier
from nltk.tokenize import RegexpTokenizer

from gensim.models import Word2Vec

path = "D:\\Vishal\\Dataset\\AV\\"
project = "Sentiment_analysis"
train_path = path +project + "\\train_.csv"
test_path = path +project + "\\test_.csv"

data = pd.read_csv(train_path)

def preprocess(sentence):
	sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	filtered_words = [w for w in tokens if not w in stopwords.words('english')]
	return " ".join(filtered_words)

data.columns
data['tweet_cln'] = data['tweet'].apply(preprocess)

data.head()
data['tweet'][1]
data['tweet_cln'][0]

model = Word2Vec(data['tweet_cln'])

model['user father dysfunctional selfish drags kids dysfunction run']
type(a)

help(Word2Vec)