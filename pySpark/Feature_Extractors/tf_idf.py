#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 13:15:54 2017

@author: vishal
"""


from __future__ import print_function

from pyspark.ml.feature import IDF, HashingTF, Tokenizer

from pyspark.sql import SparkSession

session = SparkSession.builder.appName('TF_IDF').getOrCreate()

sentenceData = session.createDataFrame([(0.0, "Hi I heard about Spark"),
        (0.0, "I wish Java could use case classes"),
        (1.0, "Logistic regression models are neat")],['leble', 'sentence'])

#sentenceData.show()
tokenizer = Tokenizer(inputCol = 'sentence',outputCol = 'words')
wordData = tokenizer.transform(sentenceData)
#wordData.show()
#dataframe.show()

hashingTF = HashingTF(inputCol = 'words', outputCol = 'rawFeatures', numFeatures = 20)
featurizedData = hashingTF.transform(wordData)
#featurizedData.show()

idf = IDF(inputCol="rawFeatures", outputCol="features")
idfModel = idf.fit(featurizedData)
rescaledData = idfModel.transform(featurizedData)
rescaledData = rescaledData.select('features')
rescaledData.show()


session.stop()