#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:48:28 2017

@author: vishal
"""
from __future__ import print_function

from pyspark.sql import SparkSession

from pyspark.ml.feature  import CountVectorizer
session = SparkSession.builder.appName("CountVectorizer").getOrCreate()

df = session.createDataFrame([(0, "a b c".split(" ")),
                              (1, "a b b c a".split(" "))],
                                ["id", "words"])

cv = CountVectorizer(inputCol = 'words', outputCol = "feature", minDF = 2.0)

model = cv.fit(df)
result = model.transform(df)

result.show(truncate=False)
session.stop()