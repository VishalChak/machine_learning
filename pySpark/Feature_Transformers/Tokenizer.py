#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 15:45:13 2017

@author: vishal
"""

from __future__ import print_function

from pyspark.sql import SparkSession

session = SparkSession.builder.appName("TOkenizer").getOrCreate()

sentenceDataFrame = session.createDataFrame([(0, "Hi I heard about Spark"),
                                             (1, "I wish Java could use case classes"),
                                             (2, "Logistic,regression,models,are,neat")],
                                                ["id", "sentence"])

from pyspark.ml.feature import Tokenizer,RegexTokenizer

tokenizer = Tokenizer(inputCol = "sentence", outputCol = 'words')
regex_tokenizer = RegexTokenizer(inputCol = 'sentence', outputCol = 'words', pattern = '\\W')

from pyspark.sql.functions import col, udf
from pyspark.sql.types import IntegerType
countTokens = udf(lambda words: len(words), IntegerType())

tokenized = tokenizer.transform(sentenceDataFrame)
tokenized.select("sentence", "words")\
    .withColumn("tokens", countTokens(col("words"))).show(truncate=False)



regexTokenized = regex_tokenizer.transform(sentenceDataFrame)
regexTokenized.select("sentence", "words") \
    .withColumn("tokens", countTokens(col("words"))).show(truncate=False)


session.stop()