#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 10:17:51 2017

@author: vishal
"""

import pandas as pd

path = "/home/vishal/ML/HackerEarthML/Happiness/"

data = pd.read_csv(path+"train.csv")

train = data[['Description','Is_Response']]
print(train.dtypes)


import nltk


data_dic = train.to_dict
print(data_dic)

classifier = nltk.NaiveBayesClassifier.train(data_dic)

from nltk.tokenize import word_tokenize
dictionary = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
print(len(dictionary))

all_words = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in train]
classifier = nltk.NaiveBayesClassifier.train(t)


from itertools import chain
vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in train]))

classifier.show_most_informative_features()


	
def cleanText(text):
    """
    removes punctuation, stopwords and returns lowercase text in a list of single words
    """
    text = text.lower()    
    
    from bs4 import BeautifulSoup
    text = BeautifulSoup(text).get_text()
    
    from nltk.tokenize import RegexpTokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)
    
    from nltk.corpus import stopwords
    clean = [word for word in text if word not in stopwords.words('english')]
    
    return clean

train['Description'] = train['Description'].apply(cleanText)

