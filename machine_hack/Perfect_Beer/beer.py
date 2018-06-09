#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 23:52:54 2018

@author: vishal
"""
path = "/home/vishal/datasets/machine_hack/How-To-Choose-The-Perfect-Beer-Data-Set/train.csv"

import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from sklearn import preprocessing

dataset = pd.read_csv(path)


dataset.dtypes
dataset.head()
dataset.shape


def print_val(val):
    return str(val)
        
dataset['Cellar Temperature'] = dataset['Cellar Temperature'].apply(print_val)
dataset['Serving Temperature'] = dataset['Serving Temperature'].apply(print_val)

le = preprocessing.LabelEncoder()
le.fit(dataset['Serving Temperature'])

dataset['ct'] = le.transform(dataset['Cellar Temperature'])
dataset['st'] = le.transform(dataset['Serving Temperature'])

dataset.head()
dataset.dtypes

dataset['Ratings'] = dataset['Ratings'].apply(lambda x: int(x))

dataset['Cellar Temperature'].value_counts(dropna = False).plot.bar()
dataset['Serving Temperature'].value_counts(dropna = False).plot.bar()


X = dataset[['ABV', ]]

'''def remove_special_char(sent):
    return re.sub('[^a-zA-Z0-9]', ' ', sent)


stop_words = set(stopwords.words('english'))
def remove_stopword(sent):
    word_tokens = word_tokenize(sent)
    sent = [w for w in word_tokens if not w in stop_words]
    return " ".join(sent)
    

dataset['Food Paring'] = dataset['Food Paring'].apply(remove_special_char)
dataset['Glassware Used'] = dataset['Glassware Used'].apply(remove_special_char)

dataset['Glassware Used'] = dataset['Glassware Used'].apply(remove_stopword)
dataset['Food Paring'] = dataset['Food Paring'].apply(remove_stopword)

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()

food_pairing = cv.fit_transform(dataset['Food Paring'])

glassware_used = cv.fit_transform(dataset['Glassware Used'])

X = dataset.head(10)

dict_data = {}
dataset.dtypes

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

le.fit(dataset['ellar Temperature'])

def fill_dict(row):
    row_dict = {}
    row_dict['ABV']
    print(row['ABV'], row['Glassware Used'])

t = X.apply(fill_dict, axis = 1)    


vec = cv.fit_transform(dataset['Food Paring'])

vec.shape


vec.toarray()

dataset['new_food'] = list(vec)

from sklearn.feature_extraction import DictVectorizer

v = DictVectorizer()
X = v.fit_transform(dataset[['ABV', 'new_food']])

from sklearn.pipeline import FeatureUnion

combined_features = FeatureUnion([('title', dataset['new_food']), ('description', vec)])



from sklearn.feature_extraction.text import TfidfVectorizer
tokenize = lambda doc: doc.lower().split(" ")
sklearn_tfidf = TfidfVectorizer(norm='l2',min_df=0, use_idf=True, smooth_idf=False, sublinear_tf=True, tokenizer=tokenize)

dataset.dtypes


a = sklearn_tfidf.fit_transform(dataset['Food Paring'])

X = dataset[['ABV', 'food_paring']]
y = dataset['Score']

from sklearn.tree import DecisionTreeClassifier
cls = DecisionTreeClassifier()
cls.fit(X.tolist(),y.tolist())

'''