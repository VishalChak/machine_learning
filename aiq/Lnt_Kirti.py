#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 23:19:07 2017

@author: vishal
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
import collections
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint
 
# Importing the dataset

path = "/home/vishal/ML/incident_new.csv"
dataset = pd.read_csv(path, encoding = "ISO-8859-1")


X = dataset.iloc[:,[2]]
 
# Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 949):
    review = re.sub('[^a-zA-Z]', ' ', X['description'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
 
print("Number of documents:",len(corpus))


# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000)
X1 = cv.fit_transform(corpus).toarray()
 
# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X1)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


def word_tokenizer(text):
           #tokenizes and stems the text
           tokens = word_tokenize(text)
           stemmer = PorterStemmer()
           tokens = [stemmer.stem(t) for t in tokens if t not in stopwords.words('english')]
           return tokens
 
 
def cluster_sentences(sentences, nb_of_clusters=5):
    tfidf_vectorizer = TfidfVectorizer(tokenizer=word_tokenizer,
                                       stop_words=stopwords.words('english'),
                                       max_df=0.9,
                                       min_df=0.1,
                                       max_features=5000,
                                       lowercase=True)
    #builds a tf-idf matrix for the sentences
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
    kmeans = KMeans(n_clusters=nb_of_clusters)
    kmeans.fit(tfidf_matrix)
    clusters = collections.defaultdict(list)
    for i, label in enumerate(kmeans.labels_):
        clusters[label].append(i)
    return dict(clusters)

import nltk
nltk.download()

if __name__ == "__main__":
     sentences = corpus
     nclusters= 3
     clusters = cluster_sentences(sentences, nclusters)
    
     dict = {'0': [], '1': [],'2':[]}
     dict = { }
     print(sentences[20])
     for cluster in range(nclusters):
         print ("cluster ",cluster,":")
         arrayList = []
         for i,sentence in enumerate(clusters[cluster]):
             arrayList.append(sentences[sentence])
             print ("\tsentence ",i,": ",sentences[sentence])



