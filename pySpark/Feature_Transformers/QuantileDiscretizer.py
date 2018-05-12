# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:01:21 2017

@author: 10639497
"""

from __future__ import print_function
from pyspark.sql import SparkSession

session = SparkSession.builder.appName("Quantilte").getOrCreate()

from pyspark.ml.feature import QuantileDiscretizer

data = [(0, 18.0), (1, 19.0), (2, 8.0), (3, 5.0), (4, 2.2)]
dataset = session.createDataFrame(data,['id', 'hour'])

dataset.show()
discretizer = QuantileDiscretizer(numBuckets=3, inputCol="hour", outputCol="result")
result = discretizer.fit(dataset).transform(dataset).select('result')
result.show()


