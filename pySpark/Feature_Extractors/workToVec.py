#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:30:55 2017

@author: vishal
"""

from __future__ import print_function

from pyspark.ml.feature import Word2Vec
from pyspark.sql import SparkSession

session = SparkSession.builder.appName('WordToVec').getOrCreate()

documentDF = session.createDataFrame([("Hi I heard about Spark".split(" "), ),
    ("I wish Java could use case classes".split(" "), ),
    ("Logistic regression models are neat".split(" "), )],['text'])

documentDF.show()
word2Vec = Word2Vec(vectorSize=3, minCount=0, inputCol = 'text', outputCol = "result")
model = word2Vec.fit(documentDF)
result = model.transform(documentDF)
result.show()
for row in result.collect():
    text, vector = row
    print("Text: [%s] => \nVector: %s\n" % (", ".join(text), str(vector)))

session.stop()