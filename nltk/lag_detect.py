#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 13:29:36 2017

@author: vishal
"""


#from nltk.tokenize import sent_tokenize
from nltk import wordpunct_tokenize
file = open("/home/vishal/IBand/sdk.txt", 'r')

text = file.read()
tokens = wordpunct_tokenize(text)

for word in tokens:
    print(word)

'''
def detect_language(text):
    ratios = _calculate_languages_ratios(text)

    most_rated_language = max(ratios, key=ratios.get)

    return most_rated_language

text = "I am Vishal Chak"

import nltk
nltk.download()



tokens = wordpunct_tokenize(text)

from nltk.corpus import stopwords

stopwords.fileids()
stopwords.words('english')[0:10]

languages_ratios = {}

words = [word.lower() for word in tokens]

for language in stopwords.fileids():
    stopwords_set = set(stopwords.words(language))
    words_set = set(words)
    common_elements = words_set.intersection(stopwords_set)
    languages_ratios[language] = len(common_elements) # language "score"


sent_tokenize_list = sent_tokenize(text)'''
