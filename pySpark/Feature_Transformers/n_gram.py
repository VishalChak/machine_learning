#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 19:57:37 2017

@author: vishal
"""


from __future__ import print_function

from pyspark.sql import SparkSession

session = SparkSession.builder.appName('StopWord').getOrCreate()

wordDataFrame = session.createDataFrame([
    (0, ["Hi", "I", "heard", "about", "Spark"]),
    (1, ["I", "wish", "Java", "could", "use", "case", "classes"]),
    (2, ["Logistic", "regression", "models", "are", "neat"])
], ["id", "words"])



from pyspark.ml.feature import NGram

ngram = NGram(n=4, inputCol = 'words', outputCol = 'ngrams')

n_gram_result = ngram.transform(wordDataFrame)
#n_gram_result.show()
row = n_gram_result.first()
print(row)
#wordDataFrame.show()
session.stop()

