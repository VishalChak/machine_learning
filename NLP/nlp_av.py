# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 12:41:11 2018

@author: 10639497
"""

import nltk

# 3.Text to Features (Feature Engineering on text data)
# 3.1 Syntactic Parsing
# 3.1.1 Dependency Trees
# 3.1.2 Part of speech tagging

from nltk import word_tokenize, pos_tag
text = "I am learning Natural Language Processing on Analytics Vidhya"

tokens = word_tokenize(text)
print(tokens)
pos_tag(tokens)


# Topic modeling 

#Ngrams as Features

def generate_ngrams(text, n):
    words = text.split()
    output = []
    for i in range (len(words) -n +1):
        output.append(words[i:i+n])
    return output

generate_ngrams('this is a sample text', 2)

# 3.3 Statistical Features  : Text data can also be quantified directly into numbers using several techniques described in this section:

# A.  Term Frequency – Inverse Document Frequency (TF – IDF)

from sklearn.feature_extraction.text import TfidfVectorizer

obj = TfidfVectorizer()
corpus = ['This is sample document.', 'another random document.', 'third sample document text']
X = obj.fit_transform(corpus)

print(X)




# word2vec


from gensim.models import Word2Vec
sentences = [['data', 'science'], ['vidhya', 'science', 'data', 'analytics'],['machine', 'learning'], ['deep', 'learning']]

# train the model on your corpus  
model = Word2Vec(sentences, min_count = 1)

print (model.similarity('data', 'science'))
print (model['learning'] )



# 4. Important tasks of NLP
# 4.1 Text Classification

# using textblob ---------------------

from textblob.classifiers import NaiveBayesClassifier as NBC

from textblob import TextBlob

training_corpus = [
                   ('I am exhausted of this work.', 'Class_B'),
                   ("I can't cooperate with this", 'Class_B'),
                   ('He is my badest enemy!', 'Class_B'),
                   ('My management is poor.', 'Class_B'),
                   ('I love this burger.', 'Class_A'),
                   ('This is an brilliant place!', 'Class_A'),
                   ('I feel very good about these dates.', 'Class_A'),
                   ('This is my best work.', 'Class_A'),
                   ("What an awesome view", 'Class_A'),
                   ('I do not like this dish', 'Class_B')]

test_corpus = [
                ("I am not feeling well today.", 'Class_B'), 
                ("I feel brilliant!", 'Class_A'), 
                ('Gary is a friend of mine.', 'Class_A'), 
                ("I can't believe I'm doing this.", 'Class_B'), 
                ('The date was good.', 'Class_A'), ('I do not enjoy my job', 'Class_B')]


model = NBC(training_corpus)
print(model.classify("Their codes are amazing."))
print(model.classify("I don't like their computer."))

print(model.accuracy(test_corpus))
#------------------------------

#using Scikit.Learn

from sklearn import svm 
from sklearn.feature_extraction import text
from sklearn.metrics import TfidfVectorizer
from sklearn.metrics import classification_report

train_data = []
train_labels = []
for row in training_corpus:
    train_data.append(row[0])
    train_labels.append(row[1])
    
test_data = [] 
test_labels = [] 
for row in test_corpus:
    test_data.append(row[0]) 
    test_labels.append(row[1])

vectorizer = TfidfVectorizer(min_df=4, max_df=0.9)
train_vectors = vectorizer.fit_transform(train_data)
test_vectors = vectorizer.transform(test_data)

# Perform classification with SVM, kernel=linear

model = svm.SVC(kernel='linear')
model.fit(train_vectors, train_labels)
prediction = model.predict(test_vectors)
prediction

print (classification_report(test_labels, prediction))