#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:13:13 2018

@author: vishal
"""
#  https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/
import nltk

# NLP Tutorial

# 1. Noise Removal

# 1.a. simple
noise_list = ["is", "a", "this", "..."]

def remove_noise (input_text):
    words = input_text.split()
    noise_free_words =  [word for word in words if word not in noise_list]
    noise_free_text = " ".join(noise_free_words)
    return noise_free_text

noise_free_text = remove_noise("this is a simple text")
print(noise_free_text)


# 1.b: useing regular expressions

import re

def remove_regex(input_text, regex_pattern):
    urls = re.finditer(regex_pattern, input_text)
    for i in urls:
        input_text = re.sub(i.group().strip(), "", input_text)
    return input_text

regex_pattern = "#[\w]*"
remove_regex("remove this #hashtag from analytics #vishal vidhya", regex_pattern)
        
# 2. Lexicon Normalization
# 2.1  Stemming
# 2.2  Lemmatizer

        
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer 
stem = PorterStemmer()

word = "multiplying" 
lem.lemmatize(word, "v")
stem.stem(word)

# Object Standardization

lookup_dict = {'rt':'Retweet', 'dm':'direct message', "awsm" : "awesome", "luv" :"love"}

def lookup_words(input_text):
    words = input_text.split()
    new_words = []
    for word in words:
        if word.lower() in lookup_dict:
            word = lookup_dict[word.lower()]
        new_words.append(word)
    return " ".join(new_words)

lookup_words("RT this is a retweeted tweet by Shivam Bansal")

# 3. Text to Features (Feature Engineering on text data)
# 3.1 : Syntactic Parsing

